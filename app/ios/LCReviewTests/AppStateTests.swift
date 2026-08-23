import SwiftData
import XCTest
@testable import LCReview

/// AppState is @MainActor-isolated, so the test case must be too.
@MainActor
final class AppStateTests: XCTestCase {

    private struct FixedTransport: ContentTransport {
        let data: Data
        func fetch(etag: String?) async throws -> ContentFetchResult {
            .updated(data: data, etag: nil)
        }
    }

    /// Always fails. These tests are about session length, and the
    /// calendar is a separate path: if a broken calendar could change a
    /// session assertion, that would itself be the bug.
    private struct StubActivityTransport: ActivityTransport {
        struct Offline: Error {}
        func fetch(year: Int) async throws -> ActivityYear { throw Offline() }
    }

    private func makeState(problemCount: Int = 30) async throws -> AppState {
        let container = try ModelContainer(
            for: CardState.self, ReviewLog.self, AppSettings.self,
            configurations: ModelConfiguration(isStoredInMemoryOnly: true)
        )
        let problems = (0..<problemCount).map { i in
            Problem(
                id: "\(i)", number: i, title: "p\(i)", difficulty: "Easy",
                technique: "贪心", statement: "s", elements: ["e"],
                pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
                retrospective: "", solutions: [], solvedAt: nil
            )
        }
        let payload = ContentPayload(version: 1, problems: problems)
        let data = try JSONEncoder().encode(payload)
        let state = AppState(
            store: ContentStore(
                transport: FixedTransport(data: data),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
            ),
            activity: ActivityStore(
                transport: StubActivityTransport(),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
                    .appendingPathComponent("activity.json")
            ),
            context: ModelContext(container)
        )
        await state.loadContent()
        return state
    }

    /// This is the gap the settings screen closes: before it existed,
    /// `AppSettings.sessionLength` had no writer, so this test could never
    /// have been made to pass by any code path a user could reach.
    func testChangingSessionLengthChangesTheNextSessionBuilt() async throws {
        let state = try await makeState(problemCount: 30)
        XCTAssertEqual(state.sessionLength, 10, "default from the design doc")

        state.startSession(scope: .all)
        XCTAssertEqual(state.activeRunner?.progress.total, 10)
        state.finishSession()

        state.updateSessionLength(15)
        XCTAssertEqual(state.sessionLength, 15)

        state.startSession(scope: .all)
        XCTAssertEqual(
            state.activeRunner?.progress.total, 15,
            "the next session built must reflect the new length"
        )
    }

    func testChangingSessionLengthDoesNotResizeASessionAlreadyInProgress() async throws {
        let state = try await makeState(problemCount: 30)
        state.startSession(scope: .all)
        XCTAssertEqual(state.activeRunner?.progress.total, 10)

        state.updateSessionLength(20)

        XCTAssertEqual(
            state.activeRunner?.progress.total, 10,
            "a session already running must not be resized underneath the user"
        )
    }

    func testChangingSessionLengthUpdatesHomeEntryCounts() async throws {
        let state = try await makeState(problemCount: 30)
        let before = state.homeEntries.first { $0.id == "all" }
        XCTAssertEqual(before?.count, 10)

        state.updateSessionLength(5)

        let after = state.homeEntries.first { $0.id == "all" }
        XCTAssertEqual(after?.count, 5, "home rows must reflect the new length immediately")
    }

    func testSessionLengthPersistsAcrossAppStateInstances() throws {
        let container = try ModelContainer(
            for: CardState.self, ReviewLog.self, AppSettings.self,
            configurations: ModelConfiguration(isStoredInMemoryOnly: true)
        )
        let first = AppState(
            store: ContentStore(
                transport: FixedTransport(data: Data()),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
            ),
            activity: ActivityStore(
                transport: StubActivityTransport(),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
                    .appendingPathComponent("activity.json")
            ),
            context: ModelContext(container)
        )
        first.updateSessionLength(20)

        let second = AppState(
            store: ContentStore(
                transport: FixedTransport(data: Data()),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
            ),
            activity: ActivityStore(
                transport: StubActivityTransport(),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
                    .appendingPathComponent("activity.json")
            ),
            context: ModelContext(container)
        )
        XCTAssertEqual(
            second.sessionLength, 20,
            "the write must land in SwiftData, not just in the in-memory mirror"
        )
    }

    // MARK: - Refreshing content on foreground

    func testARefreshDoesNotFlashTheLoadingStateOverExistingContent() async throws {
        let state = try await makeState(problemCount: 5)
        XCTAssertFalse(state.isLoading)

        await state.loadContent()

        XCTAssertFalse(state.isLoading, "a refresh must not put the spinner back over a full screen")
        XCTAssertEqual(state.problems.count, 5)
    }

    func testAFailedRefreshKeepsWhatIsAlreadyOnScreen() async throws {
        let container = try ModelContainer(
            for: CardState.self, ReviewLog.self, AppSettings.self,
            configurations: ModelConfiguration(isStoredInMemoryOnly: true)
        )
        let problems = [
            Problem(
                id: "1", number: 1, title: "p1", difficulty: "Easy",
                technique: "贪心", statement: "s", elements: ["e"],
                pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
                retrospective: "", solutions: [], solvedAt: nil
            )
        ]
        let good = try JSONEncoder().encode(ContentPayload(version: 3, problems: problems))
        let transport = SwitchableTransport(data: good)
        let state = AppState(
            store: ContentStore(
                transport: transport,
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
            ),
            activity: ActivityStore(
                transport: StubActivityTransport(),
                cacheURL: FileManager.default.temporaryDirectory
                    .appendingPathComponent(UUID().uuidString)
                    .appendingPathComponent("activity.json")
            ),
            context: ModelContext(container)
        )
        await state.loadContent()
        XCTAssertEqual(state.problems.count, 1)

        // Now the network goes away, as it does on a foreground in a lift.
        await transport.breakIt()
        await state.loadContent()

        XCTAssertEqual(
            state.problems.count, 1,
            "a moment offline must not empty the home screen"
        )
        XCTAssertFalse(state.loadFailed)
    }
}

private actor SwitchableTransport: ContentTransport {
    private var data: Data
    private var broken = false

    init(data: Data) { self.data = data }

    func breakIt() { broken = true }

    func fetch(etag: String?) async throws -> ContentFetchResult {
        struct Offline: Error {}
        if broken { throw Offline() }
        return .updated(data: data, etag: nil)
    }
}

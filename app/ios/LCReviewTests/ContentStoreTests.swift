import XCTest
@testable import LCReview

private actor FakeTransport: ContentTransport {
    var result: ContentFetchResult
    private(set) var receivedETags: [String?] = []
    private(set) var callCount = 0

    init(result: ContentFetchResult) { self.result = result }

    func set(_ result: ContentFetchResult) { self.result = result }

    func fetch(etag: String?) async throws -> ContentFetchResult {
        receivedETags.append(etag)
        callCount += 1
        return result
    }
}

private struct FailingTransport: ContentTransport {
    struct Offline: Error {}
    func fetch(etag: String?) async throws -> ContentFetchResult { throw Offline() }
}

final class ContentStoreTests: XCTestCase {

    private var cacheURL: URL!
    private var defaults: UserDefaults!

    override func setUpWithError() throws {
        cacheURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString)
            .appendingPathComponent("content.json")
        defaults = UserDefaults(suiteName: UUID().uuidString)
    }

    private func payloadData(ids: [String]) throws -> Data {
        let problems = ids.map {
            Problem(
                id: $0, number: 1, title: $0, difficulty: "Easy", technique: "贪心",
                statement: "s", elements: ["e"],
                pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
                retrospective: "", solutions: [], solvedAt: nil, firstSolvedAt: nil,
            acceptedVersions: 0
            )
        }
        return try JSONEncoder().encode(ContentPayload(version: 1, problems: problems))
    }

    func testFirstLoadFetchesWithoutAnETagAndCaches() async throws {
        let transport = FakeTransport(
            result: .updated(data: try payloadData(ids: ["a"]), etag: "\"v1\"")
        )
        let store = ContentStore(transport: transport, cacheURL: cacheURL, defaults: defaults)

        let problems = await store.load()

        XCTAssertEqual(problems.map(\.id), ["a"])
        let receivedETags = await transport.receivedETags
        XCTAssertEqual(receivedETags, [nil])
        XCTAssertTrue(FileManager.default.fileExists(atPath: cacheURL.path))
    }

    func testSecondLoadSendsTheStoredETag() async throws {
        let transport = FakeTransport(
            result: .updated(data: try payloadData(ids: ["a"]), etag: "\"v1\"")
        )
        let store = ContentStore(transport: transport, cacheURL: cacheURL, defaults: defaults)
        _ = await store.load()

        await transport.set(.notModified)
        let problems = await store.load()

        XCTAssertEqual(problems.map(\.id), ["a"], "304 must serve the cache")
        let receivedETags = await transport.receivedETags
        XCTAssertEqual(receivedETags, [nil, "\"v1\""])
    }

    func testNotModifiedDoesNotRewriteTheCache() async throws {
        let transport = FakeTransport(
            result: .updated(data: try payloadData(ids: ["a"]), etag: "\"v1\"")
        )
        let store = ContentStore(transport: transport, cacheURL: cacheURL, defaults: defaults)
        _ = await store.load()
        let before = try FileManager.default
            .attributesOfItem(atPath: cacheURL.path)[.modificationDate] as? Date

        await transport.set(.notModified)
        _ = await store.load()

        let after = try FileManager.default
            .attributesOfItem(atPath: cacheURL.path)[.modificationDate] as? Date
        XCTAssertEqual(before, after)
    }

    func testFallsBackToTheCacheWhenOffline() async throws {
        let transport = FakeTransport(
            result: .updated(data: try payloadData(ids: ["a"]), etag: "\"v1\"")
        )
        _ = await ContentStore(transport: transport, cacheURL: cacheURL, defaults: defaults).load()

        let offline = ContentStore(
            transport: FailingTransport(), cacheURL: cacheURL, defaults: defaults
        )
        let problems = await offline.load()

        XCTAssertEqual(problems.map(\.id), ["a"])
    }

    func testReturnsEmptyWhenOfflineWithNoCache() async {
        let store = ContentStore(
            transport: FailingTransport(), cacheURL: cacheURL, defaults: defaults
        )
        let problems = await store.load()
        XCTAssertTrue(problems.isEmpty, "the view layer shows the retry message")
    }

    func testCorruptCacheDoesNotCrash() async throws {
        try FileManager.default.createDirectory(
            at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true
        )
        try Data("not json".utf8).write(to: cacheURL)

        let store = ContentStore(
            transport: FailingTransport(), cacheURL: cacheURL, defaults: defaults
        )
        let problems = await store.load()
        XCTAssertTrue(problems.isEmpty)
    }

    func testContentURLPointsAtTheRepository() {
        XCTAssertEqual(
            ContentStore.contentURL.absoluteString,
            "https://raw.githubusercontent.com/echo-xiao/leetcode-journey/main/app/content.json"
        )
    }
}

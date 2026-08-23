import XCTest
@testable import LCReview

private actor FakeActivityTransport: ActivityTransport {
    private let years: [Int: ActivityYear]
    private(set) var requestedYears: [Int] = []

    init(years: [Int: ActivityYear]) { self.years = years }

    func fetch(year: Int) async throws -> ActivityYear {
        requestedYears.append(year)
        guard let found = years[year] else { throw HTTPActivityTransport.Failure.badShape }
        return found
    }
}

private struct OfflineActivityTransport: ActivityTransport {
    struct Offline: Error {}
    func fetch(year: Int) async throws -> ActivityYear { throw Offline() }
}

final class ActivityStoreTests: XCTestCase {

    private var cacheURL: URL!

    override func setUpWithError() throws {
        cacheURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString)
            .appendingPathComponent("activity.json")
    }

    private func utc(_ year: Int, _ month: Int, _ day: Int, hour: Int = 12) -> Date {
        var components = DateComponents()
        components.year = year
        components.month = month
        components.day = day
        components.hour = hour
        return ActivityCalendar.utcCalendar.date(from: components)!
    }

    private func count(_ cells: [HeatmapCell], on key: String) -> Int? {
        cells.first { ActivityCalendar.dayKey($0.day) == key }?.count
    }

    private func writeCache(_ calendar: ActivityCalendar) throws {
        try FileManager.default.createDirectory(
            at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true
        )
        try JSONEncoder().encode(calendar).write(to: cacheURL)
    }

    func testASuccessfulFetchIsFreshAndCached() async throws {
        let transport = FakeActivityTransport(years: [
            2026: ActivityYear(countsByDay: ["2026-08-20": 78], streak: 15)
        ])
        let store = ActivityStore(transport: transport, cacheURL: cacheURL)

        let snapshot = await store.load(now: utc(2026, 8, 22))

        XCTAssertEqual(snapshot.status, .fresh)
        XCTAssertEqual(snapshot.streak, 15)
        XCTAssertEqual(snapshot.cells.count, 90)
        XCTAssertEqual(count(snapshot.cells, on: "2026-08-20"), 78)
        XCTAssertTrue(FileManager.default.fileExists(atPath: cacheURL.path))
    }

    func testAWindowInsideOneYearAsksForOneYear() async throws {
        let transport = FakeActivityTransport(years: [
            2026: ActivityYear(countsByDay: [:], streak: 0)
        ])
        let store = ActivityStore(transport: transport, cacheURL: cacheURL)

        _ = await store.load(now: utc(2026, 8, 22))

        let asked = await transport.requestedYears
        XCTAssertEqual(asked, [2026])
    }

    func testAWindowCrossingNewYearAsksForBothYearsAndMergesThem() async throws {
        let transport = FakeActivityTransport(years: [
            2025: ActivityYear(countsByDay: ["2025-12-31": 4], streak: 99),
            2026: ActivityYear(countsByDay: ["2026-01-05": 7], streak: 3),
        ])
        let store = ActivityStore(transport: transport, cacheURL: cacheURL)

        let snapshot = await store.load(now: utc(2026, 1, 10))

        let asked = await transport.requestedYears
        XCTAssertEqual(asked, [2025, 2026], "oldest year first, so the newest streak wins")
        XCTAssertEqual(count(snapshot.cells, on: "2025-12-31"), 4)
        XCTAssertEqual(count(snapshot.cells, on: "2026-01-05"), 7)
        XCTAssertEqual(snapshot.streak, 3, "the streak comes from the year containing today")
    }

    func testOneFailedYearFailsTheWholeLoad() async throws {
        // 2025 is missing from the fake, so fetching it throws. A window half
        // filled in is not a smaller truth, it is a wrong picture: the missing
        // days are indistinguishable from days with no submissions.
        let transport = FakeActivityTransport(years: [
            2026: ActivityYear(countsByDay: ["2026-01-05": 7], streak: 3)
        ])
        let store = ActivityStore(transport: transport, cacheURL: cacheURL)

        let snapshot = await store.load(now: utc(2026, 1, 10))

        XCTAssertEqual(snapshot.status, .unavailable)
        XCTAssertFalse(
            FileManager.default.fileExists(atPath: cacheURL.path),
            "a failed load must not overwrite or create a cache"
        )
    }

    func testAFailedFetchFallsBackToTheCacheAndSaysHowOldItIs() async throws {
        let fetchedAt = utc(2026, 8, 20)
        try writeCache(ActivityCalendar(
            countsByDay: ["2026-08-20": 78], streak: 15, fetchedAt: fetchedAt
        ))

        let store = ActivityStore(transport: OfflineActivityTransport(), cacheURL: cacheURL)
        let snapshot = await store.load(now: utc(2026, 8, 22))

        XCTAssertEqual(snapshot.status, .stale(asOf: fetchedAt))
        XCTAssertEqual(snapshot.streak, 15)
        XCTAssertEqual(count(snapshot.cells, on: "2026-08-20"), 78)
    }

    func testTheStaleWindowStillEndsTodayNotOnTheDayItWasFetched() async throws {
        // The cached calendar was fetched on the 20th; the grid must still
        // run through the 22nd, drawing the last two days as empty rather
        // than pretending today is the 20th.
        try writeCache(ActivityCalendar(
            countsByDay: ["2026-08-20": 78], streak: 15, fetchedAt: utc(2026, 8, 20)
        ))

        let store = ActivityStore(transport: OfflineActivityTransport(), cacheURL: cacheURL)
        let snapshot = await store.load(now: utc(2026, 8, 22))

        XCTAssertEqual(ActivityCalendar.dayKey(snapshot.cells.last!.day), "2026-08-22")
        XCTAssertEqual(count(snapshot.cells, on: "2026-08-22"), 0)
    }

    func testNoNetworkAndNoCacheGivesAnEmptyGridMarkedUnavailable() async {
        let store = ActivityStore(transport: OfflineActivityTransport(), cacheURL: cacheURL)

        let snapshot = await store.load(now: utc(2026, 8, 22))

        XCTAssertEqual(snapshot.status, .unavailable)
        XCTAssertEqual(snapshot.streak, 0)
        XCTAssertEqual(
            snapshot.cells.count, 90, "the grid keeps its shape so the layout does not jump"
        )
        XCTAssertTrue(snapshot.cells.allSatisfy { $0.count == 0 })
    }

    func testACorruptCacheIsTreatedAsNoCache() async throws {
        try FileManager.default.createDirectory(
            at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true
        )
        try Data("not json".utf8).write(to: cacheURL)

        let store = ActivityStore(transport: OfflineActivityTransport(), cacheURL: cacheURL)
        let snapshot = await store.load(now: utc(2026, 8, 22))

        XCTAssertEqual(snapshot.status, .unavailable)
    }

    func testYearsSpannedByTheWindow() {
        XCTAssertEqual(ActivityStore.years(now: utc(2026, 8, 22), days: 90), [2026])
        XCTAssertEqual(ActivityStore.years(now: utc(2026, 1, 10), days: 90), [2025, 2026])
        XCTAssertEqual(ActivityStore.years(now: utc(2026, 1, 1), days: 90), [2025, 2026])
        XCTAssertEqual(ActivityStore.years(now: utc(2026, 4, 1), days: 90), [2026])
    }
}

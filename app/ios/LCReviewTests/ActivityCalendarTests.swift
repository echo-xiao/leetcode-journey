import XCTest
@testable import LCReview

final class ActivityCalendarTests: XCTestCase {

    /// A UTC instant, so the tests state exactly which day they mean without
    /// depending on where the machine running them happens to be.
    private func utc(_ year: Int, _ month: Int, _ day: Int, hour: Int = 12) -> Date {
        var components = DateComponents()
        components.year = year
        components.month = month
        components.day = day
        components.hour = hour
        return ActivityCalendar.utcCalendar.date(from: components)!
    }

    func testDayKeyIsTheUTCDate() {
        // 1787184000 is 2026-08-20T00:00:00Z, one of the real keys the API
        // returned for this account.
        let date = Date(timeIntervalSince1970: 1_787_184_000)
        XCTAssertEqual(ActivityCalendar.dayKey(date), "2026-08-20")
    }

    func testDayKeyDoesNotShiftWithTheDeviceTimeZone() {
        // 2026-08-21T02:00:00Z is still 2026-08-20 in Los Angeles. The key
        // must follow LeetCode (UTC), not the phone.
        let date = Date(timeIntervalSince1970: 1_787_184_000 + 26 * 3600)
        XCTAssertEqual(ActivityCalendar.dayKey(date), "2026-08-21")
    }

    func testCellsCoverExactlyTheWindowEndingToday() {
        let calendar = ActivityCalendar(
            countsByDay: [:], streak: 0, fetchedAt: utc(2026, 8, 22)
        )

        let cells = calendar.cells(days: 90, now: utc(2026, 8, 22))

        XCTAssertEqual(cells.count, 90)
        XCTAssertEqual(ActivityCalendar.dayKey(cells.last!.day), "2026-08-22")
        XCTAssertEqual(ActivityCalendar.dayKey(cells.first!.day), "2026-05-25")
    }

    func testCellsCarryPerDayCounts() {
        let calendar = ActivityCalendar(
            countsByDay: ["2026-08-20": 78, "2026-08-19": 48],
            streak: 15,
            fetchedAt: utc(2026, 8, 22)
        )

        let cells = calendar.cells(days: 90, now: utc(2026, 8, 22))
        let byKey = Dictionary(
            uniqueKeysWithValues: cells.map { (ActivityCalendar.dayKey($0.day), $0.count) }
        )

        XCTAssertEqual(byKey["2026-08-20"], 78)
        XCTAssertEqual(byKey["2026-08-19"], 48)
        XCTAssertEqual(byKey["2026-08-21"], 0, "a day with no submissions is zero, not missing")
    }

    func testCellsCrossTheNewYearWithoutAGap() {
        let calendar = ActivityCalendar(
            countsByDay: ["2025-12-31": 4, "2026-01-01": 7],
            streak: 2,
            fetchedAt: utc(2026, 1, 10)
        )

        let cells = calendar.cells(days: 90, now: utc(2026, 1, 10))
        let byKey = Dictionary(
            uniqueKeysWithValues: cells.map { (ActivityCalendar.dayKey($0.day), $0.count) }
        )

        XCTAssertEqual(cells.count, 90)
        XCTAssertEqual(byKey["2025-12-31"], 4)
        XCTAssertEqual(byKey["2026-01-01"], 7)
    }

    func testRoundTripsThroughJSON() {
        let original = ActivityCalendar(
            countsByDay: ["2026-08-20": 78], streak: 15, fetchedAt: utc(2026, 8, 22)
        )

        let data = try! JSONEncoder().encode(original)
        let decoded = try! JSONDecoder().decode(ActivityCalendar.self, from: data)

        XCTAssertEqual(decoded, original)
    }
}

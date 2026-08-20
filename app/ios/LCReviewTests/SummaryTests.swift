import XCTest
@testable import LCReview

final class SummaryTests: XCTestCase {

    private var calendar: Calendar = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "Asia/Shanghai")!
        return calendar
    }()

    private lazy var summary = Summary(calendar: calendar)

    private func day(_ year: Int, _ month: Int, _ day: Int, hour: Int = 12) -> Date {
        calendar.date(from: DateComponents(
            year: year, month: month, day: day, hour: hour
        ))!
    }

    private func log(_ date: Date, isRepeat: Bool = false) -> ReviewLog {
        ReviewLog(
            problemID: "15_3sum", track: .elements, grade: .good,
            isRepeat: isRepeat, timestamp: date
        )
    }

    func testCountsGradesNotProblems() {
        // One problem walked end to end is two grades, and the heatmap counts
        // the work, not the problems.
        let logs = [
            ReviewLog(problemID: "a", track: .elements, grade: .good, isRepeat: false, timestamp: day(2026, 8, 18)),
            ReviewLog(problemID: "a", track: .pseudocode, grade: .hard, isRepeat: false, timestamp: day(2026, 8, 18)),
        ]
        XCTAssertEqual(summary.totalReviews(logs: logs), 2)
        XCTAssertEqual(summary.dailyCounts(logs: logs)[calendar.startOfDay(for: day(2026, 8, 18))], 2)
    }

    func testRepeatsCountAsWork() {
        let logs = [log(day(2026, 8, 18)), log(day(2026, 8, 18), isRepeat: true)]
        XCTAssertEqual(summary.totalReviews(logs: logs), 2)
    }

    func testGradesInTheSameLocalDayShareACell() {
        let logs = [log(day(2026, 8, 18, hour: 0)), log(day(2026, 8, 18, hour: 23))]
        XCTAssertEqual(summary.dailyCounts(logs: logs).count, 1)
    }

    func testStreakCountsBackFromToday() {
        let logs = [day(2026, 8, 18), day(2026, 8, 17), day(2026, 8, 16)].map { log($0) }
        XCTAssertEqual(summary.streak(logs: logs, now: day(2026, 8, 18)), 3)
    }

    func testTodayNotYetReviewedDoesNotBreakTheStreak() {
        let logs = [day(2026, 8, 17), day(2026, 8, 16)].map { log($0) }
        XCTAssertEqual(
            summary.streak(logs: logs, now: day(2026, 8, 18)), 2,
            "the number shown on a fresh morning is the streak through yesterday"
        )
    }

    func testMissingYesterdayBreaksTheStreak() {
        let logs = [day(2026, 8, 16), day(2026, 8, 15)].map { log($0) }
        XCTAssertEqual(summary.streak(logs: logs, now: day(2026, 8, 18)), 0)
    }

    func testStreakIsZeroWithNoLogs() {
        XCTAssertEqual(summary.streak(logs: [], now: day(2026, 8, 18)), 0)
    }

    func testHeatmapCoversExactlyTheWindow() {
        let cells = summary.heatmap(
            logs: [], startDay: day(2020, 1, 1), now: day(2026, 8, 18),
            days: Summary.heatmapWindowDays
        )
        XCTAssertEqual(cells.count, 90)
        XCTAssertEqual(cells.last?.day, calendar.startOfDay(for: day(2026, 8, 18)))
    }

    func testDaysBeforeTheStartDayAreMarkedBlank() {
        let cells = summary.heatmap(
            logs: [], startDay: day(2026, 8, 10), now: day(2026, 8, 18), days: 90
        )
        // The window ends on 8/18 and the start day is 8/10, so 8/10...8/18 —
        // nine days — are real and the other 81 predate the app.
        let blank = cells.filter(\.isBeforeStart)
        XCTAssertEqual(blank.count, 81, "the app cannot claim days that predate it")
        XCTAssertFalse(cells.last!.isBeforeStart)
    }

    func testHeatmapCarriesPerDayCounts() {
        let logs = [log(day(2026, 8, 18)), log(day(2026, 8, 18)), log(day(2026, 8, 17))]
        let cells = summary.heatmap(
            logs: logs, startDay: day(2026, 1, 1), now: day(2026, 8, 18), days: 90
        )
        XCTAssertEqual(cells.last?.count, 2)
        XCTAssertEqual(cells.dropLast().last?.count, 1)
    }
}

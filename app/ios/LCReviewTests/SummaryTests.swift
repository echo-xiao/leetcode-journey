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

    // MARK: - DST transitions

    // Every test above pins the calendar to Asia/Shanghai, which has not
    // observed daylight saving since 1991 — so none of them can exercise a
    // DST transition even though the streak is documented as walking
    // calendar days one at a time. The app runs on Calendar.current, and on
    // a device in the United States that means two transitions a year: a
    // 23-hour day every spring and a 25-hour day every fall. These tests
    // pin to America/Los_Angeles instead and sit directly on those days.

    private var losAngelesCalendar: Calendar = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "America/Los_Angeles")!
        return calendar
    }()

    private lazy var losAngelesSummary = Summary(calendar: losAngelesCalendar)

    private func laDay(_ year: Int, _ month: Int, _ day: Int, hour: Int = 12) -> Date {
        losAngelesCalendar.date(from: DateComponents(
            year: year, month: month, day: day, hour: hour
        ))!
    }

    /// Hours of real time between the start of `date`'s day and the start
    /// of the next, per the calendar under test. 24 on an ordinary day, 23
    /// on the day clocks spring forward, 25 on the day they fall back.
    private func dayLengthInHours(_ date: Date, calendar: Calendar) -> Double {
        let start = calendar.startOfDay(for: date)
        let next = calendar.date(byAdding: .day, value: 1, to: start)!
        return next.timeIntervalSince(start) / 3600
    }

    func testSpringForwardDayIsTwentyThreeHoursInLosAngeles() {
        // Ground truth, asked of the calendar itself rather than assumed:
        // proves 2026-03-08 really is the transition day before the streak
        // test below leans on it.
        XCTAssertEqual(
            dayLengthInHours(laDay(2026, 3, 8), calendar: losAngelesCalendar), 23,
            "2026-03-08 must be the spring-forward 23-hour day in America/Los_Angeles for the test below to prove anything"
        )
    }

    func testFallBackDayIsTwentyFiveHoursInLosAngeles() {
        XCTAssertEqual(
            dayLengthInHours(laDay(2026, 11, 1), calendar: losAngelesCalendar), 25,
            "2026-11-01 must be the fall-back 25-hour day in America/Los_Angeles for the test below to prove anything"
        )
    }

    func testStreakSurvivesSpringForwardTransition() {
        let logs = [laDay(2026, 3, 7), laDay(2026, 3, 8), laDay(2026, 3, 9)].map { log($0) }
        XCTAssertEqual(
            losAngelesSummary.streak(logs: logs, now: laDay(2026, 3, 9)), 3,
            "a 23-hour day must count as one day of the streak, not zero and not two"
        )
    }

    func testStreakSurvivesFallBackTransition() {
        let logs = [laDay(2026, 10, 31), laDay(2026, 11, 1), laDay(2026, 11, 2)].map { log($0) }
        XCTAssertEqual(
            losAngelesSummary.streak(logs: logs, now: laDay(2026, 11, 2)), 3,
            "a 25-hour day must count as one day of the streak, not zero and not two"
        )
    }

    func testHeatmapCellCountSurvivesSpringForwardTransition() {
        let transitionDay = laDay(2026, 3, 8)
        let cells = losAngelesSummary.heatmap(
            logs: [log(transitionDay)], startDay: laDay(2020, 1, 1), now: laDay(2026, 3, 15), days: 90
        )
        XCTAssertEqual(cells.count, 90, "the window must still be exactly 90 cells across a 23-hour day")
        XCTAssertEqual(
            Set(cells.map(\.day)).count, 90,
            "the 23-hour day must be neither skipped nor duplicated into two cells"
        )
        let transitionCell = cells.first { $0.day == losAngelesCalendar.startOfDay(for: transitionDay) }
        XCTAssertEqual(
            transitionCell?.count, 1,
            "the review logged on the transition day must land in that day's cell"
        )
    }

    func testHeatmapCellCountSurvivesFallBackTransition() {
        let transitionDay = laDay(2026, 11, 1)
        let cells = losAngelesSummary.heatmap(
            logs: [log(transitionDay)], startDay: laDay(2020, 1, 1), now: laDay(2026, 11, 8), days: 90
        )
        XCTAssertEqual(cells.count, 90, "the window must still be exactly 90 cells across a 25-hour day")
        XCTAssertEqual(
            Set(cells.map(\.day)).count, 90,
            "the 25-hour day must be neither skipped nor duplicated into two cells"
        )
        let transitionCell = cells.first { $0.day == losAngelesCalendar.startOfDay(for: transitionDay) }
        XCTAssertEqual(
            transitionCell?.count, 1,
            "the review logged on the transition day must land in that day's cell"
        )
    }
}

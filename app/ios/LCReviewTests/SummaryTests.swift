import XCTest
@testable import LCReview

final class SummaryTests: XCTestCase {

    private let summary = Summary()

    private func day(_ year: Int, _ month: Int, _ day: Int, hour: Int = 12) -> Date {
        Calendar(identifier: .gregorian).date(from: DateComponents(
            year: year, month: month, day: day, hour: hour
        ))!
    }

    private func log(_ date: Date, isRepeat: Bool = false) -> ReviewLog {
        ReviewLog(
            problemID: "15_3sum", grade: .good,
            isRepeat: isRepeat, timestamp: date
        )
    }

    func testCountsGradesNotProblems() {
        let logs = [log(day(2026, 8, 18)), log(day(2026, 8, 18))]
        XCTAssertEqual(summary.totalReviews(logs: logs), 2)
    }

    func testRepeatsCountAsWork() {
        let logs = [log(day(2026, 8, 18)), log(day(2026, 8, 18), isRepeat: true)]
        XCTAssertEqual(summary.totalReviews(logs: logs), 2)
    }

    // MARK: - 今天

    private func problem(_ id: String, firstSolvedDaysAgo: Double?) -> Problem {
        Problem(
            id: id, number: 1, title: id, difficulty: "Easy", technique: "贪心",
            statement: "s", elements: ["e"],
            pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
            retrospective: "", solutions: [], solvedAt: nil,
            firstSolvedAt: firstSolvedDaysAgo.map {
                Int(Date().addingTimeInterval(-$0 * 86_400).timeIntervalSince1970)
            },
            acceptedVersions: 0
        )
    }

    func testReviewsTodayCountsOnlyTodaysGrades() {
        let now = Date()
        let logs = [
            ReviewLog(problemID: "a", grade: .good, isRepeat: false, timestamp: now),
            ReviewLog(problemID: "b", grade: .again, isRepeat: false, timestamp: now),
            ReviewLog(
                problemID: "c", grade: .good, isRepeat: false,
                timestamp: now.addingTimeInterval(-3 * 86_400)
            ),
        ]

        XCTAssertEqual(summary.reviewsToday(logs: logs, now: now), 2)
    }

    func testReviewsTodayCountsRepeatsAsWorkToo() {
        let now = Date()
        let logs = [
            ReviewLog(problemID: "a", grade: .again, isRepeat: false, timestamp: now),
            ReviewLog(problemID: "a", grade: .good, isRepeat: true, timestamp: now),
        ]

        XCTAssertEqual(summary.reviewsToday(logs: logs, now: now), 2)
    }

    func testNewlySolvedTodayCountsFirstPassesOnly() {
        let now = Date()
        let problems = [
            problem("today", firstSolvedDaysAgo: 0),
            problem("lastweek", firstSolvedDaysAgo: 7),
            problem("unknown", firstSolvedDaysAgo: nil),
        ]

        XCTAssertEqual(summary.newlySolvedToday(problems: problems, now: now), 1)
    }

    func testAProblemPractisedAgainTodayIsNotNew() {
        // The distinction the two counters rest on: revisiting an old problem
        // is a review, and counting it as new would double-count one session.
        let now = Date()
        let old = Problem(
            id: "old", number: 1, title: "old", difficulty: "Easy", technique: "贪心",
            statement: "s", elements: ["e"],
            pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
            retrospective: "", solutions: [],
            solvedAt: Int(now.timeIntervalSince1970),
            firstSolvedAt: Int(now.addingTimeInterval(-400 * 86_400).timeIntervalSince1970),
            acceptedVersions: 0
        )

        XCTAssertEqual(summary.newlySolvedToday(problems: [old], now: now), 0)
    }
}

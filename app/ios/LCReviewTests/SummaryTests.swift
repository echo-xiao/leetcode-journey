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
            problemID: "15_3sum", track: .elements, grade: .good,
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
}

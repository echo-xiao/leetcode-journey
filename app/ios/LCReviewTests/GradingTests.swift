import XCTest
@testable import LCReview

final class GradingTests: XCTestCase {

    private let grading = Grading(fsrs: FSRS())
    private let now = Date(timeIntervalSince1970: 1_800_000_000)

    private func freshState(grade: Grade = .good) -> CardState {
        grading.apply(
            grade: grade, to: nil, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now
        ).state
    }

    func testFirstGradeCreatesStateAndSchedulesForward() {
        let (state, log) = grading.apply(
            grade: .good, to: nil, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now
        )
        XCTAssertEqual(state.problemID, "15_3sum")
        XCTAssertEqual(state.track, .elements)
        XCTAssertEqual(state.reviewCount, 1)
        XCTAssertEqual(state.lastReview, now)
        XCTAssertGreaterThan(state.due, now)
        XCTAssertNotNil(log)
        XCTAssertEqual(log?.gradeRaw, Grade.good.rawValue)
        XCTAssertEqual(log?.isRepeat, false)
    }

    func testAgainPutsTheTrackInTheMistakeBank() {
        let (state, _) = grading.apply(
            grade: .again, to: nil, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now
        )
        XCTAssertTrue(state.inMistakeBank)
        XCTAssertEqual(state.consecutiveGood, 0)
    }

    func testOneGoodIsNotEnoughToLeaveTheBank() {
        let state = freshState(grade: .again)
        let (after, _) = grading.apply(
            grade: .good, to: state, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now.addingTimeInterval(86_400)
        )
        XCTAssertTrue(after.inMistakeBank, "one 会 usually just means the answer was on screen minutes ago")
        XCTAssertEqual(after.consecutiveGood, 1)
    }

    func testTwoConsecutiveGoodLeaveTheBank() {
        var state = freshState(grade: .again)
        for day in 1...2 {
            state = grading.apply(
                grade: .good, to: state, problemID: "15_3sum", track: .elements,
                isRepeat: false, now: now.addingTimeInterval(Double(day) * 86_400)
            ).state
        }
        XCTAssertFalse(state.inMistakeBank)
        XCTAssertEqual(state.consecutiveGood, 2)
    }

    func testAGoodThenAnAgainResetsTheCount() {
        var state = freshState(grade: .again)
        state = grading.apply(
            grade: .good, to: state, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now.addingTimeInterval(86_400)
        ).state
        state = grading.apply(
            grade: .again, to: state, problemID: "15_3sum", track: .elements,
            isRepeat: false, now: now.addingTimeInterval(2 * 86_400)
        ).state
        XCTAssertEqual(state.consecutiveGood, 0)
        XCTAssertTrue(state.inMistakeBank)
    }

    func testHardDoesNotCountTowardLeavingTheBank() {
        var state = freshState(grade: .again)
        for day in 1...2 {
            state = grading.apply(
                grade: .hard, to: state, problemID: "15_3sum", track: .elements,
                isRepeat: false, now: now.addingTimeInterval(Double(day) * 86_400)
            ).state
        }
        XCTAssertTrue(state.inMistakeBank)
        XCTAssertEqual(state.consecutiveGood, 0)
    }

    func testARepeatLogsButChangesNothingElse() {
        let state = freshState(grade: .again)
        let dueBefore = state.due
        let stabilityBefore = state.stability
        let countBefore = state.reviewCount

        let (after, log) = grading.apply(
            grade: .good, to: state, problemID: "15_3sum", track: .elements,
            isRepeat: true, now: now.addingTimeInterval(120)
        )

        XCTAssertEqual(after.due, dueBefore, "a repeat must not reschedule")
        XCTAssertEqual(after.stability, stabilityBefore)
        XCTAssertEqual(after.reviewCount, countBefore)
        XCTAssertTrue(after.inMistakeBank, "answering minutes later does not clear a mistake")
        XCTAssertEqual(after.consecutiveGood, 0)
        XCTAssertEqual(log?.isRepeat, true, "but it is real work and belongs in the heatmap")
    }
}

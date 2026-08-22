import XCTest
@testable import LCReview

/// SessionRunner is @MainActor-isolated, so the test case must be too.
@MainActor
final class SessionRunnerTests: XCTestCase {

    private func runner(_ ids: [String]) -> SessionRunner {
        SessionRunner(steps: ids.map { SessionStep(problemID: $0, askOnly: nil) })
    }

    func testStartsOnTheStatementWithNothingRevealed() {
        let runner = runner(["a", "b"])
        XCTAssertEqual(runner.revealed, .statement)
        XCTAssertEqual(runner.current?.problemID, "a")
        XCTAssertEqual(runner.progress.total, 2)
    }

    func testTheElementsLayerAsksBeforeItReveals() {
        let runner = runner(["a"])
        XCTAssertEqual(runner.pendingGrade(), .elements)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .statement, "reveal must not bypass the question")
    }

    func testGradingRevealsTheLayerItAskedAbout() {
        let runner = runner(["a"])
        runner.record(grade: .good)
        XCTAssertEqual(runner.revealed, .elements)
        XCTAssertEqual(runner.pendingGrade(), .pseudocode)
    }

    func testReferenceLayersRevealWithoutAsking() {
        let runner = runner(["a"])
        runner.record(grade: .good)  // elements
        runner.record(grade: .good)  // pseudocode
        XCTAssertEqual(runner.revealed, .pseudocode)
        XCTAssertNil(runner.pendingGrade())
        runner.reveal()
        XCTAssertEqual(runner.revealed, .retrospective)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .solutions)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .solutions, "the chain ends here")
    }

    func testAgainSchedulesARepeatOfOnlyThatLayer() {
        let runner = runner(["a"])
        runner.record(grade: .again)  // elements
        XCTAssertEqual(
            runner.repeatsScheduled,
            [SessionStep(problemID: "a", askOnly: .elements)]
        )
    }

    func testRepeatsDoNotChangeTheAdvertisedTotal() {
        let runner = runner(["a", "b"])
        runner.record(grade: .again)
        XCTAssertEqual(runner.progress.total, 2, "a repeat is extra, not one of the N")
    }

    func testRepeatsAreAppendedAfterTheOriginalQueue() {
        let runner = runner(["a", "b"])
        runner.record(grade: .again)   // a/elements fails
        runner.advance()               // -> b
        XCTAssertEqual(runner.current?.problemID, "b")
        runner.advance()               // -> the repeat
        XCTAssertEqual(runner.current, SessionStep(problemID: "a", askOnly: .elements))
        XCTAssertFalse(runner.isFinished)
        runner.record(grade: .good)
        runner.advance()
        XCTAssertTrue(runner.isFinished)
    }

    func testARepeatStepAsksOnlyItsOwnLayerAndThenEnds() {
        let runner = SessionRunner(
            steps: [SessionStep(problemID: "a", askOnly: .pseudocode)]
        )
        XCTAssertEqual(runner.pendingGrade(), .pseudocode)
        runner.record(grade: .good)
        XCTAssertNil(runner.pendingGrade())
        XCTAssertEqual(runner.revealed, .pseudocode)
    }

    func testALayerRepeatsAtMostTwicePerSession() {
        let runner = runner(["a"])
        runner.record(grade: .again)          // 1st repeat scheduled
        runner.advance()
        runner.record(grade: .again)          // 2nd repeat scheduled
        runner.advance()
        runner.record(grade: .again)          // must NOT schedule a 3rd
        XCTAssertEqual(runner.repeatsScheduled.count, 2)
    }

    func testAdvancingMidChainJustMovesOn() {
        let runner = runner(["a", "b"])
        runner.record(grade: .good)  // only the elements track answered
        runner.advance()
        XCTAssertEqual(runner.current?.problemID, "b")
        XCTAssertEqual(runner.revealed, .statement, "the new card starts closed")
        XCTAssertEqual(runner.progress.done, 1)
    }

    func testGoingBackRestoresHowFarThatCardWasOpen() {
        let runner = runner(["a", "b"])
        runner.record(grade: .good)   // a: elements open
        runner.record(grade: .good)   // a: pseudocode open
        runner.reveal()               // a: retrospective open
        runner.advance()
        runner.goBack()

        XCTAssertEqual(runner.current?.problemID, "a")
        XCTAssertEqual(runner.revealed, .retrospective, "a revisit is a look, not a reset")
    }

    func testGoingBackDoesNotReAskAGradedLayer() {
        let runner = runner(["a", "b"])
        runner.record(grade: .good)   // elements graded
        runner.record(grade: .again)  // pseudocode graded
        runner.advance()
        runner.goBack()

        XCTAssertNil(runner.pendingGrade(), "both tracks were answered; revisiting must not re-ask")
    }

    func testGoingBackStillLetsYouFinishALayerYouSkipped() {
        let runner = runner(["a", "b"])
        runner.record(grade: .good)   // only elements answered
        runner.advance()
        runner.goBack()

        XCTAssertEqual(
            runner.pendingGrade(), .pseudocode,
            "an unanswered layer is unfinished work, not a re-grade"
        )
    }

    func testProgressDoesNotRewindWhenGoingBack() {
        let runner = runner(["a", "b"])
        runner.advance()
        XCTAssertEqual(runner.progress.done, 1)
        runner.goBack()
        XCTAssertEqual(runner.progress.done, 1, "the counter tracks how far you got")
    }

    func testGoingBackFromTheFirstCardDoesNothing() {
        let runner = runner(["a", "b"])
        runner.goBack()
        XCTAssertEqual(runner.current?.problemID, "a")
    }
}

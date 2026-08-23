import XCTest
@testable import LCReview

@MainActor
final class SessionRunnerTests: XCTestCase {

    private func runner(_ ids: [String]) -> SessionRunner {
        SessionRunner(steps: ids.map { SessionStep(problemID: $0, isRepeat: false) })
    }

    func testStartsOnTheFirstProblemShowingOnlyTheStatement() {
        let runner = runner(["a", "b"])

        XCTAssertEqual(runner.current?.problemID, "a")
        XCTAssertEqual(runner.revealed, .statement)
        XCTAssertFalse(runner.isFinished)
    }

    func testTapRevealsOneLayerAtATime() {
        let runner = runner(["a"])

        runner.reveal()
        XCTAssertEqual(runner.revealed, .elements)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .pseudocode)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .retrospective)
        runner.reveal()
        XCTAssertEqual(runner.revealed, .solutions)
    }

    func testTappingPastTheLastLayerDoesNothing() {
        // The whole point of splitting reveal from grade: a tap can never
        // carry you out of the problem, however many times it lands.
        let runner = runner(["a", "b"])
        for _ in 0..<10 { runner.reveal() }

        XCTAssertEqual(runner.revealed, .solutions)
        XCTAssertEqual(runner.current?.problemID, "a", "tapping must never change problem")
        XCTAssertEqual(runner.index, 0)
    }

    func testGradingIsWhatMovesToTheNextProblem() {
        let runner = runner(["a", "b"])

        runner.grade(.good)

        XCTAssertEqual(runner.current?.problemID, "b")
        XCTAssertEqual(runner.revealed, .statement, "the next card starts closed")
    }

    func testGradingWorksWithoutRevealingAnything() {
        // The bar is on screen from the first second; nothing has to be
        // opened before it can be pressed.
        let runner = runner(["a", "b"])

        runner.grade(.hard)

        XCTAssertEqual(runner.current?.problemID, "b")
    }

    func testFinishedAfterGradingTheLastProblem() {
        let runner = runner(["a"])

        runner.grade(.good)

        XCTAssertTrue(runner.isFinished)
        XCTAssertNil(runner.current)
    }

    func testGradingWhenFinishedDoesNothing() {
        let runner = runner(["a"])
        runner.grade(.good)

        runner.grade(.again)

        XCTAssertEqual(runner.index, 1, "no step to grade, so nothing moves")
        XCTAssertTrue(runner.repeatsScheduled.isEmpty)
    }

    func testAgainQueuesTheProblemAgainAtTheEnd() {
        let runner = runner(["a", "b"])

        runner.grade(.again)

        XCTAssertEqual(runner.repeatsScheduled, [SessionStep(problemID: "a", isRepeat: true)])
        XCTAssertEqual(runner.current?.problemID, "b")
        runner.grade(.good)
        XCTAssertEqual(runner.current?.problemID, "a")
        XCTAssertEqual(runner.current?.isRepeat, true)
    }

    func testHardAndGoodQueueNothing() {
        let runner = runner(["a", "b"])

        runner.grade(.hard)
        runner.grade(.good)

        XCTAssertTrue(runner.repeatsScheduled.isEmpty)
        XCTAssertTrue(runner.isFinished)
    }

    func testAProblemIsNotQueuedMoreThanTwice() {
        let runner = runner(["a"])

        runner.grade(.again)   // queues repeat 1
        runner.grade(.again)   // this is the repeat: must not queue again
        XCTAssertEqual(runner.repeatsScheduled.count, 1)
        XCTAssertTrue(runner.isFinished)
    }

    func testARepeatFailedAgainIsNotRequeued() {
        let runner = runner(["a"])
        runner.grade(.again)

        XCTAssertEqual(runner.current?.isRepeat, true)
        runner.grade(.again)

        XCTAssertEqual(
            runner.repeatsScheduled.count, 1,
            "a bad problem must not fill the session with itself"
        )
    }

    func testProgressCountsPlannedProblemsNotRepeats() {
        let runner = runner(["a", "b"])
        XCTAssertEqual(runner.progress.total, 2)
        XCTAssertEqual(runner.progress.done, 0)

        runner.grade(.again)
        XCTAssertEqual(runner.progress.done, 1)

        runner.grade(.good)
        XCTAssertEqual(runner.progress.done, 2)

        // Now on the repeat, which is past the advertised length.
        runner.grade(.good)
        XCTAssertEqual(runner.progress.done, 2, "extra work must not read as 3 / 2")
        XCTAssertEqual(runner.progress.total, 2)
    }

    func testEachProblemRemembersHowFarItWasOpened() {
        let runner = runner(["a", "b"])
        runner.reveal()
        runner.reveal()
        XCTAssertEqual(runner.revealed, .pseudocode)

        runner.grade(.good)

        XCTAssertEqual(runner.revealed, .statement)
    }

    func testAnEmptySessionIsFinishedImmediately() {
        let runner = runner([])

        XCTAssertTrue(runner.isFinished)
        XCTAssertNil(runner.current)
        XCTAssertEqual(runner.progress.done, 0)
        XCTAssertEqual(runner.progress.total, 0)
    }
}

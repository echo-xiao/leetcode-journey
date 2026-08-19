import XCTest
@testable import LCReview

private struct BaselineStep: Codable {
    let grade: Int
    let elapsedDays: Double
    let stability: Double
    let difficulty: Double
    let intervalDays: Double
}

private struct BaselineCase: Codable {
    let sequence: [Int]
    let steps: [BaselineStep]
}

private struct Baseline: Codable {
    let parameters: [Double]
    let desiredRetention: Double
    let cases: [BaselineCase]
}

final class FSRSTests: XCTestCase {

    private func loadBaseline() throws -> Baseline {
        let url = try XCTUnwrap(
            Bundle(for: Self.self).url(forResource: "fsrs-baseline", withExtension: "json"),
            "fsrs-baseline.json is not in the test bundle — check Target Membership"
        )
        return try JSONDecoder().decode(Baseline.self, from: Data(contentsOf: url))
    }

    /// The port is only trustworthy if it reproduces the reference
    /// implementation. If this fails, fix FSRS.swift — never the fixture.
    /// `FSRS.defaultParameters` is what the app actually ships with — the
    /// rest of this test only exercises `baseline.parameters`, which could
    /// silently drift from it (a mistyped digit, a stale copy-paste) without
    /// this line ever noticing.
    func testDefaultParametersMatchTheBaseline() throws {
        let baseline = try loadBaseline()
        XCTAssertEqual(FSRS.defaultParameters, baseline.parameters)
    }

    func testMatchesTheReferenceImplementation() throws {
        let baseline = try loadBaseline()
        let fsrs = FSRS(
            parameters: baseline.parameters,
            desiredRetention: baseline.desiredRetention
        )

        for testCase in baseline.cases {
            var state: MemoryState?
            for (index, step) in testCase.steps.enumerated() {
                let grade = try XCTUnwrap(Grade(rawValue: step.grade))
                let label = "sequence \(testCase.sequence) step \(index)"

                if let current = state {
                    state = fsrs.nextState(
                        from: current, grade: grade, elapsedDays: step.elapsedDays
                    )
                } else {
                    state = fsrs.initialState(grade: grade)
                }

                let produced = try XCTUnwrap(state)
                XCTAssertEqual(
                    produced.stability, step.stability, accuracy: 1e-6,
                    "stability mismatch at \(label)"
                )
                XCTAssertEqual(
                    produced.difficulty, step.difficulty, accuracy: 1e-6,
                    "difficulty mismatch at \(label)"
                )
                XCTAssertEqual(
                    fsrs.intervalDays(for: produced), step.intervalDays, accuracy: 1e-4,
                    "interval mismatch at \(label)"
                )
            }
        }
    }

    /// The spec's headline claim about backlog: answering a badly overdue card
    /// correctly must stretch the next interval, not collapse it.
    func testAnOverdueSuccessStretchesTheInterval() {
        let fsrs = FSRS()
        var state = fsrs.initialState(grade: .good)
        state = fsrs.nextState(from: state, grade: .good, elapsedDays: 1)
        let onTime = fsrs.nextState(from: state, grade: .good, elapsedDays: 3)
        let overdue = fsrs.nextState(from: state, grade: .good, elapsedDays: 300)

        XCTAssertGreaterThan(
            fsrs.intervalDays(for: overdue), fsrs.intervalDays(for: onTime),
            "a card recalled after a long delay is stronger than modelled"
        )
    }

    func testDifficultyStaysInRange() {
        let fsrs = FSRS()
        var state = fsrs.initialState(grade: .again)
        for _ in 0..<50 {
            state = fsrs.nextState(from: state, grade: .again, elapsedDays: 1)
            XCTAssertGreaterThanOrEqual(state.difficulty, 1.0)
            XCTAssertLessThanOrEqual(state.difficulty, 10.0)
            XCTAssertGreaterThan(state.stability, 0.0)
        }
    }

    /// Reachable through clock skew, a timezone change, or a `lastReview`
    /// that lands in the future — not just a hostile input. Before the
    /// short-term/long-term branch existed, `elapsedDays = -0.5` pushed
    /// retrievability above 1 and collapsed stability toward the floor on a
    /// correct Good answer, and around -4.9 the long-term formula's `pow` of
    /// a negative base produced NaN that would have been persisted.
    func testNegativeElapsedDaysDoesNotProduceNaN() {
        let fsrs = FSRS()
        let state = fsrs.initialState(grade: .good)

        for elapsedDays in [-0.5, -10.0] {
            let next = fsrs.nextState(from: state, grade: .good, elapsedDays: elapsedDays)
            XCTAssertFalse(next.stability.isNaN, "stability is NaN at elapsedDays \(elapsedDays)")
            XCTAssertFalse(next.difficulty.isNaN, "difficulty is NaN at elapsedDays \(elapsedDays)")
            XCTAssertGreaterThan(next.stability, 0, "stability must stay positive at elapsedDays \(elapsedDays)")
        }
    }

    func testRetrievabilityFallsFromOneTowardZero() {
        let fsrs = FSRS()
        let state = MemoryState(stability: 10, difficulty: 5)
        XCTAssertEqual(fsrs.retrievability(state: state, elapsedDays: 0), 1.0, accuracy: 1e-9)
        let day10 = fsrs.retrievability(state: state, elapsedDays: 10)
        let day100 = fsrs.retrievability(state: state, elapsedDays: 100)
        XCTAssertLessThan(day10, 1.0)
        XCTAssertLessThan(day100, day10)
        XCTAssertGreaterThan(day100, 0.0)
    }
}

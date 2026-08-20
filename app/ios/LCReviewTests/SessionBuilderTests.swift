import XCTest
@testable import LCReview

final class SessionBuilderTests: XCTestCase {

    private let builder = SessionBuilder()
    private let now = Date(timeIntervalSince1970: 1_800_000_000)

    private func problem(_ id: String, technique: String = "数组双指针") -> Problem {
        Problem(
            id: id, number: Int(id.prefix(while: \.isNumber)) ?? 0, title: id,
            difficulty: "Medium", technique: technique, statement: "s",
            elements: ["e"], pseudocode: "p", retrospective: "", solutions: []
        )
    }

    private func state(
        _ id: String, track: Track = .elements, dueOffsetDays: Double,
        lastReviewOffsetDays: Double? = nil, inBank: Bool = false
    ) -> CardState {
        CardState(
            problemID: id, track: track, stability: 1, difficulty: 5,
            due: now.addingTimeInterval(dueOffsetDays * 86_400),
            lastReview: lastReviewOffsetDays.map {
                now.addingTimeInterval($0 * 86_400)
            },
            reviewCount: 1, inMistakeBank: inBank
        )
    }

    func testMostOverdueComesFirst() {
        let problems = ["a", "b", "c"].map { problem($0) }
        let states = [
            state("a", dueOffsetDays: -1),
            state("b", dueOffsetDays: -30),
            state("c", dueOffsetDays: -5),
        ]
        let session = builder.build(
            scope: .all, length: 10, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["b", "c", "a"])
    }

    func testUnseenProblemsCountAsDue() {
        let problems = ["a", "b"].map { problem($0) }
        // "b" has never been reviewed, so it has no state at all.
        let session = builder.build(
            scope: .all, length: 10, problems: problems,
            states: [state("a", dueOffsetDays: 5)], now: now
        )
        XCTAssertEqual(session.first?.id, "b")
    }

    func testTopsUpWithNotYetDueLeastRecentlyReviewedFirst() {
        let problems = ["a", "b", "c"].map { problem($0) }
        let states = [
            state("a", dueOffsetDays: -1, lastReviewOffsetDays: -2),
            state("b", dueOffsetDays: 5, lastReviewOffsetDays: -40),
            state("c", dueOffsetDays: 5, lastReviewOffsetDays: -3),
        ]
        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["a", "b", "c"])
    }

    func testLengthIsCappedByHowManyProblemsExist() {
        // 并查集 has exactly one problem in the real library.
        let problems = [problem("only", technique: "并查集")]
        let session = builder.build(
            scope: .technique("并查集"), length: 10, problems: problems,
            states: [], now: now
        )
        XCTAssertEqual(session.count, 1, "a short technique yields a short session")
    }

    func testNoProblemAppearsTwiceToPadTheLength() {
        let problems = [problem("a"), problem("b")]
        let session = builder.build(
            scope: .all, length: 10, problems: problems, states: [], now: now
        )
        XCTAssertEqual(Set(session.map(\.id)).count, session.count)
        XCTAssertEqual(session.count, 2)
    }

    func testTechniqueScopeExcludesEverythingElse() {
        let problems = [
            problem("a", technique: "滑动窗口"),
            problem("b", technique: "二叉树"),
        ]
        let session = builder.build(
            scope: .technique("滑动窗口"), length: 10, problems: problems,
            states: [], now: now
        )
        XCTAssertEqual(session.map(\.id), ["a"])
    }

    func testAProblemQualifiesWhenEitherTrackIsDue() {
        let problems = [problem("a")]
        let states = [
            state("a", track: .elements, dueOffsetDays: 30),
            state("a", track: .pseudocode, dueOffsetDays: -2),
        ]
        let session = builder.build(
            scope: .all, length: 10, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["a"])
    }

    func testMistakeScopeIgnoresDueDatesAndTakesOnlyBankedTracks() {
        let problems = ["a", "b", "c"].map { problem($0) }
        let states = [
            // Banked but not due for a month — must still show up.
            state("a", dueOffsetDays: 30, inBank: true),
            // Badly overdue but not banked — must not.
            state("b", dueOffsetDays: -90, inBank: false),
            state("c", dueOffsetDays: 1, inBank: true),
        ]
        let session = builder.build(
            scope: .mistakes, length: 10, problems: problems, states: states, now: now
        )
        XCTAssertEqual(Set(session.map(\.id)), ["a", "c"])
    }

    func testMistakeScopeOrdersByMostRecentFailure() {
        let problems = ["old", "recent"].map { problem($0) }
        let states = [
            state("old", dueOffsetDays: 1, lastReviewOffsetDays: -30, inBank: true),
            state("recent", dueOffsetDays: 1, lastReviewOffsetDays: -1, inBank: true),
        ]
        let session = builder.build(
            scope: .mistakes, length: 10, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["recent", "old"])
    }
}

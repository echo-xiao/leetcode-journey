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

    /// Builds a full pair of rows (elements + pseudocode) for one problem, so
    /// the problem's `earliestDue` genuinely reflects the offsets given
    /// rather than collapsing to `now` because a track was never recorded.
    /// `state(...)` only ever makes one row, which is why every existing
    /// fixture in this file has an implicit "pseudocode is due right now"
    /// track and can never land in `notYetDue`.
    private func bothTracksState(
        _ id: String,
        elementsDueOffsetDays: Double,
        pseudocodeDueOffsetDays: Double,
        lastReviewOffsetDays: Double? = nil
    ) -> [CardState] {
        [
            state(
                id, track: .elements, dueOffsetDays: elementsDueOffsetDays,
                lastReviewOffsetDays: lastReviewOffsetDays
            ),
            state(
                id, track: .pseudocode, dueOffsetDays: pseudocodeDueOffsetDays,
                lastReviewOffsetDays: lastReviewOffsetDays
            ),
        ]
    }

    func testTopsUpWithNotYetDueLeastRecentlyReviewedFirst() {
        let problems = ["a", "b", "c"].map { problem($0) }
        let states =
            // Genuinely overdue: both tracks recorded and in the past.
            bothTracksState(
                "a", elementsDueOffsetDays: -1, pseudocodeDueOffsetDays: -1,
                lastReviewOffsetDays: -2
            )
            // Genuinely not yet due: both tracks recorded and in the future.
            // Reviewed 40 days ago, far longer ago than "c" below.
            + bothTracksState(
                "b", elementsDueOffsetDays: 5, pseudocodeDueOffsetDays: 6,
                lastReviewOffsetDays: -40
            )
            // Also not yet due, but reviewed far more recently than "b", so
            // it must sort after "b" among the top-ups.
            + bothTracksState(
                "c", elementsDueOffsetDays: 5, pseudocodeDueOffsetDays: 6,
                lastReviewOffsetDays: -3
            )
        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["a", "b", "c"])
    }

    func testSessionFillsToLengthFromTopUpsWhenNotEnoughIsDue() {
        let problems = ["due", "n1", "n2", "n3", "n4"].map { problem($0) }
        let states =
            [state("due", dueOffsetDays: -1)]
            + bothTracksState("n1", elementsDueOffsetDays: 5, pseudocodeDueOffsetDays: 5, lastReviewOffsetDays: -10)
            + bothTracksState("n2", elementsDueOffsetDays: 6, pseudocodeDueOffsetDays: 6, lastReviewOffsetDays: -9)
            + bothTracksState("n3", elementsDueOffsetDays: 7, pseudocodeDueOffsetDays: 7, lastReviewOffsetDays: -8)
            + bothTracksState("n4", elementsDueOffsetDays: 8, pseudocodeDueOffsetDays: 8, lastReviewOffsetDays: -7)
        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: states, now: now
        )
        XCTAssertEqual(
            session.count, 3,
            "only one problem is due, so the other two seats must be filled from the not-yet-due top-up pool"
        )
    }

    func testProblemQualifiesWhenItsOtherTrackHasNeverBeenRecordedEvenIfTheRecordedTrackIsFarOff() {
        let problems = ["d1", "a", "n1"].map { problem($0) }
        let states =
            // Deeply overdue: leads the queue regardless of what happens to "a".
            [state("d1", dueOffsetDays: -100)]
            // Elements is due a month from now, but pseudocode has no row at
            // all. An unrecorded track is due right now, so "a" must land in
            // the *due* bucket (earliestDue == now), not the not-yet-due one
            // — even though its one recorded track is far in the future.
            // Reviewed very recently, so if it were (wrongly) treated as
            // not-yet-due it would sort *behind* "n1" below and get cut by
            // length: 2.
            + [state("a", track: .elements, dueOffsetDays: 30, lastReviewOffsetDays: -1)]
            // Genuinely not yet due, both tracks recorded, reviewed long ago
            // so it would sort ahead of "a" among not-yet-due top-ups.
            + bothTracksState("n1", elementsDueOffsetDays: 50, pseudocodeDueOffsetDays: 50, lastReviewOffsetDays: -1000)
        let session = builder.build(
            scope: .all, length: 2, problems: problems, states: states, now: now
        )
        XCTAssertEqual(
            session.map(\.id), ["d1", "a"],
            "\"a\" must be treated as due because its pseudocode track was never recorded, " +
            "so it beats \"n1\" for the second slot despite \"n1\" being reviewed longer ago"
        )
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

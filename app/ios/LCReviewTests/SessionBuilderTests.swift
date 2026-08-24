import XCTest
@testable import LCReview

final class SessionBuilderTests: XCTestCase {

    private let builder = SessionBuilder()
    private let now = Date(timeIntervalSince1970: 1_800_000_000)

    private func problem(
        _ id: String, technique: String = "数组双指针",
        solvedDaysAgo: Double? = nil, firstSolvedDaysAgo: Double? = nil
    ) -> Problem {
        Problem(
            id: id, number: Int(id.prefix(while: \.isNumber)) ?? 0, title: id,
            difficulty: "Medium", technique: technique, statement: "s",
            elements: ["e"], pseudocode: [PseudocodeBlock(kind: .text, text: "p")],
            retrospective: "", solutions: [],
            solvedAt: solvedDaysAgo.map {
                Int(now.addingTimeInterval(-$0 * 86_400).timeIntervalSince1970)
            },
            firstSolvedAt: firstSolvedDaysAgo.map {
                Int(now.addingTimeInterval(-$0 * 86_400).timeIntervalSince1970)
            }
        )
    }

    private func state(
        _ id: String, dueOffsetDays: Double,
        lastReviewOffsetDays: Double? = nil, inBank: Bool = false
    ) -> CardState {
        CardState(
            problemID: id, stability: 1, difficulty: 5,
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
            // Overdue.
            state("a", dueOffsetDays: -1, lastReviewOffsetDays: -2),
            // Not yet due, reviewed 40 days ago -- far longer ago than "c".
            state("b", dueOffsetDays: 5, lastReviewOffsetDays: -40),
            // Also not yet due, but touched recently, so it sorts after "b"
            // among the top-ups.
            state("c", dueOffsetDays: 5, lastReviewOffsetDays: -3),
        ]
        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["a", "b", "c"])
    }

    func testSessionFillsToLengthFromTopUpsWhenNotEnoughIsDue() {
        let problems = ["due", "n1", "n2", "n3", "n4"].map { problem($0) }
        let states =
            [state("due", dueOffsetDays: -1)]
            + [state("n1", dueOffsetDays: 5, lastReviewOffsetDays: -10)]
            + [state("n2", dueOffsetDays: 6, lastReviewOffsetDays: -9)]
            + [state("n3", dueOffsetDays: 7, lastReviewOffsetDays: -8)]
            + [state("n4", dueOffsetDays: 8, lastReviewOffsetDays: -7)]
        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: states, now: now
        )
        XCTAssertEqual(
            session.count, 3,
            "only one problem is due, so the other two seats must be filled from the not-yet-due top-up pool"
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

    func testADuplicateRowSchedulesFromTheEarlierDate() {
        // One row per problem is the invariant, but the builder does not
        // assume it: a stray second row must not make the choice arbitrary.
        let problems = [problem("a")]
        let states = [
            state("a", dueOffsetDays: 30),
            state("a", dueOffsetDays: -2),
        ]
        let session = builder.build(
            scope: .all, length: 10, problems: problems, states: states, now: now
        )
        XCTAssertEqual(session.map(\.id), ["a"])
    }

    func testMistakeScopeIgnoresDueDatesAndTakesOnlyBankedProblems() {
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

    func testNeverReviewedProblemsLeadWithTheMostRecentlySolvedFirst() {
        // Every problem in the library starts here: no CardState at all, so
        // they are all equally "maximally overdue". Without a tiebreak the
        // order falls out of the array, which means a problem solved
        // yesterday sits behind one solved in 2017.
        let problems = [
            problem("old", solvedDaysAgo: 900),
            problem("yesterday", solvedDaysAgo: 1),
            problem("lastmonth", solvedDaysAgo: 30),
        ]

        let session = builder.build(
            scope: .all, length: 3, problems: problems, states: [], now: now
        )

        XCTAssertEqual(session.map(\.id), ["yesterday", "lastmonth", "old"])
    }

    func testAProblemWithNoSolvedDateSortsAfterOnesThatHaveIt() {
        // Unknown is not the same as ancient. A problem the backfill could
        // not answer for should not jump the queue, and should not be
        // ordered against a real date as if it were 1970.
        let problems = [
            problem("unknown"),
            problem("old", solvedDaysAgo: 900),
        ]

        let session = builder.build(
            scope: .all, length: 2, problems: problems, states: [], now: now
        )

        XCTAssertEqual(session.map(\.id), ["old", "unknown"])
    }

    func testAnActualDueDateStillOutranksRecency() {
        // Recency only breaks ties among problems with no history. Once a
        // problem has been graded, FSRS owns when it comes back.
        let problems = [
            problem("graded", solvedDaysAgo: 900),
            problem("fresh", solvedDaysAgo: 1),
        ]
        let states = [state("fresh", dueOffsetDays: 30, lastReviewOffsetDays: -1)]

        let session = builder.build(
            scope: .all, length: 2, problems: problems, states: states, now: now
        )

        XCTAssertEqual(
            session.map(\.id), ["graded", "fresh"],
            "\"fresh\" was graded and is not due for a month, so it drops behind the unseen one"
        )
    }

    // MARK: - 按最近刷

    func testRecentScopeIsOrderedByWhenItWasSolvedNewestFirst() {
        let problems = [
            problem("old", solvedDaysAgo: 400),
            problem("yesterday", solvedDaysAgo: 1),
            problem("week", solvedDaysAgo: 6),
        ]

        let session = builder.build(
            scope: .recent(withinDays: nil), length: 10,
            problems: problems, states: [], now: now
        )

        XCTAssertEqual(session.map(\.id), ["yesterday", "week", "old"])
    }

    func testRecentScopeIgnoresTheScheduleOnPurpose() {
        // This is the one scope where FSRS does not decide the order. Asking
        // for "what I just solved" and getting the most overdue card instead
        // would make the entry pointless.
        let problems = [
            problem("yesterday", solvedDaysAgo: 1),
            problem("ancient", solvedDaysAgo: 900),
        ]
        let states = [
            state("yesterday", dueOffsetDays: 30, lastReviewOffsetDays: -1),
            state("ancient", dueOffsetDays: -300, lastReviewOffsetDays: -300),
        ]

        let session = builder.build(
            scope: .recent(withinDays: nil), length: 10,
            problems: problems, states: states, now: now
        )

        XCTAssertEqual(session.map(\.id), ["yesterday", "ancient"])
    }

    func testRecentScopeHonoursItsWindow() {
        let problems = [
            problem("d1", solvedDaysAgo: 1),
            problem("d20", solvedDaysAgo: 20),
            problem("d200", solvedDaysAgo: 200),
        ]

        let week = builder.build(
            scope: .recent(withinDays: 7), length: 10,
            problems: problems, states: [], now: now
        )
        let month = builder.build(
            scope: .recent(withinDays: 30), length: 10,
            problems: problems, states: [], now: now
        )

        XCTAssertEqual(week.map(\.id), ["d1"])
        XCTAssertEqual(month.map(\.id), ["d1", "d20"])
    }

    func testRecentScopeSkipsProblemsWithNoKnownDate() {
        // Ordering by a date they do not have would put them somewhere
        // arbitrary. Leaving them out is honest: this entry is about dates.
        let problems = [problem("known", solvedDaysAgo: 3), problem("unknown")]

        let session = builder.build(
            scope: .recent(withinDays: nil), length: 10,
            problems: problems, states: [], now: now
        )

        XCTAssertEqual(session.map(\.id), ["known"])
    }

    // MARK: - 积压

    func testBacklogCountsEveryProblemDueNowNotJustOneSession() {
        // The number the home screen used to hide. It is not capped by
        // session length: the point of showing it is how much is waiting, and
        // a figure capped at ten would say nothing.
        let problems = (0..<25).map { problem("p\($0)", solvedDaysAgo: Double($0 + 1)) }

        let backlog = builder.backlog(scope: .all, problems: problems, states: [], now: now)

        XCTAssertEqual(backlog, 25)
    }

    func testBacklogExcludesProblemsNotYetDue() {
        let problems = ["due", "later"].map { problem($0) }
        let states = [
            state("due", dueOffsetDays: -1),
            state("later", dueOffsetDays: 5),
        ]

        XCTAssertEqual(
            builder.backlog(scope: .all, problems: problems, states: states, now: now), 1
        )
    }

    func testBacklogIsScopedToTheTechnique() {
        let problems = [
            problem("a", technique: "二叉树"),
            problem("b", technique: "二叉树"),
            problem("c", technique: "贪心"),
        ]

        XCTAssertEqual(
            builder.backlog(
                scope: .technique("二叉树"), problems: problems, states: [], now: now
            ),
            2
        )
    }

    func testBacklogOfTheMistakeScopeIsTheWholeBank() {
        // Nothing in the bank is "not yet due" -- being in it is the whole
        // condition -- so the backlog is its size.
        let problems = ["a", "b", "c"].map { problem($0) }
        let states = [
            state("a", dueOffsetDays: 30, inBank: true),
            state("b", dueOffsetDays: -90, inBank: false),
            state("c", dueOffsetDays: 1, inBank: true),
        ]

        XCTAssertEqual(
            builder.backlog(scope: .mistakes, problems: problems, states: states, now: now), 2
        )
    }

    func testBacklogOfARecentWindowRespectsThatWindow() {
        // The bug this pins down: the count and the queue each had their own
        // copy of "is this problem in scope", and the count's copy forgot the
        // day window, so every time slice reported the whole library.
        let problems = [
            problem("d1", solvedDaysAgo: 1),
            problem("d20", solvedDaysAgo: 20),
            problem("d200", solvedDaysAgo: 200),
        ]

        XCTAssertEqual(
            builder.backlog(
                scope: .recent(withinDays: 7), problems: problems, states: [], now: now
            ),
            1
        )
        XCTAssertEqual(
            builder.backlog(
                scope: .recent(withinDays: 30), problems: problems, states: [], now: now
            ),
            2
        )
        XCTAssertEqual(
            builder.backlog(
                scope: .recent(withinDays: nil), problems: problems, states: [], now: now
            ),
            3
        )
    }

    func testTheCountAndTheQueueAgreeOnEveryScope() {
        // A queue can be shorter than its backlog because of session length,
        // but it must never contain a problem the count excluded.
        let problems = [
            problem("a", technique: "二叉树", solvedDaysAgo: 1),
            problem("b", technique: "贪心", solvedDaysAgo: 40),
            problem("c", technique: "二叉树", solvedDaysAgo: 400),
        ]
        let scopes: [SessionScope] = [
            .all, .technique("二叉树"), .recent(withinDays: 7), .recent(withinDays: nil),
        ]

        for scope in scopes {
            let queue = builder.build(
                scope: scope, length: 100, problems: problems, states: [], now: now
            )
            let count = builder.backlog(
                scope: scope, problems: problems, states: [], now: now
            )
            XCTAssertEqual(queue.count, count, "\(scope) disagrees")
        }
    }

    // MARK: - 范围总数

    func testTotalCountsEveryProblemInScopeIncludingOnesNotDue() {
        // The counterpart to backlog: what you have done, not what is
        // waiting. A problem reviewed this morning still belongs to the week
        // it was solved in.
        let problems = ["a", "b"].map { problem($0) }
        let states = [
            state("a", dueOffsetDays: -1),
            state("b", dueOffsetDays: 30),
        ]

        XCTAssertEqual(builder.total(scope: .all, problems: problems, states: states, now: now), 2)
        XCTAssertEqual(
            builder.backlog(scope: .all, problems: problems, states: states, now: now), 1
        )
    }

    func testTotalRespectsTheRecentWindow() {
        let problems = [
            problem("d1", solvedDaysAgo: 1),
            problem("d200", solvedDaysAgo: 200),
        ]
        let states = [state("d1", dueOffsetDays: 30)]

        XCTAssertEqual(
            builder.total(
                scope: .recent(withinDays: 7), problems: problems, states: states, now: now
            ),
            1,
            "reviewing it does not remove it from the week it was solved in"
        )
        XCTAssertEqual(
            builder.backlog(
                scope: .recent(withinDays: 7), problems: problems, states: states, now: now
            ),
            0
        )
    }

    func testTotalIsScopedToTheTechnique() {
        let problems = [
            problem("a", technique: "二叉树"),
            problem("b", technique: "贪心"),
        ]

        XCTAssertEqual(
            builder.total(scope: .technique("二叉树"), problems: problems, states: [], now: now),
            1
        )
    }
}

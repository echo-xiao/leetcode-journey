import Foundation

/// What a session is scoped to. The home screen picks exactly one.
enum SessionScope: Equatable {
    case all
    case technique(String)
    case mistakes
    /// Problems solved on LeetCode within the last `withinDays` days, or the
    /// whole library when nil. The only scope ordered by when a problem was
    /// solved rather than by when it is due.
    case recent(withinDays: Int?)
}

/// Picks which problems a session contains, and in what order.
///
/// Deliberately never pads a short session by repeating a problem: a technique
/// with one problem yields a session of one. The library's real shape shows
/// through rather than being disguised.
struct SessionBuilder {

    func build(
        scope: SessionScope,
        length: Int,
        problems: [Problem],
        states: [CardState],
        now: Date
    ) -> [Problem] {
        var byProblem: [String: [CardState]] = [:]
        for state in states {
            byProblem[state.problemID, default: []].append(state)
        }

        let candidates = problems.filter { problem in
            switch scope {
            case .all:
                return true
            case .technique(let name):
                return problem.technique == name
            case .mistakes:
                return byProblem[problem.id]?.contains(where: \.inMistakeBank) ?? false
            case .recent(let withinDays):
                // A problem with no known date is left out rather than
                // ordered by a date it does not have. This entry is about
                // dates; a problem without one has nothing to say here.
                guard let solvedAt = problem.solvedAt else { return false }
                guard let withinDays else { return true }
                let cutoff = now.addingTimeInterval(-Double(withinDays) * 86_400)
                return Date(timeIntervalSince1970: TimeInterval(solvedAt)) >= cutoff
            }
        }

        let ordered: [Problem]
        if case .recent = scope {
            // Deliberately blind to the schedule. Asking for "what I just
            // solved" and being handed the most overdue card instead would
            // make the entry pointless, so FSRS does not get a vote here.
            ordered = candidates.sorted { solvedRank($0) > solvedRank($1) }
        } else if scope == .mistakes {
            // Due dates are irrelevant here: the point is what was failed, not
            // what is scheduled. Most recent failure first.
            ordered = candidates.sorted { left, right in
                lastBankedReview(byProblem[left.id]) > lastBankedReview(byProblem[right.id])
            }
        } else {
            let due = candidates.filter { dueDate(byProblem[$0.id], now: now) <= now }
            let notYetDue = candidates.filter { dueDate(byProblem[$0.id], now: now) > now }
            // Most overdue first, then top up with the least recently touched.
            ordered = due.sorted { left, right in
                let leftDue = dueDate(byProblem[left.id], now: now)
                let rightDue = dueDate(byProblem[right.id], now: now)
                if leftDue != rightDue { return leftDue < rightDue }
                return solvedRank(left) > solvedRank(right)
            }
                + notYetDue.sorted { lastReview(byProblem[$0.id]) < lastReview(byProblem[$1.id]) }
        }

        return Array(ordered.prefix(length))
    }

    /// A problem with no state has never been seen, which makes it maximally
    /// overdue -- it leads the queue ahead of everything, including problems
    /// that are merely very overdue.
    ///
    /// There is one row per problem now, so this is just that row's due date.
    /// It used to have to reason about a problem whose elements had review
    /// history while its pseudocode had never been asked; with a single
    /// schedule per problem that case cannot arise. `min` over the array is
    /// kept rather than assuming exactly one row, so a stray duplicate would
    /// schedule early rather than pick arbitrarily.
    private func dueDate(_ states: [CardState]?, now: Date) -> Date {
        guard let states, !states.isEmpty else { return .distantPast }
        return states.map(\.due).min() ?? .distantPast
    }

    /// Breaks the tie between problems that have never been reviewed here.
    ///
    /// All of them share `.distantPast` as a due date, so without this the
    /// order falls out of the array -- which is problem number -- and a
    /// problem solved on LeetCode yesterday queues behind one solved in 2017.
    /// Sorting by the accepted-at date descending puts the freshest first,
    /// which is what "review yesterday's problems today" asks for.
    ///
    /// It only ever decides ties. Once a problem has been graded it has a real
    /// due date, and FSRS owns when it comes back.
    ///
    /// A problem with no known date ranks below every problem that has one:
    /// unknown is not the same as ancient, and `Int.min` keeps it from being
    /// compared as though it were 1970.
    private func solvedRank(_ problem: Problem) -> Int {
        problem.solvedAt ?? Int.min
    }

    private func lastReview(_ states: [CardState]?) -> Date {
        states?.compactMap(\.lastReview).max() ?? .distantPast
    }

    private func lastBankedReview(_ states: [CardState]?) -> Date {
        states?.filter(\.inMistakeBank).compactMap(\.lastReview).max() ?? .distantPast
    }
}

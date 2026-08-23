import Foundation

/// What a session is scoped to. The home screen picks exactly one.
enum SessionScope: Equatable {
    case all
    case technique(String)
    case mistakes
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
            }
        }

        let ordered: [Problem]
        if scope == .mistakes {
            // Due dates are irrelevant here: the point is what was failed, not
            // what is scheduled. Most recent failure first.
            ordered = candidates.sorted { left, right in
                lastBankedReview(byProblem[left.id]) > lastBankedReview(byProblem[right.id])
            }
        } else {
            let due = candidates.filter { dueDate(byProblem[$0.id], now: now) <= now }
            let notYetDue = candidates.filter { dueDate(byProblem[$0.id], now: now) > now }
            // Most overdue first, then top up with the least recently touched.
            ordered = due.sorted { dueDate(byProblem[$0.id], now: now) < dueDate(byProblem[$1.id], now: now) }
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

    private func lastReview(_ states: [CardState]?) -> Date {
        states?.compactMap(\.lastReview).max() ?? .distantPast
    }

    private func lastBankedReview(_ states: [CardState]?) -> Date {
        states?.filter(\.inMistakeBank).compactMap(\.lastReview).max() ?? .distantPast
    }
}

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
            let due = candidates.filter { earliestDue(byProblem[$0.id], now: now) <= now }
            let notYetDue = candidates.filter { earliestDue(byProblem[$0.id], now: now) > now }
            // Most overdue first, then top up with the least recently touched.
            ordered = due.sorted { earliestDue(byProblem[$0.id], now: now) < earliestDue(byProblem[$1.id], now: now) }
                + notYetDue.sorted { lastReview(byProblem[$0.id]) < lastReview(byProblem[$1.id]) }
        }

        return Array(ordered.prefix(length))
    }

    /// A problem with no state at all has never been seen, which makes it
    /// maximally overdue — it should lead the queue ahead of everything,
    /// including problems that are merely very overdue.
    ///
    /// A problem that has *some* state but not one row per track is a
    /// different case: one of its tracks has real review history, and the
    /// other has simply never been asked. That missing track is due right
    /// now — eligible today, but not more overdue than a track with a truly
    /// old due date — so it contributes `now` rather than `.distantPast` to
    /// the minimum. Collapsing both cases to `.distantPast` (as a naive
    /// reading of "unseen counts as due" suggests) would tie every
    /// partially-seen problem together regardless of how overdue its seen
    /// track actually is, which loses the ordering the "most overdue first"
    /// rule promises.
    private func earliestDue(_ states: [CardState]?, now: Date) -> Date {
        guard let states, !states.isEmpty else { return .distantPast }
        var dueByTrack: [Track: Date] = [:]
        for state in states {
            dueByTrack[state.track] = min(dueByTrack[state.track] ?? state.due, state.due)
        }
        return Track.allCases.map { dueByTrack[$0] ?? now }.min() ?? .distantPast
    }

    private func lastReview(_ states: [CardState]?) -> Date {
        states?.compactMap(\.lastReview).max() ?? .distantPast
    }

    private func lastBankedReview(_ states: [CardState]?) -> Date {
        states?.filter(\.inMistakeBank).compactMap(\.lastReview).max() ?? .distantPast
    }
}

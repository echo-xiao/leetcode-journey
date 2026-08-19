import Foundation

/// What FSRS remembers about one track of one problem.
struct MemoryState: Equatable {
    var stability: Double
    var difficulty: Double
}

/// FSRS-6, ported rather than depended on.
///
/// The algorithm is short and public, and a dependency here would be a
/// dependency on someone else's release cadence for a personal tool. The port
/// is pinned by `fsrs-baseline.json`, generated from the reference Python
/// implementation (py-fsrs) — that fixture, not this code, is the authority
/// on correctness.
///
/// This is FSRS-6, not FSRS-5: the installed reference implementation
/// (py-fsrs 6.3.2) uses 21 parameters, with the forgetting-curve decay read
/// from `parameters[20]` rather than a fixed constant. An earlier draft of
/// this port assumed FSRS-5 (19 parameters, decay fixed at -0.5); that was
/// wrong and was corrected against the baseline.
///
/// This app has no minute-level learning phase — that would be
/// py-fsrs's `Learning`/`Relearning` states, which never appear here because
/// every card goes straight to `Review` after its first grade. What FSRS-6
/// *does* still branch on inside `Review` is elapsed time: a review that
/// lands under a day after the previous one takes the short-term path
/// (`_short_term_stability`) instead of the long-term forgetting-curve
/// formula. `nextState` reproduces that branch — see its doc comment.
struct FSRS {

    /// FSRS-6 default weights, as shipped by the reference implementation
    /// (py-fsrs 6.3.2, `DEFAULT_PARAMETERS`). The baseline fixture carries
    /// the values actually used in tests; these are the app's runtime
    /// defaults.
    static let defaultParameters: [Double] = [
        0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194, 0.001,
        1.8722, 0.1666, 0.796, 1.4835, 0.0614, 0.2629, 1.6483, 0.6014,
        1.8729, 0.5425, 0.0912, 0.0658, 0.1542,
    ]

    /// The floor py-fsrs clamps stability to (`STABILITY_MIN`).
    private static let stabilityMin = 0.001

    /// py-fsrs never schedules a review further out than this
    /// (`maximum_interval`'s default).
    private static let maximumIntervalDays = 36500.0

    let parameters: [Double]
    let desiredRetention: Double

    /// Forgetting-curve decay. FSRS-6 learns this instead of fixing it.
    private var decay: Double { -w(20) }

    /// Forgetting-curve factor, derived from `decay` the same way py-fsrs
    /// derives it: `0.9 ** (1 / decay) - 1`.
    private var factor: Double { pow(0.9, 1 / decay) - 1 }

    init(parameters: [Double] = FSRS.defaultParameters, desiredRetention: Double = 0.9) {
        precondition(
            parameters.count == FSRS.defaultParameters.count,
            "FSRS expects \(FSRS.defaultParameters.count) parameters (FSRS-6), got \(parameters.count)."
        )
        self.parameters = parameters
        self.desiredRetention = desiredRetention
    }

    private func w(_ index: Int) -> Double { parameters[index] }

    // MARK: - Curve

    func retrievability(state: MemoryState, elapsedDays: Double) -> Double {
        pow(1 + factor * elapsedDays / state.stability, decay)
    }

    /// The interval py-fsrs would schedule for this state: rounded to a
    /// whole day, never shorter than one day, never longer than
    /// `maximumIntervalDays`.
    func intervalDays(for state: MemoryState) -> Double {
        let raw = state.stability / factor * (pow(desiredRetention, 1 / decay) - 1)
        let rounded = raw.rounded(.toNearestOrEven)
        return min(max(rounded, 1), Self.maximumIntervalDays)
    }

    // MARK: - First review

    func initialState(grade: Grade) -> MemoryState {
        MemoryState(
            stability: clampStability(w(grade.rawValue - 1)),
            difficulty: clampDifficulty(initialDifficulty(grade: grade))
        )
    }

    private func initialDifficulty(grade: Grade) -> Double {
        w(4) - exp(w(5) * Double(grade.rawValue - 1)) + 1
    }

    private func clampDifficulty(_ value: Double) -> Double {
        min(max(value, 1.0), 10.0)
    }

    private func clampStability(_ value: Double) -> Double {
        max(value, Self.stabilityMin)
    }

    // MARK: - Later reviews

    /// `elapsedDays` is real elapsed time since the last review, exactly as
    /// py-fsrs's `review_card` receives it via `(review_datetime -
    /// card.last_review)`. This function is responsible for conforming it to
    /// the reference's contract, the same way `review_card` does before
    /// touching either formula:
    ///
    /// - Under one day (including zero and negative — clock skew, timezone
    ///   changes, a `lastReview` that lands in the future), py-fsrs takes the
    ///   short-term path (`_short_term_stability`), which ignores elapsed
    ///   time entirely. Routing negative input here is also what keeps it out
    ///   of `retrievability`, where a negative `elapsedDays` would push
    ///   recall above 1, or — past about -4.9 days at this app's default
    ///   parameters — feed a negative base into `pow` and produce NaN.
    /// - One day or more, py-fsrs floors elapsed time to a whole day
    ///   (`timedelta.days`) and floors that again at zero
    ///   (`max(0, ...)` in `get_card_retrievability`) before the long-term
    ///   forgetting-curve formula sees it. A 1.5-day gap is treated as 1 day,
    ///   not 1.5.
    ///
    /// Match py-fsrs's own branch condition (`days_since_last_review < 1`),
    /// not an invented threshold.
    func nextState(from state: MemoryState, grade: Grade, elapsedDays: Double) -> MemoryState {
        let stability: Double
        if elapsedDays < 1 {
            stability = shortTermStability(state: state, grade: grade)
        } else {
            // timedelta.days truncates toward zero, and get_card_retrievability
            // floors the result at zero on top of that.
            let wholeDays = max(0, elapsedDays.rounded(.down))
            let recall = retrievability(state: state, elapsedDays: wholeDays)
            stability = nextStability(state: state, grade: grade, recall: recall)
        }
        return MemoryState(
            stability: stability,
            difficulty: nextDifficulty(from: state.difficulty, grade: grade)
        )
    }

    private func nextDifficulty(from difficulty: Double, grade: Grade) -> Double {
        let delta = -w(6) * Double(grade.rawValue - 3)
        // Linear damping: a card already near maximum difficulty moves less.
        let damped = difficulty + delta * (10 - difficulty) / 9
        // Mean reversion toward the difficulty an Easy first answer would give.
        let target = w(4) - exp(w(5) * 3) + 1
        return clampDifficulty(w(7) * target + (1 - w(7)) * damped)
    }

    /// Same-day path (`_short_term_stability`): used instead of
    /// `nextStability` when the gap since the last review is under one day.
    /// Unlike the long-term formula, this one never looks at elapsed time or
    /// retrievability at all — only the rating and the current stability.
    private func shortTermStability(state: MemoryState, grade: Grade) -> Double {
        let rating = Double(grade.rawValue)
        var increase = exp(w(17) * (rating - 3 + w(18))) * pow(state.stability, -w(19))
        if grade != .again {
            increase = max(increase, 1.0)
        }
        return clampStability(state.stability * increase)
    }

    private func nextStability(state: MemoryState, grade: Grade, recall: Double) -> Double {
        let value: Double
        if grade == .again {
            value = forgottenStability(state: state, recall: recall)
        } else {
            value = recalledStability(state: state, grade: grade, recall: recall)
        }
        return clampStability(value)
    }

    private func recalledStability(
        state: MemoryState, grade: Grade, recall: Double
    ) -> Double {
        let hardPenalty = grade == .hard ? w(15) : 1.0
        let growth = exp(w(8))
            * (11 - state.difficulty)
            * pow(state.stability, -w(9))
            * (exp(w(10) * (1 - recall)) - 1)
            * hardPenalty
        return state.stability * (1 + growth)
    }

    private func forgottenStability(state: MemoryState, recall: Double) -> Double {
        let long = w(11)
            * pow(state.difficulty, -w(12))
            * (pow(state.stability + 1, w(13)) - 1)
            * exp(w(14) * (1 - recall))
        // FSRS-6 caps the post-lapse stability by the short-term term so a
        // lapse can never make a card look stronger than it was.
        let short = state.stability / exp(w(17) * w(18))
        return min(long, short)
    }
}

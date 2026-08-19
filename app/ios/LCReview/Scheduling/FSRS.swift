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
/// This app has no minute-level learning phase — same-sitting repetition is
/// a separate mechanism handled elsewhere — so every review here goes
/// through FSRS's long-term "Review" formulas. The reference implementation
/// only takes the short-term same-day path when a card is reviewed twice
/// within a day, which the baseline's sequences deliberately avoid (every
/// step has a gap of at least one day, except the first review of a card).
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

    func nextState(from state: MemoryState, grade: Grade, elapsedDays: Double) -> MemoryState {
        let recall = retrievability(state: state, elapsedDays: elapsedDays)
        return MemoryState(
            stability: nextStability(state: state, grade: grade, recall: recall),
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

import Foundation

/// Turns one button press into a scheduling change and a log row.
///
/// Returns rather than inserting, so the rules are testable without a
/// ModelContext. The caller owns persistence.
struct Grading {
    let fsrs: FSRS

    /// Two consecutive 会 to leave the mistake bank. One is too loose: it
    /// usually means the answer was on screen minutes ago.
    static let goodStreakToLeaveBank = 2

    func apply(
        grade: Grade,
        to existing: CardState?,
        problemID: String,
        track: Track,
        isRepeat: Bool,
        now: Date
    ) -> (state: CardState, log: ReviewLog?) {
        let log = ReviewLog(
            problemID: problemID, track: track, grade: grade,
            isRepeat: isRepeat, timestamp: now
        )

        // An in-session repeat is short-term repetition inside one sitting. It
        // is real work, so it is logged, but it neither reschedules the card
        // nor counts toward leaving the mistake bank: answering correctly two
        // minutes after seeing the answer is not evidence of anything.
        //
        // This branch is taken on `isRepeat` alone, never conditional on
        // `existing`. A repeat is only ever queued after a real grade on the
        // same track, so `existing` is expected to be present. Guarding
        // rather than falling through matters because the fall-through path
        // would treat the repeat as a first-ever grade: it would schedule
        // the card, count the review, and move the mistake bank -- exactly
        // what this branch exists to prevent.
        if isRepeat {
            let state = existing ?? CardState(
                problemID: problemID, track: track,
                stability: 0, difficulty: 0, due: now
            )
            return (state, log)
        }

        let state = existing ?? CardState(
            problemID: problemID, track: track,
            stability: 0, difficulty: 0, due: now
        )

        let memory: MemoryState
        if existing == nil || state.lastReview == nil {
            memory = fsrs.initialState(grade: grade)
        } else {
            // elapsedDays is passed straight through: nextState conforms it
            // itself (floors to whole days, clamps at zero, routes sub-day
            // gaps to the short-term formula), so no clamp or rounding here
            // would duplicate a guard that already lives in the right place.
            let elapsed = now.timeIntervalSince(state.lastReview!) / 86_400
            memory = fsrs.nextState(from: state.memory, grade: grade, elapsedDays: elapsed)
        }

        state.memory = memory
        state.lastReview = now
        state.reviewCount += 1
        state.due = now.addingTimeInterval(fsrs.intervalDays(for: memory) * 86_400)

        switch grade {
        case .again:
            state.inMistakeBank = true
            state.consecutiveGood = 0
        case .hard:
            // Neither a failure nor a clean recall: it does not move the card
            // out of the bank, and it does not reset progress toward leaving.
            break
        case .good:
            if state.inMistakeBank {
                state.consecutiveGood += 1
                if state.consecutiveGood >= Self.goodStreakToLeaveBank {
                    state.inMistakeBank = false
                }
            }
        }

        return (state, log)
    }
}

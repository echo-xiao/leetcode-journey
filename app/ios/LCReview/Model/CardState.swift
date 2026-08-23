import Foundation
import SwiftData

/// One problem: its FSRS state plus what the mistake bank needs.
///
/// One row per problem, not per layer. The elements and the pseudocode used
/// to be scheduled separately, on the grounds that they are forgotten at
/// different rates; they now share one interval, which is the cost the owner
/// chose to pay for grading a problem once instead of twice.
@Model
final class CardState {
    var problemID: String
    var stability: Double
    var difficulty: Double
    var due: Date
    var lastReview: Date?
    var reviewCount: Int
    /// Entered on 不会, left once `consecutiveGood` reaches
    /// `Grading.goodStreakToLeaveBank`.
    var inMistakeBank: Bool
    /// Counts toward leaving the bank. Good advances it, Again resets it to
    /// zero, and Hard leaves it untouched -- so a Hard between two Goods
    /// does not break the run. In-session repeats never touch it.
    var consecutiveGood: Int

    init(
        problemID: String,
        stability: Double,
        difficulty: Double,
        due: Date,
        lastReview: Date? = nil,
        reviewCount: Int = 0,
        inMistakeBank: Bool = false,
        consecutiveGood: Int = 0
    ) {
        self.problemID = problemID
        self.stability = stability
        self.difficulty = difficulty
        self.due = due
        self.lastReview = lastReview
        self.reviewCount = reviewCount
        self.inMistakeBank = inMistakeBank
        self.consecutiveGood = consecutiveGood
    }

    var memory: MemoryState {
        get { MemoryState(stability: stability, difficulty: difficulty) }
        set {
            stability = newValue.stability
            difficulty = newValue.difficulty
        }
    }
}

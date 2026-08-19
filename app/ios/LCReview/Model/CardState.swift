import Foundation
import SwiftData

/// One track of one problem: its FSRS state plus what the mistake bank needs.
///
/// `trackRaw` rather than `Track` because SwiftData stores primitives; `track`
/// is the accessor everything else uses.
@Model
final class CardState {
    var problemID: String
    var trackRaw: String
    var stability: Double
    var difficulty: Double
    var due: Date
    var lastReview: Date?
    var reviewCount: Int
    /// Entered on 不会, left only after two consecutive 会.
    var inMistakeBank: Bool
    /// Counts toward leaving the bank. In-session repeats never touch it.
    var consecutiveGood: Int

    init(
        problemID: String,
        track: Track,
        stability: Double,
        difficulty: Double,
        due: Date,
        lastReview: Date? = nil,
        reviewCount: Int = 0,
        inMistakeBank: Bool = false,
        consecutiveGood: Int = 0
    ) {
        self.problemID = problemID
        self.trackRaw = track.rawValue
        self.stability = stability
        self.difficulty = difficulty
        self.due = due
        self.lastReview = lastReview
        self.reviewCount = reviewCount
        self.inMistakeBank = inMistakeBank
        self.consecutiveGood = consecutiveGood
    }

    var track: Track { Track(rawValue: trackRaw) ?? .elements }

    var memory: MemoryState {
        get { MemoryState(stability: stability, difficulty: difficulty) }
        set {
            stability = newValue.stability
            difficulty = newValue.difficulty
        }
    }
}

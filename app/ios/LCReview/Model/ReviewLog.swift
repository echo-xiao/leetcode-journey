import Foundation
import SwiftData

/// One grade, appended and never updated.
///
/// CardState alone cannot answer "how many reviews on 3 September", which both
/// the heatmap and the streak need. The scheduler never reads this table.
@Model
final class ReviewLog {
    var problemID: String
    var trackRaw: String
    var gradeRaw: Int
    /// True for the extra ask appended inside a session after a 不会.
    /// Counted as work in the heatmap, excluded from FSRS and the mistake bank.
    var isRepeat: Bool
    var timestamp: Date

    init(problemID: String, track: Track, grade: Grade, isRepeat: Bool, timestamp: Date) {
        self.problemID = problemID
        self.trackRaw = track.rawValue
        self.gradeRaw = grade.rawValue
        self.isRepeat = isRepeat
        self.timestamp = timestamp
    }
}

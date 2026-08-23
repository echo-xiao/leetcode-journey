import Foundation
import SwiftData

/// One grade, appended and never updated.
///
/// CardState alone cannot answer "how many reviews on 3 September", which the
/// home screen's review count needs. The scheduler never reads this table.
///
/// The heatmap and the streak used to be drawn from here too. They now come
/// from LeetCode, so this table is purely a record of work done inside this
/// app.
@Model
final class ReviewLog {
    var problemID: String
    var gradeRaw: Int
    /// True for the extra ask appended inside a session after a 不会.
    /// Counted as work in the heatmap, excluded from FSRS and the mistake bank.
    var isRepeat: Bool
    var timestamp: Date

    init(problemID: String, grade: Grade, isRepeat: Bool, timestamp: Date) {
        self.problemID = problemID
        self.gradeRaw = grade.rawValue
        self.isRepeat = isRepeat
        self.timestamp = timestamp
    }
}

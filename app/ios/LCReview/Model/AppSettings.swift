import Foundation
import SwiftData

/// The single settings row.
///
/// `startDay` is stamped once on first launch: the heatmap leaves everything
/// before it blank rather than drawing empty cells, so the grid never implies
/// days were skipped that predate the app.
@Model
final class AppSettings {
    var sessionLength: Int
    var startDay: Date

    init(sessionLength: Int = 10, startDay: Date) {
        self.sessionLength = sessionLength
        self.startDay = startDay
    }
}

import Foundation
import SwiftData

/// The single settings row.
///
/// `startDay` used to live here, stamped once on first launch so the heatmap
/// could leave everything before it blank. The heatmap now draws LeetCode's
/// submission history, which goes back further than this app does, so there
/// is nothing left for it to mark off.
@Model
final class AppSettings {
    var sessionLength: Int

    init(sessionLength: Int = 10) {
        self.sessionLength = sessionLength
    }
}

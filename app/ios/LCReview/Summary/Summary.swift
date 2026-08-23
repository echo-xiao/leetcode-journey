import Foundation

/// The one number on the home screen that still comes from this app's own
/// records.
///
/// The heatmap and the streak used to be derived here too, from ReviewLog.
/// They now come from LeetCode (see `ActivityStore`), which is what the grid
/// on the home screen is a picture of. This is deliberately not merged into
/// that: how much reviewing happened inside this app is the one thing
/// LeetCode has no idea about, and dropping it would leave the app with no
/// record of ever having been used.
struct Summary {

    /// Counted in grades, not problems: walking one chain end to end is two
    /// grades. A repeat counts too -- going back over a problem is work.
    func totalReviews(logs: [ReviewLog]) -> Int { logs.count }
}

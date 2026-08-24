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

    /// Grades given today, in the device's own day.
    ///
    /// Counted in grades rather than problems, like `totalReviews`: an
    /// in-session repeat is work, and a day that felt like ten answers should
    /// not read as six.
    func reviewsToday(logs: [ReviewLog], now: Date, calendar: Calendar = .current) -> Int {
        let today = calendar.startOfDay(for: now)
        return logs.filter { calendar.startOfDay(for: $0.timestamp) == today }.count
    }

    /// Problems solved on LeetCode for the first time today.
    ///
    /// First-solved, not last: practising an old problem again is a review,
    /// not a new problem, and counting it as new would make the two numbers
    /// double-count the same work.
    ///
    /// LeetCode buckets by UTC and this counts in the device's day, so the two
    /// disagree for a few hours around midnight. Deliberate: this number sits
    /// beside 今日复习, which is local by nature, and one row of counters
    /// should not mix two definitions of "today".
    func newlySolvedToday(
        problems: [Problem], now: Date, calendar: Calendar = .current
    ) -> Int {
        let today = calendar.startOfDay(for: now)
        return problems.filter { problem in
            guard let first = problem.firstSolvedAt else { return false }
            let day = Date(timeIntervalSince1970: TimeInterval(first))
            return calendar.startOfDay(for: day) == today
        }.count
    }
}

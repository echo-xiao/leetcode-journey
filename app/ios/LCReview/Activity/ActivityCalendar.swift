import Foundation

/// One square in the heatmap.
///
/// There is no "before the app existed" case any more. The counts come from
/// LeetCode, whose history predates this app by years, so every day inside
/// the window is a day that really could have had submissions.
struct HeatmapCell: Equatable {
    let day: Date
    let count: Int
}

/// A LeetCode submission calendar, in the form the app stores and draws it.
///
/// Days are keyed by a `yyyy-MM-dd` string in UTC, not by `Date`, because
/// UTC is how LeetCode buckets submissions and a string key cannot be
/// silently re-interpreted in another time zone the way a `Date` can. A
/// submission made at 6pm Pacific already counts as the next day on
/// leetcode.com; the app shows the same thing rather than guessing at a
/// correction it has no data to make -- the API returns per-day totals only,
/// never the timestamp of an individual submission.
struct ActivityCalendar: Codable, Equatable {

    /// `yyyy-MM-dd` (UTC) -> number of submissions that day.
    var countsByDay: [String: Int]

    /// LeetCode's own streak. Not recomputed locally: doing that would
    /// re-bucket UTC data with a local calendar and produce a third number
    /// that matches neither the app's grid nor the website.
    var streak: Int

    /// When this snapshot was successfully fetched. Drives the "as of" line
    /// the home screen shows when the data is stale.
    var fetchedAt: Date

    static func empty(fetchedAt: Date) -> ActivityCalendar {
        ActivityCalendar(countsByDay: [:], streak: 0, fetchedAt: fetchedAt)
    }

    static var utcCalendar: Calendar {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(secondsFromGMT: 0)!
        return calendar
    }

    private static let keyFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.calendar = Calendar(identifier: .gregorian)
        formatter.locale = Locale(identifier: "en_US_POSIX")
        formatter.timeZone = TimeZone(secondsFromGMT: 0)!
        formatter.dateFormat = "yyyy-MM-dd"
        return formatter
    }()

    static func dayKey(_ date: Date) -> String {
        keyFormatter.string(from: date)
    }

    /// The window, oldest cell first, ending on `now`'s UTC day.
    func cells(days: Int, now: Date) -> [HeatmapCell] {
        let calendar = Self.utcCalendar
        let today = calendar.startOfDay(for: now)
        return (0..<days).reversed().compactMap { offset in
            guard let day = calendar.date(byAdding: .day, value: -offset, to: today)
            else { return nil }
            return HeatmapCell(day: day, count: countsByDay[Self.dayKey(day)] ?? 0)
        }
    }
}

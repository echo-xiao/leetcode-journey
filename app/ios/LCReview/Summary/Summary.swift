import Foundation

/// Everything the home screen's numbers are derived from.
///
/// Counts are in grades, not problems: walking one chain end to end is two
/// grades, and the heatmap is a picture of work done.
struct Summary {

    static let heatmapWindowDays = 90

    let calendar: Calendar

    init(calendar: Calendar = .current) {
        self.calendar = calendar
    }

    func totalReviews(logs: [ReviewLog]) -> Int { logs.count }

    func dailyCounts(logs: [ReviewLog]) -> [Date: Int] {
        var counts: [Date: Int] = [:]
        for log in logs {
            counts[calendar.startOfDay(for: log.timestamp), default: 0] += 1
        }
        return counts
    }

    /// Consecutive days ending today or yesterday.
    ///
    /// Today with no reviews yet does not break it — otherwise the number
    /// would read zero every morning until the first card of the day.
    func streak(logs: [ReviewLog], now: Date) -> Int {
        let counts = dailyCounts(logs: logs)
        guard !counts.isEmpty else { return 0 }

        let today = calendar.startOfDay(for: now)
        var cursor = today
        if counts[cursor] == nil {
            guard let yesterday = calendar.date(byAdding: .day, value: -1, to: today),
                  counts[yesterday] != nil
            else { return 0 }
            cursor = yesterday
        }

        var length = 0
        while counts[cursor] != nil {
            length += 1
            guard let previous = calendar.date(byAdding: .day, value: -1, to: cursor)
            else { break }
            cursor = previous
        }
        return length
    }

    func heatmap(
        logs: [ReviewLog], startDay: Date, now: Date, days: Int = Summary.heatmapWindowDays
    ) -> [HeatmapCell] {
        let counts = dailyCounts(logs: logs)
        let today = calendar.startOfDay(for: now)
        let start = calendar.startOfDay(for: startDay)

        return (0..<days).reversed().compactMap { offset in
            guard let day = calendar.date(byAdding: .day, value: -offset, to: today)
            else { return nil }
            _ = start
            return HeatmapCell(day: day, count: counts[day] ?? 0)
        }
    }
}

import Foundation

/// How much the home screen should trust what it is about to draw.
enum ActivityStatus: Equatable {
    case fresh
    /// Drawn from cache. `asOf` is when that cache was successfully fetched.
    case stale(asOf: Date)
    /// Nothing to draw: never fetched successfully, and no usable cache.
    case unavailable
}

/// Everything the home screen needs in one value.
struct ActivitySnapshot: Equatable {
    let cells: [HeatmapCell]
    let streak: Int
    let status: ActivityStatus
}

/// Fetches, merges, and caches the LeetCode submission calendar.
///
/// The API answers per year, so a window crossing New Year needs two calls.
/// If any one of them fails the whole load fails: a window filled in only
/// partly is not a smaller truth but a wrong picture, since a day the fetch
/// missed is drawn exactly like a day with no submissions.
actor ActivityStore {

    /// Half a year. The grid shows as many week columns as the screen
    /// can hold and drops the rest, so this is an upper bound rather
    /// than what is drawn. It costs nothing to ask for: the API answers
    /// per year regardless of the range wanted.
    static let windowDays = 182

    private let transport: ActivityTransport
    private let cacheURL: URL

    init(transport: ActivityTransport, cacheURL: URL) {
        self.transport = transport
        self.cacheURL = cacheURL
    }

    static func defaultCacheURL() -> URL {
        let documents = FileManager.default.urls(
            for: .documentDirectory, in: .userDomainMask
        )[0]
        return documents.appendingPathComponent("activity.json")
    }

    /// Ascending, so the last year fetched is the one containing `now` and
    /// its streak is the one that survives.
    static func years(now: Date, days: Int) -> [Int] {
        let calendar = ActivityCalendar.utcCalendar
        let today = calendar.startOfDay(for: now)
        let oldest = calendar.date(byAdding: .day, value: -(days - 1), to: today) ?? today
        let first = calendar.component(.year, from: oldest)
        let last = calendar.component(.year, from: today)
        return Array(first...last)
    }

    /// Never throws. The caller is a view: it needs to know what to draw, not
    /// what went wrong.
    func load(now: Date) async -> ActivitySnapshot {
        do {
            var countsByDay: [String: Int] = [:]
            var streak = 0
            for year in Self.years(now: now, days: Self.windowDays) {
                let fetched = try await transport.fetch(year: year)
                countsByDay.merge(fetched.countsByDay) { _, newer in newer }
                streak = fetched.streak
            }
            let calendar = ActivityCalendar(
                countsByDay: countsByDay, streak: streak, fetchedAt: now
            )
            writeCache(calendar)
            return ActivitySnapshot(
                cells: calendar.cells(days: Self.windowDays, now: now),
                streak: calendar.streak,
                status: .fresh
            )
        } catch {
            return fallback(now: now)
        }
    }

    private func fallback(now: Date) -> ActivitySnapshot {
        guard let cached = readCache() else {
            return ActivitySnapshot(
                cells: ActivityCalendar.empty(fetchedAt: now)
                    .cells(days: Self.windowDays, now: now),
                streak: 0,
                status: .unavailable
            )
        }
        return ActivitySnapshot(
            cells: cached.cells(days: Self.windowDays, now: now),
            streak: cached.streak,
            status: .stale(asOf: cached.fetchedAt)
        )
    }

    private func readCache() -> ActivityCalendar? {
        guard let data = try? Data(contentsOf: cacheURL) else { return nil }
        return try? JSONDecoder().decode(ActivityCalendar.self, from: data)
    }

    private func writeCache(_ calendar: ActivityCalendar) {
        guard let data = try? JSONEncoder().encode(calendar) else { return }
        try? FileManager.default.createDirectory(
            at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true
        )
        try? data.write(to: cacheURL, options: .atomic)
    }
}

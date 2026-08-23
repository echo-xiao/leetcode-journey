import Foundation

/// One year of the submission calendar, as the API hands it over.
struct ActivityYear: Equatable {
    let countsByDay: [String: Int]
    let streak: Int
}

/// Injected so the store can be tested without a network.
protocol ActivityTransport: Sendable {
    func fetch(year: Int) async throws -> ActivityYear
}

/// The public LeetCode profile calendar.
///
/// No cookie, no CSRF token, no account of ours involved: this query answers
/// for any username. The account is hardcoded because this app has exactly
/// one user; making it configurable would be solving a problem nobody has.
///
/// This is the app's only dependency outside GitHub, and LeetCode makes no
/// stability promise about it. Every parse failure is a hard throw so the
/// caller can fall back to its cache -- a half-decoded calendar would be
/// worse than none, because a grid missing days looks exactly like a grid of
/// days you skipped.
struct HTTPActivityTransport: ActivityTransport {

    enum Failure: Error { case badShape }

    static let endpoint = URL(string: "https://leetcode.com/graphql")!
    static let username = "echo666"

    private static let query = """
    query userProfileCalendar($username: String!, $year: Int) {
      matchedUser(username: $username) {
        userCalendar(year: $year) {
          streak
          submissionCalendar
        }
      }
    }
    """

    let session: URLSession

    init(session: URLSession = .shared) {
        self.session = session
    }

    func fetch(year: Int) async throws -> ActivityYear {
        var request = URLRequest(url: Self.endpoint, timeoutInterval: 10)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("https://leetcode.com", forHTTPHeaderField: "Referer")
        request.httpBody = try JSONSerialization.data(withJSONObject: [
            "query": Self.query,
            "variables": ["username": Self.username, "year": year],
        ])

        let (data, _) = try await session.data(for: request)
        return try Self.parse(data)
    }

    /// Separated from `fetch` so the only fallible part is testable without a
    /// network.
    static func parse(_ data: Data) throws -> ActivityYear {
        guard
            let root = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
            let payload = root["data"] as? [String: Any],
            let user = payload["matchedUser"] as? [String: Any],
            let calendar = user["userCalendar"] as? [String: Any],
            let streak = calendar["streak"] as? Int,
            let calendarText = calendar["submissionCalendar"] as? String,
            let nested = try? JSONSerialization.jsonObject(
                with: Data(calendarText.utf8)
            ) as? [String: Int]
        else { throw Failure.badShape }

        var countsByDay: [String: Int] = [:]
        for (secondsText, count) in nested {
            guard let seconds = TimeInterval(secondsText) else { throw Failure.badShape }
            let day = ActivityCalendar.dayKey(Date(timeIntervalSince1970: seconds))
            countsByDay[day] = count
        }
        return ActivityYear(countsByDay: countsByDay, streak: streak)
    }
}

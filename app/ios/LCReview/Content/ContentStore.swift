import Foundation

enum ContentFetchResult: Equatable {
    case notModified
    case updated(data: Data, etag: String?)
}

/// Injected so the store can be tested without a network.
protocol ContentTransport: Sendable {
    func fetch(etag: String?) async throws -> ContentFetchResult
}

/// Conditional GET against GitHub Raw.
///
/// The payload is measured in megabytes and grows with the library, so a
/// cold launch must not re-download it when nothing changed. That is what the
/// ETag is for.
struct HTTPContentTransport: ContentTransport {
    let url: URL
    let session: URLSession

    init(url: URL = ContentStore.contentURL, session: URLSession = .shared) {
        self.url = url
        self.session = session
    }

    func fetch(etag: String?) async throws -> ContentFetchResult {
        var request = URLRequest(url: url)
        if let etag {
            request.setValue(etag, forHTTPHeaderField: "If-None-Match")
        }
        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse else {
            return .updated(data: data, etag: nil)
        }
        if http.statusCode == 304 {
            return .notModified
        }
        return .updated(
            data: data,
            etag: http.value(forHTTPHeaderField: "ETag")
        )
    }
}

/// Downloads, caches, and decodes the problem library.
///
/// The repository is public, so there is no token and no authentication. Note
/// that GitHub Raw is CDN-cached: a push takes a few minutes to become
/// visible here.
actor ContentStore {

    static let contentURL = URL(
        string: "https://raw.githubusercontent.com/echo-xiao/leetcode-journey/main/app/content.json"
    )!

    private static let etagKey = "content.etag"

    private let transport: ContentTransport
    private let cacheURL: URL
    private let defaults: UserDefaults

    init(transport: ContentTransport, cacheURL: URL, defaults: UserDefaults = .standard) {
        self.transport = transport
        self.cacheURL = cacheURL
        self.defaults = defaults
    }

    static func defaultCacheURL() -> URL {
        let documents = FileManager.default.urls(
            for: .documentDirectory, in: .userDomainMask
        )[0]
        return documents.appendingPathComponent("content.json")
    }

    /// The problems, freshest available. Never throws: offline with a cache
    /// serves the cache, and offline without one returns empty so the view can
    /// show its retry message.
    func load() async -> [Problem] {
        let storedETag = defaults.string(forKey: Self.etagKey)

        do {
            switch try await transport.fetch(etag: storedETag) {
            case .notModified:
                return cachedProblems()
            case .updated(let data, let etag):
                guard let payload = decode(data) else { return cachedProblems() }
                writeCache(data)
                defaults.set(etag, forKey: Self.etagKey)
                return payload.problems
            }
        } catch {
            return cachedProblems()
        }
    }

    private func decode(_ data: Data) -> ContentPayload? {
        try? JSONDecoder().decode(ContentPayload.self, from: data)
    }

    private func cachedProblems() -> [Problem] {
        guard let data = try? Data(contentsOf: cacheURL),
              let payload = decode(data)
        else { return [] }
        return payload.problems
    }

    private func writeCache(_ data: Data) {
        try? FileManager.default.createDirectory(
            at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true
        )
        try? data.write(to: cacheURL, options: .atomic)
    }
}

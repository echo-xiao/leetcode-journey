import Foundation

/// One accepted solution file, verbatim from the repository.
struct Solution: Codable, Hashable {
    let name: String
    let code: String
}

/// One problem, with every layer the chain reveals.
///
/// `retrospective` is empty for the 66 problems that have no review.md, and
/// `solutions` can be empty too. Both are normal, not error cases.
struct Problem: Codable, Identifiable, Hashable {
    let id: String
    let number: Int
    let title: String
    let difficulty: String
    let technique: String
    let statement: String
    let elements: [String]
    let pseudocode: String
    let retrospective: String
    let solutions: [Solution]
}

/// The whole downloaded file.
///
/// There is no timestamp by design: the exporter only rewrites the file when
/// its content changes, and freshness is the ETag's job.
struct ContentPayload: Codable {
    let version: Int
    let problems: [Problem]
}

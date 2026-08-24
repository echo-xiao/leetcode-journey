import Foundation

/// One accepted solution file, verbatim from the repository.
struct Solution: Codable, Hashable {
    let name: String
    let code: String
}

/// One typed piece of a `pseudocode.md` article.
///
/// The exporter (`lc_review/app_export.py`) parses the hand-written article
/// (headings, prose, one fenced pseudocode block, a complexity section) into
/// these before shipping it, so the app never has to interpret raw markdown:
/// a `heading` is a section title with its `#`s stripped, `text` is prose
/// with its markdown markers already cleaned, and `code` is a fenced block's
/// contents verbatim, indentation intact.
struct PseudocodeBlock: Codable, Hashable {
    enum Kind: String, Codable {
        case heading
        case text
        case code
    }

    let kind: Kind
    let text: String
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
    let pseudocode: [PseudocodeBlock]
    let retrospective: String
    let solutions: [Solution]
    /// When this problem was last accepted on leetcode.com, in unix
    /// seconds. Optional because the index behind it is filled in by a
    /// backfill that can be interrupted, and because a problem the fetch
    /// could not answer for is genuinely unknown rather than very old.
    let solvedAt: Int?
    /// The day this problem stopped being unsolved, in unix seconds.
    ///
    /// Distinct from `solvedAt`, which moves forward every time the
    /// problem is practised again. One says "new", the other says
    /// "recent", and telling a day's new problems from its revisits
    /// needs both.
    let firstSolvedAt: Int?
}

/// The whole downloaded file.
///
/// There is no timestamp by design: the exporter only rewrites the file when
/// its content changes, and freshness is the ETag's job.
struct ContentPayload: Codable {
    let version: Int
    let problems: [Problem]
}

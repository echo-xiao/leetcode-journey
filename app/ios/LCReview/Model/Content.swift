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
}

/// The whole downloaded file.
///
/// There is no timestamp by design: the exporter only rewrites the file when
/// its content changes, and freshness is the ETag's job.
struct ContentPayload: Codable {
    let version: Int
    let problems: [Problem]
}

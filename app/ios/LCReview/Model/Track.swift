import Foundation

/// The two halves of a problem the app actually asks about.
///
/// The retrospective and the accepted code ride along in the chain but are
/// never questioned and never scheduled, so they are not tracks.
enum Track: String, Codable, CaseIterable, Hashable {
    case elements
    case pseudocode
}

/// The three buttons, and nothing more.
///
/// FSRS has a fourth rating (Easy). It is deliberately not exposed: a fourth
/// button on a phone invites misgrading more than it buys precision.
enum Grade: Int, Codable, CaseIterable, Hashable {
    case again = 1
    case hard = 2
    case good = 3
}

/// How far down the chain a card is currently revealed.
///
/// `statement` is what you see before the first tap. Each tap advances by one.
enum Layer: Int, CaseIterable, Comparable, Hashable {
    case statement = 0
    case elements
    case pseudocode
    case retrospective
    case solutions

    static func < (lhs: Layer, rhs: Layer) -> Bool { lhs.rawValue < rhs.rawValue }

    /// The track this layer asks about, or nil for the reference layers.
    var track: Track? {
        switch self {
        case .elements: return .elements
        case .pseudocode: return .pseudocode
        case .statement, .retrospective, .solutions: return nil
        }
    }

    var next: Layer? { Layer(rawValue: rawValue + 1) }
}

import Foundation

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
///
/// No layer is a scheduling unit. A problem gets one grade covering the whole
/// chain, so the layers are purely how much of it is on screen -- tapping
/// looks further down, grading moves on, and the two never contend.
enum Layer: Int, CaseIterable, Comparable, Hashable {
    case statement = 0
    case elements
    case pseudocode
    case retrospective
    case solutions

    static func < (lhs: Layer, rhs: Layer) -> Bool { lhs.rawValue < rhs.rawValue }

    var next: Layer? { Layer(rawValue: rawValue + 1) }
}

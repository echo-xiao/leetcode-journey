import SwiftUI

/// The whole visual vocabulary, in one place.
///
/// Borrowed from flomo: white ground, one rounded card, no borders, generous
/// padding, large loose type. The teal-green is the only hue in the app —
/// everything else is white, grey, or near-black.
enum Theme {

    static let accent = Color(red: 0.19, green: 0.76, blue: 0.51)

    static let pageBackground = Color(uiColor: .systemGroupedBackground)
    static let cardBackground = Color(uiColor: .secondarySystemGroupedBackground)
    static let primaryText = Color(uiColor: .label)
    static let secondaryText = Color(uiColor: .secondaryLabel)

    /// Four steps, thresholds at 1, 5 and 15 reviews in a day.
    ///
    /// The palest steps are the one thing that has to be checked on a real
    /// device: a tint calibrated against white disappears against black, so
    /// these use opacity over the system background rather than fixed values.
    static let heatmapRamp: [Color] = [
        Color(uiColor: .tertiarySystemFill),
        accent.opacity(0.28),
        accent.opacity(0.58),
        accent,
    ]

    static func heatmapColor(count: Int) -> Color {
        switch count {
        case 0: return heatmapRamp[0]
        case 1..<5: return heatmapRamp[1]
        case 5..<15: return heatmapRamp[2]
        default: return heatmapRamp[3]
        }
    }

    static let cardCornerRadius: CGFloat = 18
    static let cardPadding: CGFloat = 22
    static let sectionSpacing: CGFloat = 20

    static let titleFont = Font.system(size: 21, weight: .semibold)
    static let bodyFont = Font.system(size: 17)
    static let bodyLineSpacing: CGFloat = 7
    static let tagFont = Font.system(size: 13)
    static let codeFont = Font.system(size: 13, design: .monospaced)
}

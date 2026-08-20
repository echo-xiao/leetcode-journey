import SwiftUI
import UIKit

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

    /// Measured directly off a real flomo screenshot (1125×2436, iPhone 12
    /// mini scale — same device/scale as our own screenshots, so pixels
    /// divide by 3 straight to points): body glyph bounding box is 42–44px
    /// tall, which matches a ~15–16pt system font (checked by rendering the
    /// same Chinese text at several sizes and comparing bounding boxes, since
    /// PingFang itself isn't installed on this Mac — Hiragino Sans GB was
    /// used as the closest available proxy for that comparison). Landed on
    /// 16pt, which is also exactly Apple's HIG "Callout" token. Was 17pt.
    static let bodyFont = Font.system(size: 16)

    /// Baseline-to-baseline spacing in the flomo reference measures 86–87px
    /// (28.7–29pt). A 16pt system font's default line height is ~21pt (HIG
    /// Callout leading), so the extra spacing needed is ~8pt. Was 7.
    static let bodyLineSpacing: CGFloat = 8

    /// The quiet meta line at the top of the card (difficulty + number) —
    /// flomo's timestamp equivalent. Measured off the reference screenshot:
    /// glyph bbox 27px (9pt) for "2026-08-17 15:22", which brackets 13pt when
    /// rendered with the real SF Pro font and compared the same way — also
    /// exactly Apple's HIG "Footnote" token. Was 12pt.
    static let metaFont = Font.system(size: 13)

    /// The technique tag, a pill at the top of the card. Size and colour
    /// measured directly off the flomo reference (round 2 superseded the
    /// app's teal accent here — flomo's tag is a blue-lavender pill, and the
    /// new instruction is to match flomo's colour exactly, not reuse the
    /// app's single accent hue for this element):
    /// - Text bbox 33px brackets 12pt (Hiragino Sans GB proxy) — Apple's HIG
    ///   "Caption 1" token. Was 13pt.
    /// - Pill background sampled at RGB(240,243,252) = #F0F3FC.
    /// - Pill text sampled at RGB(96,130,239) = #6082EF.
    /// - Pill is a full capsule in the reference (curvature visible a few px
    ///   from the top/bottom edges of a 68px-tall pill), same shape the app
    ///   already uses via `Capsule()`.
    static let tagFont = Font.system(size: 12, weight: .medium)
    static let tagBackground = Color(red: 240 / 255, green: 243 / 255, blue: 252 / 255)
    static let tagTextColor = Color(red: 96 / 255, green: 130 / 255, blue: 239 / 255)

    /// Body text and secondary/timestamp grey, sampled off the reference for
    /// completeness even though the app already uses system `.label` /
    /// `.secondaryLabel`, which land inside measurement noise of these:
    /// body text ≈ RGB(69,69,69) = #454545, secondary/timestamp grey ≈
    /// RGB(148,148,148) = #949494. Card background sampled at pure white
    /// (#FFFFFF) and page background sampled in the 242–249 grey range
    /// (dithering/JPEG noise) — both already matched by
    /// `secondarySystemGroupedBackground` / `systemGroupedBackground`, kept
    /// as system colors rather than hardcoded so dark mode still inverts
    /// correctly.

    /// Code must read at the same size as body text — the owner reversed an
    /// earlier decision to shrink it to 11pt. Tied to `bodyFont`'s point
    /// value (16) rather than a second literal, so the two can't drift apart.
    static let codeFont = Font.system(size: 16, design: .monospaced)

    /// The dashed vertical line connecting one chain card to the next —
    /// "beads on a string" rather than one continuous slab. Deliberately
    /// short: a long stretch would read as empty space, not a link between
    /// two adjacent cards. Colour is `secondaryText`, the same quiet grey
    /// already used for meta lines and section labels, so it reads as
    /// structural rather than as content.
    static let connectorHeight: CGFloat = 22
    static let connectorLineWidth: CGFloat = 1.5
    static let connectorDashPattern: [CGFloat] = [4, 4]
}

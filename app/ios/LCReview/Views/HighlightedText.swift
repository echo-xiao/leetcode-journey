import SwiftUI

struct HighlightSegment: Equatable {
    let text: String
    let isHighlighted: Bool
}

/// Splits a retrospective on its ``==marked==`` spans.
///
/// Those spans are the spots echo flagged as mistakes — the part of a
/// retrospective most worth seeing — so they get a background rather than
/// being rendered as literal equals signs.
enum HighlightParser {

    static func parse(_ markdown: String) -> [HighlightSegment] {
        guard !markdown.isEmpty else { return [] }

        var segments: [HighlightSegment] = []
        var rest = Substring(markdown)

        while let open = rest.range(of: "==") {
            let after = rest[open.upperBound...]
            guard let close = after.range(of: "==") else { break }

            let before = rest[rest.startIndex..<open.lowerBound]
            if !before.isEmpty {
                segments.append(HighlightSegment(text: String(before), isHighlighted: false))
            }
            let inner = after[after.startIndex..<close.lowerBound]
            segments.append(
                HighlightSegment(text: stripEmphasis(String(inner)), isHighlighted: true)
            )
            rest = after[close.upperBound...]
        }

        if !rest.isEmpty {
            segments.append(HighlightSegment(text: String(rest), isHighlighted: false))
        }
        return segments
    }

    /// Retrospectives are written ``==**like this**==``. The background already
    /// carries the emphasis, so the asterisks would just be noise.
    private static func stripEmphasis(_ text: String) -> String {
        var value = text
        for marker in ["**", "__"] {
            if value.hasPrefix(marker) && value.hasSuffix(marker) && value.count > marker.count * 2 {
                value = String(value.dropFirst(marker.count).dropLast(marker.count))
            }
        }
        return value
    }
}

/// A retrospective with its highlights drawn.
///
/// Built as an AttributedString rather than concatenated Text views: a
/// background that survives a line wrap has to live on the string, and
/// `Text + Text` cannot express one.
struct HighlightedText: View {
    let markdown: String

    var body: some View {
        Text(attributed)
            .font(Theme.bodyFont)
            .lineSpacing(Theme.bodyLineSpacing)
    }

    private var attributed: AttributedString {
        var result = AttributedString()
        for segment in HighlightParser.parse(markdown) {
            var piece = AttributedString(segment.text)
            if segment.isHighlighted {
                piece.backgroundColor = Theme.accent.opacity(0.22)
            }
            result += piece
        }
        return result
    }
}

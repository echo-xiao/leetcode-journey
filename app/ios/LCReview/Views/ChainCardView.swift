import SwiftUI

/// One problem, opened as far as `revealed`.
///
/// Layers are appended to the same card rather than replacing it, so after the
/// last tap the whole chain is on one scrollable page and can be read back
/// from the top.
struct ChainCardView: View {
    let problem: Problem
    let revealed: Layer

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: Theme.sectionSpacing) {
                Text(problem.title)
                    .font(Theme.titleFont)
                    .foregroundColor(Theme.primaryText)

                Text(problem.statement)
                    .font(Theme.bodyFont)
                    .lineSpacing(Theme.bodyLineSpacing)
                    .foregroundColor(Theme.primaryText)

                if revealed >= .elements {
                    section("要素") {
                        VStack(alignment: .leading, spacing: 10) {
                            ForEach(Array(problem.elements.enumerated()), id: \.offset) { index, slot in
                                Text("\(index + 1). \(slot)")
                                    .font(Theme.bodyFont)
                                    .lineSpacing(Theme.bodyLineSpacing)
                            }
                        }
                    }
                }

                if revealed >= .pseudocode {
                    section("伪代码") {
                        codeBlock(problem.pseudocode)
                    }
                }

                if revealed >= .retrospective, !problem.retrospective.isEmpty {
                    section("上次卡在哪") {
                        HighlightedText(markdown: problem.retrospective)
                    }
                }

                if revealed >= .solutions {
                    ForEach(problem.solutions, id: \.name) { solution in
                        section(solution.name) {
                            codeBlock(solution.code)
                        }
                    }
                }

                Text("#\(problem.technique)")
                    .font(Theme.tagFont)
                    .foregroundColor(Theme.secondaryText)
                    .padding(.top, 4)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(Theme.cardPadding)
            .background(Theme.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: Theme.cardCornerRadius, style: .continuous))
            .shadow(color: .black.opacity(0.05), radius: 12, y: 4)
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
        }
        .background(Theme.pageBackground)
    }

    /// Code and pseudocode scroll sideways inside their own strip.
    ///
    /// At 375pt wide, minus the card's padding, a 13pt monospaced line only
    /// has room for around 38-40 characters — real Python solutions run well
    /// past that. Wrapping mid-line would break indentation, the one thing
    /// that makes code readable, and shrinking the font to fit the worst line
    /// would make every other line too small. Scrolling the block sideways
    /// keeps every line's indentation intact and costs nothing for the many
    /// lines that already fit; the vertical page scroll is untouched because
    /// this horizontal scroller is clipped to the card's width, not the
    /// other way around.
    @ViewBuilder
    private func codeBlock(_ code: String) -> some View {
        ScrollView(.horizontal, showsIndicators: false) {
            Text(code)
                .font(Theme.codeFont)
                .lineSpacing(4)
                .fixedSize(horizontal: true, vertical: true)
        }
    }

    @ViewBuilder
    private func section<Content: View>(
        _ label: String, @ViewBuilder content: () -> Content
    ) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            Divider().opacity(0.5)
            Text(label)
                .font(Theme.tagFont)
                .foregroundColor(Theme.secondaryText)
            content()
                .foregroundColor(Theme.primaryText)
                .frame(maxWidth: .infinity, alignment: .leading)
        }
        .transition(.opacity)
    }
}

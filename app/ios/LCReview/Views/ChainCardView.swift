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
        // `ScrollView` in SwiftUI automatically extends edge-to-edge and
        // relies on content inset only for its *resting* scroll position —
        // once scrolled, its content can render underneath the status bar,
        // because the view itself, not just its content, spans there.
        // `GeometryReader`, left to its own (non-ignoring) default, is
        // already given the safe-area-excluded frame — that's the box we
        // want the `ScrollView` pinned to. Giving the `ScrollView` that
        // exact fixed size and clipping it means it can never render past
        // the safe area, no matter how far it's scrolled, while the grey
        // page background — a sibling that explicitly opts into
        // `ignoresSafeArea()` — is still free to bleed to the true edges of
        // the screen.
        GeometryReader { geo in
            ZStack(alignment: .top) {
                Theme.pageBackground
                    .ignoresSafeArea()

                ScrollView {
                    VStack(alignment: .leading, spacing: Theme.sectionSpacing) {
                        Text("\(problem.difficulty) · #\(problem.number)")
                            .font(Theme.metaFont)
                            .foregroundColor(Theme.secondaryText)

                        Text("#\(problem.technique)")
                            .font(Theme.tagFont)
                            .foregroundColor(Theme.accent)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 5)
                            .background(Theme.tagBackground)
                            .clipShape(Capsule())

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
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(Theme.cardPadding)
                    .background(Theme.cardBackground)
                    .clipShape(RoundedRectangle(cornerRadius: Theme.cardCornerRadius, style: .continuous))
                    .shadow(color: .black.opacity(0.05), radius: 12, y: 4)
                    .padding(.horizontal, 16)
                    .padding(.vertical, 12)
                }
                .frame(width: geo.size.width, height: geo.size.height)
                .clipped()
            }
        }
    }

    /// Code and pseudocode shrink and soft-wrap with a hanging indent —
    /// never scroll sideways, on this card or anything in it.
    ///
    /// Each source line is measured for its own leading whitespace, then laid
    /// out as a fixed-width leading spacer (the indent) plus the trimmed
    /// remainder. The spacer's width comes from `Theme.codeIndentUnit`, the
    /// measured advance width of one monospaced character at 11pt, so it
    /// lines up exactly with the characters above it rather than guessing a
    /// point value. Because the remainder `Text` starts at that offset, its
    /// own wrapped continuation lines stay under the spacer too — that's the
    /// hanging indent, and it's what keeps nested Python readable when a line
    /// wraps. Blank lines are preserved as blank rows.
    @ViewBuilder
    private func codeBlock(_ code: String) -> some View {
        let lines = code.components(separatedBy: "\n")
        VStack(alignment: .leading, spacing: 4) {
            ForEach(Array(lines.enumerated()), id: \.offset) { _, line in
                codeLine(line)
            }
        }
    }

    private func codeLine(_ raw: String) -> some View {
        let indentColumns = raw.prefix(while: { $0 == " " }).count
        let trimmed = String(raw.drop(while: { $0 == " " }))
        return HStack(alignment: .top, spacing: 0) {
            Color.clear.frame(width: CGFloat(indentColumns) * Theme.codeIndentUnit)
            Text(trimmed.isEmpty ? " " : trimmed)
                .font(Theme.codeFont)
                .lineSpacing(4)
                .fixedSize(horizontal: false, vertical: true)
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

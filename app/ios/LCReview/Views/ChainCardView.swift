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
                            .foregroundColor(Theme.tagTextColor)
                            .padding(.horizontal, 7)
                            .padding(.vertical, 6)
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

    /// Code and pseudocode scroll horizontally instead of wrapping or
    /// shrinking — the owner reversed the earlier decision that shrank this
    /// text to 11pt and soft-wrapped it with a hanging indent. Wrapping a
    /// code line mid-statement destroys the one thing that makes code
    /// legible (indentation), and shrinking to fit the worst-case line makes
    /// every other line unreadably small. Horizontal scroll preserves every
    /// line's indentation exactly and costs nothing for lines that already
    /// fit.
    ///
    /// The earlier complaint about this same pattern was that a cut-off line
    /// read as a rendering bug — nothing told the reader more content was
    /// off-screen. `CodeStrip` below fixes that: the scroll indicator is
    /// shown (not hidden), and a soft fade sits over the right edge whenever
    /// there is more content to scroll to, disappearing once scrolled to the
    /// end. Only this strip scrolls sideways — the outer page `ScrollView`
    /// above is untouched and stays vertical-only, so a long line can never
    /// push the card or the page sideways.
    @ViewBuilder
    private func codeBlock(_ code: String) -> some View {
        CodeStrip(code: code)
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

/// A single line (or block) of monospaced source that scrolls horizontally
/// instead of wrapping, with a self-announcing right edge: the system
/// scroll indicator is shown, and a soft fade covers the right edge for as
/// long as there's more content to scroll to, disappearing once the strip
/// is scrolled all the way to its end.
///
/// Content width, viewport width, and scroll offset are all read via
/// `GeometryReader` + `PreferenceKey`, the standard SwiftUI pattern for
/// tracking a `ScrollView`'s own scroll position — there's no public API for
/// "am I scrolled to the end" otherwise.
private struct CodeStrip: View {
    let code: String

    @State private var contentWidth: CGFloat = 0
    @State private var viewportWidth: CGFloat = 0
    @State private var scrollOffsetX: CGFloat = 0

    private var isScrollable: Bool { contentWidth > viewportWidth + 1 }
    private var isAtEnd: Bool {
        guard isScrollable else { return true }
        return scrollOffsetX >= (contentWidth - viewportWidth - 1)
    }

    var body: some View {
        ZStack(alignment: .trailing) {
            ScrollView(.horizontal, showsIndicators: true) {
                Text(code)
                    .font(Theme.codeFont)
                    .lineSpacing(4)
                    .fixedSize(horizontal: true, vertical: true)
                    .background(
                        GeometryReader { contentGeo in
                            Color.clear
                                .preference(key: CodeContentWidthKey.self, value: contentGeo.size.width)
                                .preference(
                                    key: CodeScrollOffsetKey.self,
                                    value: contentGeo.frame(in: .named("codeStrip")).minX
                                )
                        }
                    )
            }
            .coordinateSpace(name: "codeStrip")
            .background(
                GeometryReader { outerGeo in
                    Color.clear
                        .preference(key: CodeViewportWidthKey.self, value: outerGeo.size.width)
                }
            )
            .onPreferenceChange(CodeContentWidthKey.self) { contentWidth = $0 }
            .onPreferenceChange(CodeViewportWidthKey.self) { viewportWidth = $0 }
            .onPreferenceChange(CodeScrollOffsetKey.self) { scrollOffsetX = -$0 }

            if isScrollable && !isAtEnd {
                LinearGradient(
                    colors: [Theme.cardBackground.opacity(0), Theme.cardBackground],
                    startPoint: .leading,
                    endPoint: .trailing
                )
                .frame(width: 24)
                .allowsHitTesting(false)
            }
        }
    }
}

private struct CodeContentWidthKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) { value = nextValue() }
}

private struct CodeViewportWidthKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) { value = nextValue() }
}

private struct CodeScrollOffsetKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) { value = nextValue() }
}

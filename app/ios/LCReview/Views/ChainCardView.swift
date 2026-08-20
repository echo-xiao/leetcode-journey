import SwiftUI

/// One problem, opened as far as `revealed`.
///
/// Each layer is its own card — one card per source file — stacked
/// vertically and linked by a short dashed connector, "beads on a string"
/// rather than one continuous scrolling slab. A card that has no content
/// (an empty retrospective, a problem with no solutions yet) is simply never
/// drawn, and no orphan connector is drawn for it either. The meta line, tag
/// pill and title identify the *problem*, not any one layer, so they live on
/// the first card only.
///
/// When `revealed` advances, the newly revealed card is scrolled into view
/// and animated — without that, tapping past the last visible card produces
/// no on-screen change and reads as an unresponsive tap.
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

                ScrollViewReader { proxy in
                    ScrollView {
                        VStack(spacing: 0) {
                            card(id: Self.statementID) { statementContent }

                            if revealed >= .elements {
                                connector
                                labeledCard(id: Self.elementsID, label: "要素") {
                                    elementsContent
                                }
                            }

                            if revealed >= .pseudocode {
                                connector
                                labeledCard(id: Self.pseudocodeID, label: "伪代码") {
                                    codeBlock(problem.pseudocode)
                                }
                            }

                            if revealed >= .retrospective, !problem.retrospective.isEmpty {
                                connector
                                labeledCard(id: Self.retrospectiveID, label: "上次卡在哪") {
                                    HighlightedText(markdown: problem.retrospective)
                                }
                            }

                            if revealed >= .solutions {
                                ForEach(Array(problem.solutions.enumerated()), id: \.offset) { index, solution in
                                    connector
                                    labeledCard(id: Self.solutionID(index), label: solution.name) {
                                        codeBlock(solution.code)
                                    }
                                }
                            }
                        }
                        .padding(.vertical, 12)
                    }
                    .frame(width: geo.size.width, height: geo.size.height)
                    .clipped()
                    .onChange(of: revealed) { _, newValue in
                        guard let id = scrollTarget(for: newValue) else { return }
                        withAnimation(.easeInOut(duration: 0.3)) {
                            proxy.scrollTo(id, anchor: .top)
                        }
                    }
                }
            }
        }
    }

    // MARK: Card identity, for `ScrollViewReader`

    private static let statementID = "statement"
    private static let elementsID = "elements"
    private static let pseudocodeID = "pseudocode"
    private static let retrospectiveID = "retrospective"
    private static func solutionID(_ index: Int) -> String { "solution-\(index)" }

    /// Which card, if any, just became visible as `revealed` advanced to
    /// `layer` — nil when the step produced no new card (an empty
    /// retrospective) or needs no scroll (the statement is on screen from
    /// the start). When several solution cards appear at once, only the
    /// first is targeted: that's the new content the reveal introduced,
    /// immediately below whatever card was last on screen.
    private func scrollTarget(for layer: Layer) -> String? {
        switch layer {
        case .statement: return nil
        case .elements: return Self.elementsID
        case .pseudocode: return Self.pseudocodeID
        case .retrospective: return problem.retrospective.isEmpty ? nil : Self.retrospectiveID
        case .solutions: return problem.solutions.isEmpty ? nil : Self.solutionID(0)
        }
    }

    // MARK: Card contents

    private var statementContent: some View {
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
        }
    }

    private var elementsContent: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(Array(problem.elements.enumerated()), id: \.offset) { index, slot in
                Text("\(index + 1). \(slot)")
                    .font(Theme.bodyFont)
                    .lineSpacing(Theme.bodyLineSpacing)
            }
        }
    }

    /// The dashed link between two adjacent cards, centred in the available
    /// width. Short by design — a small gap, not a long stretch — so the
    /// chain reads as beads close together rather than cards floating far
    /// apart.
    private var connector: some View {
        Path { path in
            path.move(to: .zero)
            path.addLine(to: CGPoint(x: 0, y: Theme.connectorHeight))
        }
        .stroke(
            Theme.secondaryText,
            style: StrokeStyle(lineWidth: Theme.connectorLineWidth, lineCap: .round, dash: Theme.connectorDashPattern)
        )
        .frame(width: Theme.connectorLineWidth, height: Theme.connectorHeight)
        .frame(maxWidth: .infinity)
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

    /// One card: padded content on the flomo card background, rounded
    /// corners, a soft shadow, and a stable `id` so `ScrollViewReader` can
    /// target it. Every layer of the chain — statement, 要素, 伪代码, 复盘,
    /// each solution file — renders through this one wrapper, which is what
    /// makes them read as identical beads on the same string rather than as
    /// different kinds of thing.
    @ViewBuilder
    private func card<Content: View>(
        id: String, @ViewBuilder content: () -> Content
    ) -> some View {
        content()
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(Theme.cardPadding)
            .background(Theme.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: Theme.cardCornerRadius, style: .continuous))
            .shadow(color: .black.opacity(0.05), radius: 12, y: 4)
            .padding(.horizontal, 16)
            .id(id)
            .transition(.opacity)
    }

    /// A `card` with a section label above its content — every card past
    /// the first (which carries the problem's own title instead).
    @ViewBuilder
    private func labeledCard<Content: View>(
        id: String, label: String, @ViewBuilder content: () -> Content
    ) -> some View {
        card(id: id) {
            VStack(alignment: .leading, spacing: 12) {
                Text(label)
                    .font(Theme.tagFont)
                    .foregroundColor(Theme.secondaryText)
                content()
                    .foregroundColor(Theme.primaryText)
                    .frame(maxWidth: .infinity, alignment: .leading)
            }
        }
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

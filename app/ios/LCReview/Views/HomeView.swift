import SwiftUI

/// One row on the home screen: a scope you can start a session in.
struct HomeEntry: Identifiable, Equatable {
    let id: String
    let label: String
    /// How many problems in this scope are waiting right now, uncapped.
    ///
    /// The screen used to advertise session length here instead, deliberately
    /// hiding this number. It reads as the truer answer to "what is in here",
    /// at the cost of a large figure on a library that has barely been
    /// reviewed.
    let backlog: Int
    /// Everything in this scope, waiting or not. Reviewing a problem takes
    /// it out of the backlog but not out of the week it was solved in.
    let total: Int
    /// How many the session will actually ask, which is the smaller of the
    /// backlog and the session length.
    let sessionSize: Int
    let scope: SessionScope
}

/// One branch of the home screen's tree: a way of choosing what to practise.
///
/// A branch either has children or an explanation of why it has none. The two
/// are exclusive: an entry with no data shows a sentence saying what is
/// missing, because an empty list is indistinguishable from a broken one.
struct HomeSection: Identifiable, Equatable {
    let id: String
    let label: String
    /// How many problems the whole branch covers, or nil when there is no
    /// data behind it yet.
    let total: Int?
    let children: [HomeEntry]
    let unavailable: String?
}

/// Three numbers, the heatmap, and the list of sessions.
///
/// Rows advertise session length, never how much is overdue. Opening an app to
/// find 400 cards waiting is the failure mode this whole design exists to
/// avoid.
struct HomeView: View {
    let problemCount: Int
    let totalReviews: Int
    let reviewsToday: Int
    let newlySolvedToday: Int
    let streak: Int
    let cells: [HeatmapCell]
    /// The rows that stand on their own, above the tree.
    let entries: [HomeEntry]
    let sections: [HomeSection]
    let sessionLength: Int
    let activityStatus: ActivityStatus
    let onStart: (SessionScope) -> Void
    let onChangeSessionLength: (Int) -> Void

    @State private var showSettings = false
    /// Only one branch is open at a time. Four open branches is thirty-odd
    /// rows, which is the long list this screen exists to replace.
    @State private var openSection: String? = "recent"

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                counters
                VStack(alignment: .leading, spacing: 8) {
                    if let note = activityNote {
                        Text(note)
                            .font(.system(size: 11))
                            .foregroundColor(Theme.secondaryText)
                    }
                    HeatmapView(cells: cells)
                }
                list
                tree
            }
            .padding(Theme.cardPadding)
            .background(Theme.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: Theme.cardCornerRadius, style: .continuous))
            .padding(16)
        }
        .background(Theme.pageBackground)
        // A plain grey gear, not a labelled button: the session list below is
        // the screen's real entry point, and settings is a single knob most
        // visits never need to touch.
        .overlay(alignment: .topTrailing) {
            Button {
                showSettings = true
            } label: {
                Image(systemName: "gearshape")
                    .font(.system(size: 17))
                    .foregroundColor(Theme.secondaryText)
                    .padding(20)
            }
        }
        .sheet(isPresented: $showSettings) {
            SettingsView(
                sessionLength: sessionLength,
                onChange: onChangeSessionLength,
                onDone: { showSettings = false }
            )
        }
    }

    /// Nothing at all when the data is current: a line that is always
    /// there stops being read. The two failure cases must not share
    /// wording -- "old data" and "no data" look identical as an empty
    /// grid, and reading one as the other means reading three blank
    /// months as time you wasted.
    private var activityNote: String? {
        switch activityStatus {
        case .fresh:
            return nil
        case .stale(let asOf):
            return "数据截至 \(Self.noteFormatter.string(from: asOf))"
        case .unavailable:
            return "暂时拿不到 LeetCode 数据"
        }
    }

    private static let noteFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "M月d日"
        return formatter
    }()

    /// Progress: how many of this row are not waiting, over how many there
    /// are. "7 / 16", "0 / 66".
    ///
    /// Done over total, not remaining over total. "9 / 16" reads as nine of
    /// sixteen finished, which is the opposite of what a remaining count
    /// means, and a number that can be read backwards is worse than no number.
    ///
    /// "Done" is done for now, not forever: a problem drops out of the
    /// backlog until its next due date and then counts as waiting again. The
    /// fraction is progress against today's queue, and it is meant to go back
    /// down tomorrow.
    ///
    /// Session length is deliberately absent: it is one number for the whole
    /// app, it lives in settings, and repeating it on every row is noise.
    private static func countLabel(_ entry: HomeEntry) -> String {
        "\(entry.total - entry.backlog) / \(entry.total)"
    }

    private var counters: some View {
        HStack(spacing: 0) {
            counter(problemCount, "题目")
            counter(newlySolvedToday, "今日新刷")
            counter(reviewsToday, "今日复习")
            counter(streak, "连续天")
        }
    }

    private func counter(_ value: Int, _ label: String) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text("\(value)")
                .font(.system(size: 24, weight: .semibold))
                .foregroundColor(Theme.primaryText)
            Text(label)
                .font(.system(size: 12))
                .foregroundColor(Theme.secondaryText)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }

    private var list: some View {
        VStack(spacing: 0) {
            ForEach(entries) { entry in
                Button {
                    onStart(entry.scope)
                } label: {
                    HStack {
                        Text(entry.label)
                            .font(Theme.bodyFont)
                            .foregroundColor(Theme.primaryText)
                        Spacer()
                        Text(Self.countLabel(entry))
                            .font(Theme.tagFont)
                            .foregroundColor(Theme.secondaryText)
                        Image(systemName: "chevron.right")
                            .font(.system(size: 12, weight: .semibold))
                            .foregroundColor(Theme.secondaryText.opacity(0.6))
                    }
                    .padding(.vertical, 14)
                }
                .buttonStyle(.plain)
                if entry.id != entries.last?.id {
                    Divider().opacity(0.4)
                }
            }
        }
    }

    // MARK: - The tree

    private var tree: some View {
        VStack(alignment: .leading, spacing: 2) {
            ForEach(sections) { section in
                branch(section)
            }
        }
    }

    @ViewBuilder
    private func branch(_ section: HomeSection) -> some View {
        let isOpen = openSection == section.id

        Button {
            // Tapping the open branch closes it: with one branch open at a
            // time there would otherwise be no way back to a short screen.
            openSection = isOpen ? nil : section.id
        } label: {
            HStack(spacing: 10) {
                Text("#")
                    .font(.system(size: 15, weight: .semibold))
                    .foregroundColor(isOpen ? Theme.accent : Theme.secondaryText)
                    .frame(width: 16)
                Text(section.label)
                    .font(Theme.bodyFont)
                    .foregroundColor(Theme.primaryText)
                Spacer()
                if let total = section.total {
                    Text("\(total)")
                        .font(Theme.tagFont)
                        .foregroundColor(Theme.secondaryText)
                        .monospacedDigit()
                }
                Image(systemName: "chevron.right")
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundColor(Theme.secondaryText.opacity(0.6))
                    .rotationEffect(.degrees(isOpen ? 90 : 0))
            }
            .padding(.vertical, 12)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)

        if isOpen {
            if let missing = section.unavailable {
                Text(missing)
                    .font(.system(size: 12))
                    .foregroundColor(Theme.secondaryText)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(.leading, 26)
                    .padding(.bottom, 10)
            } else {
                VStack(alignment: .leading, spacing: 0) {
                    ForEach(section.children) { child in
                        childRow(child)
                    }
                }
                .padding(.leading, 26)
                .padding(.bottom, 6)
                // The hairline is the tree: it is what says these rows belong
                // to the branch above rather than to the screen.
                .overlay(alignment: .leading) {
                    Rectangle()
                        .fill(Theme.secondaryText.opacity(0.18))
                        .frame(width: 1)
                        .padding(.leading, 7)
                        .padding(.vertical, 4)
                }
            }
        }
    }

    private func childRow(_ child: HomeEntry) -> some View {
        Button {
            onStart(child.scope)
        } label: {
            HStack(spacing: 10) {
                Text("#")
                    .font(.system(size: 13, weight: .semibold))
                    .foregroundColor(Theme.secondaryText.opacity(0.7))
                    .frame(width: 14)
                Text(child.label)
                    .font(Theme.bodyFont)
                    .foregroundColor(Theme.primaryText)
                Spacer()
                Text(Self.countLabel(child))
                    .font(Theme.tagFont)
                    .foregroundColor(Theme.secondaryText)
            }
            .padding(.vertical, 10)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }
}

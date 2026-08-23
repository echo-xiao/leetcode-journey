import SwiftUI

/// One row on the home screen: a scope you can start a session in.
struct HomeEntry: Identifiable, Equatable {
    let id: String
    let label: String
    /// The length of the session this row will start — never a backlog count.
    let count: Int
    let scope: SessionScope
}

/// Three numbers, the heatmap, and the list of sessions.
///
/// Rows advertise session length, never how much is overdue. Opening an app to
/// find 400 cards waiting is the failure mode this whole design exists to
/// avoid.
struct HomeView: View {
    let problemCount: Int
    let totalReviews: Int
    let streak: Int
    let cells: [HeatmapCell]
    let entries: [HomeEntry]
    let sessionLength: Int
    let activityStatus: ActivityStatus
    let onStart: (SessionScope) -> Void
    let onChangeSessionLength: (Int) -> Void

    @State private var showSettings = false

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

    private var counters: some View {
        HStack(spacing: 0) {
            counter(problemCount, "题目")
            counter(totalReviews, "复习")
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
                        Text("\(entry.count) 题")
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
}

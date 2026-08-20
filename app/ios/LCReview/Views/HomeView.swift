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
    let onStart: (SessionScope) -> Void

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                counters
                HeatmapView(cells: cells)
                list
            }
            .padding(Theme.cardPadding)
            .background(Theme.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: Theme.cardCornerRadius, style: .continuous))
            .padding(16)
        }
        .background(Theme.pageBackground)
    }

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

import SwiftUI

/// Ninety days, one cell each, laid out in month columns.
///
/// Fixed window, no scrolling: there is nothing to look at beyond it, and a
/// scrollable grid invites archaeology instead of practice.
struct HeatmapView: View {
    let cells: [HeatmapCell]

    private let side: CGFloat = 11
    private let gap: CGFloat = 3

    private var weeks: [[HeatmapCell]] {
        stride(from: 0, to: cells.count, by: 7).map {
            Array(cells[$0..<min($0 + 7, cells.count)])
        }
    }

    /// One label per week column, empty string where no label belongs.
    ///
    /// The brief's version built a *compacted* array of only the non-empty
    /// labels and then laid them out with fixed spacing — that only lines up
    /// with the columns above by coincidence, since a compacted array has no
    /// notion of which week each label belongs under. This instead produces
    /// exactly `weeks.count` entries, one per column, so the label and its
    /// column can share the same `ForEach` index and a zero-spacing `HStack`
    /// each cell of which is exactly `side` wide (matching the column above).
    private var monthLabels: [String] {
        let formatter = DateFormatter()
        formatter.dateFormat = "M月"
        var seen = Set<Int>()
        return weeks.map { week -> String in
            guard let first = week.first else { return "" }
            let month = Calendar.current.component(.month, from: first.day)
            guard seen.insert(month).inserted else { return "" }
            return formatter.string(from: first.day)
        }
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(alignment: .top, spacing: gap) {
                ForEach(Array(weeks.enumerated()), id: \.offset) { _, week in
                    VStack(spacing: gap) {
                        ForEach(Array(week.enumerated()), id: \.offset) { _, cell in
                            RoundedRectangle(cornerRadius: 2.5, style: .continuous)
                                .fill(cell.isBeforeStart ? Color.clear : Theme.heatmapColor(count: cell.count))
                                .frame(width: side, height: side)
                        }
                    }
                    .frame(width: side)
                }
            }
            HStack(alignment: .top, spacing: gap) {
                ForEach(Array(monthLabels.enumerated()), id: \.offset) { _, label in
                    Text(label)
                        .font(.system(size: 9))
                        .foregroundColor(Theme.secondaryText)
                        .lineLimit(1)
                        .fixedSize()
                        .frame(width: side, alignment: .leading)
                }
            }
        }
    }
}

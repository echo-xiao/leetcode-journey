import SwiftUI

/// The submission calendar, one cell per day, laid out in week columns.
///
/// The grid draws as many week columns as the width it is given can hold,
/// keeping the most recent ones, so it always reaches the right edge instead
/// of stopping short with dead space beside it. That means the number of days
/// on screen follows the device rather than a constant: the store fetches a
/// generous window (`ActivityStore.windowDays`) and the view takes the tail
/// of it. The larger window is free -- the API answers per year whatever
/// range is asked for.
///
/// Still a fixed window and still no scrolling: there is nothing to look at
/// beyond it, and a scrollable grid invites archaeology instead of practice.
struct HeatmapView: View {
    let cells: [HeatmapCell]

    private static let side: CGFloat = 11
    private static let gap: CGFloat = 3
    private static let labelHeight: CGFloat = 12
    private static let labelSpacing: CGFloat = 6

    /// How many columns of `side` wide, separated by `gap`, fit in `width`.
    ///
    /// n columns occupy `n * side + (n - 1) * gap`. Never returns less than
    /// one: a zero-column grid would collapse the layout on the first frame,
    /// before SwiftUI has measured anything.
    static func columnsThatFit(width: CGFloat, side: CGFloat, gap: CGFloat) -> Int {
        guard width > 0, side > 0 else { return 1 }
        // The epsilon is not cosmetic: an exact fit computed in binary
        // floating point can land a hair under the integer and would
        // otherwise silently cost a column.
        let fit = Int((width + gap + 0.001) / (side + gap))
        return max(1, fit)
    }

    /// The last `columns` weeks, which are the most recent ones -- the window
    /// arrives oldest-first, so trimming the wrong end would drop today.
    static func trailingWeeks(_ weeks: [[HeatmapCell]], columns: Int) -> [[HeatmapCell]] {
        guard weeks.count > columns else { return weeks }
        return Array(weeks.suffix(columns))
    }

    private var allWeeks: [[HeatmapCell]] {
        stride(from: 0, to: cells.count, by: 7).map {
            Array(cells[$0..<min($0 + 7, cells.count)])
        }
    }

    private var gridHeight: CGFloat {
        Self.side * 7 + Self.gap * 6 + Self.labelSpacing + Self.labelHeight
    }

    var body: some View {
        // Only the width is read from the geometry; the height is known from
        // the seven rows and the label beneath them. A GeometryReader has no
        // intrinsic size of its own, so without the explicit height it would
        // swallow whatever the surrounding stack offered.
        GeometryReader { geo in
            grid(weeks: Self.trailingWeeks(
                allWeeks,
                columns: Self.columnsThatFit(
                    width: geo.size.width, side: Self.side, gap: Self.gap
                )
            ))
        }
        .frame(height: gridHeight)
    }

    private func grid(weeks: [[HeatmapCell]]) -> some View {
        VStack(alignment: .leading, spacing: Self.labelSpacing) {
            HStack(alignment: .top, spacing: Self.gap) {
                ForEach(Array(weeks.enumerated()), id: \.offset) { _, week in
                    VStack(spacing: Self.gap) {
                        ForEach(Array(week.enumerated()), id: \.offset) { _, cell in
                            RoundedRectangle(cornerRadius: 2.5, style: .continuous)
                                .fill(Theme.heatmapColor(count: cell.count))
                                .frame(width: Self.side, height: Self.side)
                        }
                    }
                    .frame(width: Self.side)
                }
            }
            HStack(alignment: .top, spacing: Self.gap) {
                ForEach(Array(monthLabels(weeks).enumerated()), id: \.offset) { _, label in
                    Text(label)
                        .font(.system(size: 9))
                        .foregroundColor(Theme.secondaryText)
                        .lineLimit(1)
                        .fixedSize()
                        .frame(width: Self.side, alignment: .leading)
                }
            }
            .frame(height: Self.labelHeight)
        }
    }

    /// One label per week column, empty string where no label belongs.
    ///
    /// Producing exactly `weeks.count` entries — rather than a compacted
    /// array of only the non-empty ones — is what keeps a label under the
    /// column it names: label and column share the same `ForEach` index, and
    /// every slot is exactly `side` wide, matching the column above.
    ///
    /// The month is read in UTC, the same calendar the day keys are bucketed
    /// in, so a column never gets labelled with a month its own cells do not
    /// belong to.
    private func monthLabels(_ weeks: [[HeatmapCell]]) -> [String] {
        let formatter = DateFormatter()
        formatter.dateFormat = "M月"
        formatter.timeZone = TimeZone(secondsFromGMT: 0)
        var seen = Set<Int>()
        return weeks.map { week -> String in
            guard let first = week.first else { return "" }
            let month = ActivityCalendar.utcCalendar.component(.month, from: first.day)
            guard seen.insert(month).inserted else { return "" }
            return formatter.string(from: first.day)
        }
    }
}

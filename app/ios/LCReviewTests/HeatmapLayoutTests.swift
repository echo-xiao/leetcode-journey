import XCTest
@testable import LCReview

final class HeatmapLayoutTests: XCTestCase {

    private let side: CGFloat = 11
    private let gap: CGFloat = 3

    func testColumnsFillTheWidthWithoutOverflowing() {
        // n columns occupy n*side + (n-1)*gap. At 11pt cells and 3pt gaps
        // that is 14n - 3, so 299pt fits 21 columns (291pt) and not 22 (305).
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 299, side: side, gap: gap), 21)
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 305, side: side, gap: gap), 22)
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 304, side: side, gap: gap), 21)
    }

    func testAnExactFitIsNotRoundedDown() {
        // 291 == 21 * 11 + 20 * 3 exactly. Floating point must not shave this
        // to 20 -- the grid would sit one column short of the edge forever.
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 291, side: side, gap: gap), 21)
    }

    func testAtLeastOneColumnEvenInAnAbsurdlyNarrowSpace() {
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 4, side: side, gap: gap), 1)
        XCTAssertEqual(HeatmapView.columnsThatFit(width: 0, side: side, gap: gap), 1)
        XCTAssertEqual(HeatmapView.columnsThatFit(width: -20, side: side, gap: gap), 1)
    }

    func testKeepsTheMostRecentColumnsNotTheOldest() {
        // The window arrives oldest-first. Trimming from the wrong end would
        // draw half a year ago and leave today off the grid.
        let weeks = (0..<26).map { column in
            (0..<7).map { row in
                HeatmapCell(
                    day: Date(timeIntervalSince1970: TimeInterval(column * 7 + row) * 86_400),
                    count: column
                )
            }
        }

        let kept = HeatmapView.trailingWeeks(weeks, columns: 21)

        XCTAssertEqual(kept.count, 21)
        XCTAssertEqual(kept.first?.first?.count, 5, "the five oldest columns are dropped")
        XCTAssertEqual(kept.last?.first?.count, 25, "the newest column survives")
    }

    func testAskingForMoreColumnsThanExistKeepsThemAll() {
        let weeks = (0..<3).map { column in
            [HeatmapCell(day: Date(timeIntervalSince1970: 0), count: column)]
        }

        XCTAssertEqual(HeatmapView.trailingWeeks(weeks, columns: 21).count, 3)
    }
}

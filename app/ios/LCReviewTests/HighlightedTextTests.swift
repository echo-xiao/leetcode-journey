import XCTest
@testable import LCReview

final class HighlightedTextTests: XCTestCase {

    func testPlainTextIsOneUnhighlightedSegment() {
        XCTAssertEqual(
            HighlightParser.parse("第一遍没想到要先排序。"),
            [HighlightSegment(text: "第一遍没想到要先排序。", isHighlighted: false)]
        )
    }

    func testMarkedSpanBecomesAHighlightedSegment() {
        XCTAssertEqual(
            HighlightParser.parse("前==中间==后"),
            [
                HighlightSegment(text: "前", isHighlighted: false),
                HighlightSegment(text: "中间", isHighlighted: true),
                HighlightSegment(text: "后", isHighlighted: false),
            ]
        )
    }

    func testBoldMarkersInsideAHighlightAreStripped() {
        // Retrospectives are written as ==**text**==, and the app draws the
        // emphasis with a background, so the asterisks must not show up.
        XCTAssertEqual(
            HighlightParser.parse("==**去重漏了。**=="),
            [HighlightSegment(text: "去重漏了。", isHighlighted: true)]
        )
    }

    func testMultipleHighlightsInOneRetrospective() {
        let segments = HighlightParser.parse("a==b==c==d==e")
        XCTAssertEqual(segments.map(\.text), ["a", "b", "c", "d", "e"])
        XCTAssertEqual(segments.map(\.isHighlighted), [false, true, false, true, false])
    }

    func testUnclosedMarkerIsLeftAlone() {
        XCTAssertEqual(
            HighlightParser.parse("前==没有闭合"),
            [HighlightSegment(text: "前==没有闭合", isHighlighted: false)]
        )
    }

    func testEmptyStringYieldsNothing() {
        XCTAssertEqual(HighlightParser.parse(""), [])
    }
}

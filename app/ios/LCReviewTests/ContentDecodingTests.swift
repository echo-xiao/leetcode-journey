import XCTest
@testable import LCReview

final class ContentDecodingTests: XCTestCase {

    private func loadSample() throws -> ContentPayload {
        let url = try XCTUnwrap(
            Bundle(for: Self.self).url(forResource: "sample-content", withExtension: "json"),
            "sample-content.json is not in the test bundle — check Target Membership"
        )
        let data = try Data(contentsOf: url)
        return try JSONDecoder().decode(ContentPayload.self, from: data)
    }

    func testDecodesEveryLayerOfTheChain() throws {
        let payload = try loadSample()
        XCTAssertEqual(payload.version, 2)
        XCTAssertEqual(payload.problems.count, 2)

        let first = payload.problems[0]
        XCTAssertEqual(first.id, "15_3sum")
        XCTAssertEqual(first.number, 15)
        XCTAssertEqual(first.title, "15. 三数之和")
        XCTAssertEqual(first.technique, "数组双指针")
        XCTAssertEqual(first.elements.count, 2)
        XCTAssertTrue(first.pseudocode.contains { $0.kind == .code && $0.text.contains("双指针夹逼") })
        XCTAssertTrue(first.pseudocode.contains { $0.kind == .heading && $0.text == "1. 核心本质" })
        XCTAssertEqual(first.solutions.first?.name, "solution_1.py")
    }

    func testKeepsHighlightMarkersVerbatim() throws {
        let payload = try loadSample()
        XCTAssertTrue(
            payload.problems[0].retrospective.contains("==**跳过重复元素那一步漏了。**==")
        )
    }

    func testEmptyRetrospectiveAndSolutionsAreNotErrors() throws {
        let payload = try loadSample()
        let second = payload.problems[1]
        XCTAssertEqual(second.retrospective, "")
        XCTAssertTrue(second.solutions.isEmpty)
    }

    func testLayerAdvancesThroughTheChainAndKnowsItsTrack() {
        XCTAssertEqual(Layer.statement.next, .elements)
        XCTAssertEqual(Layer.solutions.next, nil)
        XCTAssertEqual(Layer.elements.track, .elements)
        XCTAssertEqual(Layer.pseudocode.track, .pseudocode)
        XCTAssertNil(Layer.retrospective.track)
        XCTAssertNil(Layer.solutions.track)
    }

    func testGradeHasExactlyThreeCases() {
        XCTAssertEqual(Grade.allCases.count, 3)
        XCTAssertEqual(Grade.again.rawValue, 1)
        XCTAssertEqual(Grade.good.rawValue, 3)
    }
}

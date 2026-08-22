import XCTest
@testable import LCReview

final class ActivityTransportTests: XCTestCase {

    /// The shape leetcode.com/graphql really returns, trimmed to three days.
    /// submissionCalendar is a JSON *string* nested inside the JSON body,
    /// keyed by UTC-midnight unix seconds.
    private let realResponse = """
    {"data":{"matchedUser":{"userCalendar":{"streak":15,"totalActiveDays":48,\
    "submissionCalendar":"{\\"1785110400\\": 54, \\"1787097600\\": 48, \\"1787184000\\": 78}"}}}}
    """

    func testParsesTheRealResponseShape() throws {
        let year = try HTTPActivityTransport.parse(Data(realResponse.utf8))

        XCTAssertEqual(year.streak, 15)
        XCTAssertEqual(year.countsByDay["2026-07-27"], 54)
        XCTAssertEqual(year.countsByDay["2026-08-19"], 48)
        XCTAssertEqual(year.countsByDay["2026-08-20"], 78)
        XCTAssertEqual(year.countsByDay.count, 3)
    }

    func testRejectsAnHTMLErrorPage() {
        let html = Data("<html><body>502 Bad Gateway</body></html>".utf8)
        XCTAssertThrowsError(try HTTPActivityTransport.parse(html))
    }

    func testRejectsAGraphQLErrorEnvelope() {
        // What comes back when the query itself is rejected: valid JSON,
        // no data node.
        let body = Data(#"{"errors":[{"message":"unknown field"}]}"#.utf8)
        XCTAssertThrowsError(try HTTPActivityTransport.parse(body))
    }

    func testRejectsAnUnknownUser() {
        // matchedUser is null for a username that does not exist.
        let body = Data(#"{"data":{"matchedUser":null}}"#.utf8)
        XCTAssertThrowsError(try HTTPActivityTransport.parse(body))
    }

    func testRejectsARenamedField() {
        // The failure this design explicitly accepts: LeetCode renames
        // something and the app must fail loudly to its caller rather than
        // return a half-built calendar.
        let body = """
        {"data":{"matchedUser":{"userCalendar":{"streak":15,\
        "submissions":"{\\"1787184000\\": 78}"}}}}
        """
        XCTAssertThrowsError(try HTTPActivityTransport.parse(Data(body.utf8)))
    }

    func testRejectsANonNumericDayKey() {
        let body = """
        {"data":{"matchedUser":{"userCalendar":{"streak":1,\
        "submissionCalendar":"{\\"yesterday\\": 3}"}}}}
        """
        XCTAssertThrowsError(try HTTPActivityTransport.parse(Data(body.utf8)))
    }
}

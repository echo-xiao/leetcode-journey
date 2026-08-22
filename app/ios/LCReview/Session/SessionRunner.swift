import Foundation

/// One stop in a session.
///
/// `askOnly == nil` is a normal problem: walk the whole chain. A non-nil value
/// is an in-session repeat, which asks that one layer and nothing else.
struct SessionStep: Equatable {
    let problemID: String
    let askOnly: Track?
}

/// Drives one session: where we are, how far the card is open, and which
/// layers earned themselves a repeat.
///
/// Holds no persistence. The view calls `record(grade:)` and separately hands
/// the grade to `Grading`; keeping those apart is what makes this testable
/// without a ModelContext.
@MainActor
final class SessionRunner: ObservableObject {

    /// A third attempt in the same sitting teaches nothing; the cross-day
    /// schedule takes it from there.
    static let maxRepeatsPerLayer = 2

    @Published private(set) var index: Int = 0
    /// How far each card has been opened, kept per index so going back
    /// restores what you left rather than closing the card.
    @Published private(set) var revealedByIndex: [Int: Layer] = [:]

    private var steps: [SessionStep]
    /// How many of the N originally queued problems came before the repeats.
    private let plannedCount: Int
    /// The furthest card reached. Progress tracks this, not `index`, so
    /// looking back does not rewind the counter.
    private var furthestIndex: Int = 0
    private var repeatCounts: [SessionStep: Int] = [:]

    private(set) var repeatsScheduled: [SessionStep] = []

    init(steps: [SessionStep]) {
        self.steps = steps
        self.plannedCount = steps.count
    }

    var revealed: Layer { revealedByIndex[index] ?? .statement }

    var current: SessionStep? {
        index < steps.count ? steps[index] : nil
    }

    var isFinished: Bool { index >= steps.count }

    /// Repeats are extra work, not part of the advertised length, so the total
    /// stays at what the home screen promised.
    var progress: (done: Int, total: Int) {
        (min(furthestIndex, plannedCount), plannedCount)
    }

    /// The track the next tap must grade before it may reveal, if any.
    func pendingGrade() -> Track? {
        guard let step = current else { return nil }
        if let only = step.askOnly {
            // A repeat asks its one layer, then it is done.
            return revealed.rawValue < only.layer.rawValue ? only : nil
        }
        guard let next = revealed.next else { return nil }
        return next.track
    }

    /// Advance one layer. Refuses when a grade is owed, so no path can reveal
    /// an answer before the self-assessment is committed.
    func reveal() {
        guard pendingGrade() == nil, let next = revealed.next else { return }
        guard current?.askOnly == nil else { return }
        revealedByIndex[index] = next
    }

    /// Commit the grade for the pending layer and open it.
    func record(grade: Grade) {
        guard let step = current, let track = pendingGrade() else { return }
        revealedByIndex[index] = track.layer

        guard grade == .again else { return }
        let repeated = SessionStep(problemID: step.problemID, askOnly: track)
        let seen = repeatCounts[repeated, default: 0]
        guard seen < Self.maxRepeatsPerLayer else { return }
        repeatCounts[repeated] = seen + 1
        repeatsScheduled.append(repeated)
        steps.append(repeated)
    }

    /// Move to the next stop. Leaving a chain half-open is allowed on purpose:
    /// grades already given stand, the untouched layers keep their due dates.
    func advance() {
        index += 1
        furthestIndex = max(furthestIndex, index)
    }

    /// Go back one stop, to look rather than to re-answer.
    ///
    /// The card reopens exactly as far as it was left. Nothing is rolled back
    /// and no answered layer is asked again — that falls out of `revealed`
    /// only ever moving forward, so it needs no special case. A layer that was
    /// never answered can still be answered, which is finishing work rather
    /// than re-grading it.
    func goBack() {
        guard index > 0 else { return }
        index -= 1
    }
}

private extension Track {
    var layer: Layer {
        switch self {
        case .elements: return .elements
        case .pseudocode: return .pseudocode
        }
    }
}

extension SessionStep: Hashable {
    static func == (lhs: SessionStep, rhs: SessionStep) -> Bool {
        lhs.problemID == rhs.problemID && lhs.askOnly == rhs.askOnly
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(problemID)
        hasher.combine(askOnly)
    }
}

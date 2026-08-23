import Foundation

/// One stop in a session: a problem, and whether this is the extra pass a
/// 不会 earned it earlier in the same sitting.
struct SessionStep: Equatable, Hashable {
    let problemID: String
    let isRepeat: Bool
}

/// Drives one session: where we are, and how far the card is open.
///
/// Two movements, deliberately kept apart. `reveal()` opens one more layer and
/// never leaves the problem; `grade(_:)` is the only way to the next problem.
/// Tapping looks further down, grading moves on. Nothing navigates sideways --
/// there is no going back, and no gesture competes with the card's scroll.
///
/// Holds no persistence. The view calls `grade(_:)` and separately hands the
/// grade to `Grading`; keeping those apart is what makes this testable without
/// a ModelContext.
@MainActor
final class SessionRunner: ObservableObject {

    /// A third attempt in the same sitting teaches nothing; the cross-day
    /// schedule takes it from there.
    static let maxRepeatsPerProblem = 2

    @Published private(set) var index: Int = 0
    @Published private(set) var revealedByIndex: [Int: Layer] = [:]

    private var steps: [SessionStep]
    /// How many problems were queued before any repeats were appended.
    private let plannedCount: Int
    private var repeatCounts: [String: Int] = [:]

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

    /// Repeats are extra work appended past the advertised length, so the
    /// total stays at what the home screen promised. `index` only ever moves
    /// forward now that there is no going back, so it is its own high-water
    /// mark and no separate counter is kept.
    var progress: (done: Int, total: Int) {
        (min(index, plannedCount), plannedCount)
    }

    /// Open one more layer. Running out of layers is a no-op: tapping is how
    /// you look further down the chain, never how you leave the problem.
    func reveal() {
        guard let next = revealed.next else { return }
        revealedByIndex[index] = next
    }

    /// Commit the one grade this problem gets, and move to the next stop.
    ///
    /// A 不会 queues the problem again at the end of the session, at most
    /// twice. A repeat that is failed again is not re-queued -- that is what
    /// the cap is for, and counting from the original grade keeps a bad
    /// problem from filling the session with itself.
    func grade(_ grade: Grade) {
        guard let step = current else { return }

        if grade == .again, !step.isRepeat {
            let seen = repeatCounts[step.problemID, default: 0]
            if seen < Self.maxRepeatsPerProblem {
                repeatCounts[step.problemID] = seen + 1
                let repeated = SessionStep(problemID: step.problemID, isRepeat: true)
                repeatsScheduled.append(repeated)
                steps.append(repeated)
            }
        }

        index += 1
    }
}

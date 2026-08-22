import Foundation
import SwiftData

/// Wires the pieces together and owns everything the views read.
///
/// Each piece stays testable on its own; this is the only place that knows
/// about all of them at once.
@MainActor
final class AppState: ObservableObject {

    @Published private(set) var problems: [Problem] = []
    @Published private(set) var isLoading = true
    @Published private(set) var loadFailed = false
    @Published var activeRunner: SessionRunner?

    /// Mirrors `AppSettings.sessionLength`. Published so the home screen's
    /// rows redraw the moment the settings sheet writes a new value — the
    /// underlying SwiftData model isn't itself observable, so without this
    /// mirror `homeEntries` would only recompute the next time some other
    /// `@Published` property happened to change.
    @Published private(set) var sessionLength: Int

    private let store: ContentStore
    private let context: ModelContext
    private let builder = SessionBuilder()
    private let grading = Grading(fsrs: FSRS())
    private let summary = Summary()

    init(store: ContentStore, context: ModelContext) {
        self.store = store
        self.context = context
        self.sessionLength = Self.fetchOrCreateSettings(context: context).sessionLength
    }

    // MARK: - Content

    func loadContent() async {
        isLoading = true
        problems = await store.load()
        loadFailed = problems.isEmpty
        isLoading = false
    }

    // MARK: - Settings

    /// The single settings row, created on first access.
    ///
    /// It is saved immediately: without that, a second access before the next
    /// save would fetch nothing and insert a duplicate, and the start day —
    /// which the heatmap is drawn against — would quietly move.
    var settings: AppSettings { Self.fetchOrCreateSettings(context: context) }

    /// A `static` twin of `settings` so `init` can seed `sessionLength`
    /// before `self` exists — Swift won't let a designated initializer call
    /// an instance computed property until every stored property has a
    /// value.
    private static func fetchOrCreateSettings(context: ModelContext) -> AppSettings {
        if let existing = try? context.fetch(FetchDescriptor<AppSettings>()).first {
            return existing
        }
        let created = AppSettings(startDay: Calendar.current.startOfDay(for: .now))
        context.insert(created)
        try? context.save()
        return created
    }

    /// Writes the new session length to SwiftData and republishes it. Takes
    /// effect the next time a session is built — `activeRunner`'s queue was
    /// already fixed at start time, so a session in progress is deliberately
    /// left alone.
    func updateSessionLength(_ newValue: Int) {
        settings.sessionLength = newValue
        try? context.save()
        sessionLength = newValue
    }

    // MARK: - Home

    private var allStates: [CardState] {
        (try? context.fetch(FetchDescriptor<CardState>())) ?? []
    }

    private var allLogs: [ReviewLog] {
        (try? context.fetch(FetchDescriptor<ReviewLog>())) ?? []
    }

    var totalReviews: Int { summary.totalReviews(logs: allLogs) }
    var streak: Int { summary.streak(logs: allLogs, now: .now) }

    var heatmapCells: [HeatmapCell] {
        summary.heatmap(logs: allLogs, startDay: settings.startDay, now: .now)
    }

    var homeEntries: [HomeEntry] {
        let length = sessionLength
        let states = allStates
        var entries: [HomeEntry] = []

        let mistakes = builder.build(
            scope: .mistakes, length: length, problems: problems, states: states, now: .now
        )
        if !mistakes.isEmpty {
            entries.append(
                HomeEntry(id: "mistakes", label: "错题", count: mistakes.count, scope: .mistakes)
            )
        }

        let all = builder.build(
            scope: .all, length: length, problems: problems, states: states, now: .now
        )
        entries.append(HomeEntry(id: "all", label: "全部", count: all.count, scope: .all))

        // Ordered by how much of the library each technique covers, so the
        // ones echo actually practises sit at the top.
        let techniques = Dictionary(grouping: problems, by: \.technique)
            .sorted { $0.value.count > $1.value.count }
        for (name, group) in techniques where !name.isEmpty {
            entries.append(
                HomeEntry(
                    id: name, label: name,
                    count: min(length, group.count), scope: .technique(name)
                )
            )
        }
        return entries
    }

    // MARK: - Sessions

    func startSession(scope: SessionScope) {
        let queue = builder.build(
            scope: scope, length: sessionLength,
            problems: problems, states: allStates, now: .now
        )
        activeRunner = SessionRunner(
            steps: queue.map { SessionStep(problemID: $0.id, askOnly: nil) }
        )
    }

    func finishSession() {
        activeRunner = nil
    }

    func record(problemID: String, track: Track, grade: Grade, isRepeat: Bool) {
        let existing = allStates.first {
            $0.problemID == problemID && $0.track == track
        }
        let (state, log) = grading.apply(
            grade: grade, to: existing, problemID: problemID, track: track,
            isRepeat: isRepeat, now: .now
        )
        if existing == nil { context.insert(state) }
        if let log { context.insert(log) }
        try? context.save()
    }
}

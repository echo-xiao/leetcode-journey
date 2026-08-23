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

    /// The heatmap, the streak, and how much to trust them. All three
    /// come from LeetCode and arrive from one fetch, so they are
    /// published together and never disagree about which snapshot they
    /// belong to.
    @Published private(set) var heatmapCells: [HeatmapCell] = []
    @Published private(set) var activityStreak = 0
    @Published private(set) var activityStatus: ActivityStatus = .unavailable

    private let store: ContentStore
    private let activity: ActivityStore
    private let context: ModelContext
    private let builder = SessionBuilder()
    private let grading = Grading(fsrs: FSRS())
    private let summary = Summary()

    init(store: ContentStore, activity: ActivityStore, context: ModelContext) {
        self.store = store
        self.activity = activity
        self.context = context
        self.sessionLength = Self.fetchOrCreateSettings(context: context).sessionLength
    }

    // MARK: - Content

    /// Called on launch and again on every return to the foreground.
    ///
    /// The spinner is only for a cold start. Once there are problems on
    /// screen a refresh happens behind them: the fetch is conditional, so it
    /// usually costs a 304 and nothing else, and flashing a loading state
    /// over a screen that already has content reads as a bug.
    func loadContent() async {
        let isFirstLoad = problems.isEmpty
        if isFirstLoad { isLoading = true }
        let fetched = await store.load()
        // An empty result on a refresh is a failed fetch, not an empty
        // library. Keeping what is on screen is right either way, and it also
        // means a moment offline cannot wipe the home screen.
        if !fetched.isEmpty { problems = fetched }
        loadFailed = problems.isEmpty
        isLoading = false
    }

    /// Refreshed on every foreground, not on a timer and not by a pull
    /// gesture: the app is opened a handful of times a day, and a heatmap
    /// is retrospective enough that a few hours of lag costs nothing.
    func loadActivity() async {
        let snapshot = await activity.load(now: .now)
        heatmapCells = snapshot.cells
        activityStreak = snapshot.streak
        activityStatus = snapshot.status
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
        let created = AppSettings()
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
    /// The rows above the tree: what you start without choosing a lens.
    ///
    /// 错题 only appears when there is something in it. A row that is always
    /// there and usually says zero trains you to stop reading the screen.
    var homeEntries: [HomeEntry] {
        let states = allStates
        var entries: [HomeEntry] = []

        let mistakes = builder.build(
            scope: .mistakes, length: sessionLength, problems: problems,
            states: states, now: .now
        )
        if !mistakes.isEmpty {
            entries.append(
                HomeEntry(id: "mistakes", label: "错题", count: mistakes.count, scope: .mistakes)
            )
        }

        let all = builder.build(
            scope: .all, length: sessionLength, problems: problems, states: states, now: .now
        )
        entries.append(HomeEntry(id: "all", label: "全部", count: all.count, scope: .all))
        return entries
    }

    /// The four ways of choosing what to practise, as a tree.
    ///
    /// Recency leads: the thing this app is for is reviewing what was just
    /// solved, and a lens you reach for daily should not sit below one you
    /// reach for occasionally.
    ///
    /// Two of them have no data behind them yet and say so. Shipping them as
    /// empty lists would read as broken; naming what is missing is how the
    /// screen stays honest about its own gaps.
    var homeSections: [HomeSection] {
        [recentSection, techniqueSection, companySection, problemSetSection]
    }

    private var techniqueSection: HomeSection {
        // Ordered by how much of the library each technique covers, so the
        // ones echo actually practises sit at the top.
        let grouped = Dictionary(grouping: problems, by: \.technique)
            .filter { !$0.key.isEmpty }
            .sorted { $0.value.count > $1.value.count }
        let children = grouped.map { name, group in
            HomeEntry(
                id: "technique-\(name)", label: name,
                count: min(sessionLength, group.count), scope: .technique(name)
            )
        }
        return HomeSection(
            id: "technique", label: "按类别刷",
            total: problems.count, children: children, unavailable: nil
        )
    }

    private var recentSection: HomeSection {
        let windows: [(String, Int?)] = [
            ("这周过的", 7), ("最近 30 天", 30), ("最近 90 天", 90), ("从最新往回刷", nil),
        ]
        let states = allStates
        let children = windows.compactMap { label, days -> HomeEntry? in
            let queue = builder.build(
                scope: .recent(withinDays: days), length: sessionLength,
                problems: problems, states: states, now: .now
            )
            // A window with nothing in it is dropped rather than shown as
            // zero: it is a slice of time, not a category, and an empty slice
            // is not a thing you can start.
            guard !queue.isEmpty else { return nil }
            return HomeEntry(
                id: "recent-\(days.map(String.init) ?? "all")", label: label,
                count: queue.count, scope: .recent(withinDays: days)
            )
        }
        return HomeSection(
            id: "recent", label: "按最近刷",
            total: problems.filter { $0.solvedAt != nil }.count,
            children: children, unavailable: nil
        )
    }

    private var companySection: HomeSection {
        HomeSection(
            id: "company", label: "按公司刷", total: nil, children: [],
            unavailable: "力扣的公司标签是会员专属，仓库里没有这份数据。"
        )
    }

    private var problemSetSection: HomeSection {
        HomeSection(
            id: "problemset", label: "按题库刷", total: nil, children: [],
            unavailable: "题目只按题型分组，还没有题单归属（LC75、热题 100）。"
        )
    }

    // MARK: - Sessions

    func startSession(scope: SessionScope) {
        let queue = builder.build(
            scope: scope, length: sessionLength,
            problems: problems, states: allStates, now: .now
        )
        activeRunner = SessionRunner(
            steps: queue.map { SessionStep(problemID: $0.id, isRepeat: false) }
        )
    }

    func finishSession() {
        activeRunner = nil
    }

    func record(problemID: String, grade: Grade, isRepeat: Bool) {
        let existing = allStates.first { $0.problemID == problemID }
        let (state, log) = grading.apply(
            grade: grade, to: existing, problemID: problemID,
            isRepeat: isRepeat, now: .now
        )
        if existing == nil { context.insert(state) }
        if let log { context.insert(log) }
        try? context.save()
    }
}

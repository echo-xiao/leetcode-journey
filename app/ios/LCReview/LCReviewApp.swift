import SwiftData
import SwiftUI

@main
struct LCReviewApp: App {

    // `container` and `state` are both nil together: construction either
    // fully succeeds or fully fails, there is no partial state to reconcile.
    @State private var container: ModelContainer?
    @State private var state: AppState?

    init() {
        do {
            // NOTE: no VersionedSchema / SchemaMigrationPlan yet — this infers
            // the schema from the current model types every launch. That is
            // fine as long as every future model change is one SwiftData can
            // infer on its own (adding an optional property, for instance).
            // The day a change needs an explicit migration (renaming a
            // property, changing a type, splitting a model) and none exists,
            // this throws on every launch for everyone who already has data
            // on disk — which is exactly the failure this catch is for. The
            // real fix, before that day comes, is introducing a
            // VersionedSchema + SchemaMigrationPlan so upgrades migrate the
            // store in place instead of merely failing without crashing.
            let container = try ModelContainer(
                for: CardState.self, ReviewLog.self, AppSettings.self
            )
            _container = State(initialValue: container)
            _state = State(
                initialValue: AppState(
                    store: ContentStore(
                        transport: HTTPContentTransport(),
                        cacheURL: ContentStore.defaultCacheURL()
                    ),
                    activity: ActivityStore(
                        transport: HTTPActivityTransport(),
                        cacheURL: ActivityStore.defaultCacheURL()
                    ),
                    context: ModelContext(container)
                )
            )
        } catch {
            // Deliberately not falling back to an in-memory container: that
            // would look like the app works while silently discarding every
            // grade for the rest of the session. Showing a plain failure
            // screen is the honest option — the review schedule lives only
            // on this device, so losing it silently is worse than an app
            // that visibly refuses to open.
            _container = State(initialValue: nil)
            _state = State(initialValue: nil)
        }
    }

    var body: some Scene {
        WindowGroup {
            if let container, let state {
                RootView()
                    .environmentObject(state)
                    .modelContainer(container)
            } else {
                DataStoreFailedView()
            }
        }
    }
}

/// Shown instead of crashing when the SwiftData store can't be opened.
///
/// This is the only recovery message the app can honestly offer today: there
/// is no migration path yet (see the comment at the `ModelContainer` call in
/// `LCReviewApp.init`), so the only way out of a genuinely incompatible store
/// is removing it, which also erases the review schedule since nothing syncs
/// it anywhere else.
struct DataStoreFailedView: View {
    var body: some View {
        VStack(spacing: 14) {
            Text("数据打不开了")
                .font(Theme.titleFont)
                .foregroundColor(Theme.primaryText)
            Text("删除并重装 App 可以解决，但会丢掉复习进度。")
                .font(Theme.bodyFont)
                .foregroundColor(Theme.secondaryText)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 32)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Theme.pageBackground)
    }
}

struct RootView: View {
    @EnvironmentObject private var state: AppState
    @Environment(\.scenePhase) private var scenePhase

    var body: some View {
        Group {
            if let runner = state.activeRunner {
                SessionView(
                    problems: state.problems,
                    runner: runner,
                    onGrade: { id, grade, isRepeat in
                        state.record(problemID: id, grade: grade, isRepeat: isRepeat)
                    },
                    onFinish: { state.finishSession() }
                )
            } else if state.isLoading {
                ProgressView().tint(Theme.accent)
            } else if state.loadFailed {
                retry
            } else {
                HomeView(
                    problemCount: state.problems.count,
                    totalReviews: state.totalReviews,
                    streak: state.activityStreak,
                    cells: state.heatmapCells,
                    entries: state.homeEntries,
                    sessionLength: state.sessionLength,
                    activityStatus: state.activityStatus,
                    onStart: { state.startSession(scope: $0) },
                    onChangeSessionLength: { state.updateSessionLength($0) }
                )
            }
        }
        .task {
            await state.loadContent()
            await state.loadActivity()
        }
        // Content is fetched once per launch; the calendar is fetched
        // again on every return to the foreground, because it is the only
        // thing on this screen that changes while the app is closed.
        .onChange(of: scenePhase) { _, phase in
            guard phase == .active else { return }
            Task { await state.loadActivity() }
        }
    }

    private var retry: some View {
        VStack(spacing: 14) {
            Text("内容下载失败")
                .font(Theme.titleFont)
                .foregroundColor(Theme.primaryText)
            Text("检查网络后重试。")
                .font(Theme.bodyFont)
                .foregroundColor(Theme.secondaryText)
            Button("重试") {
                Task { await state.loadContent() }
            }
            .font(Theme.bodyFont)
            .foregroundColor(Theme.accent)
        }
    }
}

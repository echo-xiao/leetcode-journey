import SwiftData
import SwiftUI

@main
struct LCReviewApp: App {

    private let container: ModelContainer
    @StateObject private var state: AppState

    init() {
        let container = try! ModelContainer(
            for: CardState.self, ReviewLog.self, AppSettings.self
        )
        self.container = container
        _state = StateObject(
            wrappedValue: AppState(
                store: ContentStore(
                    transport: HTTPContentTransport(),
                    cacheURL: ContentStore.defaultCacheURL()
                ),
                context: ModelContext(container)
            )
        )
    }

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(state)
        }
        .modelContainer(container)
    }
}

struct RootView: View {
    @EnvironmentObject private var state: AppState

    var body: some View {
        Group {
            if let runner = state.activeRunner {
                SessionView(
                    problems: state.problems,
                    runner: runner,
                    onGrade: { id, track, grade, isRepeat in
                        state.record(
                            problemID: id, track: track, grade: grade, isRepeat: isRepeat
                        )
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
                    streak: state.streak,
                    cells: state.heatmapCells,
                    entries: state.homeEntries,
                    onStart: { state.startSession(scope: $0) }
                )
            }
        }
        .task { await state.loadContent() }
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

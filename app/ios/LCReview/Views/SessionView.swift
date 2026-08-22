import SwiftUI

/// One session: swipe sideways to change problems, tap to open the next layer.
struct SessionView: View {
    let problems: [Problem]
    /// Observed, not owned: the runner outlives this view inside AppState, and
    /// a @StateObject here would silently create a second one.
    @ObservedObject var runner: SessionRunner
    /// (problemID, track, grade, isRepeat)
    let onGrade: (String, Track, Grade, Bool) -> Void
    let onFinish: () -> Void

    private var currentProblem: Problem? {
        guard let step = runner.current else { return nil }
        return problems.first { $0.id == step.problemID }
    }

    var body: some View {
        VStack(spacing: 0) {
            header
            if let problem = currentProblem {
                ChainCardView(problem: problem, revealed: runner.revealed)
                    .contentShape(Rectangle())
                    .onTapGesture { runner.reveal() }
                    .simultaneousGesture(swipe)
                    .id(runner.index)
                    .transition(.opacity)
            } else {
                finished
            }
            if runner.pendingGrade() != nil {
                GradeBar(onGrade: grade)
                    .transition(.move(edge: .bottom))
            }
        }
        .background(Theme.pageBackground)
        .animation(.easeInOut(duration: 0.18), value: runner.revealed)
        .animation(.easeInOut(duration: 0.18), value: runner.index)
    }

    private var header: some View {
        HStack {
            // A repeat card is extra work appended past the advertised
            // length, not the Nth of N — `progress.done` is deliberately
            // capped at `total`, so the plain fraction would read the same
            // as the genuinely last card. Naming it "加练" instead keeps the
            // header truthful about which state this is.
            //
            // The remaining case is capped at total: once the last regular
            // card is graded, `done` already equals `total`, and `done + 1`
            // would read as "4 / 3" — a real bug caught by looking at the
            // actual screenshot, not implied by the brief's literal formula.
            if runner.current?.askOnly != nil {
                Text("加练一题")
                    .font(Theme.tagFont)
                    .foregroundColor(Theme.secondaryText)
            } else {
                Text("第 \(min(runner.progress.done + 1, runner.progress.total)) / \(runner.progress.total) 题")
                    .font(Theme.tagFont)
                    .foregroundColor(Theme.secondaryText)
            }
            Spacer()
            Button("结束") { onFinish() }
                .font(Theme.tagFont)
                .foregroundColor(Theme.secondaryText)
        }
        .padding(.horizontal, 20)
        .padding(.top, 8)
    }

    private var finished: some View {
        VStack(spacing: 16) {
            Spacer()
            Text("这一节做完了")
                .font(Theme.titleFont)
                .foregroundColor(Theme.primaryText)
            Button("回首页") { onFinish() }
                .font(Theme.bodyFont)
                .foregroundColor(Theme.accent)
            Spacer()
        }
    }

    private var swipe: some Gesture {
        DragGesture(minimumDistance: 40)
            .onEnded { value in
                guard abs(value.translation.width) > abs(value.translation.height) else { return }
                if value.translation.width < 0 {
                    runner.advance()
                } else {
                    // A look back, not a redo: the card reopens as far as it
                    // was left and nothing already answered is asked again.
                    runner.goBack()
                }
            }
    }

    private func grade(_ grade: Grade) {
        guard let step = runner.current, let track = runner.pendingGrade() else { return }
        onGrade(step.problemID, track, grade, step.askOnly != nil)
        runner.record(grade: grade)
        // A repeat asks one layer and is done; move on rather than leaving a
        // dead card on screen.
        if step.askOnly != nil {
            runner.advance()
        }
    }
}

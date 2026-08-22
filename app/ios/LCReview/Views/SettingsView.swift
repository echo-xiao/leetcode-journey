import SwiftUI

/// The one setting the app has: session length.
///
/// The design doc is explicit that there is exactly one knob here and it
/// applies everywhere — no per-technique overrides. A segmented control over
/// a small fixed set of values keeps that promise visible: there is nowhere
/// to type an arbitrary number, and no illusion of finer control than the
/// app actually offers.
struct SettingsView: View {
    let sessionLength: Int
    let onChange: (Int) -> Void
    let onDone: () -> Void

    private static let options = [5, 10, 15, 20]

    var body: some View {
        VStack(alignment: .leading, spacing: Theme.sectionSpacing) {
            Text("设置")
                .font(Theme.titleFont)
                .foregroundColor(Theme.primaryText)

            VStack(alignment: .leading, spacing: 10) {
                Text("每节题数")
                    .font(Theme.bodyFont)
                    .foregroundColor(Theme.primaryText)
                Picker("每节题数", selection: Binding(
                    get: { sessionLength },
                    set: { onChange($0) }
                )) {
                    ForEach(Self.options, id: \.self) { value in
                        Text("\(value)").tag(value)
                    }
                }
                .pickerStyle(.segmented)
                Text("下一节生效，进行中的这一节不受影响。")
                    .font(Theme.metaFont)
                    .foregroundColor(Theme.secondaryText)
            }

            Spacer()
        }
        .padding(Theme.cardPadding)
        .background(Theme.pageBackground)
        .presentationDetents([.fraction(0.35)])
        .overlay(alignment: .topTrailing) {
            Button("完成", action: onDone)
                .font(Theme.bodyFont)
                .foregroundColor(Theme.accent)
                .padding(Theme.cardPadding)
        }
    }
}

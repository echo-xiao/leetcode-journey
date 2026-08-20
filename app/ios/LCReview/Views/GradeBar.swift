import SwiftUI

/// The three buttons, shown before the answer appears.
///
/// They separate by weight as much as by colour so the order reads at a
/// glance: 不会 is a filled near-black block, 勉强 is outlined, 会 is filled
/// green.
struct GradeBar: View {
    let onGrade: (Grade) -> Void

    var body: some View {
        HStack(spacing: 12) {
            button("不会", grade: .again, style: .solidDark)
            button("勉强", grade: .hard, style: .outlined)
            button("会", grade: .good, style: .solidAccent)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 14)
        .background(.regularMaterial)
    }

    private enum ButtonStyleKind { case solidDark, outlined, solidAccent }

    @ViewBuilder
    private func button(_ label: String, grade: Grade, style: ButtonStyleKind) -> some View {
        Button {
            onGrade(grade)
        } label: {
            Text(label)
                .font(.system(size: 17, weight: .medium))
                .frame(maxWidth: .infinity)
                .padding(.vertical, 14)
                .foregroundColor(foreground(style))
                .background(background(style))
                .overlay(
                    RoundedRectangle(cornerRadius: 12, style: .continuous)
                        .stroke(
                            style == .outlined ? Theme.secondaryText.opacity(0.5) : .clear,
                            lineWidth: 1
                        )
                )
                .clipShape(RoundedRectangle(cornerRadius: 12, style: .continuous))
        }
        .buttonStyle(.plain)
    }

    private func foreground(_ style: ButtonStyleKind) -> Color {
        switch style {
        case .solidDark, .solidAccent: return Color(uiColor: .systemBackground)
        case .outlined: return Theme.primaryText
        }
    }

    private func background(_ style: ButtonStyleKind) -> Color {
        switch style {
        case .solidDark: return Theme.primaryText
        case .outlined: return .clear
        case .solidAccent: return Theme.accent
        }
    }
}

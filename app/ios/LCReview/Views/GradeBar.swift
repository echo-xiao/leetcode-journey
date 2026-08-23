import SwiftUI

/// The three buttons, pinned below the card for the whole problem.
///
/// Deliberately short: it is on screen the entire time now rather than
/// appearing at two gates, so every point it takes is a point the card
/// does not get. The weight difference stays -- 不会 a filled near-black
/// block, 勉强 outlined, 会 filled green -- because that, not size, is what
/// makes the order readable at a glance.
struct GradeBar: View {
    let onGrade: (Grade) -> Void

    var body: some View {
        HStack(spacing: 12) {
            button("不会", grade: .again, style: .solidDark)
            button("勉强", grade: .hard, style: .outlined)
            button("会", grade: .good, style: .solidAccent)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 8)
        .background(.regularMaterial)
    }

    private enum ButtonStyleKind { case solidDark, outlined, solidAccent }

    @ViewBuilder
    private func button(_ label: String, grade: Grade, style: ButtonStyleKind) -> some View {
        Button {
            onGrade(grade)
        } label: {
            Text(label)
                .font(.system(size: 15, weight: .medium))
                .frame(maxWidth: .infinity)
                .padding(.vertical, 10)
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

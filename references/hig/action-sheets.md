---
topic: action-sheets
tier: 3
platforms: [ios, ipados, macos, tvos, watchos]
category: components/presentation
triggers:
  - "action sheet"
  - "bottom action"
  - "destructive action"
  - "confirmationDialog"
  - "UIAlertController.Style.actionSheet"
related:
  - alerts
  - sheets
  - modality
---

# Action sheets

An action sheet is a modal view of choices for an action people initiate. SwiftUI: `confirmationDialog(_:isPresented:titleVisibility:actions:)`, all platforms. UIKit: `UIAlertController.Style.actionSheet`, iOS, iPadOS and tvOS.

## Best practices

- **Use an action sheet, not an alert, for choices related to an intentional action.** Alerts can confirm or cancel a destructive action but offer no additional related choices, and are usually unexpected.
- **Use action sheets sparingly.**
- **Aim for one-line titles.**
- **Provide a message only if necessary**; in general, title plus context suffices.
- **If necessary, provide a Cancel button to reject an action that might destroy data**, at the bottom (upper-left in watchOS). SwiftUI confirmation dialogs include one by default.
- **Make destructive choices visually prominent**: destructive style (`ButtonRole.destructive`, `UIAlertAction.Style.destructive`), placed at the top.

## Platform considerations

No additional considerations for macOS or tvOS. Not supported in visionOS.

### iOS, iPadOS

- **Use an action sheet, not a menu, for choices related to an action**; menus appear only when people reveal them.
- **Avoid letting an action sheet scroll.**

### watchOS

System style: title, optional message, Cancel and one or more other buttons; appearance varies by device. Button styles: Default (no special meaning), Destructive (destroys data or acts destructively), Cancel (dismisses without acting).

**Avoid more than four buttons, including Cancel.** Cancel is required in watchOS, so aim for at most three others.

Source: [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets), captured 2026-09-12.

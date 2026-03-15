---
topic: action-sheets
tier: 3
platforms: [ios, ipados, macos, tvos]
category: components/presentation
triggers:
  - "action sheet"
  - "bottom action"
  - "destructive action"
  - "UIActionSheet"
related:
  - alerts
  - sheets
  - modality
---
# Action Sheets

> An action sheet is a modal view that presents choices related to an action people deliberately initiated.

**Platforms:** iOS, iPadOS, macOS, tvOS, watchOS *(not visionOS)*

SwiftUI: use `confirmationDialog`. UIKit: `actionSheet` style on iOS/iPadOS/tvOS.

**Action sheet vs. alert:** Use action sheets for choices following an intentional action. Use alerts for unexpected problems or critical warnings (see alerts).

## Best Practices

- **Use sparingly** — they interrupt flow; overuse trains people to ignore them.
- **Short, single-line titles** — long titles are hard to read quickly and may be truncated.
- **Omit message text unless necessary** — title + context usually suffices.
- **Cancel button** if the action might destroy data — placed at the bottom (iOS/iPadOS) or upper-left (watchOS). SwiftUI confirmation dialogs include Cancel by default.
- **Destructive buttons:** use the destructive visual style and place at the **top** of the sheet where they're most noticeable.

## Platform Considerations

### iOS, iPadOS

- **Action sheet for post-action choices; menu for deliberately revealed choices.** People associate action sheets with appearing after they do something, and menus with revealing on demand.
- **Don't let it scroll** — more buttons = more effort + a higher risk of accidentally tapping.

### watchOS

System action sheet structure: title + optional message + Cancel + additional buttons.

Button styles:
| Style | Meaning |
|---|---|
| Default | No special meaning |
| Destructive | Destroys data or takes destructive app action |
| Cancel | Dismisses without taking action |

**Max 4 buttons total (including Cancel)** — aim for ≤3 additional choices beyond Cancel.

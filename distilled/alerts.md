---
topic: alerts
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/presentation
triggers:
  - "alert"
  - "modal alert"
  - "dialog"
  - "warning"
  - "confirmation"
  - "UIAlertController"
related:
  - action-sheets
  - modality
  - writing
---
# Alerts

> An alert gives people critical information they need right away — problems, data-loss warnings, confirmations of important actions.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Use sparingly** — alerts interrupt current tasks; overuse dilutes attention.
- **Not for information-only** — if it's not actionable, find a non-interrupting way to present it (e.g., Mail shows a server-unavailable indicator people can tap to learn more).
- **Not for common, undoable destructive actions** — don't alert on every email/file delete. Reserve alerts for uncommon, non-undoable destructive actions people might have triggered accidentally.
- **No alerts at app startup** — show cached/placeholder data and a nonintrusive label instead if a problem is detected.

## Content

All platforms: title + optional informative text + up to 3 buttons.
- iOS/iPadOS/macOS/visionOS: optional text field.
- macOS/visionOS: optional icon and accessory view.
- macOS: optional suppression checkbox and Help button.

**Title:**
- Clearly and succinctly describes what happened, in what context, and why.
- Complete sentence → sentence-style capitalization + ending punctuation. Sentence fragment → title-style capitalization, no punctuation.
- No useless titles like "Error" or "Error 329347 occurred". No titles longer than 2 lines.

**Body text:** only when it adds value. Complete sentences, sentence-style capitalization, appropriate punctuation. Keep short.

**Don't explain buttons in the body copy** — clear titles make explanation redundant. In the rare case guidance is needed, say "choose" (device-neutral) and refer to the button title exactly, without quotes.

**Text field:** only if input is needed to resolve the situation (e.g., password entry).

## Buttons

- **1–2 word titles** using verbs/verb phrases tied to the alert content: "View All", "Reply", "Ignore", "Erase", "Convert", "Delete".
- **"OK"** is acceptable only in purely informational alerts.
- **"Cancel"** always cancels; place on leading side of a row or at the bottom of a stack.
- **Default button:** trailing side of row or top of stack. Never make Cancel the default.
- **Use descriptive button titles** over "OK" for consequential alerts — "OK" is ambiguous; "Delete" or "Erase" makes the consequence clear.
- **Destructive style:** applied to buttons performing accidental-destructive actions only. If the person deliberately chose the destructive action (e.g., Empty Trash), the button performing their intent can be the default without the destructive style.
- **Always include Cancel** when a destructive action button is present. If a single-button alert must have a default, use "Done" not "Cancel".

**Quick-cancel methods:**
| Method | Platform |
|---|---|
| Home Screen exit | iOS, iPadOS |
| Escape or Command-Period | iOS, iPadOS, macOS, visionOS |
| Menu button on remote | tvOS |

## Platform Considerations

### iOS, iPadOS

- Use **action sheets for choices following intentional actions**, not alerts (see action-sheets).
- Avoid scrolling alerts — keep titles short and message text brief.

### macOS

- App icon displayed automatically; can be replaced with alternative icon/symbol.
- Optional: repeating-alert suppression, custom accessory view, Help button.
- **Caution symbol (`exclamationmark.triangle`) sparingly** — only when extra attention is genuinely needed (e.g., unexpected data loss risk). Not for deliberate tasks like Save or Empty Trash.

### visionOS

- Shared Space: alert floats in front of the app window, slightly forward on the z-axis. If the window moves, the alert stays anchored to it.
- Full Space: alert is centered in the wearer's field of view.
- Accessory view: max height 154pt, corner radius 16pt.

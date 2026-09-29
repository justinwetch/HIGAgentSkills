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
  - sheets
  - modality
---

# Alerts

An alert is a modal view, differing by platform, that gives people critical information they need right away.

## Best practices

- **Use alerts sparingly**; offer only essential information and useful actions.
- **Avoid purely informational alerts.** Prefer conveying information in context.
- **Avoid alerts for common, undoable actions, even destructive ones.** Uncommon destructive actions people can't undo warrant one.
- **Avoid alerts at app launch.** Make important information easily discoverable; for startup problems, consider cached or placeholder data with a nonintrusive label.

## Content

All platforms: title, optional informative text, up to three buttons. Text field: iOS, iPadOS, macOS, visionOS. Icon and accessory view: macOS, visionOS. Suppression checkbox and Help button: macOS.

- **Be direct, with a neutral, approachable tone**, not oblique, accusatory or masking severity.
- **Titles: clear and succinct**, describing as much as possible what happened, in what context, and why. Avoid uninformative titles ("Error") and wrapping past two lines. Sentences get sentence-style capitalization and ending punctuation; fragments get title-style and none.
- **Include informative text only if it adds value**: as short as possible, complete sentences, sentence-style, punctuated.
- **Avoid explaining buttons.** In rare cases needing guidance, say *choose* and use the exact title without quotes.
- **If supported, include a text field only if you need people's input to resolve the situation.**

## Buttons

- **Titles: succinct and logical.** Aim for one or two words describing the result; prefer verbs tied to the alert text. Avoid OK as the default title unless the alert is purely informational, where you can use OK for acceptance (not Yes/No); otherwise use a specific title ("Delete"). Always title a button that cancels the alert's action "Cancel". Title-style, no ending punctuation.
- **Place buttons where people expect.** In general, the most likely choice goes trailing in a row or top of a stack; always place the default button there. Cancel is typically leading or bottom.
- **Destructive-style a button whose destructive action people didn't deliberately choose.** Don't destructive-style a deliberately chosen action (Empty Trash); Return-to-confirm convenience wins.
- **Include Cancel if there's a destructive action.** Don't make Cancel the default; to make people read rather than press Return, avoid any default. A single default-only button is Done, not Cancel.
- **Provide alternative ways to cancel when it makes sense**, for example:

|Action|Platforms|
|---|---|
|Exit to the Home Screen|iOS, iPadOS|
|Esc or Command-Period on an attached keyboard|iOS, iPadOS, macOS, visionOS|
|Menu on the remote|tvOS|

## Platform considerations

No additional considerations for tvOS or watchOS.

### iOS, iPadOS

- **Use an action sheet, not an alert, for choices related to an intentional action.**
- **When possible, avoid scrolling alerts** (large text can cause them): keep titles short; add a brief message only when necessary.

### macOS

The system automatically shows your app icon; you can supply another icon or symbol. Append a custom view (`accessoryView`) only if necessary.

**Use a caution symbol sparingly.** Use `exclamationmark.triangle` only when extra attention is really needed, such as possible unexpected data loss. Don't use it for tasks whose only purpose is overwriting or removing data (save, empty trash).

### visionOS

Shared Space: the alert appears slightly in front of the app's window on the z-axis and stays anchored when the window moves. Full Space: centered in the field of view. Accessory views: maximum 154 pt high, 16-pt corner radius.

## Resources

Developer: `alert(_:isPresented:actions:)` (SwiftUI), `UIAlertController`, `NSAlert`.

Source: [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), captured 2026-09-12.

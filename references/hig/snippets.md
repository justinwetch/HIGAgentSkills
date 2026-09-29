---
topic: snippets
tier: 3
platforms: [ios, ipados, macos]
category: components/system
triggers:
  - "snippet"
  - "snippets"
  - "App Intents snippet"
  - "Siri snippet"
  - "Shortcuts result"
  - "confirmation snippet"
  - "result snippet"
  - "interactive snippet"
related:
  - app-shortcuts
  - live-activities
  - siri
---
# Snippets

When someone performs a task with Siri, Spotlight, or Shortcuts, a snippet is a compact view that shows a result or asks for confirmation. Include one with an [app intent](https://developer.apple.com/documentation/appintents) when a task needs a custom view, such as checking weather or updating progress toward a daily goal.

## Types and anatomy

- **Confirmation:** lets people confirm or cancel an action and may offer options affecting its result; use this optional step when needed.
- **Result:** provides information, possibly after confirmation, without requiring further action. An app intent that displays a snippet always shows a result.

A snippet contains:

- **Dialogue:** app-intent text Siri speaks; the system includes it by default above the custom view.
- **Custom view:** visual information, with optional buttons to modify content, get more information, or take another action. Its maximum height is **400 pt**, accounting for preferred text size.
- **System buttons:** below the custom view, confirmation has secondary **Cancel** and a customizable primary action; result has one **Done** button to dismiss. The illustrated confirmation layout places Cancel left and the primary action right.

## Best practices

- **Ensure legibility.** Provide sufficient contrast against the system background in light and dark appearances and consistent content margins.
- **Keep content concise.** Lightweight interactions should remain short and legible; account for preferred text size. For more result detail, deep-link into the app instead of overloading the view.
- **Label the primary confirmation action descriptively.** Choose a system-provided [`ConfirmationActionName`](https://developer.apple.com/documentation/appintents/confirmationactionname) or custom label; **Order** communicates a coffee order better than **OK** or **Proceed**. If omitted, the default is **Continue**.
- **Communicate purpose visually.** Don’t rely on dialogue text to explain the snippet. Dialogue is essential when someone isn’t looking at the screen, but visually prefer the custom view alone: repeating Calendar event title, date, time, and participants in both dialogue and view is heavy; keep those details in the custom view.

## Platform considerations

There are no additional considerations for iOS, iPadOS, or macOS. Snippets aren’t supported in tvOS, visionOS, or watchOS.

## Resources and provenance

- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets)
- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2025/281)

Source: [Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets) (captured 2026-09-12).

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

> A snippet shows the result of a Siri/App Shortcut task or asks for confirmation.

**Platforms:** iOS, iPadOS, macOS. Not supported in tvOS, visionOS, or watchOS.

Snippets are compact views that appear after an action through Siri, Spotlight, or the Shortcuts app. Present snippets through App Intents for task-specific needs.

## Types

| Type | Purpose | Buttons |
|---|---|---|
| Confirmation | Lets people confirm/cancel an action; can include options that affect result. | Secondary Cancel + primary customizable action |
| Result | Provides information, possibly after confirmation; requires no further action. | Done |

An app intent that displays a snippet always shows a result; confirmation is optional.

## Anatomy

- **Dialogue**: app intent dialogue Siri speaks. System includes dialogue text by default and places it above the custom view.
- **Custom view**: visually communicates snippet information; can include buttons for modifying content, getting more information, or taking another action.
- **System buttons**: confirmation snippets include Cancel and a primary button; result snippets include Done.

Custom view maximum height: **400 pt**.

## Best Practices

- **Ensure legibility.** Maintain sufficient contrast between custom content and system background in light/dark appearances. Keep consistent margins.
- **Keep content concise.** Snippets support lightweight, quick interactions. Keep text short and legible. Respect Dynamic Type; fonts draw at different sizes.
- **Do not exceed the 400 pt custom-view height.**
- **For detailed result content, deep-link into the app** instead of adding detail to the custom view.
- **Use a descriptive confirmation primary label.** Choose an appropriate `ConfirmationActionName` or custom label. Example: "Order" is clearer than "OK" or "Proceed". Default is "Continue".
- **Communicate purpose visually.** Do not rely on displaying dialogue text to communicate snippet purpose. Spoken dialogue is essential when someone is not looking at the screen, but visual snippets should use custom view content instead of repeating dialogue.

## Developer Reference

- App Intents
- Displaying static and interactive snippets
- `ConfirmationActionName`


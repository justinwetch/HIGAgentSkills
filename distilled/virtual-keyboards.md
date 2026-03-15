---
topic: virtual-keyboards
tier: 3
platforms: [ios, ipados, tvos, visionos]
category: components/controls
triggers:
  - "virtual keyboard"
  - "on-screen keyboard"
  - "software keyboard"
  - "keyboard extension"
related:
  - keyboards
  - text-fields
  - entering-data
---
# Virtual Keyboards

> On devices without physical keyboards, the system provides virtual keyboards optimized for the current task.

**Platforms:** iOS, iPadOS, tvOS, visionOS, watchOS *(not macOS)*

Virtual keyboards don't support keyboard shortcuts. Can be replaced with a custom input view (in-app) or a custom keyboard app extension (systemwide, iOS/iPadOS/tvOS only).

## Best Practices

- **Match keyboard type to the content** — e.g., numeric keyboard for numbers, email keyboard (includes @ and period) for email addresses. Specifying semantic meaning lets the system auto-select and refine suggestions.
- **Customize the Return key type if it helps** — e.g., use "Search" return key type instead of the default when the field initiates a search.

## Custom Input Views

Replaces the system keyboard only within your app (e.g., Numbers uses a custom numeric input view in spreadsheets).

- **Must be contextually appropriate** — people should clearly understand why the system keyboard isn't available.
- **Play the standard keyboard sound** — people expect the click sound. They can disable it in Settings > Sounds for all keyboards.

## Custom Keyboards (App Extension)

Available in iOS, iPadOS, tvOS. Replaces the system keyboard in any app, except secure text fields (passwords) and phone number fields.

- **Easy Globe-key-equivalent switching** — the Globe key on the standard keyboard switches keyboards; your keyboard needs an equally intuitive switch mechanism.
- **Don't duplicate system keys** — the Emoji/Globe and Dictation keys appear automatically below custom keyboards; don't repeat them.
- **Provide a tutorial in your app** — not inside the keyboard itself. Explain: how to select the keyboard in Settings, how to activate it, how to use it, how to switch back.

## Platform Considerations

### iOS, iPadOS
- **Use the keyboard layout guide** — keeps important UI visible while the keyboard is onscreen.
- **Input accessory view (controls above keyboard)** — ensure controls are relevant to the current task. Apply Liquid Glass if other views in your app use it, or if the view looks inconsistent above the keyboard. Standard toolbars adopt Liquid Glass automatically.

### tvOS
- Siri Remote: linear virtual keyboard in text fields.
- Other devices (e.g., game controllers): grid keyboard layout.
- Digit entry view → digit-specific keyboard. See digit-entry-views.

### visionOS
- System keyboard appears in a separate moveable window. No need to account for keyboard position in your layouts.

### watchOS
- If the screen is large enough, a keyboard appears in text fields; otherwise, dictation or Scribble is offered.
- Can't change keyboard type; can set content type (system uses it for suggestions).
- People can use a paired iPhone to enter text on Apple Watch.

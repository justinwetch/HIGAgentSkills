---
topic: virtual-keyboards
tier: 3
platforms: [ios, ipados, tvos, visionos, watchos]
category: components/controls
triggers:
  - "virtual keyboard"
  - "on-screen keyboard"
  - "software keyboard"
  - "keyboard extension"
  - "UIKeyboardType"
  - "UITextContentType"
  - "keyboardType(_:)"
  - "textContentType(_:)"
  - "UIKeyboardLayoutGuide"
  - "inputAccessoryView"
  - "inputViewController"
  - "custom input view"
  - "submitLabel"
  - "submitLabel(_:)"
  - "UIReturnKeyType"
  - "playInputClick()"
related:
  - keyboards
  - text-fields
  - entering-data
---

# Virtual keyboards

On devices without physical keyboards, system virtual keyboards can offer task-specific keys but don't support keyboard shortcuts.

## Best practices

- **Match the keyboard to the content being edited**, like numbers and punctuation for numeric data (`keyboardType(_:)`, `UIKeyboardType`). With a semantic content type (`textContentType(_:)`, `UITextContentType`), the system can automatically match the keyboard and may refine corrections.
- Distinct iPhone keys: Email address (@, period), URL (period, slash, ".com"), Web search (period, Go), Twitter (@, hash), Decimal pad (period), Phone pad (plus/star/hash).
- Other types: Default, ASCII capable, ASCII capable number pad, Name phone pad, Number pad, Numbers and punctuation.
- **Consider customizing the Return key type if it clarifies text entry** (`submitLabel(_:)`, `UIReturnKeyType`), like a search Return key where your app initiates search. By default it follows the keyboard type.

## Custom input views

In some cases, you can create a custom *input view* that replaces the system keyboard in your app for custom data entry (`ToolbarItemPlacement`, `inputViewController`).

- **Make sure your custom input view makes sense in your app's context** and its benefits are clear, or people may wonder why they can't regain the system keyboard.
- **Play the standard keyboard sound while people type** (`playInputClick()`). People can turn off all keyboard sounds in Settings > Sounds.

## Custom keyboards

In iOS, iPadOS and tvOS, a custom keyboard app extension can replace the system keyboard in any app once people choose it in Settings, except in secure text and phone number fields. People can choose several and switch anytime. Custom keyboards make sense for unique systemwide functionality (e.g. novel input methods, unsupported languages); for in-app-only use, consider a custom input view instead.

- **Provide an obvious, easy way to switch keyboards**, as intuitive as the Globe key (which replaces the Emoji key when multiple keyboards are available).
- **Avoid duplicating system keyboard features.** On some devices, Emoji/Globe and Dictation keys automatically appear beneath even custom keyboards; you can't affect them, and repeating them is likely confusing.
- **Consider an in-app keyboard tutorial**, like how to choose, activate, use and switch away from your keyboard. Avoid help content within the keyboard itself.

## Platform considerations

Not supported in macOS.

### iOS, iPadOS

- **Use the keyboard layout guide (`UIKeyboardLayoutGuide`) to integrate the keyboard with your interface**, keeping important UI, like text fields and buttons, visible.
- **Place custom controls above the keyboard thoughtfully.** Make sure input accessory controls that augment the keyboard (`inputAccessoryView`, `ToolbarItemPlacement`) are relevant to the current task. If other views use Liquid Glass, or your view looks out of place above the keyboard, apply Liquid Glass to it; a standard toolbar adopts it automatically. Use the keyboard layout guide and standard padding so the system positions them as expected.

### tvOS

Selecting a text field with the Siri Remote shows a linear keyboard; other devices show a grid keyboard screen, and content layout adapts automatically. [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views) show a digit-specific keyboard.

### visionOS

The keyboard supports direct and indirect gestures in a separate, movable window; you don't need to account for its location in layouts.

### watchOS

A text field can show a keyboard if the screen is large enough; otherwise, people can use dictation or Scribble. You can't change the keyboard type, but you can set the content type (`textContentType(_:)`), which the system uses for help like suggestions. People can also type on a nearby paired iPhone.

Source: [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards), captured 2026-09-12.

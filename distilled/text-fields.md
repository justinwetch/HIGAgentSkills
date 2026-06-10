---
topic: text-fields
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "text field"
  - "text input"
  - "UITextField"
  - "NSTextField"
  - "form field"
related:
  - text-views
  - combo-boxes
  - virtual-keyboards
  - entering-data
---
# Text Fields

> A text field is a rectangular area for entering or editing small, specific pieces of text.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Use text fields for small amounts of input. For larger text input, use text-views.

## Best Practices

- **Placeholder text** — describes the field's purpose (e.g., "Email", "Password"). Since it disappears on typing, also consider a separate persistent label for important fields.
- **Secure text fields** for sensitive data (passwords) — always.
- **Match field size to anticipated text** — field width visually communicates expected input length.
- **Even spacing for multiple fields** — clearly associate each label with its field. Stack vertically when possible; use consistent widths within a form section.
- **Tab order** — flows logically between fields; system handles this automatically in most cases, rarely needs manual customization.
- **Validate at the right time:**
  - Email address → validate when focus moves to another field.
  - Username/password → validate before focus moves away.
- **Number formatters** for numeric fields — restricts to numeric input, configures decimal places, percentage, or currency display. Format varies by locale; don't hardcode.
- **Line breaks** — clip (default), wrap at character or word, or truncate (beginning, middle, end) as appropriate.
- **Expansion tooltip** for clipped/truncated text — hovering pointer reveals the full text.
- **Show the appropriate keyboard type** (iOS, iPadOS, tvOS, visionOS) — e.g., number pad, URL, email. See virtual-keyboards.
- **Minimize text entry on tvOS and watchOS** — long text entry is slow on those platforms; prefer buttons or other input methods.

## Platform Considerations

### iOS, iPadOS

- **Clear button** at the trailing end — tapping clears the field without repeated backspace.
- **Images and buttons** in text fields — leading end: indicates purpose; trailing end: offers extra features (e.g., Bookmarks).

### macOS

- **Combo box** — when pairing text input with a list of choices.

### watchOS

- **Show a text field only when necessary** — prefer lists of options over text entry.

---
topic: entering-data
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/input
triggers:
  - "data entry"
  - "form"
  - "input"
  - "fill in"
  - "autocomplete"
  - "autofill"
related:
  - text-fields
  - keyboards
  - pickers
---
# Entering Data

> Design data entry to be easy, accurate, and as automatic as possible.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Get data from the system automatically** — don't ask for info you can gather from settings, location, calendar, or other system sources (with permission). Never make people re-enter what you already know.
- **Be clear about what's needed** — use placeholder text to show format (e.g., "username@company.com") and introductory labels for context. Pre-fill fields with sensible defaults to reduce decision-making.
- **Use a secure text field for sensitive data** — displays filled circle symbols per character. In tvOS, use `isSecureDigitEntry` for digit fields. In visionOS, secure fields are automatically blurred for AirPlay viewers while remaining visible to the wearer.
- **Never prepopulate a password field** — always require fresh entry, biometrics, or keychain auth.
- **Offer choices instead of text entry when possible** — pickers, menus, or selection components are faster and less error-prone than typing.
- **Support drag-and-drop and paste** for data entry — reduces effort and feels integrated with the system.
- **Validate fields dynamically** — check values as people type and provide immediate feedback on errors. Use number formatters on numeric fields to prevent invalid input and auto-format values (decimal places, percentage, currency).
- **Require data before enabling progression** — if a Next or Continue button needs data, keep it disabled until required fields are filled.

## Platform Considerations

### macOS

Use **expansion tooltips** to show the full value of clipped/truncated text in fields that are too narrow to display the complete content. Works on iOS/iPadOS apps running on Mac via Mac Catalyst too.

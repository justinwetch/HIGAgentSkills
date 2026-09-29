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
  - "SecureField"
related:
  - text-fields
  - keyboards
  - pickers
---

# Entering data

Support all available input methods so people can choose.

## Best practices

- **Don't ask people to enter data you can get from the system**, such as from settings or, with permission, location or calendar.
- **Be clear about the data you need**, such as with a field prompt or label. You can prefill reasonable defaults.
- **Use a secure text-entry field for sensitive data** (`SecureField`); it obscures input, typically one small filled circle per character. tvOS digit entry views can also obscure numerals (`isSecureDigitEntry`). In visionOS, system-provided text fields show input only to the wearer; for example, secure fields automatically blur in AirPlay.
- **Never prepopulate a password field.** Always require entry or biometric or keychain authentication.
- **When possible, offer choices instead of text entry.** When it makes sense, consider a picker, menu or other selection component.
- **As much as possible, support drag and drop and paste.**
- **Dynamically validate field values**, giving feedback as soon as you detect a problem. For numeric data, consider a number formatter, which automatically accepts only numbers and can show values such as with set decimal places, as percentages or as currency.
- **When data entry is necessary, make sure people understand they must provide required data to proceed**, e.g., enable Next or Continue only afterward.

## Platform considerations

No additional considerations for iOS, iPadOS, tvOS, visionOS or watchOS.

### macOS

**Consider an expansion tooltip to show a field's full clipped or truncated text.** iOS and iPadOS apps on a Mac can use it too.

Source: [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data), captured 2026-09-12.

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

# Text fields

A text field is a rectangular area for entering or editing text.

## Best practices

- **Use a text field for small amounts of information** (a name, an email address); use a text view for more.
- **Show a hint of purpose.** Placeholder text (such as "Email") disappears on typing, so a separate label can also help.
- **Always use a secure text field (`SecureField`) for sensitive data** such as passwords.
- **To the extent possible, size fields to the anticipated text.**
- **Evenly space multiple fields;** stack vertically when possible, with consistent widths.
- **Ensure tabbing moves focus in a logical sequence;** the system attempts this automatically, so customization is rarely needed.
- **Validate fields when it makes sense,** such as flagging non-digits in a digits-only field. Email addresses are best validated when people switch fields; new user names and passwords need validation before they switch.
- **Use a number formatter for numeric data:** it accepts only numeric values and can display decimals, percentages or currency. Formatting can vary significantly by locale, so don't assume the presentation.
- **Adjust line breaks per field.** Default: clip overflow. Alternatives: wrap by character or word; truncate with an ellipsis at the beginning, middle or end.
- **Consider an expansion tooltip** for full clipped or truncated text on pointer hover.
- **In iOS, iPadOS, tvOS and visionOS, show the appropriate keyboard type** (such as numbers or URLs).
- **Minimize text entry in tvOS and watchOS;** consider alternatives such as buttons.

## Platform considerations

No additional considerations for tvOS or visionOS.

### iOS, iPadOS

- **Display a trailing Clear button** for erasing input without repeated Delete taps.
- **Use images and buttons for clarity and functionality:** custom images at either end, or system buttons such as Bookmarks. In general, the leading end indicates purpose; the trailing end, additional features.

### macOS

- **Consider a combo box to pair text input with a list of choices.**

### watchOS

- **Present a text field only when necessary;** whenever possible, prefer a list of options.

## Resources

Developer: `TextField` (SwiftUI), `UITextField`, `NSTextField`.

Source: [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields), captured 2026-09-12.

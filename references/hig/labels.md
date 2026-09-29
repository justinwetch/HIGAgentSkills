---
topic: labels
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "label"
  - "UILabel"
  - "Text"
  - "NSTextField"
  - "caption"
  - "body text"
  - "description text"
related:
  - typography
  - text-views
---

# Labels

A label is a static piece of text that people can read and often copy, but not edit. It appears in buttons, menu items, and views to explain context and actions: a button label generally names the action (Edit, Cancel, Send); a list label describes each item, often beside a symbol/image; a view label introduces a control or common action/task. SwiftUI [`Label`](https://developer.apple.com/documentation/swiftui/label) is a standard label with an icon and title; [`Text`](https://developer.apple.com/documentation/swiftui/text) displays one or more lines of read-only text. [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [menus](https://developer.apple.com/design/human-interface-guidelines/menus), and [lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) may add text guidance.

## Best practices

- **Use labels for small text people don’t need to edit.** Use a [text field](https://developer.apple.com/design/human-interface-guidelines/text-fields) for small editable text; use a [text view](https://developer.apple.com/design/human-interface-guidelines/text-views) for large text that may also be editable.
- **Prefer system fonts.** Labels support plain or styled text and Dynamic Type (where available) by default; custom styles/fonts must remain legible.
- **Use system-provided label colors to communicate relative importance.** Their appearance varies by level:

  | System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
  | --- | --- | --- | --- |
  | Label | Primary information | [`UIColor.label`](https://developer.apple.com/documentation/uikit/uicolor/label) | [`NSColor.labelColor`](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
  | Secondary label | Subheading or supplemental text | [`UIColor.secondaryLabel`](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) | [`NSColor.secondaryLabelColor`](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
  | Tertiary label | Text describing an unavailable item or behavior | [`UIColor.tertiaryLabel`](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) | [`NSColor.tertiaryLabelColor`](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
  | Quaternary label | Watermark text | [`UIColor.quaternaryLabel`](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) | [`NSColor.quaternaryLabelColor`](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |

- **Make useful text selectable.** If a label contains useful information—such as an error message, location, or IP address—consider letting people select and copy it.

## Platform considerations

### macOS

For uneditable text, use [`NSTextField.isEditable`](https://developer.apple.com/documentation/appkit/nstextfield/iseditable) (`Bool`) on [`NSTextField`](https://developer.apple.com/documentation/appkit/nstextfield).

### watchOS

Date/time text components display the current date, time, or both; configure formats, calendars, and time zones. A timer component displays a precise countdown or count-up with configurable count formats.

System date/timer components automatically fit the available space and update without app input. Consider them in complications; see [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications) and [`Text`](https://developer.apple.com/documentation/swiftui/text).

## Resources

- Related: [Color](https://developer.apple.com/design/human-interface-guidelines/color).
- Developer documentation: [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) — UIKit view displaying one or more lines of informational text.

Source: [Apple HIG — Labels](https://developer.apple.com/design/human-interface-guidelines/labels), captured 2026-09-12.

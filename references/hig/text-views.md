---
topic: text-views
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "text view"
  - "UITextView"
  - "NSTextView"
  - "multiline text"
  - "text editor"
related:
  - text-fields
  - labels
  - combo-boxes
---

# Text views

A text view displays multiline, styled text that can optionally be editable. It can be any height and scrolls when content extends outside its bounds. Content defaults to leading alignment and the system label color. On iOS, iPadOS, and visionOS, selecting an editable text view displays a keyboard.

## Best practices

- **Use a text view for long, editable, or specially formatted text.** It offers the most options for specialized display and text input; use a label for small read-only text and a text field for small editable text.
- **Keep text legible** across fonts, colors, and alignments; consider Dynamic Type when people change device text size, and test accessibility settings such as bold text. See [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) and [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).
- **Make useful text selectable.** Consider selection/copy for useful information such as an error message, serial number, or IP address.

## Platform considerations

- **iOS and iPadOS:** While editing, show a keyboard type suited to the text view’s content to streamline entry; see [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards).
- **tvOS:** Text views can display text, but because text input is minimal by design, use text fields for editable text.
- **macOS, visionOS, and watchOS:** No additional considerations.

## Resources

- Related: [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes).
- Developer documentation: [`Text`](https://developer.apple.com/documentation/swiftui/text) — SwiftUI (one or more lines of read-only text); [`UITextView`](https://developer.apple.com/documentation/uikit/uitextview) — UIKit (scrollable, multiline text region); [`NSTextView`](https://developer.apple.com/documentation/appkit/nstextview) — AppKit (draws text and handles interactions with it).

Source: [Apple HIG — Text views](https://developer.apple.com/design/human-interface-guidelines/text-views), captured 2026-09-12.

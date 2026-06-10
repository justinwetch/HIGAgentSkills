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

> A label is static text people can read and often copy, but not edit.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Appears in buttons (action name), list rows (item description), and views (context or instructions).

## Best Practices

- **Small non-editable text** — for small editable text, use a text field; for large text (editable or not), use a text view.
- **Prefer system fonts** — support Dynamic Type by default. If using custom fonts/styles, verify legibility.
- **Use system-provided label colors to indicate hierarchy:**

| Color level | Usage | iOS/iPadOS/tvOS/visionOS | macOS |
|---|---|---|---|
| Label | Primary info | `label` | `labelColor` |
| Secondary label | Subheadings, supplemental text | `secondaryLabel` | `secondaryLabelColor` |
| Tertiary label | Unavailable item/behavior descriptions | `tertiaryLabel` | `tertiaryLabelColor` |
| Quaternary label | Watermark text | `quaternaryLabel` | `quaternaryLabelColor` |

- **Make useful label text selectable where available** — error messages, locations, or IP addresses.

## Platform Considerations

### macOS

- For uneditable label text, use `NSTextField.isEditable`.

### watchOS

- **Date and time text components** — display current date, time, or both. Configurable for format, calendar, time zone. Auto-adjusts to available space; auto-updates without app input.
- **Countdown/count-up timer components** — displays a running timer, configurable format.
- Use these in complications. System manages layout and updates automatically.

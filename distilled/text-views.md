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
  - entering-data
---
# Text Views

> A text view displays multiline, styled text — optionally editable — and scrolls when content exceeds the view bounds.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Default: leading-aligned, system label color. Editable text views show the keyboard when tapped (iOS, iPadOS, visionOS).

## Best Practices

- **Use for long, editable, or specially formatted text.** For small non-editable text → label; for small editable text → text field.
- **Maintain legibility** — if using multiple fonts, colors, or alignments, keep content readable. Support Dynamic Type. Test with bold text and other accessibility settings.
- **Make useful text selectable** — error messages, serial numbers, IP addresses — allow copy/paste.

## Platform Considerations

### iOS, iPadOS

- **Show the appropriate keyboard type** for the editing context. See virtual-keyboards.

### tvOS

- Text views display text in tvOS but are read-only. tvOS uses text fields (not text views) for editable text, because text input is minimal by design.

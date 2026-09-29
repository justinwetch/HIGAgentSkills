---
topic: ornaments
tier: 3
platforms: [visionos]
category: patterns/visionos
triggers:
  - "ornament"
  - "window ornament"
  - "floating controls"
  - "spatial toolbar"
  - "ornament(visibility:attachmentAnchor:contentAlignment:ornament:)"
  - "Toolbars"
  - "visionOS TabView ornament"
related:
  - layout
  - toolbars
  - tab-bars
  - eyes
---

# Ornaments

An ornament (visionOS only) presents a window's related controls and information, like buttons, segmented controls and other views, on any edge without crowding or obscuring its contents. It floats parallel to and slightly in front of the window, moves with it, and doesn't scroll with content. System toolbars, tab bars and video playback controls are ornaments; custom ones can use `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`.

## Best practices

- **Consider ornaments for frequently needed controls or information** in a consistent location.
- **In general, keep ornaments visible**; hiding can make sense when people dive into content, like a video or photo.
- **With multiple ornaments, prioritize the window's visual balance**; when necessary, consider limiting their number (or move elements into the main window).
- **Aim to keep an ornament no wider than its window**; wider ones can interfere with a side tab bar or other vertical content.
- **Consider borderless buttons** on the default glass background; the system automatically applies the hover effect when people look at them.
- **Use system toolbars and tab bars (SwiftUI Toolbars, `TabView`) unless you need custom components**; they automatically appear as ornaments.

## Resources

Source: [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments), captured 2026-09-12.

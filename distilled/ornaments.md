---
topic: ornaments
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/visionos
triggers:
  - "ornament"
  - "window ornament"
  - "floating controls"
  - "spatial toolbar"
related:
  - designing-for-visionos
  - toolbars
  - windows
---
# Ornaments

> In visionOS, an ornament presents controls and information related to a window without crowding or obscuring window contents.

**Platforms:** visionOS only

Ornaments float in a plane parallel to and slightly in front of the window (z-axis). They move with the window; they don't scroll with window content. System toolbars and tab bars in visionOS are automatically implemented as ornaments.

## Best Practices

- **Use for frequently needed controls that need a consistent, predictable location** — e.g., Music's Now Playing controls always in the same place.
- **Keep ornaments visible by default** — hiding during immersive content interaction (video, photos) is acceptable, but generally people appreciate consistent access.
- **Multiple ornaments: prioritize visual balance** — ornaments elevate important actions but can distract from content. Limit the total number; if needed, remove an ornament and move its elements into the main window.
- **Width ≤ window width** — wider ornaments interfere with a tab bar or other vertical content on the window's side.
- **Borderless buttons** — ornament background is glass; buttons on the glass surface typically don't need a border. System applies hover effect automatically when people look at a borderless button.
- **Use system toolbars/tab bars instead of custom ornaments for those functions** — they auto-appear as ornaments; no manual setup needed.

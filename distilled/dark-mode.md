---
topic: dark-mode
tier: 1
platforms: [ios, ipados, macos, tvos]
category: foundations
triggers:
  - "dark mode"
  - "dark appearance"
  - "light mode"
  - "color scheme"
related:
  - color
  - materials
  - typography
---
# Dark Mode

> Dark Mode is a systemwide appearance using a dark color palette for comfortable low-light viewing.

**Platforms:** iOS, iPadOS, macOS, tvOS *(not visionOS or watchOS)*

## Best Practices

- Don't offer an app-specific appearance setting — it conflicts with the systemwide preference.
- Ensure the app looks good in both appearances. The Auto setting switches dynamically throughout the day, potentially while running.
- Test with Increase Contrast and Reduce Transparency (separately and together) in Dark Mode.
- Permanently dark appearance is acceptable only for immersive media apps where UI receding helps people focus.

## Dark Mode Colors

Dark palette uses dimmer backgrounds + brighter foregrounds — not a simple inversion.

- Use semantic colors (`labelColor`, `controlColor` on macOS; `separator` on iOS/iPadOS) — they adapt automatically.
- For custom colors: add a Color Set asset in Xcode with both bright and dim variants. Never hard-code color values.
- Minimum contrast ratio: 4.5:1 between foreground and background. For custom colors, target 7:1 (especially small text).
- Slightly darken white-background images to prevent glowing in Dark Mode context.

### Icons and Images

- Use SF Symbols — they automatically adapt to Dark Mode.
- Design separate light/dark icon variants when needed (e.g., full-moon icon needs outline on light, not on dark).
- Use asset catalogs to combine light/dark image variants into a single named image.

### Text

- Use system label colors (`primary`, `secondary`, `tertiary`, `quaternary`) — they adapt automatically.
- Use system views for text fields/text views — they handle vibrancy and background adaptation automatically.

## Platform Considerations

### iOS, iPadOS

Two dark background levels — **base** (dimmer, receding) and **elevated** (brighter, advancing) — to convey depth when dark UIs stack.

- Prefer system background colors — the system switches base/elevated automatically for popovers, sheets, multitasking, and multi-window contexts. Custom background colors break this system distinction.

### macOS

When user picks graphite accent + desktop picture, windows pick up color from the desktop via **desktop tinting**.

- Include subtle transparency in custom component backgrounds (where component has a visible background or bezel) to harmonize with desktop tinting.
- Only add transparency in neutral/non-colored states — colored states with transparency cause visual inconsistency as the desktop shifts.

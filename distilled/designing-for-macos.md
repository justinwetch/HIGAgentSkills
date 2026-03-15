---
topic: designing-for-macos
tier: 2
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: platforms
triggers:
  - "macOS"
  - "Mac"
  - "AppKit"
  - "Mac Catalyst"
  - "desktop"
related:
  - the-menu-bar
  - windows
  - toolbars
---
# Designing for macOS

> Mac users rely on power, spaciousness, and flexibility for deep productivity, media, and multi-app work.

**Platform:** macOS

## Device Characteristics

| | |
|---|---|
| **Display** | Large, high-resolution; can extend with additional displays including iPad via Sidecar |
| **Ergonomics** | Stationary, desk/table use; viewing distance ~1–3 ft |
| **Inputs** | Physical keyboard, pointing device (mouse/trackpad), game controllers, Siri |
| **Usage pattern** | Quick tasks to hours of deep focus; multiple apps open simultaneously; smooth active/inactive state transitions |

**Key system integrations:** Menu bar, file management, full-screen mode, Dock menus.

## Best Practices

- Leverage large display to show more content in fewer nested levels with less modality; maintain comfortable information density.
- Let people resize, hide, show, and move windows; support full-screen mode.
- Put all commands in the menu bar — comprehensive, accessible command structure is expected.
- Enable high-precision interactions (pixel-perfect selection, editing) via mouse/trackpad.
- Support keyboard shortcuts for all important actions; support keyboard-only workflows.
- Support personalization — customizable toolbars, window configurations, font and color preferences.

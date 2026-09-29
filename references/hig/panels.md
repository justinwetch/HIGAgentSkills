---
topic: panels
tier: 4
platforms: [macos]
category: components/macos
triggers:
  - "panel"
  - "NSPanel"
  - "hudWindow"
  - "floating window"
  - "inspector panel"
  - "heads-up display"
related:
  - windows
  - modality
---

# Panels

A panel (`NSPanel`) typically floats above other windows with supplementary controls or information for the active window or selection, and is in general less prominent than the main window. Panels are macOS-only; on other platforms, consider a modal view for such content.

## Best practices

- **Use a panel for quick access to important controls or information** about the current content.
- **Consider a panel (or, depending on layout, a [split view](https://developer.apple.com/design/human-interface-guidelines/split-views) pane) for an inspector**, which updates automatically to show the selected item's details. Use a regular window, not a panel, for an Info window, whose contents stay fixed.
- **Prefer simple adjustment controls**; consider sliders and steppers. As much as possible, avoid controls requiring typing text or selecting items to act upon.
- **Give it a title bar and a brief noun or noun-phrase title** describing its purpose, in title-style capitalization ("Inspector").
- When your app becomes active, bring all open panels to the front, whichever window was active when they opened; when it's inactive, hide them all.
- **Avoid listing panels in the Window menu's documents list**; show/hide commands there are fine.
- **In general, avoid making a panel's minimize button available.**
- **Refer to panels by title**: "Show Fonts" in menus, without "panel"; in help, generally the title, appending "window" when clearer ("Fonts window").

## HUD-style panels

A HUD (`NSWindow.StyleMask.hudWindow`) is a darker, translucent panel with the same function; HUDs work well in highly visual or immersive apps, like media editing or full-screen slide shows.

- **Prefer standard panels**; a HUD might not match the current appearance setting. In general, use a HUD only:
  - In a media-oriented app presenting movies, photos or slides
  - When a standard panel would obscure essential content
  - When you don't need controls; most system-provided controls, except the disclosure triangle, don't match a HUD
- **Keep one panel style across modes**: if you use a HUD in full screen, prefer keeping it outside full screen.
- **Use color sparingly**; often a little high-contrast color suffices to highlight important information.
- **Keep HUDs small**, and don't let one obscure or compete for attention with the content it adjusts.

Source: [Panels](https://developer.apple.com/design/human-interface-guidelines/panels), captured 2026-09-12.

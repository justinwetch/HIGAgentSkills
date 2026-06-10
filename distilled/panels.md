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

> In a macOS app, a panel floats above other windows, providing supplementary controls, options, or information related to the active window or current selection.

**Platforms:** macOS only

Less visually prominent than main windows. Can use a dark, translucent HUD style for immersive/media contexts. Non-macOS alternative: use a modal view for supplementary content (see modality).

## Best Practices

- **Quick access to controls/information related to the active content** — e.g., controls affecting the selected item in the active document.
- **Consider for inspector functionality** — an *inspector* auto-updates when the selection changes. An *Info window* (fixed content regardless of selection) uses a regular window, not a panel. A split view pane is also a viable inspector alternative.
- **Prefer simple adjustment controls** — sliders, steppers (direct manipulation). Avoid controls requiring typing or multi-step item selection.
- **Brief, noun-phrase title** — title-style capitalization. People need to identify and reposition the panel. Classic examples: "Fonts", "Colors", "Inspector."
- **Show/hide appropriately** — show all open panels when the app becomes active (regardless of which window was active when the panel opened). Hide all panels when the app is inactive.
- **Don't list panels in the Window menu's documents list** — show/hide commands in the Window menu are fine; panels aren't documents.
- **In general, avoid making panels minimizable** — panels normally appear only when needed and disappear with the app.
- **Refer to panels by title** in UI and docs — "Show Fonts" / "Show Colors" / "Show Inspector" (no word "panel"). In help docs, use the title alone ("Inspector") or append "window" for clarity ("Fonts window", "Colors window").

## HUD-Style Panels

Dark, translucent appearance. Ideal for media editing, full-screen slideshows (e.g., QuickTime Player inspector).

**Use a HUD only when:**
- Running a media-oriented app (movies, photos, slides)
- A standard panel would obscure essential content
- You don't need in-panel controls (most system controls don't match HUD appearance — disclosure triangles are acceptable)

**HUD rules:**
- **Prefer standard panels** — HUDs can be distracting if their presence isn't logical or if they don't match the current appearance setting.
- **Maintain one panel style across mode changes** — e.g., if you use a HUD in full-screen, keep the HUD when exiting full-screen.
- **Use color sparingly** — small amounts of high-contrast color are sufficient; too much color is distracting in the dark appearance.
- **Keep HUDs small** — unobtrusive by design; don't let them obscure the content they adjust or compete for attention.

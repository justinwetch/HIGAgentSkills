---
topic: dock-menus
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/macos
triggers:
  - "Dock menu"
  - "right-click Dock"
  - "Dock context menu"
  - "NSApplicationDockTile"
related:
  - menus
  - app-icons
---
# Dock Menus

> On Mac, a secondary click on an app's Dock icon reveals a Dock menu with system-provided and custom items.

**Platforms:** macOS only

System items vary by app state (open/closed). Example: Safari Dock menu shows current windows and "New Window."

iOS/iPadOS equivalent: home-screen-quick-actions (long press on Home Screen or Dock icon).

## Best Practices

- **Follow general menu labeling and organization rules** (see menus).
- **Make all Dock menu items available elsewhere** — not everyone uses the Dock menu. Mirror the same commands in the menu bar or main UI.
- **Prefer high-value, context-independent items** — useful when the app is backgrounded or has no open windows. Good candidates: open windows list, "New Message", "Get Mail." Dock menus can conveniently list all open windows for fast switching.

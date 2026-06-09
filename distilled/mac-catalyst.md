---
topic: mac-catalyst
tier: 3
platforms: [ipados, macos]
category: platforms
triggers:
  - "Mac Catalyst"
  - "Catalyst"
  - "iPad app on Mac"
  - "scaled idiom"
  - "Mac idiom"
related:
  - designing-for-macos
---
# Mac Catalyst

> Mac Catalyst lets you create a Mac app from your iPad app, giving it automatic macOS features and a more native Mac experience.

**Platforms:** iPadOS, macOS

## Good Candidates

iPad apps that support: drag and drop, keyboard navigation/shortcuts, multitasking (split view, slide over), and multiple windows translate especially well to Mac.

**Poor candidates**: apps that require gyroscope, accelerometer, rear camera, HealthKit, ARKit, or whose core purpose is marking, handwriting, or navigation.

**macOS features you get automatically**: pointer interactions, keyboard focus/navigation, window management, toolbars, rich text (copy/paste, contextual menus), file management, menu bar menus, system Settings app.

**System UI elements that become more Mac-like**: split view, file browser, activity view, form sheet, contextual actions, color picker.

## Idioms

| Idiom | Behavior | When to use |
|---|---|---|
| iPad (default) | Scales iPad layout to 77% in macOS. Text scales from 17 pt → 13 pt | When your app feels right at home without extra layout work |
| Mac | Text and artwork render at 100%. Even more Mac-like controls. Better performance for graphics-heavy apps | When your app shows lots of text, detailed artwork, or animations — requires additional layout work |

**Mac idiom caveats:**
- Thoroughly audit and update layout — unscaled views report different metrics.
- Adjust font sizes — full size often appears too large. Use text styles, not fixed sizes.
- Keep assets looking great at 100% — some images may appear too detailed without adjustment.
- Not all iPadOS appearance customizations are available in macOS.

## Navigation

| iPad pattern | Mac equivalent |
|---|---|
| Tab bar | Split view with sidebar, or segmented control |
| Page control (dots) | Next/Previous buttons |

- **Tab bar → sidebar**: best option. Sidebar shows all top-level items + child items. Consistent layout across iPad + Mac.
- **Tab bar → segmented control**: works for flat navigation hierarchies.
- **Always list top-level tab bar items in the Mac View menu**, regardless of navigation control used.
- Offer **Next / Previous buttons** for pagination (supports mouse, trackpad, and keyboard users).

## Input Translation

| iPadOS gesture | Mouse | Trackpad |
|---|---|---|
| Tap | Left or right click | Click |
| Touch and hold | Click and hold | Click and hold |
| Pan | Left click and drag | Click and drag |
| Pinch | — | Pinch |
| Rotate | — | Rotate |

> Note: Pinch and rotate send both touches to the view under the pointer, not the views under each touch.

## App Icons

Create a macOS version of your app icon — lifelike rendering style expected by macOS users.

## Layout

- Use regular-width and regular-height size classes. Reflow to side-by-side layout as the window resizes.
- Divide single columns into multiple columns to take advantage of wider screens.
- Present inspector UI beside main content (not in a popover).
- Move controls from main UI → Mac toolbar. List toolbar commands in the menu bar.
- **Top-down layout** — most important actions/content near the top.
- Relocate buttons from side and bottom edges (ergonomic on iPad; not necessary on Mac). Move to toolbar instead.

## Menus

- Mac users expect all commands in the persistent menu bar.
- Context menus in iPadOS are automatically converted to macOS context menus.
- Look for additional context menu opportunities — Mac users expect every object to have one. (macOS calls them *contextual menus*.)
- Use `UIKeyCommand` for keyboard shortcut support.
- Use `UIMenuBuilder` + `UICommand` to add/remove custom menu items.

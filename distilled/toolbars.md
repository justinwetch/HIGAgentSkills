---
topic: toolbars
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/navigation
triggers:
  - "toolbar"
  - "UIToolbar"
  - "NSToolbar"
  - "toolbar item"
  - "toolbar button"
  - "navigation bar"
related:
  - sidebars
  - tab-bars
  - layout
  - buttons
  - search-fields
  - icons
---
# Toolbars

> A toolbar provides convenient access to frequently used commands, controls, navigation, and search.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Arranged horizontally along the top or bottom edge of the view. Three content types: (1) view title, (2) navigation controls (back/forward, search), (3) action bar items (buttons, menus). **Tab bars are for navigation; toolbars act on content.**

## Best Practices

- **Choose items deliberately** — people must distinguish and activate each item. Define overflow priority for narrow views. System auto-adds overflow menus in iPadOS/macOS; don't add one manually or design defaults that overflow.
- **More menu** — for additional secondary actions. Include all actions in the toolbar if possible; add More only if truly needed.
- **Let people customize the toolbar** (iPadOS, macOS) for apps with many items or long sessions (e.g., editing apps). Especially valuable for advanced functionality not everyone needs.
- **Minimize custom backgrounds and tinted controls** — custom backgrounds can conflict with system-provided effects. Use the content layer to inform toolbar color; use `ScrollEdgeEffectStyle` to separate toolbar from content area.
- **Avoid similar colors for toolbar item labels and content backgrounds** — prefer monochromatic when content is colorful.
- **Prefer standard components** (buttons, text fields, headers/footers) — they have corner radii concentric with bar corners; custom components must match.
- **Consider hiding toolbars for distraction-free mode** — provide reliable ways to restore hidden elements.

## Titles

- **Provide a useful title per window** (not the app name). App name adds no hierarchy info.
- **Concise** — a word or short phrase under 15 characters, leaving room for other controls.
- **Omit when redundant** — e.g., Notes doesn't title a single open note (first line suffices); it uses the first line as a title only when multiple windows are open.

## Navigation

- **Standard Back and Close buttons** — use the standard symbols (no text "Back" or "Close" labels). If customized, it must look identical and behave identically.
- Can include a search field for quick content navigation. In iOS, a navigation-only toolbar is sometimes called a *navigation bar*.

## Actions

- **Support main tasks** — prioritize most-used commands or commands for the highest-value objects.
- **Clear meaning for every control** — prefer symbols over text (except for hard-to-symbolize actions like "Edit"). See icons#Standard-icons.
- **System-provided symbols without borders** — borders are unnecessary (the bar is the container). System handles hover and selection states automatically.
- **`.prominent` style for key actions** (Done, Submit) — one primary action only, on the trailing side.

## Item Groupings

Three zones (leading, center, trailing):

| Zone | Contents | Customizable? |
|---|---|---|
| Leading | Back/Forward, Show/Hide Sidebar, view title, document menu | No |
| Center | Common actions, view title (if not leading) | Yes (iPadOS, macOS) |
| Trailing | Critical/persistent items, inspector toggles, search, More menu, primary action (Done) | No |

- Items in the center auto-collapse into overflow when the window shrinks.
- **Group by function and frequency** — e.g., Keynote: presentation-level, playback, object insertion.
- **Navigation controls and critical actions (Done, Close, Save) in distinct, visually separate sections.**
- **Consistent groupings across platforms.**
- **Max ~3 groups** — more feels cluttered.
- **Keep text-labeled actions separate from icon-only actions** — adjacent labels run together visually; insert fixed space between text buttons.

## Platform Considerations

### iOS

- **Only the most important items** in the main toolbar area — space is very limited. Put secondary actions in More.
- **Large title** — transitions to standard title on scroll; returns on scroll to top. Keeps people oriented.

### iPadOS

- Can combine toolbar with a tab bar in the same horizontal space at the top. Useful for layouts with a few main areas but full-width content.

### macOS

- Toolbar sits in the frame at the top of the window (below or integrated with the title bar). Toolbar items have no bezel; window title can appear inline with controls.
- **Every toolbar item must also exist as a menu bar command.** People can hide or customize the toolbar; it can't be the only place a command lives. (Not every menu command needs a toolbar item.)

### visionOS

- System toolbar appears along the **bottom** edge of the window, slightly in front on the z-axis. Uses variable blur for legibility as content scrolls behind.
- Items can be a symbol or text label; looking at a symbol item reveals its text label.
- **Use the system-provided toolbar** — familiar, optimized for eye/hand input, auto-positioned correctly.
- **No vertical toolbars** — tab bars are vertical in visionOS; a vertical toolbar would cause confusion.
- **Prevent windows from resizing below toolbar width** — no menu bar in visionOS means the toolbar must always show essential controls.
- **Context-specific controls in modal states** — provide relevant modal controls and restore standard controls on exit.
- **Avoid pull-down menus in the toolbar** — hard to discover, clutters interface, and may obscure window controls below the bottom edge.

### watchOS

- Toolbar buttons in **top corners** or **along the bottom**.
- Buttons above scrolling content remain **always visible**.
- Scrolling toolbar button: hidden by default, revealed by scrolling up. Use for important-but-not-primary actions (e.g., Mail's New Message at the top of Inbox).

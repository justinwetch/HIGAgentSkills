---
topic: menus
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/presentation
triggers:
  - "menu"
  - "menu item"
  - "pull-down menu"
  - "submenu"
  - "NSMenu"
related:
  - context-menus
  - pull-down-buttons
  - the-menu-bar
---
# Menus

> A menu reveals its options when people interact with it — a space-efficient way to present commands in all experiences.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Applies to all menu types: menu bar menus, context menus, pop-up/pull-down buttons, in-game menus.

## Labels

- **Verb or verb phrase** for action items (View, Close, Select). Match your app's communication style.
- **Title-style capitalization** — capitalize every word except articles, coordinating conjunctions, and short prepositions; always capitalize the last word.
- **No articles** (a, an, the) — "View Settings" not "View the Settings". Articles lengthen without adding clarity.
- **Ellipsis (…)** — append when the action requires more input before completing.
- **Show unavailable items dimmed** — item responds to no interactions. Keep the menu itself accessible even if all items are unavailable.

## Icons

- Use **familiar icons** for common actions (Copy, Share, Delete) — same icons as the system, wherever they appear.
- **No icon if no clear match** — avoid ornamentation; don't add icons that might be confused with other actions.
- **Single icon to introduce a group** — use the first item's symbol as a group-theme anchor; let text distinguish the rest.

## Organization

- **Important/frequent items first** — people scan from the top.
- **Group logically related items with a separator** (horizontal line or gap). Keep related items together even if some are rarely used (Paste and Paste & Match Style go together).
- **Limit menu length** — long menus require more time/attention. Split into separate menus or use submenus. Exception: user-defined or dynamically generated content (History, Bookmarks) may be long.

## Submenus

- A submenu item shows a chevron after its label. Functionally identical to a regular menu with hierarchical positioning.
- **Use sparingly** — each level hides content and adds complexity. Appropriate when a term appears in 2+ menu items in the same group (e.g., "Sort by Date", "Sort by Score" → "Sort by" submenu with Date / Score items).
- **Max one level deep** — multiple hierarchical levels are difficult to navigate.
- **Max ~5 items** per submenu — beyond that, create a new menu.
- **Submenu must stay available** even when all its nested items are unavailable.
- **Prefer submenus over indenting** — indented items don't clearly express hierarchy and are inconsistent with the platform.

## Toggled Items

Menu items that represent attributes people can turn on/off:
- **Changeable label** — "Show Map" ↔ "Hide Map" (single toggled item, label changes with state).
- **Add a verb when the changeable label is ambiguous** — "HDR On/Off" may read as a state, not an action. "Turn HDR On / Turn HDR Off" is clearer.
- **Show both items simultaneously** when viewing both states at once helps — e.g., "Take Account Online" and "Take Account Offline" where only the applicable one is available.
- **Checkmark** — for a group of attributes, a checkmark on the active item makes it easy to scan which are applied (e.g., Format > Font for bold/italic/underline).
- **"Plain" / remove-all item** — if people can apply multiple styles, consider an item that clears all at once.

## In-Game Menus

- **Use platform's default navigation** — touch on iOS, direct/indirect gestures on visionOS, etc.
- **Ensure menus remain readable and tappable** at all screen sizes. Scaling game content down can make menus too small. Adjust tap target sizes and consider alternative content presentation if needed.

## Platform Considerations

### iOS, iPadOS

Three menu layouts:
- **Small** — 4 unlabeled icon-only items in a top row, remaining items in list below.
- **Medium** — 3 items (icon + short label) in top row, remaining items in list below.
- **Large** (default) — all items in a list.

Use **medium** for 3 important frequently used actions (e.g., Notes: Scan, Lock, Pin).
Use **small** only for closely related groups (Bold, Italic, Underline, Strikethrough) — all must have recognizable symbols.

### visionOS

- Supports small and large layouts (same as iOS/iPadOS).
- Menus can extend beyond window boundaries (as on macOS).
- Use `presentationBreakthroughEffect(_:)` to keep the menu visible above other content.
- **Display menu near the content it controls** — people look at items before tapping; distant content means the effect is missed.
- **Prefer subtle breakthrough effect** — blends with surroundings, maintains depth/context. Use `prominent` only when it's critical the menu appears over the entire scene (can disrupt experience). Use `none` only in specific games where navigation around barriers is intentional.

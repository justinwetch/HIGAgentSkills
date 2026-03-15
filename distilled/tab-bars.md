---
topic: tab-bars
tier: 3
platforms: [ios, ipados, macos, tvos]
category: components/navigation
triggers:
  - "tab bar"
  - "TabView"
  - "bottom navigation"
  - "tab item"
  - "tab icon"
related:
  - sidebars
  - toolbars
  - focus-and-selection
---
# Tab Bars

> A tab bar lets people navigate between top-level sections of an app, preserving navigation state within each section.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

**Tab bar vs. toolbar:** tab bars are for navigation; toolbars are for actions on content in the current view.

## Best Practices

- **Navigation only — no actions** in the tab bar.
- **Always visible** when navigating between sections. Exception: a modal view may cover it (modals are temporary and self-contained).
- **Appropriate number of tabs** — weigh complexity vs. frequency of access. Fewer tabs = easier to navigate. Consider a sidebar for complex information structures.
- **No overflow tabs** — on iOS/iPadOS, if too many tabs exist, the trailing one becomes "More" (a separate list). Harder to discover; avoid designs that trigger it.
- **Never disable or hide tab bar buttons** even when content is unavailable — explain why the section is empty.
- **Include tab labels** — single words preferred. Appear beside or below the icon.
- **SF Symbols** — use filled symbols for consistency. Auto-adapts between compact (icon above label) and regular (icon beside label) views.
- **Badges** — red oval with number or "!" for critical new/updated information. Reserve for critical info only.
- **Avoid similar colors for tab labels and content layer backgrounds** — prefer monochromatic tab bars when app content is colorful.

## Platform Considerations

### iOS

- Tab bar floats at the bottom on a Liquid Glass background.
- With an accessory (e.g., MiniPlayer in Music): tab bar can minimize and move accessory inline when scrolling down. Tapping a tab or scrolling to top restores it.
- Can include a distinct search item at the trailing end.

### iPadOS

- Tab bar appears near the top of the screen.
- Can be fixed or include a button that converts it to a sidebar.
- **Prefer tab bar for navigation.** Offer sidebar conversion for complex apps with many sections.
- **Let people customize tab bar items** — for apps with many sections, allow adding/removing items. Aim for ≤5 default items for consistency across compact and regular sizes.

### tvOS

Highly customizable (background tint/color/image, font, active/inactive tints, icon buttons). Defaults: translucent, selected tab is opaque, selected tab has drop shadow.

- **Height:** 68pt. **Top edge:** 46pt from top of screen. Neither is customizable.
- Items that don't fit are truncated with a fade on the right (or left + right if scrollable).
- Tab bar scrolls offscreen by default in single-view tabs. Pinned in split-view tabs (e.g., Library, Settings).
- Focus always returns to tab bar when people press Menu on the remote.
- **Live-viewing apps tab order:** (1) Live content, (2) Cloud DVR/recorded content, (3) Other content.

### visionOS

- Tab bar is always **vertical**, floating at the leading edge of the window.
- Expands when people look at it; tap to open a tab. May temporarily obscure content behind it.
- **Supply a symbol AND text label for each tab** — symbol always visible; labels revealed on look. Keep labels short for at-a-glance reading.
- Optionally include a sidebar within a tab for deep hierarchies. Sidebar selections must not change the open tab.

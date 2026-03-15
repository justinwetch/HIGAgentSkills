---
topic: sidebars
tier: 3
platforms: [ios, ipados, macos, tvos]
category: components/navigation
triggers:
  - "sidebar"
  - "navigation sidebar"
  - "NavigationSplitView"
  - "inspector"
related:
  - split-views
  - tab-bars
  - outline-views
---
# Sidebars

> A sidebar appears on the leading side of a view and provides flat, broad navigation between sections of an app.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

Floats above content (Liquid Glass layer). Shows multiple top-level areas or modes simultaneously. Requires substantial vertical + horizontal space — consider a tab bar in constrained contexts.

## Best Practices

- **Extend content beneath the sidebar** — let content horizontally scroll beneath, or use a background extension view (mirrors adjacent content to create the visual impression it stretches under).
- **Let people customize sidebar contents** — who decides which areas are important and in what order.
- **Use disclosure controls for deep hierarchies** — keeps vertical space manageable.
- **Use SF Symbols or custom symbols** (not bitmap images) for sidebar icons.
- **Let people hide the sidebar** — use platform-standard interactions (iPadOS: edge swipe; macOS: show/hide button or View menu commands). Don't hide by default.
- **Max 2 levels of hierarchy** — deeper structure calls for a split view with an intermediate content list.
- **Succinct group labels** for two-level hierarchies — omit unnecessary words.

## Platform Considerations

### iOS

**Avoid using a sidebar on iPhone.** Takes too much landscape space; unavailable in portrait. Use a tab bar instead.

### iPadOS

- Use `sidebarAdaptable` tab view style to offer a convertible tab bar ↔ sidebar, responding automatically to rotation and window size.
- To show a sidebar only (no tab bar toggle), use `NavigationSplitView`.
- **Prefer a tab bar first** — only upgrade to sidebar when sections exceed tab bar capacity.

### macOS

- Sidebar size: small, medium, or large. Settable programmatically; people override via General > Sidebar Icon Size.
- **Don't fix sidebar icon colors** — use the current app accent color so people's chosen accent shows throughout. A fixed color may help meaning but should be the exception.
- **Auto-collapse on window resize** — collapse the sidebar when the window shrinks to give more room for content.
- **No critical info/actions at the bottom** — window repositioning often hides the bottom edge.

### visionOS

For deep hierarchies, use a sidebar within a tab (secondary navigation). Sidebar selections must not change the active tab.

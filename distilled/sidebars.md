---
topic: sidebars
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/navigation
triggers:
  - "sidebar"
  - "navigation sidebar"
  - "NavigationSplitView"
  - "backgroundExtensionEffect()"
  - "sidebarAdaptable"
  - "UISplitViewController"
  - "UICollectionLayoutListConfiguration.Appearance.sidebar"
  - "NSSplitViewController"
related:
  - split-views
  - tab-bars
  - layout
---
# Sidebars

> A sidebar appears on the leading side of a view and provides broad navigation between app areas or top-level collections.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

Shows multiple top-level areas or modes simultaneously and can include limited hierarchy. Requires substantial vertical and horizontal space; consider a tab bar in constrained contexts.

## Best Practices

- **Extend visually rich content beneath the sidebar on iOS, iPadOS, and macOS** - sidebars can float in the Liquid Glass layer; let content horizontally scroll beneath or use a background extension effect.
- **Let people customize sidebar contents** - people decide which areas are important and in what order.
- **Use disclosure controls for deep hierarchies** - keeps vertical space manageable.
- **Use familiar symbols** for sidebar icons; prefer SF Symbols or custom symbols over bitmap images.
- **Don't fix sidebar icon colors unless color carries meaning** - prefer system/accent behavior.
- **Let people hide the sidebar** - use platform-standard interactions (iPadOS edge swipe; macOS show/hide button or View menu commands). Don't hide by default.
- **Max 2 levels of hierarchy** - deeper structure calls for a split view with an intermediate content list.
- **Succinct group labels** for two-level hierarchies; omit unnecessary words.

## Platform Considerations

### iOS, iPadOS

- Use `sidebarAdaptable` tab view style to offer a convertible tab bar/sidebar that adapts to platform, rotation, and window size.
- To show a sidebar only, use `NavigationSplitView`.
- **Prefer a tab bar first** - upgrade through convertible sidebar appearance when areas exceed tab bar capacity or are less frequently used.

### macOS

- Sidebar size: small, medium, or large. People can override in General > Sidebar Icon Size.
- **Auto-collapse on window resize** - collapse the sidebar when the window shrinks to give more room for content.
- **No critical info/actions at the bottom** - window repositioning often hides the bottom edge.

### visionOS

For deep hierarchies, use a sidebar within a tab as secondary navigation. Sidebar selections must not change the active tab.

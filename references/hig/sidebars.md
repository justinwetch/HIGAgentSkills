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

A sidebar appears on the leading side of a view and navigates between app areas or top-level collections such as folders and playlists. It needs substantial space; consider a tab bar when space is limited or you want more room for content. When more areas are needed than fit in a tab bar, its convertible sidebar-style appearance can expose less-frequent areas.

## Best practices

- In iOS, iPadOS, and macOS, let rich content extend beneath a Liquid Glass sidebar by horizontal scrolling or a background extension effect that mirrors, flips, and blurs adjacent content to the window edge. Don’t stop the image at the sidebar edge. [`backgroundExtensionEffect()`](<https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()>).
- Let people customize sidebar contents/order when possible. If the app has a lot of content, use disclosure controls to keep vertical space manageable; generally show no more than two hierarchy levels, with succinct descriptive group labels. For deeper hierarchies, consider a split view with a content list between sidebar and detail.
- Consider using familiar SF Symbols. If a custom icon is needed, consider a custom symbol rather than a bitmap image. Sidebar icons normally use the app/system accent color; in macOS, honor the accent color people choose. Sparingly used fixed colors can clarify meaning or draw attention (Mail’s yellow VIP icon is an example).
- Consider letting people hide/show the sidebar using platform conventions when possible, but do not hide it by default: iPadOS provides edge swipe; macOS a show/hide button or View-menu commands. visionOS windows usually expand for a sidebar, so hiding is rarely needed.

## Platform considerations

**iOS/iPadOS:** [`sidebarAdaptable`](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) lets the app choose whether to open as a sidebar or tab bar; both provide a switch button, and the style adapts to platform, rotation, and window width. Consider using a tab bar first; when more areas are needed than fit, its convertible sidebar appearance exposes less-frequent areas. To display only a sidebar, use [`NavigationSplitView`](https://developer.apple.com/documentation/swiftui/navigationsplitview) to put it in the split view’s primary pane, or use [`UISplitViewController`](https://developer.apple.com/documentation/uikit/uisplitviewcontroller). If necessary and not using SwiftUI, use [`UICollectionLayoutListConfiguration.Appearance.sidebar`](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar).

**macOS:** Row height, text, and glyph size follow a small/medium/large sidebar size. The app can set the size programmatically; people can also change the sidebar icon size in General settings. Consider auto-hiding/revealing when the container resizes. Keep critical information/actions away from the bottom, which may be offscreen.

**visionOS:** For deep hierarchy, a sidebar inside a tab can provide secondary navigation. Sidebar selections must not change the currently open tab.

No additional considerations for tvOS; sidebars are not supported in watchOS.

Source: [Apple HIG — Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), captured 2026-09-12.

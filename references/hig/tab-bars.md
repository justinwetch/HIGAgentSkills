---
topic: tab-bars
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/navigation
triggers:
  - "tab bar"
  - "TabView"
  - "bottom navigation"
  - "tab item"
  - "tab icon"
  - "Liquid Glass tab bar"
  - "TabBarMinimizeBehavior"
  - "UITabBarController.MinimizeBehavior"
  - "tabBarOnly"
  - "sidebarAdaptable"
  - "TabViewCustomization"
  - "UITab.Placement"
  - "TabViewBottomAccessoryPlacement"
related:
  - sidebars
  - tab-views
  - toolbars
  - materials
  - focus-and-selection
---
# Tab bars

A tab bar navigates among an app’s top-level sections, explains the app’s information or functionality, and preserves navigation state within each section.

## Best practices

- Use tabs for navigation, not current-view actions; use a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars) for actions. Keep the bar visible between sections (a temporary, self-contained modal may cover it), use as few tabs as the hierarchy needs, and consider a sidebar/adaptive sidebar for complex structures.
- Avoid overflow. On iOS/iPadOS, insufficient width turns the trailing item into **More**, hiding the remaining items in a separate list. Don’t disable or hide unavailable sections; explain an empty one instead.
- Label tabs, preferably with single words. SF Symbols adapt between compact (icon above label) and regular (beside label) layouts; prefer filled symbols. Use [Apple Design Resources](https://developer.apple.com/design/resources/) for custom icon dimensions.
- Reserve badges (red oval, white number or exclamation point) for critical new/updated information. Keep labels distinct from colorful content; use monochrome or a differentiated accent with [Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color).

## Platform considerations

**macOS:** No additional considerations. **watchOS:** Not supported.

**iOS:** The bar floats at the bottom over [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass), allowing content to peek through. With an attached accessory such as Music’s MiniPlayer, scrolling down can minimize the bar and move the accessory inline; tapping a tab or scrolling to the top exits. In the illustrated Music example, the expanded MiniPlayer is above the bar; when minimized, the current tab is at the leading bottom, the accessory is centered, and Search is trailing. Use [`TabBarMinimizeBehavior`](https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior) or [`UITabBarController.MinimizeBehavior`](https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior). A dedicated Search tab may be trailing.

**iPadOS:** The bar is near the top and can be fixed or offer conversion to a sidebar ([`tabBarOnly`](https://developer.apple.com/documentation/swiftui/tabviewstyle/tabbaronly), [`sidebarAdaptable`](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable)). Prefer tabs for frequent sections; complex apps can offer sidebar conversion. A sidebar without conversion uses [`NavigationSplitView`](https://developer.apple.com/documentation/swiftui/navigationsplitview). For apps with many sections, let people add frequently used/remove less-used tabs (Music can add a favorite playlist); if you offer customization, aim for **five or fewer default tabs** for compact/regular continuity. See [`TabViewCustomization`](https://developer.apple.com/documentation/swiftui/tabviewcustomization) and [`UITab.Placement`](https://developer.apple.com/documentation/uikit/uitab/placement).

**tvOS:** Customize background tint/color/image, item fonts (including selected), selected/unselected tints, and icons such as Settings/Search. By default the bar is translucent, only the selected tab opaque, and remote focus adds a drop shadow. Height is **68 points**; top edge is **46 points** from screen top; neither changes. Overflow fades the rightmost item; scrolling also fades from the left. With one main view, the bar can scroll offscreen; with a split view (TV Library/Settings), it stays pinned while panes scroll. Menu returns focus to the top bar. Live-viewing order: **Live → Cloud DVR/recorded → Other**.

**visionOS:** The bar is vertical and fixed relative to the window’s leading side. Looking expands it; look at a tab and tap to open it, and expansion may obscure content. Supply a symbol (always visible) and short label (revealed on expansion). A sidebar can provide secondary navigation inside a deep tab hierarchy, but its selections must not change the open tab.

## Resources

Developer references: [`TabView`](https://developer.apple.com/documentation/swiftui/tabview), [`TabViewBottomAccessoryPlacement`](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement), [`Enhancing your app’s content with tab navigation`](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation), [`UITabBar`](https://developer.apple.com/documentation/uikit/uitabbar), and [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar). Videos: [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356), [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208). Source: [Apple HIG — Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), captured 2026-09-12.

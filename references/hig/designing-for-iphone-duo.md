---
topic: designing-for-iphone-duo
tier: 2
platforms: [ios]
category: platforms
triggers: [iPhone Duo, folding iPhone, foldable iPhone, reserved regions, ToolbarItemVisibilityPriority, UIBarButtonItemVisibilityPriority, ToolbarOverflowMenu]
related: [designing-for-ios, layout, split-views, toolbars, tab-bars, designing-for-games]
---
# Designing for iPhone Duo

An iPhone Duo app adapts as the device opens and closes across two displays. iOS patterns apply. Each display has its own front-facing camera; a center hinge supports different poses; the hinge reduces usable space when folded. Standard, resizable components adapt with little adjustment.

## Displays, poses, and continuity

- The outer display is used closed and the inner open. Support closed, fully open, partially folded/book-like, surface-resting, and edge-standing poses with adaptive layout, not a custom layout per pose.
- Use size classes: compact width outer, regular width inner. Expand the existing layout with space; use margins/safe-area insets and avoid fixed widths or display-specific dependencies.
- Preserve functionality, element state, hierarchy, and access across displays/poses. More space may expose another level if it makes sense for your content: Mail shows either a list or message closed, then both side by side open. Content may move/resize and controls overflow, but access remains.
- Games may lock portrait or landscape, but be sure to fill the screen as the pose changes, keep text and controls as consistent in size as possible, and prefer changing aspect ratio over letterboxing/pillarboxing. If padding is unavoidable, fill it with artwork.

## Dynamic layouts and reserved regions

Reserved regions are areas content avoids or components accommodate:

| Region | Condition and behavior |
|---|---|
| Outer camera | Always present in a corner; expands into the Dynamic Island for Live Activities. Side controls are arranged around it automatically. |
| Inner camera | Hidden behind the display until active; when it activates, UI moves aside to signal it. |
| Folding region | Present when partially open; divides the inner display into usable regions while excluding the center fold. |

Alerts, context menus, sheets, and standard split views adapt to the fold; split columns adjust width/margins for inner-display symmetry. If the system doesn’t move a custom component automatically, use reserved-region APIs to keep important elements clear of the center. Notes keeps list/detail panes visible, with a narrower list fully open and equal panes when folded. Prefer a layout container that adapts automatically, and even grid column counts. Avoid extreme changes: move only what’s necessary to keep elements visible and easy to tap; favor small adjustments over disappearing or dramatically shifting controls.

Split views expand to multiple panes inner and one pane outer, as in regular/compact iPhone environments. An arrangement view holds primary and secondary views and responds to size, orientation, and reserved regions:

- **Split:** divides the area horizontally when wider than tall and vertically when taller than wide; axes can be limited.
- **Overlay:** layers the views; while partially folded they occupy separate sides, otherwise the primary overlays the secondary. The secondary can collapse.

Consider an arrangement view when your layout already resembles one: side-by-side or stacked (`HStack`/`VStack`) translates to split; layered (`ZStack`) to overlay.

Arrangement views lay out content, not navigation; put navigation split views and tab views around them. Split view developer guidance: `NavigationSplitView` (SwiftUI), `UISplitViewController` (UIKit).

## Vertical controls

The outer display is wider and shorter than other iPhone displays, so toolbars, tab bars, navigation controls, status bar, and Dynamic Island move to one side; standard components get this automatically, but you may refine it. On the outer display’s trailing edge, the order from top to bottom is Dynamic Island, status bar, toolbar, then tab bar. Inner landscape keeps side controls; inner portrait keeps horizontal bars. In inner Split View, each app uses its outer edge. Vertical controls align to the hardware, keeping their position relative to the outer camera, and stay on the same side in right-to-left languages.

- Use safe areas so controls don’t cover content, including when that app’s controls move to the opposite edge in Split View. Keep controls’ relative positions as similar as possible across poses; in general, don’t override the default bar placement.
- Place primary navigation (Back/Close) at the top, then prominent actions (Done); retain other top/bottom groups with system spacing. Items overflow bottom-to-top by default. Set visibility priority by group, then by item within a group if you need finer control, to preserve frequent actions (Compose/New Note) and status/badged items.
- Group related items with `ToolbarItemGroup`/`UIBarButtonItemGroup`; system spacing adapts, so don’t add fixed spacing. Keep controls near the content they affect: controls for a content area other than the trailing-edge one stay with that area rather than moving to the side, such as list controls above Mail’s leading pane.
- Give every non-text-only item a title and symbol so the system can choose its representation and use the title in overflow/expanded forms. Minimize text buttons because they remain horizontal; prefer a symbol wherever one works.
- When space is limited, navigation-focused views preserve the tab bar and move toolbar items to overflow by default; task-focused views minimize the tab bar into a single control, as on other iPhone devices, to preserve task-critical toolbar actions. Put app overflow actions in the system overflow menu, reserve ellipsis for overflow, and use another symbol for other menus.
- Consider the full display width for interfaces where bars aren’t necessary; it suits visual, immersive, non-scrolling interfaces when nothing conflicts with the Dynamic Island or status bar. A full-width background/header can coexist with inset scrolling content. Calculator reflows from four columns of five items on iPhone 16 in portrait to five columns of four on the iPhone Duo outer display.

Developer APIs: [SwiftUI safeAreaInsets](https://developer.apple.com/documentation/swiftui/geometryproxy/safeareainsets), [UIKit safeAreaInsets](https://developer.apple.com/documentation/uikit/uiview/safeareainsets), [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview), [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller), [HStack](https://developer.apple.com/documentation/swiftui/hstack), [VStack](https://developer.apple.com/documentation/swiftui/vstack), [ZStack](https://developer.apple.com/documentation/swiftui/zstack), [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority), [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority), [ToolbarItemGroup](https://developer.apple.com/documentation/swiftui/toolbaritemgroup), [UIBarButtonItemGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup), [Label](https://developer.apple.com/documentation/swiftui/label), [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem), [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu), and [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems).

Source: [Apple HIG — Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), new page dated September 9, 2026; captured 2026-09-12.

---
topic: layout
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "layout"
  - "spacing"
  - "margin"
  - "padding"
  - "safe area"
  - "grid"
  - "alignment"
related:
  - windows
  - split-views
  - sidebars
---
# Layout

## Hierarchy

- Place important content toward the top/leading side in reading order. Prefer standard components that adapt to RTL. Align related elements; indentation communicates subordination. Group related information/functions using negative space, containers, or separators.
- Use progressive disclosure to reduce initial choices/content: disclosure triangles, menus, nested views; scrollable sections can reveal more media.
- Where supported, Liquid Glass distinguishes controls from content. Prefer scroll-edge effects to solid/semi-opaque backgrounds beneath controls. Extend full-screen backgrounds beneath sidebars, toolbars, and tab bars to window/screen edges.
- If edge-filling artwork would hide important parts behind a sidebar/inspector, a background extension can mirror, flip, and blur the image beneath adjacent components: [`backgroundExtensionEffect()`](<https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()>), [`UIBackgroundExtensionView`](https://developer.apple.com/documentation/uikit/uibackgroundextensionview).
## Adaptability and size classes

- Adapt to display/window sizes, compact/regular size classes, orientation/aspect ratio, Dynamic Island, external displays, Display Zoom, resizable iPad/Mac windows, text size, and locale (direction, formatting, font variation, text length). SwiftUI/Auto Layout handles these characteristics in iOS, iPadOS, tvOS, and visionOS.
- Respect system safe areas, margins, and guides; use layout modifiers to refine placement. Preserve familiarity when rotating, resizing, adding a display, or changing devices; orientation-locked apps/games must still resize well.
- Accommodate Dynamic Type: horizontal views may stack; rows/containers may grow to avoid clipping/overlap and allow multiple lines. Unity games can use [Apple’s accessibility plug-in](https://github.com/apple/unityplugins/blob/main/plug-ins/Apple.Accessibility/Apple.Accessibility_Unity/Assets/Apple.Accessibility/Documentation~/Apple.Accessibility.md).
- Preview different devices, size classes, localizations, and text sizes; start with largest/smallest layouts. Use Xcode [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) simulations to check clipping/resizing, including iPad and iPhone Mirroring on Mac.
- If context changes crop, letterbox, or pillarbox background artwork, scale it to fill the screen **without changing the artwork’s aspect ratio**. Extreme window proportions may require artwork beyond the ordinarily visible area.
- In iOS/iPadOS, horizontal compact/regular describes narrow/wide; vertical compact/regular describes short/tall. Device, window, and multitasking state determine classes (full screen, Slide Over, iPhone Mirroring); every combination can occur, including resized iPad apps in macOS.
- **Choose layout from size classes, not device type/idiom or orientation:** those do not establish actual available space. Consider all combinations in either aspect ratio. APIs: [`UITraitChangeObservable`](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94), [`UserInterfaceSizeClass`](https://developer.apple.com/documentation/swiftui/userinterfacesizeclass).
- Keep functionality constant as classes change. Larger spaces may show more functionality, switch a tab bar to a sidebar, or expose overflow items. The idiom remains the same when resizing; preserve familiar platform layout.

## Guides and safe areas

- A layout guide is a rectangle for positioning, alignment, and spacing. Predefined guides supply standard margins and readable text widths; custom guides are possible. [`UILayoutGuide`](https://developer.apple.com/documentation/uikit/uilayoutguide), [`NSLayoutGuide`](https://developer.apple.com/documentation/appkit/nslayoutguide).
- A safe area excludes edge-obstructing hardware or views (toolbar/tab/status bars, Dynamic Island). Respect it so system UI and hardware do not cover controls/content. [`SafeAreaRegions`](https://developer.apple.com/documentation/swiftui/safearearegions), [UIKit safe-area positioning](https://developer.apple.com/documentation/uikit/positioning-content-relative-to-the-safe-area).

## Platform considerations

**macOS:** Avoid controls/critical information at the window bottom (the window may be moved below the screen edge) and content behind the top-edge camera housing. See [`NSPrefersDisplaySafeAreaCompatibilityMode`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode).

**tvOS:** Inset primary content **60 pt top/bottom and 80 pt sides** for overscan/compatibility. Focus enlarges UIKit elements, so pad them and prevent overlap. Space unfocused grid rows/columns accordingly; [`UICollectionViewFlowLayout`](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout) derives column count from content width/spacing.

| Columns | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
|---:|---:|---:|---:|
| 2 | 860 pt | 40 pt | 100 pt |
| 3 | 560 pt | 40 pt | 100 pt |
| 4 | 410 pt | 40 pt | 100 pt |
| 5 | 320 pt | 40 pt | 100 pt |
| 6 | 260 pt | 40 pt | 100 pt |
| 7 | 217 pt | 40 pt | 100 pt |
| 8 | 184 pt | 40 pt | 100 pt |
| 9 | 160 pt | 40 pt | 100 pt |

Titled rows need space from the prior unfocused row to the title center and from title bottom to the next row. Keep grid spacing consistent; make partially hidden offscreen content equal in width on both sides.

**visionOS:** Content may be in a window, bounded 3D volume, or immersive space; this guidance covers windows/volumes (see [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)). In general, support resizing; when allowed, adapt well as size changes and prefer horizontally centered content at very large sizes. Minimum/maximum sizes can apply to windows, volumes, and attached UI such as ornaments to prevent overlap or unwieldy layouts, not to prevent resizing; for example, Safari’s navigation ornament can have a fixed maximum while its window remains resizable. Reserve fixed-depth inline 3D in windows for meaningful moments alongside 2D, inset it to prevent collisions or unpredictable out-of-window appearance, and consider a volume/immersive space for larger models or primarily 3D views. Put supplemental content in an adjacent window with [`defaultWindowPlacement(_:)`](https://developer.apple.com/documentation/swiftui/scene/defaultwindowplacement(_:)); reserve ornaments for app controls. Space controls for clear identification and unobscured hover effects; button centers should be at least **60 pt apart**.

**watchOS:** Usually show no more than three glyph buttons or two text buttons in a row. Full-width text buttons are preferred; two short-labeled side-by-side buttons can work if the screen does not scroll. Support autorotation for views people may show others (for example, an image or QR code); [`WKExtension.isAutorotating`](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating) (deprecated, with no documented replacement).

Source: [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout), captured 2026-09-12.

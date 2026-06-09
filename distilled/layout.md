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

> Consistent, adaptive layouts ground people in your content and help them discover features across all devices.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- Group related items with negative space, background shapes, colors, materials, or separators.
- Give essential information sufficient space — don't crowd primary content with secondary details.
- Extend backgrounds and artwork to screen edges. Scrollable content reaches display bottom and sides. Controls/bars float above content, not on the same plane.
- Use a background extension view when content doesn't span the full window (e.g., beneath sidebar or inspector). APIs: `backgroundExtensionEffect()`, `UIBackgroundExtensionView`.

## Visual Hierarchy

- Use Liquid Glass material for controls — distinct from content layer. Use scroll edge effects to transition between content and the control area.
- Place most important items near the top and leading edge (reading order: top→bottom, leading→trailing; reverses in RTL languages).
- Align components to aid scanning and communicate organization. Use indentation to show information hierarchy.
- Use progressive disclosure to reveal hidden content (disclosure controls, partial-item hints that invite scrolling).
- Include enough space around controls and group them in logical sections.

## Adaptability

Handle these common variations:
- Different screen sizes, resolutions, color spaces
- Portrait/landscape orientation
- Dynamic Island, camera controls, and other system features
- External displays, Display Zoom, resizable iPad windows
- Dynamic Type text-size changes
- Locale differences (RTL/LTR, date/number formatting, text length variation)

- Use SwiftUI or Auto Layout for automatic trait adaptation.
- Respect system-defined safe areas, margins, and layout guides. APIs/references: `SafeAreaRegions`, `UILayoutGuide`, `NSLayoutGuide`.
- Test with the largest and smallest layouts first. Also test on Simulator for clipping before testing on hardware.
- When artwork is cropped in a different aspect ratio context, scale (don't distort) to keep important content visible. In visionOS, system auto-scales windows along z-axis.

## Guides and Safe Areas

A **layout guide** defines a rectangular region for positioning, aligning, and spacing content. A **safe area** is the visible region not covered by toolbars, tab bars, or other overlay views. Safe areas avoid Dynamic Island, camera housings, and other interactive features.

Respect safe areas on every platform — they account for interactive bars that reposition dynamically.

## Platform Considerations

### iOS

- Support both portrait and landscape unless your experience genuinely requires one. If landscape-only, support both left and right rotation.
- Games: prefer full-bleed fullscreen accommodating corner radius, sensor housing, and Dynamic Island. Optionally offer letterbox/pillarbox toggle.
- Avoid full-width buttons — prefer system-margin-inset buttons. If necessary, harmonize with hardware curvature and align to safe areas.
- Hide status bar only when it meaningfully enhances the experience (games, media).

### iPadOS

- Support the full range of window sizes (people resize freely, similar to macOS).
- Defer switching to compact view as long as possible — design full-screen first.
- For split views, hide tertiary columns (inspectors) as width narrows before switching to compact view.
- Test at common sizes: half, third, and quadrant of screen on multiple devices.
- Consider a convertible tab bar (sidebar ↔ tab bar, switches automatically with width).
- Use `sidebarAdaptable` where appropriate for sidebar/tab bar adaptation.

### macOS

- Avoid placing controls or critical info at the bottom of windows — windows are often moved below screen bottom.
- Avoid content within the camera housing at the top edge.

### tvOS

- Layouts don't automatically adapt to TV size — design explicitly for range of screens.
- Safe area insets: **60pt top/bottom, 80pt left/right**. Keep primary content within this zone.
- Allow only partial/off-screen elements or deliberate overflow outside safe area.
- Include padding between focusable elements — focused items grow larger; prevent overlap with nearby content.

**Grids:**
- Use UIKit collection view flow for automatic column count based on content width/spacing.
- tvOS grid unfocused widths for 2/3/4/5/6/7/8/9 columns: 860/560/410/320/260/217/184/160pt. Use 40pt horizontal spacing and at least 100pt vertical spacing.
- Add extra vertical spacing for titled rows: space between bottom of previous row and center of title.
- Use consistent spacing — inconsistent spacing destroys the grid perception.
- Keep partially hidden offscreen content symmetrical on both sides.

### visionOS

- Center most important content and controls — easier to discover and interact with near the window center.
- Keep content within window bounds — system controls (Share, resize, move, close) appear just outside bounds and must remain accessible.
- Don't let 2D or 3D content encroach on system-provided window controls below the window.
- For controls outside the window, use an **ornament** (toolbar and tab bar appear as ornaments automatically).
- Space interactive components with at least 60pt center-to-center between buttons.
- Content extending beyond bounds along z-axis will be clipped by the system past a threshold.

### watchOS

- Extend content edge-to-edge — the bezel provides natural visual padding; minimize internal padding.
- Max 3 glyph buttons or 2 text buttons side by side.
- Prefer full-width text buttons; two narrow side-by-side text buttons work if screen doesn't scroll.
- Support autorotation in views people might show others (images, QR codes).

## Specifications

### iOS, iPadOS device screen dimensions

| Model | Dimensions (portrait) |
| --- | --- |
| iPad Pro 13-inch | 1032x1376 pt (2064x2752 px @2x) |
| iPad Pro 12.9-inch | 1024x1366 pt (2048x2732 px @2x) |
| iPad Pro 11-inch 5th and 6th generation | 834x1210 pt (1668x2420 px @2x) |
| iPad Pro 11-inch 1st–4th generation | 834x1194 pt (1668x2388 px @2x) |
| iPad Pro 10.5-inch | 834x1112 pt (1668x2224 px @2x) |
| iPad Pro 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad Air 13-inch | 1024x1366 pt (2048x2732 px @2x) |
| iPad Air 11-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad Air 10.9-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad Air 10.5-inch | 834x1112 pt (1668x2224 px @2x) |
| iPad Air 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad 11-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad 10.2-inch | 810x1080 pt (1620x2160 px @2x) |
| iPad 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad mini 8.3-inch | 744x1133 pt (1488x2266 px @2x) |
| iPad mini 7.9-inch | 768x1024 pt (1536x2048 px @2x) |
| iPhone 17 Pro Max | 440x956 pt (1320x2868 px @3x) |
| iPhone 17 Pro | 402x874 pt (1206x2622 px @3x) |
| iPhone Air | 420x912 pt (1260x2736 px @3x) |
| iPhone 17 | 402x874 pt (1206x2622 px @3x) |
| iPhone 16 Pro Max | 440x956 pt (1320x2868 px @3x) |
| iPhone 16 Pro | 402x874 pt (1206x2622 px @3x) |
| iPhone 16 Plus | 430x932 pt (1290x2796 px @3x) |
| iPhone 16 | 393x852 pt (1179x2556 px @3x) |
| iPhone 16e | 390x844 pt (1170x2532 px @3x) |
| iPhone 15 Pro Max | 430x932 pt (1290x2796 px @3x) |
| iPhone 15 Pro | 393x852 pt (1179x2556 px @3x) |
| iPhone 15 Plus | 430x932 pt (1290x2796 px @3x) |
| iPhone 15 | 393x852 pt (1179x2556 px @3x) |
| iPhone 14 Pro Max | 430x932 pt (1290x2796 px @3x) |
| iPhone 14 Pro | 393x852 pt (1179x2556 px @3x) |
| iPhone 14 Plus | 428x926 pt (1284x2778 px @3x) |
| iPhone 14 | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 Pro Max | 428x926 pt (1284x2778 px @3x) |
| iPhone 13 Pro | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 mini | 360x780 pt (1080x2340 px @3x) |
| iPhone 12 Pro Max | 428x926 pt (1284x2778 px @3x) |
| iPhone 12 Pro | 390x844 pt (1170x2532 px @3x) |
| iPhone 12 | 390x844 pt (1170x2532 px @3x) |
| iPhone 12 mini | 360x780 pt (1080x2340 px @3x) |
| iPhone 11 Pro Max | 414x896 pt (1242x2688 px @3x) |
| iPhone 11 Pro | 375x812 pt (1125x2436 px @3x) |
| iPhone 11 | 414x896 pt (828x1792 px @2x) |
| iPhone XS Max | 414x896 pt (1242x2688 px @3x) |
| iPhone XS | 375x812 pt (1125x2436 px @3x) |
| iPhone XR | 414x896 pt (828x1792 px @2x) |
| iPhone X | 375x812 pt (1125x2436 px @3x) |
| iPhone 8 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 8 | 375x667 pt (750x1334 px @2x) |
| iPhone 7 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 7 | 375x667 pt (750x1334 px @2x) |
| iPhone 6s Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 6s | 375x667 pt (750x1334 px @2x) |
| iPhone 6 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 6 | 375x667 pt (750x1334 px @2x) |
| iPhone SE 4.7-inch | 375x667 pt (750x1334 px @2x) |
| iPhone SE 4-inch | 320x568 pt (640x1136 px @2x) |
| iPod touch 5th generation and later | 320x568 pt (640x1136 px @2x) |

> **note:**
> All scale factors in the table above are UIKit scale factors, which may differ from native scale factors. For developer guidance, see [scale](https://developer.apple.com/documentation/UIKit/UIScreen/scale) and [nativeScale](https://developer.apple.com/documentation/UIKit/UIScreen/nativeScale).

### iOS, iPadOS device size classes

A size class is a value that’s either regular or compact, where *regular* refers to a larger screen or a screen in landscape orientation and *compact* refers to a smaller screen or a screen in portrait orientation. For developer guidance, see [UserInterfaceSizeClass](https://developer.apple.com/documentation/SwiftUI/UserInterfaceSizeClass).

Different size class combinations apply to the full-screen experience on different devices, based on screen size.

| Model | Portrait orientation | Landscape orientation |
| --- | --- | --- |
| iPad Pro 12.9-inch | Regular width, regular height | Regular width, regular height |
| iPad Pro 11-inch | Regular width, regular height | Regular width, regular height |
| iPad Pro 10.5-inch | Regular width, regular height | Regular width, regular height |
| iPad Air 13-inch | Regular width, regular height | Regular width, regular height |
| iPad Air 11-inch | Regular width, regular height | Regular width, regular height |
| iPad 11-inch | Regular width, regular height | Regular width, regular height |
| iPad 9.7-inch | Regular width, regular height | Regular width, regular height |
| iPad mini 7.9-inch | Regular width, regular height | Regular width, regular height |
| iPhone 17 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 17 Pro | Compact width, regular height | Compact width, compact height |
| iPhone Air | Compact width, regular height | Regular width, compact height |
| iPhone 17 | Compact width, regular height | Compact width, compact height |
| iPhone 16 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 16 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 16 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 16 | Compact width, regular height | Compact width, compact height |
| iPhone 16e | Compact width, regular height | Compact width, compact height |
| iPhone 15 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 15 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 15 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 15 | Compact width, regular height | Compact width, compact height |
| iPhone 14 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 14 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 14 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 14 | Compact width, regular height | Compact width, compact height |
| iPhone 13 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 13 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 13 | Compact width, regular height | Compact width, compact height |
| iPhone 13 mini | Compact width, regular height | Compact width, compact height |
| iPhone 12 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 12 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 12 | Compact width, regular height | Compact width, compact height |
| iPhone 12 mini | Compact width, regular height | Compact width, compact height |
| iPhone 11 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 11 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 11 | Compact width, regular height | Regular width, compact height |
| iPhone XS Max | Compact width, regular height | Regular width, compact height |
| iPhone XS | Compact width, regular height | Compact width, compact height |
| iPhone XR | Compact width, regular height | Regular width, compact height |
| iPhone X | Compact width, regular height | Compact width, compact height |
| iPhone 8 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 8 | Compact width, regular height | Compact width, compact height |
| iPhone 7 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 7 | Compact width, regular height | Compact width, compact height |
| iPhone 6s Plus | Compact width, regular height | Regular width, compact height |
| iPhone 6s | Compact width, regular height | Compact width, compact height |
| iPhone SE | Compact width, regular height | Compact width, compact height |
| iPod touch 5th generation and later | Compact width, regular height | Compact width, compact height |

### watchOS device screen dimensions

| Series | Size | Width (pixels) | Height (pixels) |
| --- | --- | --- | --- |
| Apple Watch Ultra (3rd generation) | 49mm | 422 | 514 |
| 10, 11 | 42mm | 374 | 446 |
| 10, 11 | 46mm | 416 | 496 |
| Apple Watch Ultra (1st and 2nd generations) | 49mm | 410 | 502 |
| 7, 8, and 9 | 41mm | 352 | 430 |
| 7, 8, and 9 | 45mm | 396 | 484 |
| 4, 5, 6, and SE (all generations) | 40mm | 324 | 394 |
| 4, 5, 6, and SE (all generations) | 44mm | 368 | 448 |
| 1, 2, and 3 | 38mm | 272 | 340 |
| 1, 2, and 3 | 42mm | 312 | 390 |

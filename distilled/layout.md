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
- Use a background extension view when content doesn't span the full window (e.g., beneath sidebar or inspector).

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
- Respect system-defined safe areas, margins, and layout guides.
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

### iOS, iPadOS Device Screen Dimensions (portrait)

| Model | Dimensions |
|---|---|
| iPad Pro 12.9-inch | 1024×1366pt (2048×2732px @2x) |
| iPad Pro 11-inch | 834×1194pt (1668×2388px @2x) |
| iPad Pro 10.5-inch | 834×1194pt (1668×2388px @2x) |
| iPad Pro 9.7-inch | 768×1024pt (1536×2048px @2x) |
| iPad Air 13-inch | 1024×1366pt (2048×2732px @2x) |
| iPad Air 11-inch | 820×1180pt (1640×2360px @2x) |
| iPad Air 10.9-inch | 820×1180pt (1640×2360px @2x) |
| iPad Air 10.5-inch | 834×1112pt (1668×2224px @2x) |
| iPad Air 9.7-inch | 768×1024pt (1536×2048px @2x) |
| iPad 11-inch | 820×1180pt (1640×2360px @2x) |
| iPad 10.2-inch | 810×1080pt (1620×2160px @2x) |
| iPad 9.7-inch | 768×1024pt (1536×2048px @2x) |
| iPad mini 8.3-inch | 744×1133pt (1488×2266px @2x) |
| iPad mini 7.9-inch | 768×1024pt (1536×2048px @2x) |
| iPhone 17 Pro Max | 440×956pt (1320×2868px @3x) |
| iPhone 17 Pro | 402×874pt (1206×2622px @3x) |
| iPhone Air | 420×912pt (1260×2736px @3x) |
| iPhone 17 | 402×874pt (1206×2622px @3x) |
| iPhone 16 Pro Max | 440×956pt (1320×2868px @3x) |
| iPhone 16 Pro | 402×874pt (1206×2622px @3x) |
| iPhone 16 Plus | 430×932pt (1290×2796px @3x) |
| iPhone 16 | 393×852pt (1179×2556px @3x) |
| iPhone 16e | 390×844pt (1170×2532px @3x) |
| iPhone 15 Pro Max | 430×932pt (1290×2796px @3x) |
| iPhone 15 Pro | 393×852pt (1179×2556px @3x) |
| iPhone 15 Plus | 430×932pt (1290×2796px @3x) |
| iPhone 15 | 393×852pt (1179×2556px @3x) |
| iPhone 14 Pro Max | 430×932pt (1290×2796px @3x) |
| iPhone 14 Pro | 393×852pt (1179×2556px @3x) |
| iPhone 14 Plus | 428×926pt (1284×2778px @3x) |
| iPhone 14 | 390×844pt (1170×2532px @3x) |
| iPhone 13 Pro Max | 428×926pt (1284×2778px @3x) |
| iPhone 13 Pro | 390×844pt (1170×2532px @3x) |
| iPhone 13 | 390×844pt (1170×2532px @3x) |
| iPhone 13 mini | 375×812pt (1125×2436px @3x) |
| iPhone 12 Pro Max | 428×926pt (1284×2778px @3x) |
| iPhone 12 Pro | 390×844pt (1170×2532px @3x) |
| iPhone 12 | 390×844pt (1170×2532px @3x) |
| iPhone 12 mini | 375×812pt (1125×2436px @3x) |
| iPhone 11 Pro Max | 414×896pt (1242×2688px @3x) |
| iPhone 11 Pro | 375×812pt (1125×2436px @3x) |
| iPhone 11 | 414×896pt (828×1792px @2x) |
| iPhone XS Max | 414×896pt (1242×2688px @3x) |
| iPhone XS | 375×812pt (1125×2436px @3x) |
| iPhone XR | 414×896pt (828×1792px @2x) |
| iPhone X | 375×812pt (1125×2436px @3x) |
| iPhone 8 Plus | 414×736pt (1080×1920px @3x) |
| iPhone 8 | 375×667pt (750×1334px @2x) |
| iPhone SE 4.7-inch | 375×667pt (750×1334px @2x) |
| iPhone SE 4-inch | 320×568pt (640×1136px @2x) |

Scale factors above are UIKit scale factors (may differ from native).

### iOS, iPadOS Size Classes

| Model | Portrait | Landscape |
|---|---|---|
| All iPads | Regular W, Regular H | Regular W, Regular H |
| iPhone 17 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 17 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone Air | Compact W, Regular H | Regular W, Compact H |
| iPhone 17 | Compact W, Regular H | Compact W, Compact H |
| iPhone 16 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 16 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone 16 Plus | Compact W, Regular H | Regular W, Compact H |
| iPhone 16 | Compact W, Regular H | Compact W, Compact H |
| iPhone 16e | Compact W, Regular H | Compact W, Compact H |
| iPhone 15 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 15 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone 15 Plus | Compact W, Regular H | Regular W, Compact H |
| iPhone 15 | Compact W, Regular H | Compact W, Compact H |
| iPhone 14 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 14 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone 14 Plus | Compact W, Regular H | Regular W, Compact H |
| iPhone 14 | Compact W, Regular H | Compact W, Compact H |
| iPhone 13 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 13 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone 13 / mini | Compact W, Regular H | Compact W, Compact H |
| iPhone 12 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 12 Pro / 12 / mini | Compact W, Regular H | Compact W, Compact H |
| iPhone 11 Pro Max | Compact W, Regular H | Regular W, Compact H |
| iPhone 11 Pro | Compact W, Regular H | Compact W, Compact H |
| iPhone 11 | Compact W, Regular H | Regular W, Compact H |
| iPhone XS Max / XR | Compact W, Regular H | Regular W, Compact H |
| iPhone XS / X | Compact W, Regular H | Compact W, Compact H |
| iPhone 8 Plus / 7 Plus / 6s Plus / 6 Plus | Compact W, Regular H | Regular W, Compact H |
| iPhone 8 / 7 / 6s / 6 / SE | Compact W, Regular H | Compact W, Compact H |

### watchOS Device Screen Dimensions

| Series | Size | Width (px) | Height (px) |
|---|---|---|---|
| Apple Watch Ultra 3rd gen | 49mm | 422 | 514 |
| Series 10, 11 | 42mm | 374 | 446 |
| Series 10, 11 | 46mm | 416 | 496 |
| Apple Watch Ultra 1st/2nd gen | 49mm | 410 | 502 |
| Series 7, 8, 9 | 41mm | 352 | 430 |
| Series 7, 8, 9 | 45mm | 396 | 484 |
| Series 4, 5, 6, SE | 40mm | 324 | 394 |
| Series 4, 5, 6, SE | 44mm | 368 | 448 |
| Series 1, 2, 3 | 38mm | 272 | 340 |
| Series 1, 2, 3 | 42mm | 312 | 390 |

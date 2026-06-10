---
topic: app-icons
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "app icon"
  - "icon design"
  - "icon grid"
  - "icon size"
related:
  - images
  - branding
  - icons
---
# App Icons

> A unique, memorable icon expresses your app's purpose at a glance across every system location.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Specifications

| Platform | Layout shape | Masked shape | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

Color spaces: sRGB, Gray Gamma 2.2, Display P3 (iOS/iPadOS/macOS/tvOS/watchOS only).

The system automatically scales icons to smaller variants (Settings, notifications, etc.) and can auto-generate missing appearance variants; custom variants usually preserve identity better.

## Layer Design

- iOS/iPadOS/macOS/watchOS: background layer + foreground layers -> Liquid Glass attributes (specular highlights, refraction, translucency). Built with **Icon Composer** (included in Xcode).
- tvOS: 2-5 layers -> parallax effect (depth, sway, illumination on focus).
- visionOS: background + 1-2 layers -> 3D shadow depth + alpha-channel embossing.

**Layer guidelines:**
- **Clearly defined edges** in foreground layers - avoid soft/feathered edges (impairs system highlights).
- **Vary opacity** in foreground layers for depth and vitality.
- **Group layers** to apply effects at the group level when multiple elements should behave as one surface.
- **Background**: if you choose a gradient, make sure it responds well to system lighting. Keep full-bleed and opaque.
- **Prefer vector graphics** (SVG, PDF) over raster. For mesh gradients/raster, use PNG.
- **Produce unmasked, appropriately shaped layers** - let the system apply masking. Pre-masked layers cause jagged edges and impede specular highlights.
- **Don't apply custom visual effects** (shadows between layers, bevels, glows) - system applies dynamic versions. If you do add effects: test in Icon Composer, Simulator, or on device.

## Icon Shape

- iOS/iPadOS/macOS: square layers -> system applies rounded corners matching device bezel curvature.
- visionOS/watchOS: square layers -> system applies circular masking.
- tvOS: rectangular layers -> system applies rounded corners.
- **Keep primary content centered** to avoid clipping at corner adjustments.

## Design Principles

- **Simplicity** - one core concept, minimal shapes, simple background (solid or gradient). Complex details look noisy at small sizes with system effects applied.
- **Consistent design across all platforms your app supports** - prevents people from thinking it's multiple different apps.
- **Filled, overlapping shapes** + transparency create depth.
- **Text only when essential** - not accessible, not localizable, often too small. Avoid words like "Watch," "Play," "New," or "For visionOS." If text is in a tvOS icon, place it above other layers so parallax doesn't crop it.
- **Illustrations, not photos** - photos have details that break down at small sizes and across appearances.
- Avoid UI-component replicas, app screenshots, extremely thin line weights, sharp corners, and Apple hardware replicas.

## Appearances (iOS, iPadOS, macOS)

People can choose: **default, dark, clear, or tinted** icon appearances.

- **Keep core visual features consistent across all variants** - don't swap elements between variants.
- **Dark/tinted variants**: more subdued; ensure visibility, legibility, and recognizability.
- **Use your light icon as the basis for dark** - complementary colors that reflect the default.
- **Alternate icons**: iOS/iPadOS/tvOS/compatible visionOS apps can offer alternate icons via in-app settings. iOS/iPadOS alternates need dark, clear, and tinted variants. Must be related to your app's content - never look like a different app.

## Platform Considerations

### tvOS
- **Include a safe zone** - the system may crop edges as the icon scales and moves during focus. Safe zone varies by image size, layer depth, and motion. Foreground layers crop more than background.

### visionOS
- **Don't add concave shapes or holes to the background layer** - system highlights make them look convex instead of recessed.

### watchOS
- **Don't use black for the background** - lightened black prevents blending with the display background.

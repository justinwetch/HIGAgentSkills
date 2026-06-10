---
topic: images
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "image"
  - "photo"
  - "artwork"
  - "asset"
  - "resolution"
  - "scale factor"
related:
  - sf-symbols
  - icons
  - app-icons
---
# Images

> Deliver artwork at appropriate scale factors so it looks great across all supported devices.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Resolution

A **point** is an abstract measurement unit. On 2D platforms, one point maps to N pixels based on display resolution. In visionOS, a point is angular, scaling with distance.

Scale factors by platform:

| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x, @3x |
| visionOS | @2x or higher |
| macOS, tvOS | @1x, @2x |

Name files with `@1x`, `@2x`, `@3x` suffix and add to Xcode asset catalog.
Design at lowest resolution and scale up. Position vector control points at whole values for clean @1x alignment.

## Formats

| Image type | Format |
|---|---|
| Bitmap/raster | De-interlaced PNG |
| PNG not needing full 24-bit color | 8-bit palette PNG |
| Photos | JPEG (optimized) or HEIC |
| Stereo/spatial photos | Stereo HEIC |
| Flat icons, interface icons, flat artwork | PDF or SVG |

## Best Practices

- Include a color profile with every image.
- Always test images on actual devices — design-time appearance often differs from device rendering.

## Platform Considerations

### tvOS

tvOS uses **layered images** to create the parallax depth effect when elements come into focus.

- App icon **must** use a layered image. Other focusable images (top-shelf, etc.) strongly encouraged.
- Layered images: 2–5 distinct layers with transparency creating depth. Closer layers elevate/scale on focus.
- Use standard views + focus APIs (`FocusState`) for automatic parallax treatment.
- Structure layers: **foreground** (prominent elements, text), **middle** (secondary content, shadows), **background** (opaque backdrop).
- Keep text in foreground for clarity.
- Background layer must be opaque (system error if not).
- Keep parallax subtle — excessive 3D looks unrealistic.
- Maintain a safe zone in foreground layers — content near edges may be cropped during focus scaling.
- Preview layered images in Xcode, Parallax Previewer (macOS), or Parallax Exporter (Photoshop). Preview on actual TV hardware before finalizing.
- Runtime layered images (downloaded, not embedded): use `.lcr` format, generated via `layerutil` from LSR or PSD files.

### visionOS

- Images can be scaled across a wide range; system dynamically scales resolution to match display size/distance.
- Prefer **vector-based art** for 2D images — bitmap may not scale cleanly.
- If using raster: @2x is fine at common distances, but use higher resolution for close viewing. Above @6x, file size and runtime performance suffer — apply high-quality image filtering.
- Use high-quality filtering for high-resolution raster images (`CALayer.filters` where applicable).
- Create a **layered app icon** (2–3 layers) for depth effect on focus.

**Spatial photos and scenes:**
- Use stereo HEIC with spatial metadata for spatial photos. Spatial metadata lets visionOS recognize spatial photos and apply comfort treatments.
- Display spatial photos and scenes in **standalone views** (sheet, window) where possible. Avoid inline display; if stereoscopic images must appear inline, provide generous spacing so eyes can adjust to depth changes.
- Use `ImagePresentationComponent` for spatial photos/scenes.
- Use feathered glass background effect (`GlassBackgroundEffect`) when placing text over spatial photos.
- Avoid adjusting disparity metadata carelessly — can cause visual discomfort.
- Spatial scenes take up to several seconds to generate; use scroll views, pagination, or explicit actions to limit simultaneous scenes.
- In immersive display, prefer minimal UI (single content + small caption + back button).
- Prefer **large, centered** spatial scenes — gives more parallax range.

### watchOS

- Avoid transparency to keep image files small (exception: complication images, menu icons, template images where transparency controls system colorization).
- Use autoscaling PDFs designed for 40mm/@2x. WatchKit scales automatically:

| Screen | Scale |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

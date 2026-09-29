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

Deliver bitmap art at every supported scale factor, in formats suited to each image type.

## Resolution

Points are abstract: display-dependent pixels in 2D, angular (scaling with distance) in visionOS. Scale factor @Nx = N pixels per point.

- **Provide high-resolution assets for all bitmap images, for every device you support**, suffixing asset catalog filenames @1x, @2x or @3x. Guidance values ([more](https://developer.apple.com/design/human-interface-guidelines/layout)):

|Platform|Scale factors|
|---|---|
|iPadOS, watchOS|@2x|
|iOS|@2x and @3x|
|visionOS|@2x or higher|
|macOS, tvOS|@1x and @2x|

- **In general, design at the lowest resolution and scale up.** You might put resizable vector control points on whole values to stay grid-aligned at every scale.

## Formats

|Image type|Recommended format|
|---|---|
|Bitmap or raster|De-interlaced PNG|
|PNG not needing full 24-bit color|8-bit color palette|
|Photos|JPEG, optimized as necessary, or HEIC|
|Stereo or spatial photos|Stereo HEIC|
|Flat artwork, like icons, needing high-resolution scaling|PDF or SVG|

## Best practices

- **Include a [color profile](https://developer.apple.com/design/human-interface-guidelines/color#Color-management) with each image.**
- **Always test images on a range of actual devices.**

## Platform considerations

No additional considerations for iOS, iPadOS or macOS.

### tvOS

Parallax, applied on focus, raises, sways and lights the element; after inactivity, unfocused content dims and the focused element expands. It requires layered images: two to five layers, upper ones rising and scaling over lower ones.

- **Your app icon must be layered.** For other focusable images, including Top Shelf, layers are strongly encouraged but optional.
- You can embed layered images or fetch them at runtime ([guide](https://help.apple.com/itc/parallaxpreviewer/)). Fetched ones must be runtime layered images (`.lcr`), built from LSR or Photoshop files with Xcode's `layerutil`; don't embed them.
- **Display layered images with standard interface elements**; standard views and focus APIs like `FocusState` apply parallax automatically.
- **Identify logical layers**: foreground for prominent elements like a game character or poster text; middle for secondary content and shadows; background as an unobtrusive opaque backdrop.
- **Generally, keep text in the foreground** unless you want to obscure it.
- **Keep the background layer opaque**, or you get an error. Higher layers can vary opacity.
- **Keep layering simple and subtle**; excessive 3D effects can look jarring.
- **Leave a safe zone around foreground layers** for essential content; focus scaling and movement may crop layers (see [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)).
- **Always preview layered images** in Xcode, [Parallax Previewer or Exporter](https://developer.apple.com/design/resources/#parallax-previewer) while designing, readjusting as scaling and clipping occur, and on an actual TV when final.

### visionOS

The system dynamically scales image resolution to the displayed size, which varies far more than elsewhere; image pixels may not map 1:1 to screen pixels.

- **Create a layered app icon**: two to three layers that move at subtly different rates in focus (see [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)).
- **Prefer vector art for 2D images.** Avoid bitmaps; they might look poor scaled up. See [sharp Core Animation layers](https://developer.apple.com/documentation/visionOS/drawing-sharp-layer-based-content).
- **If you need raster images, balance quality with performance.** @2x looks fine at common distances but might not look sharp close up; higher resolutions can help, but each step enlarges the file and may impact runtime performance, especially over @6x. Above @2x, be sure to also apply high-quality filtering (`CALayer` `filters`).

#### Spatial photos and spatial scenes

Apps can display both with RealityKit `ImagePresentationComponent`. Spatial photo: stereo photo plus spatial metadata, like those from iPhone 15 Pro or later or Vision Pro. Spatial scene: 3D image generated from 2D, with head-tracked parallax.

- **Make sure spatial photos render correctly: use stereo HEIC.** With spatial metadata, visionOS recognizes it as spatial and applies treatments that help minimize stereo-viewing discomfort.
- **Prefer the feathered glass background effect (`GlassBackgroundEffect`) for text over spatial photos.**
- **Consider visual comfort when making spatial photos from 2D content**; metadata like [disparity adjustment](https://developer.apple.com/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata) can cause discomfort from certain viewing positions.
- **Display spatial photos and scenes in standalone views** like a sheet or window. Avoid spatial photos inline with other content; if you must show stereoscopic images inline, space them generously.
- **Use spatial scenes for specific moments**, like an explicit create action; each can take up to several seconds to generate. Avoid showing too many at once; use scroll views, pagination or explicit actions.
- **When immersive, prefer minimal UI**, like one item with a small caption, one Back button and swipe navigation.
- **Prefer larger spatial scenes centered in view**; smaller ones give less parallax.

### watchOS

- **In general, avoid transparency to keep files small**; if an image always sits on one solid color, including that background is more efficient. Template images, like complication and menu icons, need transparency to receive color.
- **Use autoscaling PDFs for one asset across screens.** Design for 40mm and 42mm at 2x; WatchKit scales automatically:

|Screen|38mm|40mm|41mm|42mm|44mm|45mm|49mm|
|---|---|---|---|---|---|---|---|
|Scale|90%|100%|106%|100%|110%|119%|119%|

## Resources

Developer: SwiftUI Images, `UIImageView`, `NSImageView`.

Source: [Images](https://developer.apple.com/design/human-interface-guidelines/images), captured 2026-09-12.

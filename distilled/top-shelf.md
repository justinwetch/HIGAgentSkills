---
topic: top-shelf
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/tvos
triggers:
  - "Top Shelf"
  - "TVTopShelfProvider"
  - "hero image"
  - "featured content"
  - "tvOS shelf"
related:
  - live-viewing-apps
  - designing-for-tvos
  - app-icons
---
# Top Shelf

> Top Shelf showcases your tvOS app's content in a rich, engaging experience when your app is selected in the Dock. Supports full-screen video, carousels, rows, and scrolling banners.

**Platforms:** tvOS only

## Best Practices

- **Feature new, unreleased, or recommended content** — not previously purchased/watched items.
- **Personalize**: resume points, targeted recommendations, jump-back-into-active-gameplay.
- **No advertisements or prices** (prominently). Prices OK for purchasable content, but secondary.
- **Dynamic content preferred** over static — layered images, video previews.
- **Static image fallback** (if no full-screen content): 2320×720 pt (4640×1440 px @2x), 16:9, tvOS flips/blurs it.
- **Don't imply interactivity** in a static image — it's not focusable.

## Dynamic Layout Styles

### Carousel Actions
Full-screen video/images with a primary (Play) button and a More Info button. Best for familiar content (e.g., returning shows, user photo albums). Provide a title + optional subtitle.

### Carousel Details
Extends Carousel Actions with plot summary, cast list, metadata. Title appears near screen top. Optional attribution line above title (e.g., "Featured on *My App*").

### Sectioned Content Row
Focused, scrollable row of labeled content thumbnails. Load enough images to fill the full screen width. Individual focus brings up a label. Include at least one label.

**Content row image sizes:**

| Aspect | Actual size (pt) | Focused/safe zone (pt) | Unfocused (pt) |
|---|---|---|---|
| Poster (2:3) | 404×608 | 380×570 | 333×570 |
| Square (1:1) | 608×608 | 570×570 | 500×500 |
| 16:9 | 908×512 | 852×479 | 782×440 |

> Note: Mixed sizes in the same row auto-scale to match the tallest image (e.g., 16:9 scales to 500 pt tall alongside poster/square images).

### Scrolling Inset Banner
Large images (~full screen width), auto-scrolled on a timer. Focus applies lighting effects and 3D parallax on layered images. Circular remote gesture pans between banners.

- **3–8 images** recommended. Fewer than 3 = ineffective; more than 8 = hard to navigate.
- **Text must be baked into the image** — no labels in this layout style. Add text to the accessibility label too.

**Banner image sizes:**

| Aspect | Actual size (pt) | Focused/safe zone (pt) | Unfocused (pt) |
|---|---|---|---|
| Inset banner | 1940×692 | 1740×620 | 1740×560 |

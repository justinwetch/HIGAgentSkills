---
topic: top-shelf
tier: 3
platforms: [tvos]
category: components/tvos
triggers:
  - "Top Shelf"
  - "TVTopShelfProvider"
  - "hero image"
  - "featured content"
  - "tvOS shelf"
  - "Carousel actions"
  - "Carousel details"
  - "sectioned content row"
  - "scrolling inset banner"
  - "Top Shelf static image"
related:
  - live-viewing-apps
  - designing-for-tvos
  - app-icons
  - voiceover
  - images
---

# Top Shelf

The tvOS Home Screen area above the Dock showcasing the focused app's content, optionally as full-screen, swipeable previews. Templates: [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps).

## Best practices

- **Help people jump right into your content.** Carousel actions and details each include two default buttons: primary, intended to start playback, and More Info, intended to open your app's details view.
- **Feature new content**; avoid promoting content people already purchased, rented or watched.
- **Personalize.** You can show targeted recommendations and let people resume playback or gameplay.
- **Avoid showing advertisements or prices.** Purchasable content is fine, but prefer focusing on new content; consider showing prices only when people show interest.
- **Showcase dynamic content.** You can use static images if necessary, but people typically prefer dynamic, newest or highest rated content; prefer [layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images).
- **Without the recommended full-screen content, supply at least one static fallback image** (guidance: 2320x720 pt, 4640x1440 px @2x); tvOS flips and blurs it to fit 1920 px wide at 16:9.
- **Avoid implying interactivity in a static image**; it isn't focusable.

## Dynamic layouts

### Carousel actions

Full-screen video and images; works especially well for content people already know, like their photos.

**Provide a title**, succinct. If necessary, add a brief subtitle, like an album's date range.

### Carousel details

Carousel actions plus details that help people choose, like a plot summary.

**Provide a title identifying the currently playing content**, shown near the top. Above it, you can add a succinct phrase or app attribution ("Featured on *My App*").

### Sectioned content row

A scrollable row of focusable content, suited to recent, new or favorite items. The focused item shows a label (multiple are configurable) and animates with small Touch-surface movements.

**Fill a complete row**: at minimum, images spanning the full screen width, plus at least one label.

### Scrolling inset banner

Near-full-width images auto-scroll on a timer, looping, until one is focused, when small circular Touch-surface gestures apply the system focus effect (3D with layered images) and swipes pan between banners. Use for rich, captivating content.

- **Provide three to eight images**; more than eight can make a specific image hard to reach.
- **If you need text, add it to your image**; no labels appear. In layered images, consider a dedicated top text layer. Also put the text in the accessibility label for VoiceOver.

### Image sizes

|Image, pt (@2x px)|Actual|Focused/safe zone|Unfocused|
|---|---|---|---|
|Banner|1940x692 (3880x1384)|1740x620 (3480x1240)|1740x560 (3480x1120)|
|Row: poster (2:3)|404x608 (808x1216)|380x570 (760x1140)|333x570 (666x1140)|
|Row: square (1:1)|608x608 (1216x1216)|570x570 (1140x1140)|500x500 (1000x1000)|
|Row: 16:9|908x512 (1816x1024)|852x479 (1704x958)|782x440 (1564x880)|

Row = sectioned content row; banner = scrolling inset banner. **Be aware of scaling when mixing row sizes**: images automatically scale up to the tallest one's height if necessary (16:9 becomes 500 px high beside poster or square).

## Platform considerations

Not supported in iOS, iPadOS, macOS, visionOS or watchOS.

## Resources

Source: [Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf), captured 2026-09-12.

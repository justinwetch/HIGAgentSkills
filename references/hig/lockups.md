---
topic: lockups
tier: 4
platforms: [tvos]
category: components/tvos
triggers:
  - "lockup"
  - "TVCardView"
  - "caption button"
  - "monogram"
  - "poster tvOS"
  - "TVLockupView"
  - "TVLockupHeaderFooterView"
  - "TVCaptionButtonView"
  - "TVMonogramContentView"
  - "TVPosterView"
related:
  - designing-for-tvos
  - focus-and-selection
---

# Lockups

Lockups combine separate views into one interactive unit in tvOS. Each consists of a content view, a header above the main content, and a footer below it; all three expand and contract together as the lockup receives focus.

## Best practices

- **Allow adequate space between lockups.** A focused lockup expands; leave enough room to avoid overlapping or displacing neighboring lockups.
- **Use consistent sizes within a row or group.** Matching widths and heights make button groups and rows of content images more visually appealing.

## Types

| Type | Structure and use |
|---|---|
| Card | Header, footer, and content view; presents ratings and reviews for media items. |
| Caption button | Button containing either an image or text, with optional title and subtitle beneath. On focus, tilt with the swipe motion: vertically aligned buttons tilt up/down; horizontally aligned buttons tilt left/right; grid buttons tilt both vertically and horizontally. |
| Monogram | Circular picture of a person plus name; usually identifies cast and crew for a media item. If no image is available, show the person’s initials; **prefer images**, which create a more intimate connection. |
| Poster | Image with optional title and subtitle hidden until focus. Posters can be any size, but size them appropriately for their content. |

A focused caption button expands slightly and appears to float above the background.

## Developer references

- [`TVLockupView`](https://developer.apple.com/documentation/tvuikit/tvlockupview) is a focusable view for main content (such as a movie poster) with optional header and footer; [`TVLockupHeaderFooterView`](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) contains header/footer information.
- [`TVCardView`](https://developer.apple.com/documentation/tvuikit/tvcardview) applies a focus motion effect to its subviews; [`TVCaptionButtonView`](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview) is a button-like interactive view; [`TVMonogramContentView`](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview) contains a circular person image or initials; [`TVPosterView`](https://developer.apple.com/documentation/tvuikit/tvposterview) is optimized for an image, header, and footer.

## Platform considerations

Lockups aren’t supported in iOS, iPadOS, macOS, visionOS, or watchOS.

Source: [Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups), captured 2026-09-12.

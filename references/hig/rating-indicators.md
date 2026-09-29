---
topic: rating-indicators
tier: 4
platforms: [macos]
category: components/controls
triggers:
  - "rating indicator"
  - "star indicator"
  - "level indicator stars"
  - "NSLevelIndicator.Style.rating"
related:
  - ratings-and-reviews
---

# Rating indicators

A rating indicator uses horizontally arranged graphical symbols—stars by default—to communicate a ranking level. It doesn’t display partial symbols: it rounds the value to complete symbols. Symbols remain equally spaced and don’t expand or shrink to fit the component’s width.

## Best practices

- In a list of ranked items, let people change an individual item’s ranking inline without navigating to a separate editing screen.
- If replacing stars with a custom symbol, make its purpose clear. The star is a recognizable ranking symbol; people may not associate another symbol with a rating scale.

## Platform considerations

No additional considerations for macOS. Rating indicators aren’t supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

## Resources

Related: [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)

Developer documentation: [`NSLevelIndicator.Style.rating`](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) — AppKit; Objective-C alias: `NSLevelIndicatorStyleRating`.

Source: [Apple Human Interface Guidelines — Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators) (captured 2026-09-12).

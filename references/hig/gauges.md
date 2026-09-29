---
topic: gauges
tier: 3
platforms: [ios, ipados, macos, visionos, watchos]
category: components/controls
triggers:
  - "gauge"
  - "circular gauge"
  - "linear gauge"
  - "level indicator"
related:
  - ratings-and-reviews
  - rating-indicators
---

# Gauges

A gauge (`Gauge`) shows a value's position in a range along a circular or linear path.

## Anatomy

- **Standard** gauges mark the value with an indicator; **capacity** gauges fill to it.
- The **accessory** variant, available for both shapes and styles, resembles watchOS complications. It works well in iOS Lock Screen widgets and anywhere you want a complication look.

## Best practices

- **Write succinct labels for the current value and both endpoints.** Not every style shows all labels; VoiceOver reads the visible ones.
- **Consider a gradient fill that conveys the gauge's purpose**, like red to blue for hot to cold.

## Platform considerations

No additional considerations for iOS, iPadOS, visionOS or watchOS. Not supported in tvOS.

### macOS

Level indicators (`NSLevelIndicator`) also show a value in a range, in a capacity, rating or, rarely, relevance style.

- **Capacity** indicators are horizontal: continuous (a translucent track filled by a solid bar) or discrete (equal rectangular segments, one per unit of total capacity, each filled completely, never partially).
- **Consider continuous for large ranges**; discrete segments can get too small to be useful.
- **Consider changing the capacity fill color (default green for both styles) to flag significant parts of the range**, when the value reaches levels like very low, very high or just past the middle. Recolor the entire indicator, or use the tiered state for a color sequence in one indicator.
- **Relevance** (rarely used): a shaded horizontal bar, e.g. in search results people sort or compare.

## Resources

Source: [Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges), captured 2026-09-12.

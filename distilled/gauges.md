---
topic: gauges
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "gauge"
  - "Gauge"
  - "circular gauge"
  - "linear gauge"
  - "level indicator"
related:
  - progress-indicators
  - sliders
  - activity-rings
---
# Gauges

> A gauge displays a specific numerical value within a range, optionally with context labels and color gradients.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

**Anatomy:** circular or linear path representing a range. Two display styles:
- **Standard** — indicator dot/marker at the current value.
- **Capacity** — fill that stops at the current value.

An *accessory* variant mimics watchOS complication appearance — useful in iOS Lock Screen widgets or other complication-style contexts.

## Best Practices

- **Succinct labels for current value and both endpoints** — even when not all labels display visually, VoiceOver reads them for accessibility.
- **Gradient fill to reinforce meaning** — e.g., red→blue for hot→cold temperature range.

## Platform Considerations

### macOS

macOS additionally supports **level indicators** — three configurable styles:

**Capacity (2 sub-styles):**
- *Continuous* — horizontal translucent track with a solid fill bar.
- *Discrete* — a horizontal row of equal-sized rectangular segments; segments fill completely (never partially).
  - Note: for large ranges, the continuous style is better (discrete segments would be too small).
- **Change fill color at meaningful thresholds** — default fill is green. You can change color at specified levels (very low, very high, etc.) or use tiered state to show multiple colors in one indicator.

**Rating** — uses stars (or custom symbols) for ranking. See rating-indicators.

**Relevance** (rarely used) — shaded horizontal bar communicating relevancy level. Useful in search result lists for sorting/comparing multiple items.

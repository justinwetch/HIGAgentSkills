---
topic: charting-data
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/data
triggers:
  - "data chart design"
  - "charting design"
  - "data story"
  - "chart accessibility"
related:
  - charts
  - accessibility
---
# Charting Data

> Guidelines for deciding when and how to present data in a chart.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Not every dataset needs a chart. If you only need to provide raw data — without conveying insights or supporting analysis — use a list or table (scrollable, searchable, sortable) instead.

## When to Use a Chart

- Analyzing trends from historical or predicted values
- Visualizing a changing quantity's current state
- Comparing items or the same item across multiple categories

**Use a chart to highlight important information** — charts are visually prominent and draw attention. Use that prominence to communicate something meaningful.

## Best Practices

- **Keep charts simple; let people opt into details** — don't pack in all available data. Too much data obscures relationships and is overwhelming. Provide progressive disclosure (e.g., let people choose scope or detail level). Consider a series of chart versions, each revealing more functionality.
- **Prefer common chart types** (bar, line, scatter) — familiar types require no learning curve. For novel chart types, teach people how to read them (e.g., Activity rings animate individually on first pairing to show what each ring means).
- **Multi-level data analysis** — macro (totals, averages), mid-level (subsets), micro (individual values). Displaying data from multiple perspectives encourages engagement.
- **Add descriptive text** — title, subtitle, annotations emphasize key information and provide glanceable headlines (e.g., Weather: "Chance of light rain in the next hour" above the hourly chart). Descriptive text aids accessibility but doesn't replace accessibility labels.
- **Match chart size to purpose** — large enough to read details and support interaction; small charts work for glanceable summaries or previews of a full chart.
- **Consistent style across multiple charts** — if multiple charts serve similar purposes, use the same type, colors, and style. Deviate only to signal meaningful differences.
- **Maintain continuity across charts for the same dataset** — same type, colors, annotations, layout. Example: Health Trends shows small charts in a consistent style; tapping to expand preserves the same visual language.
- **Make every chart accessible** — see charts#Enhancing-the-accessibility-of-a-chart for accessibility label and Audio Graphs guidance.

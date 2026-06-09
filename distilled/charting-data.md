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

Not every dataset needs a chart. If you only need to provide raw data without conveying insights or supporting analysis, use a scrollable, searchable, sortable list or table instead.

## When To Use A Chart

- Analyzing trends from historical or predicted values.
- Visualizing a changing quantity's current state.
- Comparing items or the same item across multiple categories.
- **Use charts to highlight important information** - charts are visually prominent, so use that prominence to communicate something meaningful.

## Best Practices

- **Keep charts simple; let people opt into details** - too much data obscures relationships and becomes overwhelming. Reveal scope/detail progressively.
- **Make every chart accessible** - provide accessibility labels that describe chart values/components and accessibility elements that help people interact with the chart.
- **Prefer common chart types** - people are familiar with bar and line charts. For novel charts, teach people how to read them.
- **Analyze data at multiple levels** - macro (totals/averages), mid-level (subsets), and micro (individual values) can each reveal useful detail.
- **Add descriptive text** - titles, subtitles, annotations, and concise summaries emphasize key information. They help accessibility but do not replace accessibility labels.
- **Match chart size to purpose** - large enough for details and interaction; small charts work for glanceable summaries or previews.
- **Use consistent style across related charts** - same type, colors, annotations, layout, and descriptive text when charts show the same dataset or purpose.

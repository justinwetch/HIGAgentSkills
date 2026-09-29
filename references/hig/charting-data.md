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

# Charting data

A chart presents data graphically to communicate complex information without much text. If you only need to provide data, not information about it or analysis, consider a list or table people can scroll, search and sort.

## Best practices

- **Use a chart to highlight important information about a dataset**, clearly communicating what people can learn.
- **Keep a chart simple, letting people choose when they want details.** For a lot of data or functionality, consider revealing it gradually, like choosable detail levels or data subsets. You might teach an interactive chart with several versions, each adding functionality.
- **Make every chart accessible.** It's crucial to provide accessibility labels for chart values and components, and accessibility elements for interaction.

## Designing effective charts

- **In general, prefer common chart types**, such as bar and line charts, which people more likely already know how to read.
- **Help people interpret a novel chart**, as Activity does by animating each ring individually at Watch pairing.
- **Examine the data at multiple levels for details to display:** summaries like totals, useful subsets, specific values or items.
- **Add descriptive text.** Titles, subtitles and annotations emphasize key information and can highlight actionable takeaways. A brief headline or summary aids glanceability but doesn't replace accessibility labels.
- **Match chart size to its functionality, topic and level of detail.** In general, make it large enough for needed details and intended interactivity, always keeping details, labels and annotations easy to read. You might use a small chart for glanceable item information or to preview a larger version in another view.
- **Prefer consistency across charts, deviating only to highlight meaningful differences.** Different types or styles for similar-purpose charts generally imply they're unrelated.
- **Maintain continuity among charts of the same dataset.** It's important to use one chart type and consistent colors, marks, annotations, layouts and descriptive text, including in a small chart's expanded version.

## Platform considerations

No additional platform considerations.

## Resources

Developer: Swift Charts (`Charts`).

Source: [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data), captured 2026-09-12.

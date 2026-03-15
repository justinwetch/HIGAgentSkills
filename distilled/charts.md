---
topic: charts
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/content
triggers:
  - "chart"
  - "Swift Charts"
  - "bar chart"
  - "line chart"
  - "data visualization"
  - "graph"
related:
  - charting-data
  - accessibility
---
# Charts

> Organize data in a chart to communicate information with clarity and visual appeal.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Core Concepts

- **Mark** — visual representation of a single data value. Mark types: bar, line, point, and others.
- **Plot area** — region containing all marks.
- **Scale** — maps data values (numbers, dates, categories) to visual attributes (position, color, height).
- **Axis** — defines the frame of reference; typically one horizontal + one vertical. Can include ticks and grid lines.
- **Ticks** — reference points on an axis for important values (0%, 50%, 100%).
- **Grid lines** — extend from ticks across the plot area to help estimate values.
- **Labels** — name axes, ticks, grid lines, or marks.
- **Legend** — describes properties not tied to position (e.g., color or shape representing categories).

## Mark Types

| Type | Use |
|---|---|
| Bar | Comparing values across categories or parts of a whole; sums over time |
| Line | Trends over time; slope communicates rate of change |
| Point | Individual values; relationships between two properties; outliers, clusters |

**Combine mark types for clarity** — e.g., line chart + point marks to highlight individual values within a trend.

## Axes

- **Fixed range** when min/max have absolute meaning (battery: always 0–100%).
- **Dynamic range** when data varies widely and you want marks to fill the plot area (e.g., Health Steps chart: Y-axis upper bound adapts to the time period's max).
- **Lower bound:** bar charts work well with 0 (visual height comparison). For data like heart rate, a 0 lower bound can obscure meaningful differences — use a dynamic lower bound.
- **Familiar tick sequences** — 0, 5, 10, 15 is familiar; 1, 6, 11, 16 is not. People parse familiar sequences faster.
- **Appropriate grid-line density and weight** — too many: overwhelming; too few: hard to estimate. Consider context and whether interaction exposes individual values (if so, fewer grid lines are fine).

## Descriptive Content

- **Write descriptions before people view the chart** — information-rich titles/labels give context upfront, especially critical for VoiceOver and cognitive accessibility.
- **Summarize the main message** — e.g., Weather shows "Expected precipitation next hour" above the chart. People grasp the insight without analyzing the data.

## Best Practices

- **Consistent visual hierarchy** — data most prominent; axes and descriptions provide context without competing.
- **Maximize plot area width in compact environments** — short vertical-axis labels; describe units in titles; optionally shift Y-axis to trailing side.
- **Accessibility is required** — support VoiceOver + Audio Graphs. Swift Charts auto-generates accessibility elements per mark + Audio Graphs default. Customize with chart title and summary.
- **Don't require interaction to reveal critical info** — interaction (e.g., scrubbing a timeline) is an enhancement, not the only way to get data.
- **Expand hit targets** — small marks are hard to tap; expand the hit region to the full plot area for scrubbing interactions.
- **Keyboard/Switch Control navigation** — use accessibility APIs to define a logical path (e.g., along X axis), or let people move among value subsets rather than visiting every mark.
- **Animate chart changes** — helps people notice axis/mark changes; also communicate changes through accessibility labels for those who disable animations.
- **Align charts with surrounding UI** — align leading edge with other views. Place vertical grid labels on their trailing side; consider moving Y axis to the trailing side.

## Color

- **Don't rely solely on color** — also use shapes/patterns to distinguish data series. Example: Health uses two shapes for blood pressure components, not just two colors.
- **Add visual separators between contiguous color areas** — e.g., between stacked bar segments of different colors.

## Accessibility Labels (Charts)

- **Per-mark vs. group labels** — decide based on chart purpose. High-density charts may use group labels; interactive charts need per-mark labels.
- **Single label for thumbnail charts** that open a full view — acceptable.
- Label guidelines:
  - Include context for each value (date, location) not just the number.
  - Use actual values, not subjective terms (not "rapidly increased" — use the actual value change).
  - Avoid ambiguous formats: "June 6" > "6/6"; spell out units ("60 minutes" not "60m").
  - Describe what data represents, not its visual appearance (don't say "the red bar").
  - Consistent axis reference order throughout the app.
- **Hide visible axis/tick labels from assistive technologies** — VoiceOver gets this info from accessibility labels + Audio Graphs.

## Platform Considerations

### watchOS

- **Avoid complex chart interactions** — glanceable information at small size is the goal. Use iPhone/iPad app for detailed charts and advanced interactions. Example: Watch Heart Rate shows today's data; iPhone Health shows multiple time periods + individual mark inspection.

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

A chart highlights a few key pieces of information in a dataset to help people gain insights and make decisions.

## Anatomy

- **Mark:** represents one data value; the mark type (bar, line, point) sets the chart style. Marks sit in the *plot area*. A *scale* maps values to attributes like position, color or height.
- **Axis:** a frame of reference for a variable like time, amount or category. *Ticks* locate important values; *grid lines* extend from ticks across the plot area.
- **Descriptive content:** labels, accessibility labels, titles, subtitles, annotations and, when needed, a legend for non-position properties such as color or shape.

## Marks

**Choose a mark type based on the information you want to communicate.**
- *Bar:* compare categories or parts of a whole; for change over time, best when each value is a sum (steps per day).
- *Line:* shows change over time; connects one series, and slope shows magnitude of change and trend.
- *Point:* distinct values; relates two properties and reveals outliers and clusters.

**Consider combining mark types when it adds clarity**, such as points on a line.

## Axes

- **Use a fixed or dynamic axis range depending on the chart's meaning.** Consider fixed bounds when specific minimum and maximum values are meaningful for all data (battery 0-100%). Consider dynamic bounds when values vary widely and marks should fill the plot area.
- **Define the lower bound based on mark type and chart usage.** Zero often works for bar charts; it can sometimes hide meaningful differences far from zero (resting vs. active heart rate).
- **Prefer familiar sequences in tick and grid-line labels** (0, 5, 10, not 1, 6, 11).
- **Tailor grid-line and label density and weight to the chart's use cases**: its context, interactions and tasks. Too many overwhelm; too few make values hard to estimate. If people can inspect points, you might use fewer grid lines and light label colors.

## Descriptive content

- **Write descriptions that help people understand what a chart does before they view it**, especially for VoiceOver users and people with certain cognitive disabilities.
- **Summarize the chart's main message** so people get key information without examining details (a title and subtitle describing next-hour precipitation).

## Best practices

- **Establish a consistent visual hierarchy.** Typically the data is most prominent; descriptions and axes add context without competing.
- **In a compact environment, maximize plot-area width.** Keep vertical-axis labels as short as clarity allows. Consider stating units elsewhere (title) and placing a long axis label inside the plot area when it doesn't obscure important information.
- **Make every chart in your app accessible**, including VoiceOver support. Beyond accessibility labels, you can use Audio Graphs (tones representing values and trend, plus text summaries).
- **Let people interact with the data when it makes sense, but don't require interaction to reveal critical information.**
- **Make it easy for everyone to interact with a chart.** When marks are too small to target, consider making the whole plot area the hit target for scrubbing.
- **Make an interactive chart easy to navigate with keyboard commands (including Full Keyboard Access) or Switch Control.** By default these tend to visit elements linearly (such as in data order). To customize, use accessibility APIs (such as `accessibilityRespondsToUserInteraction(_:)`) for a logical, predictable path (along the X axis), or, especially for very large datasets, move focus among subsets of values. Both can also improve VoiceOver, even in noninteractive charts.
- **Help people notice important changes** to marks or axes. Animation helps, but also highlight changes in other ways for VoiceOver users and people who turn off animations (`UIAccessibility.Notification`, `NSAccessibility.Notification`).
- **Align a chart with surrounding interface elements**, often by leading edge. To keep it clean, put vertical grid-line labels on their trailing side, and also consider moving the Y axis to the trailing side. Anchor an unassociated-looking label to its grid line with a tick.

## Color

- **Avoid relying solely on color to differentiate data or communicate essential information.** Supplement with shapes or patterns (Health uses two point shapes for systolic and diastolic).
- **Add visual separation between contiguous areas of color**, such as separators between segments of a stacked bar.

## Enhancing the accessibility of a chart

Swift Charts provides default Audio Graphs and a default accessibility element describing each mark's (or group's) value.

- **Consider using Audio Graphs to give VoiceOver users more information**; customize the default with a chart title and descriptive summary. Without Audio Graphs, you need to provide an overview: chart type, what each axis represents, and details like axis bounds.
- **Important:** A chart often needs an accessibility label for each important or interactive element, not one like an image. Decide per purpose and mark density whether to describe each mark or groups. A single high-level label can make sense, such as for a small chart in a button that reveals a detailed version.
- **Write accessibility labels that support the chart's purpose.** Maps' elevation chart summarizes changes over route portions; Health's Steps chart labels each bar because actual counts are the purpose.

For label content:
- **Prioritize clarity and comprehensiveness.** Give a value context (date, location) without repeating what's available elsewhere, such as an axis name that Audio Graphs or your overview provides. Context first, then succinct details.
- **Avoid subjective terms** (rapidly, gradually, almost); use actual values.
- **Avoid ambiguous formats and abbreviations:** "June 6", not "6/6"; "60 minutes", not "60m".
- **Describe what details represent, not what they look like** (the series, not its color).
- **Be consistent throughout your app when referring to a specific axis**, such as always mentioning X first.

**Hide visible axis and tick text labels from assistive technologies**, since accessibility labels and Audio Graphs supply values and trends.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS or visionOS.

### watchOS

**In general, avoid requiring complex chart interactions.** As much as possible, prefer at-a-glance information and simple interactions that add value. If your app exists on another platform, consider offering more detail and interaction there.

## Resources

Developer: `Charts` (Swift Charts), Audio Graphs, `accessibilityRespondsToUserInteraction(_:)`, `UIAccessibility.Notification`, `NSAccessibility.Notification`.

Source: [Charts](https://developer.apple.com/design/human-interface-guidelines/charts), captured 2026-09-12.

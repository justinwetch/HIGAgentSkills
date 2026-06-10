---
topic: progress-indicators
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/status
triggers:
  - "progress bar"
  - "spinner"
  - "activity indicator"
  - "ProgressView"
  - "UIProgressView"
  - "UIActivityIndicatorView"
  - "UIRefreshControl"
  - "NSProgressIndicator"
  - "determinate"
related:
  - loading
  - feedback
---
# Progress Indicators

> Progress indicators tell people an app isn't stalled while loading content or performing long operations.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Transient — appear during operations, disappear on completion.

Developer APIs: `ProgressView`, `UIProgressView`, `UIActivityIndicatorView`, `UIRefreshControl`, `NSProgressIndicator`.

**Two types:**
- **Determinate** — task has a known duration; fills a linear (progress bar) or circular track as the task completes.
- **Indeterminate** — duration unknown; animated spinner (all platforms) or indeterminate bar (macOS).

## Best Practices

- **Prefer determinate** — helps people decide whether to wait, pause, restart, or abandon.
- **Be accurate with advancement** — uneven progress (90% in 5s, last 10% in 5 min) feels deceptive and causes anxiety.
- **Keep indicators animated** — stationary indicators suggest a stall or freeze. If the process stalls, provide actionable feedback.
- **Switch indeterminate → determinate when possible** — as soon as duration is known, upgrade to a progress bar.
- **Don't switch between circular and bar styles** — different shapes and sizes; transitions confuse people.
- **Descriptions: accurate and succinct** — avoid vague terms like "Loading" or "Authenticating."
- **Consistent location** — pick a spot and use it consistently; helps people find status information reliably.
- **Cancel/Pause buttons:**
  - Include Cancel if interruption has no side effects.
  - Include Pause (in addition to Cancel) if cancellation causes data loss (e.g., partially downloaded file).
  - If canceling causes data loss: show an alert with a confirm/resume option.

## Platform Considerations

### iOS, iPadOS

**Refresh control (pull-to-refresh):**
- Specialized activity indicator shown when people drag a table/scroll view down.
- **Perform automatic updates too** — don't make people manually trigger every refresh.
- Optional title: use it only for value-adding information (e.g., "Last updated: 2 minutes ago"), not instructions. Most of the time no title is needed.

### macOS

- Indeterminate progress can be a bar or circular spinner; both are animated.
- **Prefer a spinner for background operations or constrained space** — small and unobtrusive; good alongside controls (next to a button or inside a text field).
- **No label on a spinner** — people already initiated the process; labeling is usually unnecessary.

### watchOS

- Default color: white over scene background. Set a tint color to change.

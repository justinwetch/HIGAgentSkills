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

# Progress indicators

Progress indicators show an app isn't stalled during loading or lengthy operations, appearing only while one is ongoing (`ProgressView`).

- **Determinate**, for a well-defined duration, like a file conversion. Bars fill leading to trailing; circles, clockwise.
- **Indeterminate** (*activity indicator*, *spinner*), for unquantifiable tasks, like loading or synchronizing complex data. All platforms spin a circle; macOS also offers a bar.

## Best practices

- **When possible, use a determinate indicator** so people can estimate the wait.
- **Report determinate advancement as accurately as possible.** Consider evening out the pace; 90% in 5 s then 10% in 5 min can seem stalled.
- **Keep indicators moving.** If a process stalls, explain the problem and what people can do.
- **When possible, switch a progress bar from indeterminate to determinate.**
- **Don't switch from the circular style to the bar style.**
- **If it's helpful, add an accurate, succinct description.** Avoid vague terms like *loading* or *authenticating*.
- **Display progress indicators in a consistent location.**
- **When it's feasible, let people halt processing**: include Cancel if interrupting is harmless; if not (like losing a partial download), adding Pause can be useful.
- **Let people know when halting has a negative consequence.** If canceling loses progress, an alert to confirm or resume helps.

## Platform considerations

No additional considerations for tvOS or visionOS.

### iOS, iPadOS

A refresh control (`UIRefreshControl`) is a hidden activity indicator revealed by dragging down a view, typically a table view, to reload.
- **Perform automatic content updates** regularly; don't make people initiate every update.
- **Supply a short title only if it adds value** about the refreshed content, like last-update time. Don't use it to explain how to refresh.

### macOS

- **Prefer a spinner for background operations or constrained space**, like server fetches, within a text field or next to a button.
- **Avoid labeling a spinner**; it typically follows a person's action.

### watchOS

Indicators default to white over the scene's background; setting a tint color changes this.

## Resources

Developer: `UIProgressView`, `UIActivityIndicatorView`, `NSProgressIndicator`.

Source: [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), captured 2026-09-12.

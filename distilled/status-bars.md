---
topic: status-bars
tier: 4
platforms: [ios, tvos, visionos]
category: components/system
triggers:
  - "status bar"
  - "status bar color"
  - "status bar style"
  - "UIStatusBar"
related:
  - layout
  - designing-for-ios
---
# Status Bars

> The status bar displays device state info (time, carrier, battery) at the top of the screen. Don't obscure or permanently hide it.

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

Status bar background is transparent by default — content shows through.

## Best Practices

- **Don't let interactive controls show behind the status bar** — they'll look tappable but won't respond. Use a scroll edge effect (blurred view) to keep the status bar readable.
- **Temporarily hide for full-screen media** — immersive content (photos, video) benefits from hiding the status bar. Provide a simple, discoverable gesture to restore it (e.g., single tap).
- **Never permanently hide the status bar** — people need it to check time and connectivity without leaving your app.

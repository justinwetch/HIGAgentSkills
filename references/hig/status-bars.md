---
topic: status-bars
tier: 4
platforms: [ios, ipados]
category: components/system
triggers:
  - "status bar"
  - "status bar color"
  - "status bar style"
  - "UIStatusBar"
  - "UIStatusBarStyle"
  - "preferredStatusBarStyle"
  - "ScrollEdgeEffectStyle"
  - "UIScrollEdgeEffect"
related:
  - layout
  - designing-for-ios
---
# Status bars

A status bar runs along the upper edge and reports device state: time, cellular carrier, Wi‑Fi, and battery.

## Best practices

- Keep content beneath it visually obscured and the status information readable. Its default transparent background can reveal controls that appear interactive even though people can’t use them; prefer a blurred scroll-edge effect via [`ScrollEdgeEffectStyle`](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) or [`UIScrollEdgeEffect`](https://developer.apple.com/documentation/uikit/uiscrolledgeeffect).
- Consider temporarily hiding it for immersive full-screen media (Photos hides it while browsing full-screen photos); if hidden, let people restore it with a simple, discoverable gesture such as a single tap.
- Avoid hiding it permanently: otherwise people must leave the app to check the time or Wi‑Fi.

**Scope:** applies to iOS and iPadOS only; not supported in macOS, tvOS, visionOS, or watchOS.

Developer references: [`UIStatusBarStyle`](https://developer.apple.com/documentation/uikit/uistatusbarstyle) (status-bar style constants) and [`preferredStatusBarStyle`](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) (view controller’s preferred style; source metadata marks it deprecated). Source: [Apple HIG — Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars), captured 2026-09-12.

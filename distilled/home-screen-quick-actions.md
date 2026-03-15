---
topic: home-screen-quick-actions
tier: 3
platforms: [ios, tvos, visionos]
category: patterns/system
triggers:
  - "quick action"
  - "3D Touch"
  - "haptic touch"
  - "long press icon"
  - "UIApplicationShortcutItem"
related:
  - app-icons
  - app-shortcuts
---
# Home Screen Quick Actions

> Home Screen quick actions give people fast access to key tasks directly from the Home Screen icon — via touch-and-hold (or 3D Touch press).

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

Each quick action includes a **title**, **interface icon** (left or right depending on icon position on screen), and an **optional subtitle**. Title and subtitle are always left-aligned in LTR languages. Maximum of **4 quick actions** per app.

## Best Practices

- **High-value, compelling tasks only** — e.g., Maps' "Directions Home." People expect at least one useful action from every app.
- **Dynamic actions are great; keep changes predictable.** Update based on location, recent activity, time of day, or settings changes — but don't surprise people.
- **Succinct title** — instantly communicates the result (e.g., "Directions Home," "New Message"). No app name, no extraneous info. Keep text short (localization aware, avoid truncation). Use subtitle for extra context only when needed.
- **SF Symbols for icons** — prefer standard SF Symbols. If you design a custom icon, use the Quick Action Icon Template from Xcode iOS app resources.
- **No emoji** — quick action icons are monochromatic and adapt to Dark Mode; emoji don't.

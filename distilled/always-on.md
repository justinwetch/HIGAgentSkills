---
topic: always-on
tier: 3
platforms: [macos, tvos]
category: patterns/system
triggers:
  - "Always On"
  - "always-on display"
  - "AOD"
  - "wrist down"
  - "low power display"
related:
  - designing-for-watchos
  - complications
---
# Always On

> On Always On displays, the system dims the screen and reduces motion when the device is set aside (iPhone) or the wrist is lowered (Apple Watch), while continuing to show glanceable info.

**Platforms:** iOS (iPhone 14 Pro and later), watchOS *(not iPadOS, macOS, tvOS, visionOS)*

**iPhone**: Displays Lock Screen items (widgets, Live Activities) when set face-up without interaction.
**Apple Watch**: Dims and continues showing the frontmost app or a background session app.

Both: Display notifications in Always On state. Tap display to exit.

## Best Practices

- **Redact sensitive information** — bank balances, health data, and sensitive notification content must be hidden from casual observers.
- **Keep non-sensitive glanceable info visible** — pace, heart rate during workout; flight arrival; ride-share arrival. Users can turn off Always On if they want nothing visible.
- **Dim nonessential content** — increase dimming on secondary text, images, color fills to emphasize key info. Remove decorative images or large color areas; use dimmed colors instead.
- **Maintain consistent layout** — avoid distracting changes on Always On start/end. Transition interactive elements to an unavailable appearance rather than removing them. Within Always On, make updates infrequent and subtle (e.g., sports app updates score, not play-by-play).
- **Gracefully transition motion** — smoothly finish current animation before entering rest state; don't abruptly stop.

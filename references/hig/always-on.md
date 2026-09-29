---
topic: always-on
tier: 3
platforms: [ios, watchos]
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

Always On can keep showing dimmed, low-motion content after people stop interacting.

- iPhone 14 Pro/Pro Max, idle face up: Lock Screen items like widgets and Live Activities.
- Apple Watch, wrist dropped: dims, still showing your app if frontmost or running a background session.
- Both show notifications; tapping the display exits Always On.

## Best practices

- **Hide sensitive information**, like bank balances or health data, including in [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications).
- **Keep other personal information glanceable when it makes sense**, like workout heart rate or flight arrival.
- **Keep important content legible; dim nonessential content.** You can dim secondary text, images and fills further; consider swapping rich images and large color areas for dimmed colors. E.g., remove row backgrounds and dim item details so titles stand out.
- **Maintain a consistent layout.** Avoid distracting changes when Always On begins or ends, and while it runs (especially on iPhone). When it begins, prefer showing interactive components as unavailable; don't just remove them. Aim for infrequent, subtle updates.
- **Ease motion to rest; don't stop it instantly.**

## Platform considerations

iOS and watchOS only; no additional considerations.

Source: [Always On](https://developer.apple.com/design/human-interface-guidelines/always-on), captured 2026-09-12.

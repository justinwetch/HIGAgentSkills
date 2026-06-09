---
topic: launching
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "launch"
  - "launch screen"
  - "splash screen"
  - "app startup"
  - "cold start"
  - "state restoration"
related:
  - onboarding
  - loading
---
# Launching

> A streamlined launch experience lets people start using your app immediately.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Launch instantly** — target within a couple of seconds.
- **Restore previous state on restart** — scroll position, window position and size, last location in the app. Avoid making people retrace steps.
- **Use the launch screen only on iOS, iPadOS, tvOS** — macOS, visionOS, and watchOS don't require them.
- **Splash screens:** if needed, show as the first step of onboarding, or immediately after launch if there's no onboarding. Keep brief.

## Launch Screens (iOS, iPadOS, tvOS only)

Launch screens serve one purpose: creating the perception of fast startup. They are **not** a branding opportunity.

- Design nearly identical to your app's first screen — jarring transitions undermine the fast-launch illusion.
- Use only a solid background color if your first screen transitions from a solid color.
- **No text** — it won't be localized.
- **No logos or branding** — unless they're a fixed part of the actual first screen.
- Launch screens are **static** (tvOS note: unlike the rest of tvOS UI).

## Platform Considerations

### iOS, iPadOS

- Launch in the device's current orientation. If your app is orientation-locked, launch in that orientation and handle either left/right landscape rotation correctly.

### tvOS

- In live-viewing apps, consider auto-starting playback after a few seconds of inactivity — people come to watch content.

### visionOS

- Even for fully immersive apps, **consider launching in the Shared Space first** — open a window to provide context and give the app time to load. Let people choose when to transition to a Full Space.

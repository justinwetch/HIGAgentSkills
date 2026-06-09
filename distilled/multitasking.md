---
topic: multitasking
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: patterns/system
triggers:
  - "multitasking"
  - "Picture in Picture"
related:
  - layout
  - windows
  - playing-video
---
# Multitasking

> Multitasking lets people switch quickly between apps and perform tasks simultaneously.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

Most apps must support multitasking. Exceptions: some games, visionOS apps running in a Full Space.

## Best Practices

- **Pause on switch-away, resume on return** — games and media apps must not let people miss content when they switch away. Restore state seamlessly on return.
- **Handle audio interruptions correctly:**
  - Primary audio (music, podcasts, audiobooks): pause indefinitely when interrupted.
  - Short interruptions (GPS directions, notifications): duck volume or pause temporarily; resume automatically when the interruption ends.
- **Finish user-initiated background tasks** — downloads, video processing, and similar tasks must complete even when the app isn't foregrounded.
- **Notify sparingly** — only for important/time-sensitive task completions that people need to act on. Don't send notifications for routine or secondary completions.

## Platform Considerations

### iOS

Picture in Picture: FaceTime or video can play in PiP while using another app.

### iPadOS

- Full-screen or windowed mode. In windowed mode, windows are resizable and arrangeable (similar to macOS). System provides window controls for tiling, full screen, minimize, and close.
- Frontmost window indicated by colored window controls and drop shadow.
- Multiple windows per app supported — people can view and interact with more than one window in the same app.
- PiP for video/FaceTime works in both full-screen and windowed modes.
- Apps don't control or receive notice of multitasking configurations.
- Adapt to all window sizes gracefully (see layout, windows).

### macOS

Multitasking is the default — multiple apps running simultaneously is standard. macOS uses drop shadows and visual effects to distinguish window layers and states (see windows#macOS-window-states).

### tvOS

Picture in Picture: people can browse or play content while a movie or TV show plays in PiP.

### visionOS

- Closing the Now Playing app window pauses audio; people can resume from Control Center.
- Multiple apps visible simultaneously in the Shared Space.
- One window is **active** at a time — gaze determines active window. The unfocused window becomes more translucent and recedes along the z-axis.
- Closing an app window transitions it to the background without quitting.
- **Don't interfere with system multitasking behavior** — don't change window edge appearance (system applies a feathered mask to inactive windows; interfering breaks that feedback).
- **Don't pause video playback when people look away** — video in one window continues while people interact with another window.
- **Be prepared for audio ducking** — unless your app is the Now Playing app, audio ducks when people look away to another app.

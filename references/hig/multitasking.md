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

Multitasking lets people switch among apps and perform tasks in each. It is expected except for some games and visionOS Full Space apps; watchOS doesn’t support it.

## Shared behavior

- Save and restore context because multitasking can begin at any time.
- Pause attention/participation activities on switch-away; resume as if uninterrupted.
- For primary-audio interruptions (such as music, podcasts, or audiobooks interrupting the app), pause the app’s audio indefinitely. For short interruptions (such as GPS directions), duck volume or pause temporarily, then restore playback/volume when they end.
- Finish user-initiated background work, such as downloads or video processing, before suspending when no more input is needed.
- Consider notifying for important/time-sensitive completions of user-initiated tasks; avoid routine notifications and let people check on return.

## Platform considerations

- **iOS:** FaceTime or video can continue in Picture in Picture while another app is in use.
- **iPadOS:** Full-screen or resizable windowed apps can be arranged with macOS-like tiling, full-screen, minimize, and close controls; multiple windows can come from one app. In full screen, the app switcher switches among app windows. Colored controls and a drop shadow identify the frontmost window. Picture in Picture works in both modes. Apps don’t control or receive notice of the chosen configuration, so adapt to every window size.
- **macOS:** Multiple apps and windows are the default; drop shadows and other effects distinguish layered window states. Video started in one window continues while people view or work in another.
- **tvOS:** People can browse or play content while a supported movie or show plays in Picture in Picture.
- **visionOS:** Multiple apps run in Shared Space, with windows and volumes, but only one window is active. Looking at another activates it; the previous becomes translucent and recedes on the z-axis. Closing a window backgrounds the app without quitting it; closing Now Playing pauses audio, resumable in Control Center. Don’t alter window edges because the system’s feathered mask communicates inactivity. Don’t pause video when people look away; non–Now Playing audio can duck.

Developer links: [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) and [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro).

Source: [Apple HIG — Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), captured 2026-09-12.

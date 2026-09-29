---
topic: airplay
tier: 4
platforms: [ios, ipados, macos, tvos, visionos]
category: technologies
triggers:
  - "AirPlay"
  - "screen mirroring"
  - "external display"
  - "wireless streaming"
related:
  - playing-audio
  - playing-video
---

# AirPlay

Wireless media streaming from iOS, iPadOS, macOS and tvOS devices to Apple TV, HomePod and AirPlay-compatible TVs and speakers.

## Best practices

- **Prefer the system media player** (`AVPlayerViewController`); consider a custom one only if it doesn't meet your needs.
- **Include the full range of resolutions in your HLS playlist**; AVFoundation picks per device.
- **Stream only content people expect**; avoid content like background loops or in-app-only short videos (`usesExternalPlaybackWhileExternalScreenIsActive`).
- **Support both AirPlay streaming and mirroring.**
- **Support remote control events** (Remote command center events) for actions like play, pause and fast forward on the lock screen, Siri and HomePod.
- **Don't stop playback when your app enters the background or the device locks.** While backgrounded or locked, it's also crucial to avoid automatic mirroring.
- **Don't interrupt another app's playback unless yours is starting immersive content.** Play launch and auto-playing inline videos on only the local device (`AVAudioSession.Category.ambient`).
- **Let people use other parts of your app during playback**; make sure other in-app videos don't start and interrupt the stream.
- **If necessary, provide custom playback controls.** Be sure to match system buttons' look and behavior, with distinct starting, playing and unavailable states. Use only Apple-provided symbols in controls that initiate AirPlay; put the AirPlay icon lower-right (iOS 16, iPadOS 16 and later).

## Using AirPlay icons

These rules cover the AirPlay icon shown with other technology icons, not the playback-control symbol. Download audio and video icons from [Apple Design Resources](https://developer.apple.com/design/resources/). Match other technology icons' color: black on light backgrounds, white on dark ones, or a custom color.

- **Position the icon consistently with other technology icons**; if those sit within shapes, it can too.
- **Don't use the AirPlay icon or name in custom buttons or interactive elements.**
- You can show the name below or beside the icon if other technologies appear that way; use your layout's font. Avoid the icon within text or in place of the name.
- **Make AirPlay references less prominent than your app name or main identity.**

## Referring to AirPlay

- *AirPlay*: one word, uppercase A and P. You can use all caps if your layout shows only all-uppercase designations.
- **Always use AirPlay as a noun:** "Use AirPlay to listen on your speaker", not "AirPlay to your speaker".
- **Use terms like *works with*, *use*, *supports* and *compatible*:** "AirPlay-enabled speaker", optionally "Apple AirPlay"; not "[App Name] has AirPlay".
- **Refer to AirPlay if appropriate and clarifying**, such as for AirPlay-specific content or technical specifications.

## Platform considerations

Not supported in watchOS. No additional considerations for other platforms.

## Resources

Developer: `AVKit`.

Source: [AirPlay](https://developer.apple.com/design/human-interface-guidelines/airplay), captured 2026-09-12.

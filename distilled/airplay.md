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

> AirPlay streams media content wirelessly from Apple devices to Apple TV, HomePod, and AirPlay-compatible speakers and TVs.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

## Best Practices

- **Use the system-provided media player** - built-in AirPlay support, chapter navigation, subtitles, captioning. Design a custom player only if it genuinely doesn't meet your needs.
- **Provide content at the highest available resolution** - include the full HLS resolution range. AVFoundation selects the right resolution automatically. Without a full range, content looks low quality when streamed to a higher-resolution device (e.g., 720p to 4K TV).
- **Stream only content people expect** - don't stream background loops or short in-app-only experiences.
- **Support both AirPlay streaming and mirroring** - gives maximum flexibility.
- **Support remote control events** - enables play/pause/fast-forward from lock screen, Siri, and HomePod.
- **Don't stop playback on background or lock** - people expect streaming to continue when they check mail or put the device to sleep.
- **No automatic mirroring** - people should explicitly choose to mirror.
- **Don't interrupt another app's playback** unless your app is starting immersive content. If your app auto-plays video on launch or inline, play it on the local device only.
- **App stays functional during AirPlay** - if people navigate away from the playback screen, ensure no other in-app videos start playing and interrupt the stream.
- **Custom AirPlay button placement**: lower-right corner (iOS 16+ / iPadOS 16+). Use only Apple-provided AirPlay symbols in custom controls.
- API cues: use `usesExternalPlaybackWhileExternalScreenIsActive` for external playback behavior; use `ambient` when immersive content shouldn't interrupt other playback.

## AirPlay Icon Usage

- **Black icon**: on white or light backgrounds when other tech icons are also black.
- **White icon**: on dark backgrounds when other tech icons are also white.
- **Custom color**: when other tech icons use the same color.
- Don't use the AirPlay icon or name in custom interactive buttons/controls - icons and name are for noninteractive references only.
- If pairing icon with the name "AirPlay": name can appear below or beside the icon. Use the same font as the rest of the layout. Don't embed the icon within text.
- **Emphasize your app over AirPlay** - AirPlay references should be less prominent than your brand.

## Referring to AirPlay

- Correct capitalization: **AirPlay** (one word, capital A, capital P).
- All-uppercase only in layouts where all designations are all-uppercase.
- **Always use as a noun** - "Use AirPlay to listen" is correct; "You can AirPlay with [App]" is incorrect.
- Use terms like *works with*, *use*, *supports*, *compatible* - "AirPlay-enabled speaker" is correct, "[App] is compatible with AirPlay" is correct, and "Compatible with Apple AirPlay" is acceptable for technical specifications.

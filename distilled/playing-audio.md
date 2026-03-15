---
topic: playing-audio
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "audio"
  - "sound"
  - "AVAudioSession"
  - "background audio"
  - "Now Playing"
  - "media controls"
related:
  - playing-video
  - airplay
---
# Playing Audio

> People expect audio to automatically adjust when context changes — volume, output, silence mode, and headphone events all require correct behavior.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Core Audio Behaviors

- **Silence switch (iPhone)**: silences non-essential sounds (keyboard clicks, effects, game soundtracks). Only explicitly user-initiated media (playback, alarms, messaging) plays while silent.
- **Volume**: people expect volume changes to affect all in-app sound. Never override system volume — only adjust relative internal levels to achieve a good mix.
- **Headphone disconnection**: reroute audio automatically when headphones connect; **pause immediately when they disconnect**.

## Best Practices

- **Never adjust the system volume** — adjust relative, internal mix levels only.
- **Permit audio rerouting** — let people output to any device (AirPlay, Bluetooth speakers, etc.) unless there's a compelling reason not to.
- **Use the system-provided volume view** — includes a slider and rerouting control; appearance of the slider can be customized.
- **Respond to audio controls only in context** — Controls (Control Center, headphone controls) should be handled only if your app is actively playing audio, in an audio context, or connected via Bluetooth/AirPlay. Otherwise, don't interrupt another app's playback.
- **Don't repurpose audio controls** — people expect consistent behavior from play/pause/skip everywhere.
- **Custom audio player controls only when necessary** — e.g., for custom skip increments or related content like a sports score.
- **Signal end of temporary audio interruption** — flag your audio session so other apps know when to resume.

## Audio Categories

| Category | Use case | Silent switch | Background | Mixes |
|---|---|---|---|---|
| Solo ambient | Non-essential; silences other audio (e.g., game soundtrack) | Respects | No | No |
| Ambient | Non-essential; lets other audio play alongside (e.g., game with user music) | Respects | No | Yes |
| Playback | Essential audio people may continue after leaving app (e.g., audiobook) | Ignores | Yes | Optional |
| Record | Audio being recorded (e.g., voice notes) | Ignores | Yes (record) | No |
| Play and record | Simultaneous playback + recording (e.g., video calls) | Ignores | Yes (both) | Optional |

## Handling Interruptions

- **Decide how to respond to interruptions** — e.g., recording apps can request to not be interrupted by calls unless people accept. VoIP apps should not restart the microphone audio session automatically after closing a Smart Folio (privacy risk — would unmute without consent).
- **Auto-resume only for resumable interruptions** — check the interruption type (resumable vs nonresumable). Media playback apps: check before auto-resuming. Games: auto-resume without checking (games play audio without explicit user action).

## Platform Considerations

### iOS, iPadOS
Use system sound services for short sounds and vibrations.

### macOS
Notification sounds mix with other audio by default.

### tvOS
Audio plays only when people initiate it. No sounds for alerts or notifications.

### visionOS
Spatial Audio is core to the experience — sound perceived as coming from specific locations in space.
- **Play sound** — an immersive moment without audio feels lifeless or broken.
- **Design custom sounds for custom elements** — system elements already have sounds; custom components need their own.
- **Use Spatial Audio for immersion** — ambient audio (world anchor) + audio sources (object-attached). Match source to object positionality.
- **Vary sounds to avoid repetition** — randomize pitch/volume during playback instead of creating multiple files.
- **Fixed vs. tracked sound**: tracked = sounds move with the object; fixed = sounds always face the user. Use tracked for realism; fixed for ambient envelopment (e.g., Mindfulness).
- **Now Playing**: audio pauses automatically when the app window closes. Audio from non-Now-Playing apps can duck when the user looks away.
- Don't communicate important info with sound alone — always provide visual/accessibility alternatives.

### watchOS
- Short clips while active and foreground; longer audio can continue when wrist lowered or app switched.
- **Encoding**: 64 kbps HE-AAC for good quality with low data use.
- **Provide a Now Playing view** — lets people control audio (from this or another app) without leaving your app.

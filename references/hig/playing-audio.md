---
topic: playing-audio
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "audio"
  - "sound"
  - "AVAudioSession"
  - "AVAudioSession.Category"
  - "background audio"
  - "Now Playing"
  - "media controls"
  - "MPVolumeView"
related:
  - playing-video
  - airplay
---

# Playing audio

Sound must behave as people expect when they change volume or output:

- **Silence:** Silent mode plays only user-initiated audio (media, alarms, A/V messaging); people want nonessential sounds, like keyboard clicks and game soundtracks, silenced too.
- **Volume:** People expect volume settings, by any method, to affect all sound, except iPhone ringer volume (set in Settings).
- **Headphones:** People expect connecting to reroute automatically without interruption, and disconnecting to pause playback immediately.

## Best practices

- **Adjust relative levels automatically when necessary; don't adjust the overall volume.** System volume always governs final output.
- **Permit rerouting output when possible**, unless there's a compelling reason not to.
- **Use the system volume view (`MPVolumeView`)**: a volume slider (appearance customizable) plus a rerouting control.
- **Choose an audio category (`AVAudioSession.Category`) that fits your sound use.** As much as possible, meet expectations; for example, don't stop another app's music if you don't need to.

|Category|Use (example)|Obeys silence switch|Mixes|In background|
|---|---|---|---|---|
|Solo ambient|Nonessential; silences other audio (game soundtrack)|Yes|No|No|
|Ambient|Nonessential; doesn't silence other audio (game allowing another app's music)|Yes|Yes|No|
|Playback|Essential (audiobook)|No|Maybe|Can play|
|Record|Recording (note app; might switch to Playback to play notes)|No|No|Can record|
|Play and record|Both, potentially simultaneously (video calls)|No|Maybe|Can record and play|

- **Respond to external audio controls, which reach your app even in the background, only when it makes sense**: fine when actively playing, in a clear audio context, or connected via Bluetooth or AirPlay. Otherwise, avoid halting another app's audio.
- **Avoid repurposing audio controls.** Don't respond to unsupported ones.
- **Consider custom player controls only for commands the system doesn't support**, like custom skip increments or related content like a sports score.
- **If your app can temporarily interrupt others' audio, be sure to flag your session (`notifyOthersOnDeactivation`) so they know when to resume.**

## Handling interruptions

Most apps rely on default interruption behavior; customize if needed.

- **Determine how to respond to audio-session interruptions**; you can inspect them to decide. For example, an app doing recording or other tasks people don't want interrupted can ask the system not to interrupt for an incoming call unless people accept it. A VoIP app using the built-in mic must end the call when an iPad Smart Folio closes (it mutes the mic and by default interrupts the session); restarting the session on reopen risks unmuting the mic without people's knowledge.
- **When an interruption ends, decide whether to resume automatically** by app and interruption type: *resumable* (incoming call) or *nonresumable* (new playlist). A media app playing when interrupted can check for resumable first; a game needn't check, since its audio plays without explicit user choice. `shouldResume` is deprecated.

## Platform considerations

### iOS, iPadOS

**Use system sound services (Audio Services) for short sounds and vibrations.**

### macOS

Notification sounds mix with other audio by default.

### tvOS

The system plays audio only when people initiate it (app and game interactions, device calibration); alerts and notifications are silent.

### visionOS

The system uses people's physical surroundings to produce *Spatial Audio*, perceived as coming from specific locations.

- **Important: As on every platform, avoid communicating important information using only sound**; always provide other ways.
- Now Playing app audio pauses automatically when its window closes; other apps' audio can duck when people look to a different app.
- **Prefer playing sound**, especially in immersive moments. Look for meaningful sounds that aid navigation and convey space.
- **Design custom sounds for custom UI elements** to give feedback and enhance the spatial experience.
- **Use Spatial Audio for an intuitive, engaging experience**, especially when fully immersive. Consider both *ambient audio* (pervasive, anchoring) and *audio sources* (from a specific object).
- **Consider defining a range of places sounds originate from**; a moved window's audio follows the window.
- **Consider varying sounds that could seem repetitive over time**: randomize a file's pitch and volume during playback instead of creating different files (the system subtly varies keyboard sounds).
- **Decide whether sound is fixed to or tracked by the wearer.** *Fixed*: aimed at the wearer regardless of gaze or objects; *tracked*: comes from an object, so its distance changes what people hear. In general, use tracked for realism; fixed can suit cases like Mindfulness enveloping the wearer.

### watchOS

The system manages playback: apps can play short clips while in the foreground, or longer audio that continues after wrist-down or app switch (Playing Background Audio).

- **Use 64 kbps HE-AAC**, the recommended encoding.
- **Consider a Now Playing view** so people control current or recent audio without leaving your app. It shows and auto-selects the current or most recent source (possibly another app on Watch or iPhone).

## Resources

Developer: Configuring your app for media playback (`AVFoundation`), `MusicKit`.

Source: [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio), captured 2026-09-12.

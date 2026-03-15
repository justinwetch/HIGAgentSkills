---
topic: playing-video
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "video"
  - "AVPlayer"
  - "AVPlayerViewController"
  - "playback"
  - "video controls"
  - "PiP"
related:
  - playing-audio
  - live-viewing-apps
  - going-full-screen
---
# Playing Video

> People expect rich, familiar video experiences across all platforms. Use the system-provided video player whenever possible.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Playback Modes (System Video Player)

| Mode | Scale behavior | Default for |
|---|---|---|
| Full-screen (aspect-fill) | Fills display; edges may crop | Wide video (2:1–2.40:1) |
| Fit-to-screen (aspect) | Letterbox/pillarbox as needed | Standard (4:3, 16:9, up to 2:1) and ultrawide (>2.40:1) |

tvOS and visionOS also show **transport controls** (subtitles, audio language, favorites) and **content tabs** (Info, Episodes, Chapters). In visionOS, transport controls appear as ornaments.

## Best Practices

- **Use the system video player** — provides familiar interactions people already know. A slightly divergent custom player causes confusion (people don't know which habitual interactions still apply).
- **Always display at the original aspect ratio** — embedded letterbox/pillarbox padding prevents correct scaling and breaks PiP mode on iPad.
- **Provide additional info when useful** — image, title, description; don't let it obscure playback.
- **Support Space bar to play/pause** on keyboards across all platforms.
- **Prevent audio mixing when switching modes** (especially full-screen ↔ PiP) — ensure background content handles secondary audio correctly.

## Integrating with the TV App

- **Seamless transition**: fade to black immediately (no launch screen). The TV app fades to black; match that by showing your own black screen before starting playback.
- **Show content immediately** — no splash screens, detail screens, or intros after transition. In rare interstitial cases, allow Select to step through or Play to skip.
- **Auto-resume playback** — don't ask for confirmation before resuming.
- **Space bar = play/pause** (Bluetooth keyboard in tvOS).
- **Multi-profile apps**: TV app may specify a profile; switch to it before playback. If none specified, ask the viewer before playback starts.
- **Resume at previous end time** for long video clips.
- **Loading screens**: only show if load takes >2 seconds → black screen + centered activity spinner. Start playback as soon as minimum content is loaded; continue buffering in background. Minimal branding on black background only.
- **After exiting playback**: show the content's detail view (with resume option), or a menu listing it. Prepare the exit view immediately on receiving a playback notification.

## Platform Considerations

### tvOS
- **Logos/overlays**: small and unobtrusive. Prefer translucent SDR graphics (avoid bright, opaque overlays — some devices have image retention risk).
- **Interactive overlays** (quizzes, check-ins): minimum 0.5-second delay before pausing media. Give a clear option to dismiss and resume.

### visionOS
- **Viewer comfort**: let people choose when to start; use a small window they can resize; keep surroundings visible.
- **Fully immersive**: don't auto-start. Keep virtual content from occluding playback controls/ornament.
- **Scrubbing thumbnails**: create a thumbnail track; provide thumbnails 160px wide for best performance.
- **Inline player**: don't expand to fill the window — window content must remain visible so people don't expect a more immersive experience.
- **Background/transitional video** (splash, transitions): use a RealityKit video player — no playback controls needed, correct aspect ratio auto-applied for 2D and 3D, closed captions supported.

### watchOS
- Short clips while app is active and foreground; use movie element for inline playback or a separate interface.
- **Clip length**: prefer ≤30 seconds — longer clips waste disk space and tire people's wrists.
- **Recommended encoding:**

| Attribute | Value |
|---|---|
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208×260 px (portrait) |
| Resolution (16:9) | 320×180 px (landscape) |
| Audio | 64 kbps HE-AAC |

- **Poster images**: use representative content; don't make the poster look like a system control.

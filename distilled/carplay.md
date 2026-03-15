---
topic: carplay
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: platforms
triggers:
  - "CarPlay"
  - "car"
  - "driving"
  - "in-vehicle"
  - "CPTemplate"
related:
  - designing-for-ios
---
# CarPlay

> CarPlay displays compatible iPhone apps on a car's built-in display, using system-defined templates and auto-scaled layout. Designed for in-vehicle use while driving.

**Platforms:** iOS only

## Core Principles

- **Minimal interaction while driving.** Quick tasks only; no complex flows.
- Use **system-defined templates** (audio, communication, navigation, fueling). Your app supplies content; iOS renders the CarPlay UI. No need to manage screen resolution, input hardware (touchscreen, knob, touch pad).

## iPhone Interactions

- **Eliminate iPhone interactions while CarPlay is active.** Setup must be done pre-drive.
- **Never lock people out of CarPlay because iPhone requires input.** App must function when iPhone is locked or physically inaccessible (in a bag, in the trunk).
- **Must work with iPhone locked** — most people use CarPlay with iPhone locked.

## Audio

- **Don't auto-start playback unless**: app plays a single source, or resuming previously interrupted audio. Starting an audio session silences the car's radio.
- **Playback must start as soon as audio is sufficiently buffered.** Show a spinner while loading; display Now Playing when ready.
- **Resume after a temporary interruption** (e.g., phone call) only if audio was actively playing before the interruption.
- Nonresumable interruptions: Siri-initiated music playlists, etc.
- **Adjust relative audio levels only** — never change the overall output volume.

## Layout

System auto-scales content to the car's display. Common display sizes:

| Dimensions (px) | Aspect ratio |
|---|---|
| 800×480 | 5:3 |
| 960×540 | 16:9 |
| 1280×720 | 16:9 |
| 1920×720 | 8:3 |

- Primary content and controls in the **upper half** of the screen (easier to see from driver's seat).
- Clean layout, easy to scan. No nonessential visual embellishments.
- Consistent appearance throughout — similar functions should look similar.

## Color

- **Limited palette** coordinated with your app logo.
- **Don't use the same color for interactive and noninteractive elements.**
- **Test in an actual car** under varying light conditions (day, night, sun, tinting, darkness). Adjust for night-mode brightness and direct-sunlight washout.
- Support both **light and dark appearances** — CarPlay auto-adjusts based on lighting.
- Follow inclusive color guidelines.

## Icons and Images

- Provide **@2x and @3x** versions of all artwork.
- **Mirror your iPhone app icon** — a good icon works without redesign.
- **Don't use black for the icon background** — lighten it or add a border.

**CarPlay icon sizes:**

| Scale | Size (px) |
|---|---|
| @2x | 120×120 |
| @3x | 180×180 |

## Error Handling

- **Report errors in CarPlay, not on the iPhone.** Never ask people to pick up their iPhone to resolve an issue.
- Show errors only when absolutely necessary.

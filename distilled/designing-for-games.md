---
topic: designing-for-games
tier: 2
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: platforms
triggers:
  - "game"
  - "gaming"
  - "game design"
  - "game loop"
  - "game controller"
related:
  - game-center
  - game-controls
  - focus-and-selection
  - loading
  - privacy
  - ratings-and-reviews
  - typography
  - buttons
  - accessibility
---
# Designing for Games

> Games on Apple devices should integrate platform capabilities while feeling at home across all Apple hardware.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Jump into Gameplay

- **Minimize install-before-play time** — include maximum playable content in initial install, keep download ≤30 min, download remaining content in background.
- **Provide great default settings** — use device info to auto-configure resolution, detect paired controllers/accessories, and respect accessibility settings. No configuration required to start playing.
- **Teach through play** — integrate tutorials into playable gameplay; offer written tutorials as an optional reference, not a prerequisite.
- **Defer permission requests until the right time** in context (e.g., ask hand-tracking permission between a cutscene and the first hand-controlled moment). Don't front-load requests before gameplay starts.
- Ask for ratings/reviews only after people have spent quality time with the game.

## Visual Quality

Minimum text sizes (same as platform defaults):

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17pt | 11pt |
| macOS | 13pt | 10pt |
| tvOS | 29pt | 23pt |
| visionOS | 17pt | 12pt |
| watchOS | 16pt | 12pt |

Minimum button/touch target sizes:

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44×44pt | 28×28pt |
| macOS | 28×28pt | 20×20pt |
| tvOS | 66×66pt | 56×56pt |
| visionOS | 60×60pt | 28×28pt |
| watchOS | 44×44pt | 28×28pt |

- Use resolution-independent textures/graphics. In visionOS, prefer vector-based art.
- Accommodate device hardware features (rounded corners, camera housing) in layout; use platform safe areas.
- In-game menus must adapt to multiple aspect ratios (16:10, 19.5:9, 4:3, both orientations on iPhone/iPad). Use dynamic layouts; avoid fixed layouts.
- Support full-screen/distraction-free gameplay on all platforms.

## Interactions

Default and supported interaction methods per platform:

| Platform | Default | Additional |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard + mouse/trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | — |

- Support physical game controllers on all platforms except watchOS — but always provide alternatives for players who can't use one.
- Offer touch-based game controls on iPhone/iPad: direct interaction with game elements and virtual on-screen controls.
- In visionOS, expect eyes and hands for indirect and direct gestures even though the game interaction table lists Touch as the default.

## Inclusivity

- Never rely solely on color to convey important information. Provide descriptive subtitles for cutscenes.
- Let players customize: type size, control mapping, motion intensity, sound balance.
- Support avatar/character customization across a full spectrum of human characteristics.
- Audit game characters and scenarios for stereotypes — avoid mapping enemies or heroes to specific races, genders, or cultural identities.

## Apple Technologies

- **Game Center** — social gaming network on all platforms. Achievements, leaderboards, challenges, multiplayer. Use GameKit.
- **GameSave (iCloud)** — sync game state across devices so players resume exactly where they left off.
- **Core Haptics** — custom haptic + audio patterns on iOS, iPadOS, tvOS, visionOS, and many game controllers.
- **Spatial Audio** — multichannel audio adapts automatically to device; enables immersive visionOS soundscapes.
- Additional integrations: augmented reality, machine learning, HealthKit, location, camera, microphone.

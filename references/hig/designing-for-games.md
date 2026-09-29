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

# Designing for games

Making games feel at home on Apple platforms.

## Jump into gameplay

- **Let people play as soon as installation completes.** Include as much playable content as you can while keeping download time to 30 minutes or less; download additional content in the background.
- **Provide great defaults** from device information, like resolution, automatic recognition of paired accessories and game controllers, and accessibility settings.
- **Teach through play.** A playable tutorial that integrates configuration and onboarding can work well; consider making any written tutorial a reference, not a prerequisite.
- **Defer requests.** Don't bombard people with too many requests before play. Certain device sensors and data like hand tracking require permission first; request it within the scenario that needs the data. Make sure people spend quality time with the game before you ask for a rating or review.

## Look stunning on every display

- **Make sure text is always legible** (good contrast, at least the minimum size) **and buttons always easy to use** (not too small or too close together). Recommended button minimums follow each platform's default interaction method; iOS buttons must be at least 44x44 pt for touch (the size table lists 28x28 pt as the iOS minimum).

|Platform|Text (pt), default/min|Button (pt), default/min|
|---|---|---|
|iOS, iPadOS|17/11|44x44/28x28|
|macOS|13/10|28x28/20x20|
|tvOS|29/23|66x66/56x56|
|visionOS|17/12|60x60/28x28|
|watchOS|16/12|44x44/28x28|

- **Prefer resolution-independent textures and graphics**; otherwise, match the device resolution. In visionOS, prefer vector art, which holds up as the system dynamically scales it for viewing distance and angle.
- **Accommodate device features** like rounded corners and camera housings, relying on safe areas when possible.
- **Make sure in-game menus** stay legible and easy to use at various aspect ratios (like 16:10, 19.5:9, 4:3) and in supported iPhone/iPad orientations, without obscuring content. Consider dynamic relative-constraint layouts; avoid fixed layouts as much as possible, and aim for device-specific ones only when necessary. See Menus > In-game menus.
- **Design for full screen**: in macOS, iOS and iPadOS, full-screen mode lets people hide other apps and system UI; in visionOS, a Full Space can completely surround people.

## Enable intuitive interactions

- **Support each platform's default and most common interaction methods.** Pay special attention to control sizing and menu behavior, especially going from pointer to touch. In visionOS, people expect eyes and hands with indirect and direct gestures.

|Platform|Default|Additional|
|---|---|---|
|iOS|Touch|Game controller|
|iPadOS|Touch|Game controller, keyboard, mouse, trackpad, Apple Pencil|
|macOS|Keyboard, mouse, trackpad|Game controller|
|tvOS|Remote|Game controller, keyboard, mouse, trackpad|
|visionOS|Touch|Game controller, keyboard, mouse, trackpad, spatial game controller|
|watchOS|Touch|-|

- **Support physical game controllers** (all platforms but watchOS) **and also offer alternatives**: not every player can use one.
- **Offer touch controls on iPhone and iPad**: direct interaction with game elements and virtual controls overlaid on content.

## Welcome everyone

- **Prioritize perceivability** through sight, hearing or touch. For example, avoid relying solely on color for important details, or cutscenes without descriptive subtitles or another way to read them.
- **Let players personalize** parameters like type size, control mapping, motion intensity and sound balance. You can use built-in Apple accessibility technologies with system frameworks or Unity plug-ins.
- **Give players tools to represent themselves, and avoid stereotypes in stories and characters.** If players create avatars or supply names or descriptions, support the spectrum of self-identity with options for as many human characteristics as possible. Review the game to remove biases and stereotypes (e.g., enemies of a certain race, gender or cultural heritage); if real-life cultural and language references are necessary, be sure they're respectful.

## Adopt Apple technologies

- **Integrate Game Center** (`GameKit`; all platforms): cross-device discovery, friends, progress, achievements, leaderboards, challenges, multiplayer.
- **Support `GameSave`** so people can resume where they left off on another device on the same iCloud account.
- **Support haptics** with `Core Haptics`: custom patterns, optionally with custom audio, in iOS, iPadOS, tvOS, visionOS and many game controllers.
- **Use Spatial Audio**: multichannel audio can adapt automatically to the device, enabling it where supported.
- **Use Apple technologies for unique mechanics**: you can integrate e.g. AR, machine learning, HealthKit, and request access to location data and functionality like camera and microphone.

## Resources

Source: [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games), captured 2026-09-12.

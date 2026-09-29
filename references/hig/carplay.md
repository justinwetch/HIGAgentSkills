---
topic: carplay
tier: 3
platforms: [ios]
category: platforms
triggers:
  - "CarPlay"
  - "car"
  - "driving"
  - "in-vehicle"
related: []
---

# CarPlay

Help drivers perform tasks quickly with minimal interaction, using the system-defined templates for your app type ([CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf)); iOS renders your content and handles input hardware like touchscreens, knobs and touch pads.

## iPhone interactions

- **Eliminate app interactions on iPhone when CarPlay is active**; use the car's controls and display. Make sure any required iPhone setup happens before the vehicle moves.
- **Never lock people out because the connected iPhone requires input.** Your app needs to function with iPhone out of reach, like in a bag; let people resolve iPhone problems after the vehicle stops.
- **Make sure your app works with iPhone locked.**

### Audio

- **Let people choose when to start playback.** In general, avoid autoplay unless your app's purpose is playing a single audio source or it's resuming interrupted audio. Avoid starting an audio session until you're ready to play; it silences other sources, like the car radio.
- **Start playback as soon as audio has sufficiently loaded**; until your app signals readiness, the system keeps the selection highlighted with a spinning activity indicator.
- **Show Now Playing when audio is ready**; don't delay playback for descriptive information, which can load in the background if necessary.
- **Resume after an interruption only when appropriate.** Your app can resume after a temporary interruption like a phone call; permanent ones, like a Siri-started playlist, are nonresumable. When a resumable one ends, your app needs to resume if audio was actively playing when it started.
- **When necessary, automatically adjust relative audio levels, but don't change the overall volume.**

## Layout

Displays can be landscape or portrait; the system scales icons and interfaces to appear roughly the same size on each. Common sizes (px): 800x480 (5:3), 960x540 and 1280x720 (16:9), 1920x720 (8:3).

- **Provide high-value information in a clean layout that's easy to scan from the driver's seat**; don't clutter it with nonessential details or embellishments.
- **Maintain a consistent appearance**; in general, ensure elements with similar functions look similar.
- **Ensure primary content stands out and feels actionable**. In general, place the most important content and controls in the upper half of the screen.

## Color

- **In general, prefer a limited palette that coordinates with your app logo.**
- **Avoid using the same color for interactive and noninteractive elements.**
- **Test colors in an actual car under varied lighting**, considering brightness at night and low-contrast washout in direct sunlight; adjust if necessary.
- **Ensure your app looks great in dark and light environments**; CarPlay may switch appearance automatically with lighting.
- **Choose colors that communicate effectively with everyone** ([Inclusive color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color)).

## Icons and images

- **Supply @2x and @3x images for all CarPlay artwork**; the system picks and scales them for the display's resolution and size.
- **Mirror your iPhone app icon.**
- **Don't use black for your icon's background**; lighten it or add a border.
- App icon: 120x120 px (@2x), 180x180 px (@3x).

## Error handling

Handle errors gracefully and report them only when absolutely necessary. **Report errors clearly in CarPlay, not on the connected iPhone**; never direct people to their iPhone to read or resolve one.

## Platform considerations

No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS or watchOS.

## Resources

Source: [CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay), captured 2026-09-12.

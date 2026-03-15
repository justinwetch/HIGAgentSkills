---
topic: remotes
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/tvos
triggers:
  - "Siri Remote"
  - "Apple TV remote"
  - "remote control"
  - "swipe remote"
  - "click pad"
related:
  - focus-and-selection
  - gestures
  - designing-for-tvos
---
# Remotes

> The Siri Remote is the primary input method for Apple TV, combining a clickpad, touch surface, and buttons.

**Platforms:** tvOS only

Supports swipe, press, and directional taps on the touch surface, plus dedicated buttons.

## Best Practices

- **Use standard gestures for standard actions** — repurposing remote behaviors adds confusion. Custom gestures only when contextually appropriate (games).
- **Maintain the tvOS focus experience** — always move focus in the same direction as the gesture.
- **Clear gesture feedback** — e.g., a light touch hint can preview the swipe-down reveal of an info area.
- **Distinguish press vs. tap** — press = intentional (confirm selection, trigger gameplay action). Tap = lighter (navigation, show more info). Avoid responding to inadvertent taps (people rest thumbs on the remote, pick it up, hand it off). Especially important during live video playback.
- **Positional taps**: touch surface distinguishes up/down/left/right taps. Use only when intuitive and discoverable.
- **Back button behavior** — almost always: navigate to the parent of the current screen. Exception in games: Back opens an in-game pause menu (prevents accidental game exit). While the pause menu is open, Back closes it and resumes the game. Note: press-and-hold Back always goes to the Apple TV Home Screen from anywhere.
- **Play/Pause**: during media playback, plays, pauses, or resumes — no other mapping.

## Gestures (Touch Surface)

- **Swipe** — scrolls through items; momentum-based (fast then slows). Swiping on the edge speeds through items even faster.
- **Press** — activates a control or selects an item. Pressing before swiping activates scrubbing mode.

## Button Reference

| Button/area | Expected app behavior | Expected game behavior |
|---|---|---|
| Touch surface (swipe) | Navigates; changes focus | Directional pad |
| Touch surface (press) | Activates control or item; navigates deeper | Primary button |
| Back | Returns to previous screen; exits to Home | Opens pause menu; on Back again: resumes game |
| Play/Pause | Activates/pauses/resumes media | Secondary button; skips intro video |

## Compatible Remotes (EPG/Live TV)

Remotes with EPG buttons:
- "Guide/Browse" button → opens your EPG if you have one.
- "Page up/down" in EPG → navigates through it; upper/lower touch surface taps also navigate EPG.
- "Page up/down" during content playback → changes the channel.
- Don't repurpose these buttons while people browse the EPG; if your app has no EPG, the system routes them to the default guide app.

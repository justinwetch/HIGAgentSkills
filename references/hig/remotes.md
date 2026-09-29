---
topic: remotes
tier: 3
platforms: [tvos]
category: components/tvos
triggers:
  - "Siri Remote"
  - "Apple TV remote"
  - "remote control"
  - "swipe remote"
  - "clickpad"
  - "Providing Channel Navigation"
related:
  - focus-and-selection
  - gestures
  - designing-for-tvos
---

# Remotes

The Siri Remote is Apple TV's primary input.

## Best practices

- **Prefer standard gestures for standard actions**, which people expect outside active gameplay.
- **Match the tvOS focus experience**, like always moving focus in the gesture's direction.
- **Give clear gesture feedback.**
- **Define new gestures only when it makes sense**, like in gameplay.
- **Differentiate press from tap; avoid responding to inadvertent taps.** Press is intentional (choosing, confirming, gameplay actions); taps are fine for navigation or extra info but may be accidental (resting a thumb on or handling the remote), so ignoring taps during live video often works well.
- **Consider positional taps (up, down, left, right) in navigation or gameplay**, only if sensible, intuitive and discoverable.
- **In almost all cases, open the current screen's parent when people press Back** (Home Screen at top level; otherwise the app-hierarchy parent, not necessarily the previous screen). In active gameplay, respond instead by opening a pause menu offering another route to the main menu; Back there resumes the game. People press and hold Back to go Home from anywhere.

## Gestures

Clickpad swipes scroll fast, then slow by strength; edge swipes up or down speed through items very quickly. Pressing before swiping starts scrubbing.

## Buttons

Ensure these responses:

| Input | App | Game |
|---|---|---|
| Swipe | Navigates; changes focus | Directional pad |
| Press | Activates a control or item; navigates deeper | Primary button |
| Back | Returns to previous screen; exits to Home Screen | Pauses/resumes gameplay; returns to previous screen, exits to main game menu or to Home Screen |
| Play/Pause | Activates, pauses or resumes media playback | Secondary button; skips intro video |

## Compatible remotes

- **If your live-viewing app provides an electronic program guide ([EPG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#EPG-experience)), respond to a compatible remote's EPG buttons as people expect**: "guide" or "browse" opens it; "page up"/"page down" navigates it. Avoid other responses during browsing. On the Siri Remote and compatible remotes, upper or lower touch-surface taps also browse it. Without an app EPG, the system routes these presses to the default guide app.
- **While content plays, make "page up"/"page down" change the channel.**

## Platform considerations

Not supported in iOS, iPadOS, macOS, visionOS or watchOS.

## Resources

Developer: [Providing Channel Navigation](https://developer.apple.com/documentation/tvservices/providing-channel-navigation)

Source: [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes), captured 2026-09-12.

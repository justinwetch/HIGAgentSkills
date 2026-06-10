---
topic: shareplay
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: technologies
triggers:
  - "SharePlay"
  - "Group Activities"
  - "GroupActivities"
  - "SystemCoordinator"
  - "SpatialTemplatePreference"
  - "shared experience"
  - "FaceTime activity"
related:
  - collaboration-and-sharing
---
# SharePlay

> SharePlay lets multiple people share real-time activities — video, music, games, whiteboards — during a FaceTime call or Messages conversation, synchronized across all devices.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

## Best Practices

- **Indicate SharePlay support in your UI** — use the `shareplay` SF Symbol on shareable content.
- **Help non-subscribers join quickly** — consider temporary access, one-time passes, or Family Sharing. Present a streamlined sign-up flow if someone needs to subscribe mid-session.
- **Support Picture in Picture** for shared video (iPhone/iPad = PiP window; Mac = background window).
- **Use "SharePlay" correctly**: noun ("Join SharePlay") or verb ("SharePlay Movie"). Never adjective (*spatial SharePlay*). Never modified (*SharePlayed*, *SharePlaying*).

## Activities

- If the app isn't installed, use the SharePlay alert/App Store path and support `Universal Purchase` where appropriate.

- An *activity* = an app-defined shareable experience type.
- **Brief activity descriptions** — shown in the invitation; short enough to avoid truncation.
- **Let people initiate sharing easily** when no session exists. The system asks whether to share or go solo.
- **Help people prepare before showing the activity** — login, downloads, payments first.
- **Defer non-critical tasks** (e.g., profile setup) until playback pauses.

## visionOS — Spatial Personas

People choose the Spatial option in FaceTime to share with Personas in the same virtual space.

### Spatial Persona Templates

| Template | Arrangement | Best for |
|---|---|---|
| Side-by-side | Participants along a curved line, all facing shared content | Media viewing; less face-to-face interaction |
| Surround | Participants arranged all the way around 3D content | 3D content; promotes verbal + nonverbal interaction |
| Conversational | Participants around a center point; content along the circle perimeter | Background activities (e.g., music); content not the main focus |

**Design rules for visionOS SharePlay:**

- **Launch directly into the shared activity** — suppress unrelated windows on auto-launch. Pre-login/sign-up in auto-dismissing windows.
- **Don't force immersion changes** — check if transitioning immersion levels would disrupt someone's task; offer them a choice.
- **Smoothly integrate new joiners** — don't disrupt ongoing participants. Design for up to 5 participants.
- **Maintain shared state** — everyone sees the same app state. Exception: temporary individual exits.
- **Use Spatial Audio** to strengthen realism.
- **Prefer social solutions over UI** for conflicts — let people speak or gesture rather than triggering system alerts.
- **Keep shared vs. private windows visually distinct.** Let people drag content between private → shared.
- **Let people personalize their experience** (volume, subtitles) without affecting others.
- **Provide unique per-person views when content has one correct angle** (e.g., Spatial Captures in a Full Space, while others stay in Shared Space).
- **Make it easy to exit and rejoin** — show an obvious rejoin button; keep showing shared content while they're away.

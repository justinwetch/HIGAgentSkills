---
topic: accessibility
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "accessibility"
  - "a11y"
  - "contrast ratio"
  - "tap target"
  - "touch target"
related:
  - voiceover
  - focus-and-selection
  - inclusion
---
# Accessibility

> Accessible interfaces empower everyone regardless of their capabilities or how they use their devices.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

An accessible interface is **intuitive** (familiar, consistent interactions), **perceivable** (no single-modality dependency), and **adaptable** (responds to system accessibility features).

## Vision

**Text sizes:**
- Support enlargement up to 200% (140% minimum in watchOS). Use Dynamic Type or custom UI.
- Default/min font sizes by platform:

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17pt | 11pt |
| macOS | 13pt | 10pt |
| tvOS | 29pt | 23pt |
| visionOS | 17pt | 12pt |
| watchOS | 16pt | 12pt |

- Thin-weight custom fonts: target larger than minimums.

**Color contrast (WCAG Level AA via Accessibility Inspector):**

| Text size | Weight | Min contrast ratio |
|---|---|---|
| Up to 17pt | Any | 4.5:1 |
| 18pt+ | Any | 3:1 |
| Any | Bold | 3:1 |

- If not met by default, provide it when Increase Contrast is on. Check both light and dark.
- Prefer system colors — they have built-in accessible variants.
- Never rely on color alone: add distinct shapes, icons, or labels to convey state/function.
- Provide VoiceOver descriptions for all interface elements.

## Hearing

- Provide captions for video/audio-only content (synchronized text).
- Provide subtitles for multilingual dialogue.
- Provide audio descriptions for visual-only info in video.
- Provide transcripts for longer-form audio (podcasts, audiobooks).
- Pair audio cues with haptics (success, error, game feedback).
- Add visual cues alongside audio cues — critical for off-screen game events.

## Mobility

**Minimum control sizes:**

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44×44pt | 28×28pt |
| macOS | 28×28pt | 20×20pt |
| tvOS | 66×66pt | 56×56pt |
| visionOS | 60×60pt | 28×28pt |
| watchOS | 44×44pt | 28×28pt |

- Add ~12pt padding around bezeled elements, ~24pt around unbezel elements.
- Use simplest gestures for frequent interactions. Avoid custom multi-finger/multi-hand gestures.
- Always provide an onscreen alternative to every gesture (e.g., button alongside swipe-to-dismiss).
- Label elements correctly for Voice Control and VoiceOver.
- Support mobility assistive technologies: VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control.

## Speech

- Support Full Keyboard Access — app must be fully navigable by keyboard alone.
- Don't override system keyboard shortcuts.
- Support Switch Control (hardware, game controllers, or sound inputs).

## Cognitive

- Use simple, consistent, memorable interactions. Prefer system-native gestures.
- Avoid time-boxed auto-dismissing UI — prefer explicit dismissal actions.
- Let players customize game difficulty (reaction time, success criteria, control assistance).
- Provide controls to start/stop all auto-playing audio and video. Support Dim Flashing Lights for video.
- When Reduce Motion is on, reduce: repetitive/automatic animations, zoom/scale transitions, z-axis depth changes. Replace motion transitions with fades. Tighten animation springs.

**Assistive Access (iOS/iPadOS — cognitive disability mode):**
- Identify core functionality; remove noncritical workflows and UI elements.
- Break multistep flows into single-interaction screens.
- Require double confirmation for hard-to-recover actions (e.g., delete).

## Platform Considerations

### visionOS

- Provide alternatives to gaze interactions; support Pointer Control.
- Comfort guidelines: keep UI within field of view, prefer horizontal layouts, reduce peripheral animation speed, avoid head-anchored content, minimize large/repetitive gestures.
- Be cautious with camera motion — avoid involuntary world-movement sensations.

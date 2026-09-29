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
  - inclusion
  - typography
---
# Accessibility

Accessible interfaces empower everyone. Design so people can experience your app or game regardless of their capabilities or how they use their devices. An accessible interface is:

- **Intuitive:** familiar, consistent interactions make tasks straightforward.
- **Perceivable:** information does not depend on one method; people can use sight, hearing, speech, or touch.
- **Adaptable:** the interface supports system accessibility features and personalization.

Audit with [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector), which highlights issues and shows how the app represents itself to system accessibility features. [Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) communicate support on the App Store.

## Vision

Support adjusting text and icon size for legibility, visibility, and comfort. Ideally, offer text enlargement of at least **200%** (**140%** in watchOS apps), through custom UI or Dynamic Type. For custom type styles, use these defaults and minimums:

| Platform | Default | Minimum |
|---|---:|---:|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Thicker weights are easier to read at smaller font sizes. Thin custom weights can reduce legibility; aim larger than the recommended sizes. Strive for acceptable contrast using a standard contrast calculator. WCAG and APCA are popular measurement standards; the following WCAG Level AA values guide Accessibility Inspector:

| Text size | Weight | Minimum ratio |
|---|---|---:|
| Up to 17 pt | All | 4.5:1 |
| 18 pt | All | 3:1 |
| All | Bold | 3:1 |

If the default does not meet these minimums, provide a higher-contrast scheme when **Increase Contrast** is on. If your app supports **Dark Mode**, check the minimum contrast in both light and dark appearances. Prefer system-defined colors, whose accessible variants adapt to contrast and appearance settings. Convey state and function with shapes or icons in addition to color (red-green and blue-orange can be difficult to distinguish); consider letting people customize chart or game colors. Describe the interface and content for VoiceOver.

## Hearing

Do not communicate dialogue or crucial information through audio alone. Depending on context, offer the following text-based media alternatives, and allow people to customize the visual presentation of that text:

- **Captions:** synchronized text equivalent of audible information in video or audio-only content.
- **Subtitles:** live onscreen dialogue in a preferred language, useful for shows and movies.
- **Audio descriptions:** spoken narration of important visual-only information during natural pauses.
- **Transcripts:** complete textual accounts of audible and visual information, useful for longer media such as podcasts and audiobooks.

If the interface conveys information through audio cues such as success, error, or game feedback, consider pairing them with matching haptics for people who cannot perceive audio or have it turned off. In iOS and iPadOS, [Music Haptics](https://developer.apple.com/documentation/mediaaccessibility/music-haptics) and [Audio Graphs](https://developer.apple.com/documentation/accessibility/audio-graphs) can convey music and infographics through vibration and texture. Add visual indicators alongside audio guidance, especially for off-screen events in games and spatial apps.

## Mobility

Strive for the platform’s recommended minimum control size:

| Platform | Default | Minimum |
|---|---:|---:|
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

Spacing matters too: about **12 pt** around elements with a bezel and about **24 pt** around the visible edges of elements without one can reduce accidental taps. Use the simplest gesture for frequent actions; avoid custom multifinger or multihand gestures. Offer another physical interaction for core functionality—for example, provide a button as well as swipe-to-dismiss.

Label elements appropriately for [Voice Control](https://developer.apple.com/documentation/accessibility/voice-control). Integrate Siri and Shortcuts so important, repetitive tasks can be done by voice, including from Siri, the Action button on iPhone or Apple Watch, the Home Screen, or Control Center. Test support for VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, and Switch Control, and verify labels.

## Speech

Support keyboard-only navigation with Full Keyboard Access. Avoid overriding system-defined keyboard shortcuts. Support Switch Control, which can use separate hardware, game controllers, or sounds to select, tap, type, and draw.

## Cognitive

Prefer familiar system gestures and easy-to-remember interactions. Minimize time-boxed UI: controls and views that auto-dismiss can leave people who need more processing time or assistive-technology traversal behind; prefer explicit dismissal. Consider game difficulty accommodations such as reduced success criteria, adjustable reaction time, or control assistance.

Give people discoverable controls to start and stop audio/video, and consider a global opt-out for autoplay. Respond to **Dim Flashing Lights** during video playback. Be cautious with fast-moving and blinking effects: in excess they can distract, cause dizziness, or trigger epileptic episodes. When **Reduce Motion** is on, reduce automatic and repetitive animation, including zooming, scaling, and peripheral motion; best practices include tightening springs, tracking gestures directly, avoiding z-axis depth animation, replacing axis transitions with fades, and avoiding animation into or out of blurs. For implementation references, see [Flashing lights](https://developer.apple.com/documentation/mediaaccessibility/flashing-lights) and [isVideoAutoplayEnabled](https://developer.apple.com/documentation/uikit/uiaccessibility/isvideoautoplayenabled).

When [Assistive Access](https://developer.apple.com/documentation/accessibility/assistive-access) is on (iOS and iPadOS), identify core functionality and consider removing noncritical workflows and UI. Break up multistep workflows so people can focus on a single interaction per screen, and ask twice before an action that is difficult to recover from, such as deleting a file.

## visionOS

visionOS includes hand and head Pointer Control and Zoom. Consider these comfort practices: keep UI in the field of view and prefer horizontal layouts over neck-straining vertical ones; avoid demanding attention in rapidly changing locations; reduce the speed and intensity of animated objects, particularly in the periphery; be gentle with camera/video motion and avoid making the world feel as if it moves without the person’s control; avoid head-anchored content, which can feel confining and interfere with Pointer Control; and minimize large, repetitive gestures. With hand Pointer Control, a pointer moves as the person moves their hand; with head Pointer Control, the pointer stays centered while head movement positions content beneath it. Zoom displays a magnified view of content beneath a lens.

## Resources

Related: [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography), [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover).

Developer references: [Building accessible apps](https://developer.apple.com/accessibility/), [Accessibility framework](https://developer.apple.com/documentation/accessibility), and [Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels).

Platform considerations: no additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS; visionOS guidance is above.

Source: [Apple HIG — Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), captured 2026-09-12.

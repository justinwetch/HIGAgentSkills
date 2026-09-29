---
topic: voiceover
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/accessibility
triggers:
  - "VoiceOver"
  - "screen reader"
  - "accessibility label"
  - "rotor"
  - "custom rotor"
  - "AccessibilityNotification"
  - "shouldGroupAccessibilityChildren"
  - "Direct Gesture mode"
  - "Unity plug-ins"
related:
  - accessibility
  - focus-and-selection
  - inclusion
  - charts
---

# VoiceOver

VoiceOver is a screen reader for people who are blind or have low vision, supported in Apple-platform apps and games, including Unity ones using Apple's Unity plug-ins.

## Descriptions

- **Provide alternative labels for all key interface elements.** You should give system controls more descriptive labels than their generic defaults, conveying your app's functionality; label any custom elements; be sure to keep labels current as interface and content change (SwiftUI accessibility modifiers).
- **Describe meaningful images**, but only what the image itself conveys, not nearby captions or other interface.
- **Make charts and other infographics fully accessible.** Concisely describe what each conveys; if people can interact with it for more or different information, make those interactions available to VoiceOver too.
- **Exclude purely decorative images** that convey no useful or actionable information (SwiftUI `accessibilityHidden(_:)`, AppKit `accessibilityElement`, UIKit `isAccessibilityElement`).

## Navigation

- **Use titles and headings to convey hierarchy.** Give each page or screen a unique, succinct title describing its content and purpose; assistive technology announces it first. Use accurate section headings.
- **Specify how elements are grouped, ordered or linked** where relationships are only visual, like proximity or alignment. VoiceOver reads in the active language and locale's order (US English: top-to-bottom, left-to-right); ungrouped images with captions beneath read all images first, then all captions; group each image with its caption (`shouldGroupAccessibilityChildren`).
- **Inform VoiceOver of visible content or layout changes** (`AccessibilityNotification`).
- **Support the VoiceOver rotor when possible** by identifying headings, links and other content types to it for navigation. The rotor can also bring up the braille keyboard (SwiftUI `AccessibilityRotorEntry`, UIKit `UIAccessibilityCustomRotor`, AppKit `NSAccessibilityCustomRotor`).

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS or watchOS.

### visionOS

**Be mindful that custom gestures aren't always accessible.** With VoiceOver on, apps and games that define custom gestures don't receive hand input by default. People can opt out by enabling Direct Gesture mode, which disables standard VoiceOver gestures and lets apps process hand input directly.

## Resources

Developer: `Accessibility` framework.

Source: [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover), captured 2026-09-12.

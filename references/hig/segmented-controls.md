---
topic: segmented-controls
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/controls
triggers:
  - "segmented control"
  - "UISegmentedControl"
  - "segmented"
  - "NSSegmentedControl"
  - "isMomentary"
  - "NSSegmentedControl.SwitchTracking.momentary"
  - "picker strip"
  - "option group"
related:
  - toggles
  - pickers
  - buttons
  - split-views
---

# Segmented controls

A linear set of two or more segments, each a button, holding text or images; optional text labels can sit beneath segments or the whole control. It offers one choice (in macOS, one or multiple), or acts as action buttons without selection state (UIKit `UISegmentedControl.isMomentary`; AppKit `NSSegmentedControl.SwitchTracking.momentary`).

## Best practices

- **Use for closely related choices that affect an object, state or view.**
- **Consider it when grouping functions or clearly showing selection state matters.**
- **Don't mix action segments and selection-state segments in one control.**
- **Limit segments**: aim for at most about 5-7 in a wide interface, about 5 on iPhone.
- **In general, keep segment size consistent.**

## Content

- **Prefer text or images, not a mix, in one control.**
- **As much as possible, use similar-size content in each segment.**
- **Label with nouns or noun phrases** in title-style capitalization. Text labels need no introductory text.

## Platform considerations

Not supported in watchOS.

### iOS, iPadOS

**Consider it for switching between closely related subviews**; use a tab bar for completely separate app sections.

### macOS

- **Consider introductory text to clarify purpose.** For symbols or icons, you could also label each segment below; if your app has tooltips, give each segment one.
- **Use a tab view for main-window view switching**; consider a segmented control for view switching in a toolbar or inspector pane.
- **Consider supporting spring loading** (Magic Trackpad): force clicking while dragging items over a segment activates it without dropping them; dragging can continue.

### tvOS

- **Consider a split view instead on content-filtering screens.**
- **Avoid other focusable elements close to segmented controls.** Segments select on focus, not click, so people might accidentally focus nearby elements.

### visionOS

Looking at an icon segmented control shows a system tooltip with your descriptive text.

## Resources

Developer: `.segmented` picker style (SwiftUI), `UISegmentedControl`, `NSSegmentedControl`.

Source: [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls), captured 2026-09-12.

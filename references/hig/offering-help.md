---
topic: offering-help
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "help"
  - "coach mark"
  - "hint"
  - "tooltip"
  - "tips"
  - "help documentation"
related:
  - onboarding
  - feedback
  - writing
  - the-menu-bar
---
# Offering help

Provide contextual help when necessary.

- Match help to the task: use a succinct inline view for simple one- or two-step tasks, a tutorial for complex/multistep goals. Relate it to the precise current action and make it dismissible/avoidable.
- Keep language/images relevant to context and platform (for example, when someone uses Siri Remote in tvOS, show Siri Remote rather than game-controller guidance; say “tap” on iPhone and “click” on Mac). Make help inclusive.
- Don’t explain standard components; describe their app-specific action. For unique controls/nonstandard input (such as holding a Siri Remote rotated 90°), orient people quickly with animation/graphics rather than long text.

## Tips

A tip is a small transient view briefly explaining a feature, useful for new/less-obvious features or faster task completion. [TipKit](https://developer.apple.com/documentation/tipkit) provides developer guidance.

- Choose by layout: a popover preserves flow but obscures underlying content; inline keeps surrounding information visible. Annotation-style inline tips point at a specific UI element (displacing nearby text); hint-style tips have no specific UI target.
- Use tips for simple features people can complete in a few steps; more than three actions is probably too complex.
- Keep each tip to one or two sentences: direct, action-oriented, and engaging; explain what the feature does and how to use it, and omit promotional/unrelated content.
- Use parameter- or event-based eligibility rules; show a tip only when someone may benefit (someone who already used the feature won’t). When there are multiple tips, set a reasonable cadence, such as once every 24 hours.
- If an associated image/symbol helps identify the feature, consider including the filled variant (a star can signal favorites). If the tip directly points to an image already representing the feature, avoid repeating that image in both tip and UI.
- If a feature has customizable settings or people need more information, consider a button linking directly to settings or resources such as a setup flow.

## Tooltips on macOS and visionOS

On macOS (including iPhone/iPad apps on Mac), a tooltip—called a help tag in user documentation—can appear when the pointer rests over a component. In visionOS it can appear when someone looks at an element or holds the pointer over it. SwiftUI [`help(_:)`](https://developer.apple.com/documentation/swiftui/view/help(_:)-6oiyb) adds supplied-string help text to a view; AppKit [`NSHelpManager`](https://developer.apple.com/documentation/appkit/nshelpmanager) displays online app help.

- Describe only the indicated control, not nearby controls/a larger task; explain its action, preferably beginning with a verb (“Restore default settings”; “Add or remove a language from the list”). Generally omit the control name.
- Keep tooltip text to at most 60–75 characters where possible (localization can change length); consider a brief fragment and omitting articles. If it needs much more text, consider simplifying the interface.
- Use sentence case; omit final punctuation for complete sentences unless the app’s style requires it. Consider context-sensitive text for different control states.

**Resources:** [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Writing](https://developer.apple.com/design/human-interface-guidelines/writing), [Help menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#help-menu), [Make features discoverable with TipKit](https://developer.apple.com/videos/play/wwdc2023/10229).

Source: [Apple HIG — Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help), captured 2026-09-12.

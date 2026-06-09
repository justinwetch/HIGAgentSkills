# Components Batch F Verification

Source corpus: `sources/apple-hig-2026-06-09`

Reviewer: Averroes (`019eae2a-352e-7b30-bd06-1a8e85888bc2`)

## Accepted Without Distilled Changes

- `offering-help` -> `distilled/offering-help.md`
- `onboarding` -> `distilled/onboarding.md`
- `playing-audio` -> `distilled/playing-audio.md`
- `playing-video` -> `distilled/playing-video.md`

These files were checked against the current rendered Apple HIG source and remained appropriately compressed for trigger-based agent use.

## Revised And Resolved

- `ornaments` -> added current visionOS platform/API triggers and clarified that system toolbars/tab bars become ornaments.
- `outline-views` -> scoped to macOS and added `OutlineGroup` trigger.
- `page-controls` -> added watchOS and current page-control API triggers, custom indicator image guidance, and iOS/iPadOS interaction-mode guidance.
- `panels` -> scoped to macOS, added `hudWindow`, and linked modality.
- `path-controls` -> scoped to macOS.
- `photo-editing` -> added iOS/iPadOS/macOS scope and extension/PhotoKit triggers.
- `pickers` -> added SwiftUI/AppKit/navigation triggers, refreshed related routing, and removed duplicate trigger casing.
- `playing-haptics` -> added AppKit/watchOS haptic triggers and watchOS pattern names.
- `pointing-devices` -> added current platform scope and band-selection/pointer-accessory triggers; retained agent-useful pointer/finger distinction guidance.
- `pop-up-buttons` -> added visionOS and current menu-picker triggers.

## Result

Batch F is ready to mark as current-source reviewed. Changes were regenerated into `routing-index.md` and validated with zero corpus errors.

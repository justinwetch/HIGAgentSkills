# Components Batch I Verification

Source corpus: `sources/apple-hig-2026-06-09`

Reviewer: Volta (`019eae36-90cc-74c0-9002-b238e44e5830`)

## Accepted Without Distilled Changes

- `toolbars` -> `distilled/toolbars.md`

## Revised And Resolved

- `toggles` -> added macOS checkbox/radio/switch/toggle-style triggers and related routing.
- `top-shelf` -> scoped to tvOS and added layout/static-image/accessibility/image triggers.
- `undo-and-redo` -> added visionOS, three-finger swipe, feedback/pointer/keyboard/menu routing.
- `virtual-keyboards` -> added watchOS and current keyboard/content/layout/input triggers.
- `voiceover` -> added current VoiceOver API/routing triggers and Unity plug-ins support note.
- `wallet` -> refreshed for iOS 27/Pass Designer, poster generic passes, semantic tags, WalletOrders, identity verification APIs, and corrected pass image specs.
- `watch-faces` -> scoped to watchOS and added ClockKit/sharing/watchOS 7 triggers.
- `web-views` -> added visionOS and WebKit routing.
- `widgets` -> added visionOS and CarPlay/StandBy/rendering/RelevanceKit triggers.
- `windows` -> scoped to iPadOS/macOS/visionOS and added window style/open/volume triggers.
- `workouts` -> scoped to iOS/iPadOS/watchOS, added WorkoutKit, and clarified live/recorded session device contexts.

## Result

Batch I is ready to mark as current-source reviewed. Changes were regenerated into `routing-index.md` and validated with zero corpus errors.

# Components Batch H Verification

Source corpus: `sources/apple-hig-2026-06-09`

Reviewer: Peirce (`019eae36-7cb8-7153-b821-42134e6b73d0`)

## Accepted Without Distilled Changes

- `sign-in-with-apple` -> `distilled/sign-in-with-apple.md`
- `split-views` -> `distilled/split-views.md`
- `text-fields` -> `distilled/text-fields.md`
- `text-views` -> `distilled/text-views.md`

## Revised And Resolved

- `siri` -> replaced stale SiriKit/custom-intent guidance with current Siri AI/App Intents/App schema domains guidance.
- `sliders` -> added watchOS scope and current API/routing triggers.
- `spatial-layout` -> scoped to visionOS and added RealityKit/volume/scale/recenter routing.
- `status-bars` -> scoped to iOS/iPadOS and added status bar / scroll edge API triggers.
- `steppers` -> added visionOS and text-field routing.
- `tab-bars` -> added visionOS plus Liquid Glass, minimization, customization, and placement triggers.
- `tab-views` -> scoped to macOS/watchOS and added SwiftUI/watchOS page-control routing.
- `tap-to-pay-on-iphone` -> scoped to iOS and added ProximityReader setup/result/error guidance and triggers.
- `the-menu-bar` -> scoped to iPadOS/macOS and added command/menu-extra/status-bar/keyboard routing.

## Result

Batch H is ready to mark as current-source reviewed. Changes were regenerated into `routing-index.md` and validated with zero corpus errors.

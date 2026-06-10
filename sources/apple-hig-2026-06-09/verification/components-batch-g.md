# Components Batch G Verification

Source corpus: `sources/apple-hig-2026-06-09`

Reviewer: Confucius (`019eae2a-4945-77a2-a722-235b8d1ea59b`)

## Accepted Without Distilled Changes

- `progress-indicators` -> `distilled/progress-indicators.md`
- `settings` -> `distilled/settings.md`
- `shazamkit` -> `distilled/shazamkit.md`

These files were checked against the current rendered Apple HIG source and remained appropriately compressed for trigger-based agent use.

## Revised And Resolved

- `popovers` -> added visionOS, SwiftUI/AppKit triggers, and action-sheet/alert routing.
- `printing` -> added visionOS and `NSDocument` trigger.
- `pull-down-buttons` -> added visionOS and current menu/action triggers.
- `rating-indicators` -> scoped to macOS and added `NSLevelIndicator.Style.rating`.
- `ratings-and-reviews` -> added `RequestReviewAction` and platform-qualified system prompt guidance.
- `remotes` -> scoped to tvOS and corrected `clickpad`/channel-navigation triggers.
- `researchkit` -> scoped to iOS/iPadOS.
- `scroll-views` -> added Look to Scroll and current scroll-edge-effect triggers/guidance.
- `search-fields` -> added current search API triggers and updated iOS tab terminology to Standard tab / Button appearance.
- `searching` -> added suggestions, Core Spotlight, Quick Look, and import-extension triggers.
- `segmented-controls` -> added visionOS and SwiftUI/AppKit momentary-tracking triggers.
- `shareplay` -> added visionOS, GroupActivities/SystemCoordinator/spatial-template triggers, and app-not-installed handling.
- `sheets` -> added current sheet/detent/modal triggers and March 2026 button-placement guidance.
- `sidebars` -> added visionOS and current split/sidebar/background-extension triggers; removed duplicate trigger.

## Result

Batch G is ready to mark as current-source reviewed. Changes were regenerated into `routing-index.md` and validated with zero corpus errors.

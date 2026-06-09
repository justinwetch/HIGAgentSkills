# Full Fidelity Audit Manifest

Date: 2026-06-09

Purpose: second-pass source-fidelity audit for every distilled Apple HIG entry, following `process.md` Goal-Mode Strategy.

Coverage target: 156 distilled files, each audited exactly once in the batch list below. Batch 1 starts with the practice-run findings so known risks are rechecked and remediated first.

Required auditor output schema:

`slug | ACCEPTED/REVISE/NEEDS-SOURCE-REVIEW | P1/P2/P3/Info | source evidence | required fix`

Severity:

- `P1`: missing/wrong guidance that could materially mislead an agent.
- `P2`: source fidelity or routing issue likely to affect real use.
- `P3`: minor trigger, related, wording, or compression issue.
- `Info`: accepted or intentionally documented overlap.

## Batches

- B01: `feedback`, `lists-and-tables`, `toolbars`, `text-fields`, `controls`, `token-fields`, `sidebars`, `widgets`
- B02: `branding`, `icons`, `motion`, `right-to-left`, `writing`, `charts`, `loading`, `progress-indicators`, `entering-data`, `playing-audio`, `playing-video`, `launching`
- B03: `offering-help`, `onboarding`, `settings`, `mac-catalyst`, `icloud`, `image-views`, `text-views`, `shazamkit`, `accessibility`, `color`, `dark-mode`, `design-principles`
- B04: `images`, `inclusion`, `layout`, `materials`, `privacy`, `sf-symbols`, `typography`, `designing-for-games`, `designing-for-ios`, `designing-for-ipados`, `designing-for-macos`, `designing-for-tvos`
- B05: `designing-for-visionos`, `designing-for-watchos`, `snippets`, `managing-accounts`, `collections`, `labels`, `scroll-views`, `column-views`, `live-photos`, `outline-views`, `web-views`, `action-button`
- B06: `buttons`, `disclosure-controls`, `gauges`, `page-controls`, `pickers`, `pop-up-buttons`, `pull-down-buttons`, `search-fields`, `segmented-controls`, `sliders`, `toggles`, `virtual-keyboards`
- B07: `color-wells`, `combo-boxes`, `digit-entry-views`, `image-wells`, `path-controls`, `rating-indicators`, `steppers`, `boxes`, `dock-menus`, `panels`, `tab-views`, `split-views`
- B08: `tab-bars`, `the-menu-bar`, `windows`, `action-sheets`, `activity-views`, `alerts`, `context-menus`, `menus`, `popovers`, `sheets`, `live-activities`, `notifications`
- B09: `status-bars`, `remotes`, `top-shelf`, `lockups`, `activity-rings`, `complications`, `digital-crown`, `watch-faces`, `app-icons`, `voiceover`, `charting-data`, `file-management`
- B10: `keyboards`, `drag-and-drop`, `edit-menus`, `focus-and-selection`, `game-controls`, `gestures`, `modality`, `pointing-devices`, `searching`, `undo-and-redo`, `always-on`, `going-full-screen`
- B11: `home-screen-quick-actions`, `multitasking`, `playing-haptics`, `printing`, `collaboration-and-sharing`, `ratings-and-reviews`, `eyes`, `immersive-experiences`, `ornaments`, `spatial-layout`, `carplay`, `app-clips`
- B12: `app-shortcuts`, `apple-pay`, `apple-pencil-and-scribble`, `augmented-reality`, `camera-control`, `game-center`, `generative-ai`, `healthkit`, `homekit`, `imessage-apps-and-stickers`, `in-app-purchase`, `live-viewing-apps`
- B13: `machine-learning`, `maps`, `shareplay`, `sign-in-with-apple`, `siri`, `tap-to-pay-on-iphone`, `wallet`, `workouts`, `airplay`, `carekit`, `gyro-and-accelerometer`, `id-verifier`
- B14: `nearby-interactions`, `nfc`, `photo-editing`, `researchkit`

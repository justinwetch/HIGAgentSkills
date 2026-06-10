# Full Fidelity Audit Results

Source corpus: `sources/apple-hig-2026-06-09`

Audit scope: all 156 distilled files, organized by `full-audit-manifest.md`.

Method: read-only subagents compared each rendered source page with its distilled file. Main-agent integration checked current local rendered source before patching, then updated distilled files, metadata, routing, and disposition artifacts.

## Batch Outcomes

| Batch | Slugs audited | Outcome |
|---|---|---|
| B01 | `feedback`, `lists-and-tables`, `toolbars`, `text-fields`, `controls`, `token-fields`, `sidebars`, `widgets` | 8 revised; all findings remediated |
| B02 | `branding`, `icons`, `motion`, `right-to-left`, `writing`, `charts`, `loading`, `progress-indicators`, `entering-data`, `playing-audio`, `playing-video`, `launching` | 10 revised; `branding` and `right-to-left` accepted |
| B03 | `offering-help`, `onboarding`, `settings`, `mac-catalyst`, `icloud`, `image-views`, `text-views`, `shazamkit`, `accessibility`, `color`, `dark-mode`, `design-principles` | 12 revised; all findings remediated |
| B04 | `images`, `inclusion`, `layout`, `materials`, `privacy`, `sf-symbols`, `typography`, `designing-for-games`, `designing-for-ios`, `designing-for-ipados`, `designing-for-macos`, `designing-for-tvos` | 8 revised; remaining files accepted |
| B05 | `designing-for-visionos`, `designing-for-watchos`, `snippets`, `managing-accounts`, `collections`, `labels`, `scroll-views`, `column-views`, `live-photos`, `outline-views`, `web-views`, `action-button` | 10 revised; `snippets` and `web-views` accepted |
| B06 | `buttons`, `disclosure-controls`, `gauges`, `page-controls`, `pickers`, `pop-up-buttons`, `pull-down-buttons`, `search-fields`, `segmented-controls`, `sliders`, `toggles`, `virtual-keyboards` | 9 revised; `pickers`, `pop-up-buttons`, and `toggles` accepted |
| B07 | `color-wells`, `combo-boxes`, `digit-entry-views`, `image-wells`, `path-controls`, `rating-indicators`, `steppers`, `boxes`, `dock-menus`, `panels`, `tab-views`, `split-views` | 8 revised; remaining files accepted |
| B08 | `tab-bars`, `the-menu-bar`, `windows`, `action-sheets`, `activity-views`, `alerts`, `context-menus`, `menus`, `popovers`, `sheets`, `live-activities`, `notifications` | 8 revised or previously remediated; remaining files accepted |
| B09 | `status-bars`, `remotes`, `top-shelf`, `lockups`, `activity-rings`, `complications`, `digital-crown`, `watch-faces`, `app-icons`, `voiceover`, `charting-data`, `file-management` | 5 revised or previously remediated; remaining files accepted |
| B10 | `keyboards`, `drag-and-drop`, `edit-menus`, `focus-and-selection`, `game-controls`, `gestures`, `modality`, `pointing-devices`, `searching`, `undo-and-redo`, `always-on`, `going-full-screen` | 8 revised; remaining files accepted |
| B11 | `home-screen-quick-actions`, `multitasking`, `playing-haptics`, `printing`, `collaboration-and-sharing`, `ratings-and-reviews`, `eyes`, `immersive-experiences`, `ornaments`, `spatial-layout`, `carplay`, `app-clips` | 10 revised; `playing-haptics` and `collaboration-and-sharing` accepted |
| B12 | `app-shortcuts`, `apple-pay`, `apple-pencil-and-scribble`, `augmented-reality`, `camera-control`, `game-center`, `generative-ai`, `healthkit`, `homekit`, `imessage-apps-and-stickers`, `in-app-purchase`, `live-viewing-apps` | 11 revised; `imessage-apps-and-stickers` accepted |
| B13 | `machine-learning`, `maps`, `shareplay`, `sign-in-with-apple`, `siri`, `tap-to-pay-on-iphone`, `wallet`, `workouts`, `airplay`, `carekit`, `gyro-and-accelerometer`, `id-verifier` | 6 revised or previously remediated; remaining files accepted |
| B14 | `nearby-interactions`, `nfc`, `photo-editing`, `researchkit` | 4 revised; all findings remediated |

## Defect Rate

All 156 files received second-pass source-fidelity coverage. The audit produced source-backed or routing-backed changes in 117 files, a 75% file-level revision rate. This is high, but the distribution matters:

- Most findings were P2/P3 fidelity, trigger, related-routing, platform-scope, or spec-table compression issues.
- The highest-risk class was unsupported stale guidance that survived from the prior HIG version.
- The second-highest-risk class was over-compression of exact specifications, especially dimensions, API names, and platform-specific behavior.
- No `NEEDS-SOURCE-REVIEW` items remain after checking the local rendered source corpus.

## Remediation Summary

The integration pass remediated all `REVISE` findings by:

- Removing unsupported old guidance and broad triggers.
- Restoring exact measurements and platform distinctions where the source uses tables.
- Adding missing API/framework triggers where current source names them.
- Tightening related routing to current source links and strong in-page references.
- Moving broad design-principles routing into tier 1 so design judgment queries load it immediately.
- Updating `disposition-overrides.json`, `inventory.json`, `dispositions.md`, `routing-index.md`, and `README.md` after source-backed edits.

## Accepted Warning Classes

Remaining validator warnings are cross-file trigger overlaps. They are accepted as intentional routing overlaps when:

- A foundation file and a detailed topic share a concept.
- A platform overview and a component/pattern file share an Apple term.
- An API legitimately appears in adjacent topics.
- A feature family needs adjacent context, such as Siri/App Shortcuts/Snippets or HealthKit/Activity Rings.

There are no within-file duplicate trigger warnings.

## Result

Status: accepted after remediation.

No unremediated source-drift findings are deferred from the full-audit batches.

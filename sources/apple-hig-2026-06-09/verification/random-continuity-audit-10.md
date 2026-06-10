# Random Continuity Audit - 10 Entries

Compared current `ios27` distills against `origin/main` prior distills.

Random seed: `20260611`

Excluded prior continuity sample: `file-management`, `apple-pencil-and-scribble`, `wallet`, `gestures`, `designing-for-games`.

Sample universe: 145 distilled files present in both current branch and `origin/main` after exclusions.

Sampled files:

- `virtual-keyboards`
- `live-photos`
- `segmented-controls`
- `text-fields`
- `id-verifier`
- `designing-for-macos`
- `disclosure-controls`
- `action-sheets`
- `app-icons`
- `boxes`

## Results

| Slug | Result | Notes |
|---|---|---|
| `virtual-keyboards` | Pass | Current file preserves prior keyboard-extension/custom-input guidance and adds source-backed watchOS availability plus API triggers. |
| `live-photos` | Pass | Current file preserves edit/intact/share/download/badge rules, adds source-backed visionOS view-only note and LivePhotosKit JS trigger. |
| `segmented-controls` | Pass | Current file correctly updates prior stricter "text or images, not both" wording to current-source "prefer either text or images, not a mix"; adds visionOS and momentary API triggers. |
| `text-fields` | Pass | Current related routing aligns with current source links: text views, combo boxes, virtual keyboards, and entering data. No old source-backed guidance lost. |
| `id-verifier` | Pass | Current file corrects platform scope to iOS, removes unsupported `MRZ`, adds current ProximityReader APIs, and preserves age/data-minimization and button-label guidance. |
| `designing-for-macos` | Pass | Only continuity-relevant change is removing the old Sidecar-specific wording; current source says additional displays including iPad. |
| `disclosure-controls` | Pass | Current file preserves triangle/button behavior and adds source-backed visionOS, AppKit API names, and buttons related routing. |
| `action-sheets` | Pass | Current file preserves old action-sheet rules and adds source-backed watchOS support and current SwiftUI/UIKit APIs while removing stale `UIActionSheet`. |
| `app-icons` | Pass | Current file preserves icon sizes, safe zones, alternate-icon, text/photo/hardware prohibitions, and updates Icon Composer/Liquid Glass guidance from current source. |
| `boxes` | Pass | Current file preserves box title, nested-box, padding, and platform behavior; adds source-backed visionOS support. |

## Incidence

This 10-entry sample found `0/10` new continuity regressions.

Combined with the prior 5-entry continuity sample, continuity-specific findings are `1/15` sampled files after one `wallet` remediation. The observed rate is therefore about 6.7%, but the sample is still too small to treat continuity risk as zero.

## Outcome

No changes required from this 10-entry sample.

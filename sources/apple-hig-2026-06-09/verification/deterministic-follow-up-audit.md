# Deterministic Follow-Up Audit

Source corpus: `sources/apple-hig-2026-06-09`

Sample seed: `20260609`

Reviewer: Kepler (`019eae50-0250-7972-b256-152c1eb86ea0`)

## Sample Results

| Slug | Result |
|---|---|
| `gauges` | Accepted; duplicate trigger issue resolved |
| `airplay` | Accepted |
| `controls` | Accepted |
| `designing-for-macos` | Accepted |
| `sidebars` | Revised; Liquid Glass/background-extension guidance scoped to iOS, iPadOS, and macOS |
| `shareplay` | Accepted |
| `app-shortcuts` | Accepted |
| `pop-up-buttons` | Accepted |
| `windows` | Revised; added plain-window style note |
| `camera-control` | Accepted |
| `dark-mode` | Accepted |
| `action-sheets` | Revised; replaced stale `UIActionSheet` trigger with current APIs |

## Adjacent-Category Follow-Up

Reviewer: Archimedes (`019eae55-8a22-7ce2-a0e1-ff138dd4156c`)

Triggered by substantive findings in `sidebars`, `windows`, and `action-sheets`.

| Slug | Result |
|---|---|
| `sidebars` | Revised; iOS/iPadOS guidance reframed around adaptable sidebar/tab bar behavior and source-related `layout` |
| `windows` | Accepted after plain-window note |
| `split-views` | Revised; related routing aligned to `sidebars`, `tab-bars`, `layout` |
| `tab-bars` | Accepted |
| `outline-views` | Revised; related routing aligned to `column-views`, `lists-and-tables`, `split-views` |
| `action-sheets` | Accepted after API trigger fix |
| `alerts` | Revised; related routing includes `sheets` and removes unsupported `writing` |
| `sheets` | Revised; related routing includes `panels` |
| `popovers` | Accepted |
| `modality` | Revised; added sheets/popovers distinct-task guidance and `activity-views` routing |

## Result

Follow-up audit findings were remediated and recorded in `final-audit-remediation.md`.

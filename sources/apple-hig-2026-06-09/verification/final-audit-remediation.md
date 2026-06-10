# Final Audit Remediation

Source corpus: `sources/apple-hig-2026-06-09`

This note records remediation from the post-update caveat audit and random source audit.

## Source-Drift Fixes Applied

- `charting-data` -> removed unsupported scatter/Audio Graphs wording; preserved current-source accessibility labels/elements requirement.
- `sign-in-with-apple` -> added prominent/no-smaller/no-scroll Sign in with Apple button rule and private relay identification guidance.
- `sheets` -> removed unsupported macOS bottom-trailing dismiss-button placement and unsupported watchOS Done/toolbar detail.
- `menus` -> corrected submenu threshold from `2+` to "more than two."
- `widgets` -> added automatic-vs-configurable content, rasterized-text prohibition, Dynamic Type Large-through-AX5 support, and light/dark full-color guidance.
- `sidebars` -> scoped Liquid Glass/background-extension guidance to iOS, iPadOS, and macOS.
- `windows` -> added the `PlainWindowStyle` note that plain windows omit the glass background.
- `action-sheets` -> replaced stale `UIActionSheet` trigger with current `confirmationDialog` and `UIAlertController.Style.actionSheet` triggers.
- Adjacent-category audit follow-up -> aligned related routing for `sidebars`, `split-views`, `outline-views`, `alerts`, `sheets`, and `modality`; added modality guidance for sheets/popovers as scoped distinct-task presentations.

## Routing Caveats Fixed

- Removed case-only duplicate triggers in `gauges` and `lists-and-tables`.
- Qualified broad collision triggers for notification Focus, Liquid Glass tab bars, ornament TabView routing, and Apple Pay Wallet routing.
- Removed the redundant `look`/`Look to Scroll` duplicate from scroll views while keeping `Look to Scroll`.

## Accepted Remaining Warning Classes

Remaining validation warnings are accepted cross-file trigger overlaps. They represent intentional adjacent routing for:

- Tier-1/foundation concepts that are always loaded, such as glyphs, labels, localization, placeholder text, and vibrancy.
- Platform overview plus detailed topic pairs, such as split view, pointer, Stage Manager, Siri Remote, watch faces, and complications.
- API names that legitimately span adjacent topics, such as `NavigationSplitView`, `UISplitViewController`, `MenuPickerStyle`, `ScrollEdgeEffectStyle`, `RealityKit`, and `ProximityReader`.
- Closely related feature families, such as Siri/App Shortcuts/Snippets, Activity rings/HealthKit, Wallet/Apple Pay, and feedback/haptics.

There are no remaining within-file duplicate-trigger warnings after remediation.

## Validation State

After remediation, `scripts/validate_corpus.py` reports `errors: 0`. The remaining warnings are documented above as intentional routing overlaps.

## Full-Audit Follow-Up

The earlier next action item for an expanded audit is superseded by `full-audit-results.md`, which records second-pass coverage for all 156 distilled files. No source-drift findings remain deferred from that full audit.

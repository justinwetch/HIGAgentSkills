# Random Continuity and Skill Compliance Audit

Compared current `ios27` distills against `origin/main` prior distills.

Random seed: `20260610`

Sample universe: 150 distilled files present in both current branch and `origin/main`.

Sampled files:

- `file-management`
- `apple-pencil-and-scribble`
- `wallet`
- `gestures`
- `designing-for-games`

## Continuity Results

| Slug | Result | Notes |
|---|---|---|
| `file-management` | Pass | Current file preserves prior core guidance and adds source-backed macOS/visionOS, `DocumentGroupLaunchScene`, File Provider, and Finder Sync coverage. |
| `apple-pencil-and-scribble` | Pass | Current file preserves Pencil/Scribble behavior, corrects platform scope to iPadOS, removes unsupported `drag-and-drop` related routing, and adds source-backed PaperKit/App Shortcuts details. |
| `wallet` | Fixed during audit | Random comparison found continuity/source regression: current file had dropped explicit expiration/relevant-date/voided pass properties, change-message restrictions, and field-role detail that existed in `origin/main` and remains in current Apple source. Restored compact source-backed bullets. |
| `gestures` | Pass | Current file preserves prior standard/custom gesture guidance and adds source-backed visionOS system overlay and watchOS Double Tap API details. |
| `designing-for-games` | Pass | Current file preserves prior game design guidance; visionOS table now matches current source (`Touch`) while retaining a clarifying note about eyes/hands and indirect/direct gestures. |

## Skill Compliance Results

Checked against Agent Skills spec, Claude Code skill behavior, and OpenAI hosted skill limits.

| Check | Result | Evidence |
|---|---|---|
| Single `SKILL.md` | Pass | One manifest found: root `SKILL.md`. |
| Skill name | Pass with packaging caveat | `apple-hig`, 9 chars, lowercase/hyphen valid. Spec requires name to match parent directory; install/package folder should be named `apple-hig`, not the local workspace folder `AppleHIG`. |
| Description length | Pass | Folded description is 591 chars; Agent Skills spec cap is 1,024 chars. Claude Code listing cap is 1,536 chars for combined `description` + `when_to_use`; no `when_to_use` is present. |
| `SKILL.md` length | Pass | 87 lines, below the 500-line recommendation. |
| OpenAI hosted file count | Pass for clean checkout/runtime package; caution for dirty workspace zip | Tracked clean checkout: 187 files; runtime-only package: 167 files. Current local working directory without `.git` has 542 files because ignored raw/rendered source captures are present; do not zip the whole workspace with ignored files included for hosted upload. |
| OpenAI hosted file size | Pass | Runtime-only package: ~0.63 MB; clean checkout is under 50 MB; largest runtime file is `distilled/typography.md` at ~31.9 KB, far below 25 MB. |
| Corpus structural validation | Pass | `python scripts/validate_corpus.py` reports `errors: 0`; remaining warnings are documented cross-file trigger overlaps. |
| Routing index | Pass | `python scripts/generate_routing_index.py --check` reports current. |

## Outcome

Continuity sanity check passes after the `wallet` remediation. Technical installability passes if the skill is packaged from a clean checkout or runtime-only folder named `apple-hig`.

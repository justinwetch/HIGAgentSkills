# Shipping assessment — 2026-09-27

**Scope:**
- ordinary Apple HIG guidance;
- opt-in enforce mode;
- a new guided **Duo mode** that adapts an existing iOS app to iPhone Duo in the app's own native code.

There is no browser intake, onboarding site, dashboard or setup-server dependency.

## Corpus

All 157 references were revised for fidelity-first compression. **261,621 source guidance words become 90,027, a 65.589% reduction**, up from 108,246 words (58.625%) in the 2026-09-21 release.

- 106 topics changed. Every topic rewritten from Apple's source was independently re-reviewed against the 2026-09-12 capture.
- Other changed topics received only a narrow removal of source-narration lines, keeping every operative fact.
- `home-screen-quick-actions` now lists `menus` as related, since Apple's page points there.
- The 16 mandatory foundations are preserved.

Full reference files total **163,033 o200k_base / 162,491 cl100k_base tokens**. The foundations alone total **27,096 / 26,936**. Per-topic hashes and counts are in [`topics.csv`](../corpus-2026-09-12/topics.csv).

## Duo mode

`/duo [journey]`, or "Use apple-hig in Duo mode", runs fixed stages:

**resume → assess → match → decide → build → verify**

- **Assess, match, decide:** the agent inspects the app's code and matches it against [a checklist](../../references/duo-checklist.md). It then recommends options and stops for the user's choices.
- **Build:** it builds the chosen changes natively in Apple's order.
- **Verify:** it reports each check as run or not run.
- **Notes:** a short `duo-notes.md` in the app project carries decisions across sessions.
- **Command:** `commands/duo.md` is part of the install. Some hosts pick it up from the skill folder; others need it copied into their custom command or prompt directory, which SKILL.md and README now tell the agent to do during installation.
- **No mockups:** HTML, SVG and web mockups are prohibited outright. The retired 2026-09 feature failed because it allowed them.

The checklist paraphrases the iPhone Duo HIG reference and six Apple tech talks (linked in it), with a source tag on every item.
- An independent reviewer checked it against the HIG file and the talk transcripts. All 8 medium and 9 low findings were fixed, and none were high.
- Five claimed conflicts between the HIG and the talks turned out to be consistent guidance, so they were folded into plain rules. Four genuine tensions remain listed for the user to decide.

## Duo mode trials

The workflow was trialled on a native SwiftUI fixture: a 10-file reading app with planted adaptation problems. Each run was a fresh agent using the shipped command and skill.

**Trial 1:** `/duo the library and reading flow`
- It assessed the code only and said so.
- It matched against the checklist and presented a sourced decision table.
- It wrote `duo-notes.md` and stopped for the user.
- It produced no HTML, SVG or CSS.

**Trial 2:** `/duo continue — go with your recommendations`, in a new session
- It resumed from the notes and edited five app files natively: managed toolbar, split view, size-class layout, titled symbols and a non-ellipsis sort menu.
- It left the unconfirmable iOS 27.1 API signatures as marked TODOs.
- It reported the build, previews and simulator checks as not run, because no Xcode was available.

Instruction ambiguities found in the trials were fixed in `references/duo.md`:
- routing of the two Duo topics;
- the notes-file length cap;
- recording recommendations as pending decisions;
- how to handle API signatures;
- honest preview offers;
- resuming without repeating stages.

The trials show the agent following the workflow. They are not a compiled build and do not certify behavior on a native device.

## Package

The candidate contains **167 files**: the previous 166, plus `references/duo.md`, `references/duo-checklist.md` and `commands/duo.md`, minus the two README images. The packaged README links its header image and the /duo still from GitHub instead, which cuts the ZIP from about 3.2 MB to 386 KB.
- Two builds are byte-identical.
- A clean extraction passes exact membership, hashes, routing/frontmatter and 13 local links.
- **35 helper tests pass.**
- The runtime skill, README and maintainer records name no specific agent host or model; maintainer records use drafting and review tiers.

`.gitattributes` now keeps text files LF in every checkout, so manifest hashes are the same on any platform.

The full shipped text totals **187,987 o200k_base / 187,401 cl100k_base tokens** (tiktoken 0.14.0). Normal requests load only a relevant subset.
- `SKILL.md` plus `README.md` total 4,154 / 4,148.
- Duo mode's three files total 5,658 / 5,651, loaded only in Duo mode.

## Remaining limits

- Automatic discovery has not been tested in every host.
- Duo mode's native output has not been compiled or run on the iPhone Duo simulator or a device in these trials.
- Enforce still requires two independent reviewers, Python 3.10+ and suitable observation tools.
- No claim is made of native folding, VoiceOver or six-platform runtime certification.

## Reproduce

From the repository root, with the maintenance dependencies available:

```text
python -m unittest discover -s tests -p "test_hig_*.py"
python scripts/package_runtime_zip.py --output work/release-check.zip
python scripts/validate_hig_runtime.py --root <clean-extraction>/apple-hig --manifest sources/apple-hig-2026-09-12/verification/shipping-manifest-2026-09-27.json --output work/release-check.json
python -X utf8 scripts/measure_hig_release.py --candidates references/hig --output work/release-check-measurements.json
```

The compact result is `verification.json` beside this document. The full local outputs, trial fixture and transcripts are under `work/` (local only).

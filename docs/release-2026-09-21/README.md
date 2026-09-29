# Shipping assessment — 2026-09-21

Scope: the Apple HIG reference skill and opt-in enforce mode. The standalone Duo
redesign feature, command, profile/supplement, session helper, tests and README
illustration have been removed from the active product. Apple’s iPhone Duo HIG
reference guidance remains, as requested. There is no browser intake, onboarding
site, dashboard or setup-server dependency.

156 HIG references are byte-identical to the accepted September corpus;
`designing-for-iphone-duo` was revised on 2026-09-23 (see below). 261,621 source
guidance words become 108,246 words, a **58.625%** reduction.
The 16 mandatory foundations are preserved. Independent review reconfirmed the
accepted reference hashes and all 11 linked assembly evidence hashes.

The candidate contains **166 files**. Two builds are byte-identical; clean
extraction passes exact membership, hashes, routing/frontmatter and local links.
**35 helper tests pass**, including explicit target exclusions, source validation,
evidence gates, score calculation, regression handling and output protection.

Historical real enforce observations remain valid evidence for unchanged behavior:
**68.75 needs changes → 100 pass → 93.75 needs changes → 100 pass**. The third
result rejected an introduced accessibility regression despite clearing the score
threshold. An independent reviewer checked the saved A/B review/evidence hashes.
This is a bounded actual fix/re-review exercise, not native-device certification.

A fresh agent answered the setup/help request from the extracted
candidate using only `SKILL.md` and `README.md`. It correctly identified the release,
ordinary/enforce modes, optional versus required Python use, installation locations
and absence of a browser requirement. Those two complete files total **2,996
o200k_base / 3,006 cl100k_base tokens**; this is static text volume, not billing.
No HIG references were needed for that observed help response.

The full shipped text totals **218,490 o200k_base / 216,953 cl100k_base tokens**
using tiktoken 0.14.0, counted from the package members (the pre-revision package
measures 217,784 / 216,260 the same way). Those totals include all references and
helpers; normal requests load a relevant subset. The corpus alone is 200,088 / 198,647.

## Revision 2026-09-23

A fresh pre-release review found and fixed the following before shipping:

- **Skill description** had unintentionally lost its platform, framework and
  "any digital interface" discovery wording; restored, adding OS 27 and iPhone Duo.
- **Routing helper** crashed on Windows for requests containing emoji or non-Latin
  text, missed plural/hyphenated forms (`tab bars`, `games`, `full-screen`) and bare
  API symbols, and wrote request files into the user's project. It now emits UTF-8,
  reads UTF-8 or UTF-16 input (or stdin), matches those forms, reports errors without
  a traceback, and SKILL.md places the request file outside the project.
- **Duo triggers** `duo`, `vertical controls` and `arrangement view` fired on
  unrelated requests (duo-tone, Google Duo, DAW arrangement view); removed, and
  `foldable iPhone` added.
- **Duo reference** restored source conditions and recommendation strength (e.g.
  "wider and shorter *than other iPhone displays*", "*Consider* the full display
  width for interfaces *where bars aren't necessary*", pane-specific controls stay
  with their pane), re-reviewed independently against the captured source.
- **Enforce helper** accepts BOM-prefixed JSON and returns `blocked` instead of
  crashing on a malformed `--previous` result. Scoring logic is unchanged.
- **Committed audit records** no longer contain absolute local paths; links from
  published docs into ignored `work/` evidence are marked local-only.

The fresh setup/help trial above used the pre-revision `SKILL.md`; the entry-point
protocol is unchanged apart from the description, request-file location and the
matching note.

## Remaining limits

- Automatic discovery and upgrades have not been tested in every host or on the
  user's MacBook. README now supplies supported host locations, explicit version
  identification and a setup check; the isolated help trial is not discovery proof.
- Enforce requires two independent reviewers, Python 3.10+ and suitable observation
  tools. Missing capabilities/evidence remain blocked. No pass is implied by hashes
  or scoring alone. Scored checks remain frozen within a run; genuinely changed
  scope requires a new run with old unresolved findings kept visible.
- No claim of native folding, VoiceOver or six-platform runtime certification is
  made. The accepted source corpus and reference-skill functionality are distinct
  from certification of an application using it.

These limits do not block shipping the stated reference/review product. No install,
push or publication has been performed. Previous diagnostic runs remain ignored
historical evidence under `work/`; they are not active features or package members.

## Reproduce

From the repository root with the maintenance dependencies available:

```text
python -m unittest discover -s tests -p "test_hig_*.py"
python scripts/package_runtime_zip.py --output work/release-check.zip
python scripts/validate_hig_runtime.py --root <clean-extraction>/apple-hig --manifest sources/apple-hig-2026-09-12/verification/shipping-manifest-2026-09-21.json --output work/release-check.json
```

The package manifest pins every shipped byte. The clean extraction must be new
and contain only the archive's members. Helper scripts shipped to users require
only Python's standard library; Markdown validation/token measurement dependencies
are maintainer-only. Full local outputs are under
`work/ship-without-duo-2026-09-21/`; the compact final result is `verification.json`
beside this document. Prior corpus and observed enforce evidence are retained in
`docs/corpus-2026-09-12/` and
`sources/apple-hig-2026-09-12/verification/enforce-runtime-2026-09-14.json`.

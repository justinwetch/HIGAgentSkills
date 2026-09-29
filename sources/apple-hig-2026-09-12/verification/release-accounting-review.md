# Independent source-accounting review — pass after repair

Scope: Chunk 1 C1/C3/C6 accounting method only. Independent review-tier reviewer; did not author or edit generator, sources, registers, or candidates. No whole-corpus semantic-fidelity acceptance is claimed. Decision-making move: check what the choice depends on, by testing counterexamples to a lossless canonical-source denominator.

## Evidence that passes

- Independently verified all 346 available source file hashes and byte sizes against inventory, with zero mismatches.
- Parsed all 173 source JSON pages and all registers. All 7,642 primary blocks map bijectively to register pointers, with no extra/missing/duplicate pointers and no raw node differences. Every one of 16,583 primary text leaves appears in its rendered block. This checks structural coverage, not semantic reconstruction.
- All 17 primary AST kinds are recognized; all 294 tables use row headers. No missing linked reference entries; all 61 video occurrences render nonempty source text. The 719 language-variant patches change API reference titles/fragments/navigator titles, not primary guidance.
- Privacy `/primaryContentSections/0/content/24` retains both cancel/close captions that native export omits. Typography retains `small` footnotes and tab/table content absent from native text. Layout `/primaryContentSections/0/content/64` exposes `isAutorotating` deprecation metadata. Playing Haptics `/primaryContentSections/0/content/31` retains both Selection caption and video description.
- Resources cutoff inspection found expected resource headings/links/change-log tables, with no detected long source prose paragraph after cutoff. Collection dispositions belong to the separate reviewer.

## Initial findings (preserved; resolved below)

1. **Merged-cell relationships are invisible in the read aid.** Nine `table.extendedData` nodes survive in raw but do not render: Apple Pay content/118, HomeKit content/48, Icons content/26,28,32,34,36, Widgets content/142, Workouts content/10. Apple Pay's Buy/Check Out/Donate/Set Up/Subscribe rows inherit the Book row's 140pt minimum width, 30pt minimum height and 1/10-height margins. Native Markdown uses `^`; the aid currently presents blanks. Render the relationship or add an explicit review warning excluded from counts. Do not expand merged cells into repeated denominator text.
2. **Nested list context flattens.** Game Center content/39 has classic and recurring leaderboard parents, each owning example bullets. Indent nested/continuation content so the reading aid preserves association.
3. **Minor tab-label double count.** Typography has 23 exact tab-title/first-heading duplicates, adding 31 words. Deduplicate the identical displayed label, retaining raw fields. This is minor, not a material 75% threshold issue.
4. **Output guidance must count wherever placed.** The measurement script correctly includes body comments and Resources sections, but permitted frontmatter fields can contain uncounted instructions. Constrain and audit excluded values as routing-only or count them. Count substantive guidance in any packaged sidecar as well. A partial candidate subset must not be called corpus-wide.

## Limits and acceptance rule

C1 raw block preservation passes; complete C1 dispositions are separate. C3 method needs the bounded revisions above. C6 independent review is satisfied only for this review, not the rest of the release workflow. No external visual/audio inspection occurred. Native Markdown alone is insufficient for captions, footnotes, deprecated API flags and table spans. The register is a reading aid with raw evidence, not an automatic semantic substitute.

The denominator currently includes figure descriptions, including decorative alt text, and counts repeated source occurrences. State that definition; 75% remains a corpus heuristic rather than a fidelity score or per-file quota. Unlinked reference dictionaries must not be counted wholesale as guidance. Current output-body accounting properly avoids hiding guidance in body Resources/comments; equivalent treatment is needed for all other output locations.

Full hashes, source pointers, actual read scopes, measurements and machine-readable findings are in `accounting-review.json`. Sources were parsed across the corpus; native human reading was targeted to Privacy, Typography, Layout, Playing Haptics, Apple Pay and Workouts. Other native files were hash-verified only. Generator edits during review are disclosed in JSON; repairs need a targeted independent rereview bound to updated hashes.

## Targeted repair acceptance

**PASS for the Chunk 1 source-accounting method gate.** Independently inspected the changed scripts, regenerated source-reading examples, register metadata and actual pilot measurement report. Recompared all 7,642 primary raw nodes to original JSON: zero mismatches. All nine span tables have exact original pointers/span metadata plus a visible caution before the storage-cell view. These cautions remain outside counted block text. Game Center nested examples now indent correctly. Typography identical tab/first-heading duplication is removed without altering raw nodes.

Every topic metric now explicitly requires a semantic reviewer to verify that excluded frontmatter is routing-only. That obligation is part of the method; it is not proof of candidate compliance. Final release acceptance must still count guidance in any packaged sidecar/field and distinguish partial measurement from full-corpus accounting.

Actual five-topic pilot report: 13,756 source words, 5,195 output words, **62.235% ratio-of-totals reduction**. The report declares 5 measured candidates out of 157 mapped topics, with named `o200k_base` and `cl100k_base` encodings and tiktoken 0.14.0. No full-corpus compression or content acceptance is inferred. Token values were inspected in the generated artifact; no independent tokenization replay or semantic candidate audit was performed in this source-accounting review.

Final hash bindings:

- `scripts/hig_source_blocks.py`: `e36ecf107f82e9378b8f81e292b468dd85436c720cf665345d755acfaba501b4`
- `scripts/measure_hig_release.py`: `1aaac0b76251917d6f30c34f1fe198d460c264f44200eb85589e736acd7c297a`
- `work/release-2026-09-12/pilot-remeasurement.json`: `e120c9e372290b27e4f6c29e98bc575d99e25efdc96d990726acbce12b0d4c2a`

The machine-readable review preserves the initial revise findings and records their resolutions. C1 raw-block preservation and the defined C3 accounting method pass; disposition acceptance and later fidelity/exam/release checks retain their separate scope.

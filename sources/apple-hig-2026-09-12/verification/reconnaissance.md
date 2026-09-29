# September 12, 2026: source capture and next-version inputs

The source-gathering stage is complete. The existing 156-topic runtime remains the June release; this investigation does not constitute a new distillation or an implemented enforce mode.

## When and how we last updated

Reviewed the full accessible turn history of **Review and update Apple HIG**, task ID `019eadda-9b0d-72c2-8b7a-372ff90e7a66`, together with Git history, `process.md`, and the saved verification notes.

- **Last source refresh: June 9, 2026.** The update worked on branch `ios27`, was integrated into `main`, and ended at commit `701151a` (June 9, 21:34:22, UTC−08:00). That final commit clarified the README installation prompt; the substantive refresh release commit was `4777697` at 21:11:32 the same day.
- The starting corpus contained 150 distilled topics. The source crawl recorded 176 paths, including four aliases. It used Apple's `/tutorials/data/...json` endpoints, saved raw responses, then rendered its own Markdown for distillation.
- Every source received a disposition. Six reference topics were added: Design Principles, Privacy, Controls, Managing Accounts, Snippets, and Token Fields. Managing Notifications was incorporated into Notifications. Collection pages were evaluated rather than automatically made into low-value reference files.
- Distillation and verification proceeded in batches. Read-only subagents compared sources and distills; the main agent checked source evidence and integrated corrections. Routing was regenerated from frontmatter, with schema and related-file validation.
- Early acceptance proved insufficient. Practice audits found revisions needed in 9 of 15 sampled files. The subsequent full second-pass audit covered all 156 files and resulted in changes to **117 files (75%)**. The dominant issues were unsupported old guidance, missing concrete rules/specifications, platform scope, over-compression, and trigger/related-link errors. This is a historical file-level revision rate, not a measured final error rate.
- A later old/new continuity comparison restored omitted Wallet guidance. An additional ten-file continuity sample found no new issues. Trigger testing exposed substring false positives such as `AR` in “tab bar” and `AI` in “explain,” leading to standalone word/phrase/API matching.
- The resulting runtime had 156 files, 16 always-loaded foundations, 1,057 triggers, and a documented rough floor of 33,600 tokens per invocation. It was packaged through a deterministic Python ZIP script and installed and tested in two agent hosts.

Historical effort context: the task's completion messages reported about 1.09 million tokens / 97 minutes for the main update and 463,000 tokens / 24 minutes for the full audit. These are historical task-reported figures, not a forecast for the next run.

Evidence: [full audit](../../apple-hig-2026-06-09/verification/full-audit-results.md), [continuity audit](../../apple-hig-2026-06-09/verification/random-continuity-and-skill-compliance-audit.md), [second continuity sample](../../apple-hig-2026-06-09/verification/random-continuity-audit-10.md), [trigger test](../../apple-hig-2026-06-09/verification/practical-trigger-test.md).

One testing limitation matters for the next version: the trigger-test artifact describes computing loaded-file sets by applying the protocol. That supports routing logic, but does not independently prove actual agent loading behavior or answer quality in fresh production invocations. Future evaluation should retain actual observed file access and answers.

## Native Markdown capture

The screenshot's correction is essential: prepend `/tutorials/data` to the HIG path **and** append `.md`.

```text
https://developer.apple.com/design/human-interface-guidelines/{slug}
→ https://developer.apple.com/tutorials/data/design/human-interface-guidelines/{slug}.md
```

Verified directly against Apple: [root Markdown](https://developer.apple.com/tutorials/data/design/human-interface-guidelines.md) and [iPhone Duo Markdown](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/designing-for-iphone-duo.md). Responses were HTTP 200 with `text/markdown; charset=utf-8`.

Captured September 12, 2026, 21:10–21:11 UTC (13:10–13:11 Anchorage time):

| Coverage | Result |
| --- | --- |
| HIG paths discovered and attempted | 177 |
| Native Apple Markdown pages saved | 173 |
| Raw Apple JSON companions saved | 173 |
| Native Markdown bytes | 2,227,549 |
| New slug relative to June | `designing-for-iphone-duo` |
| Canonical topic gaps / unexplained fetch failures | 0 |
| Unavailable historical aliases | 4 paths, each returning 404 for both formats after three attempts |

Scope: the complete **discoverable English HIG link closure**, including collection pages, checked against the June inventory and all existing distilled slugs. Every discovered HIG path has a capture or an explained failure. This does not claim to include unlinked/unpublished pages, translations, all Apple developer documentation, downloaded media, or video transcripts. Linked API documentation and media references are inventoried separately for later use.

The four unavailable aliases are `components/layout-and-organization/tab-views` → `tab-views`; `components/presentation/page-controls` → `page-controls`; `components/system-experiences/complications` → `complications`; and `spatial-interactions` → `nearby-interactions`. All canonical targets were captured. These mappings were already documented as same-source aliases in June; current links still expose the obsolete paths.

Local files:

- `../native/*.md`: unmodified Apple Markdown responses.
- `../raw/*.json`: unmodified Apple JSON responses.
- `../inventory.json`: identities, URLs, timestamps, HTTP metadata, hashes, sizes, source links, and dispositions.
- `../failures.json`: actual failed fetch records; retained rather than erased after alias explanation.
- `../capture-summary.json`: crawl counts and raw-byte comparison against June.
- `capture-assessment.json`: offline integrity results, explained aliases, comparison categories, and export-check candidates.
- `../supplements/*.md`: 40 generated evidence supplements containing exact JSON blocks with unmatched text and JSON pointers.
- `../diffs/*.diff`: 19 renderer-based comparison files after URL-case normalization, for triage only.
- `../linked-resources.json`: 4,940 source/reference records for linked developer documentation and image/video metadata; these are not 4,940 unique downloaded resources.

Raw captures, supplements, and generated diffs remain local and ignored. Lightweight manifests, this report, and maintenance scripts are trackable. No ZIP, installation, push, or runtime update was performed.

## Native Markdown is useful but not fully faithful by itself

All captured files passed checksum, byte-count, JSON parsing, Markdown/JSON title/identifier, and JSON discovery-closure checks. No Unicode replacement characters were found in the captured source files.

A lexical comparison checked 7,570 distinct text segments within their source pages (at least 30 normalized characters) from JSON primary-content blocks. **156 segments across 40 pages did not match the native Markdown.** This is a screening result, not a semantic coverage percentage or a count of distinct rules lost.

Confirmed missing content includes image-caption guidance and small-print text:

- Privacy: a caption prohibits visual cues that draw attention to the system permission alert's Allow buttons. JSON pointer `/primaryContentSections/0/content/29/tabs/3/content/1/inlineContent/0/metadata/abstract/0/text` contains the text, which is absent from the native Markdown.
- Widgets: the Display Zoom “More Space” footnote is present at `/primaryContentSections/0/content/143/inlineContent/0/text` in JSON but absent from the native Markdown.
- ResearchKit: the informational/legal-advice qualification is a `small` block in JSON and is absent from the native Markdown.

Other candidates include captions explaining correct/incorrect examples, controls, appearance variants, and screenshot states. Each affected page now has a separate generated supplement containing the original enclosing JSON blocks. Apple's native Markdown was not modified. Shorter fragments, table structure, images, link resolution, and semantic equivalence still require deliberate review during distillation.

**Source recommendation:** use native Markdown as the primary reading surface, with JSON, supplements, and relevant visuals as required fidelity checks. The new native endpoint reduces rendering work; it does not eliminate source-preservation work. `doc://` developer references and relative image paths also need their JSON reference metadata for reliable resolution.

## What changed since June

Every comparable raw JSON hash changed. That fact alone would wildly overstate editorial change. Using the same existing renderer on both snapshots:

| Triage category | Pages |
| --- | --- |
| Rendered text identical | 25 |
| Rendered difference consists only of Apple documentation URL capitalization | 128 |
| Other renderer-visible differences | 19 |
| New page | 1 |

These categories prioritize review; even identical output from the old renderer cannot prove full source equivalence, since a renderer may omit information.

The 19 comparison candidates are: root collection, App Clips, App Icons, Branding, Buttons, Collaboration and Sharing, Complications, Game Center, Generative AI, Getting Started, Layout, Live Activities, Motion, Ornaments, Searching, SharePlay, Tap to Pay on iPhone, VoiceOver, and Wallet. Some changes are captions, anchors, typo corrections, link destinations, or ordering rather than new guidance.

Highest-priority confirmed editorial changes:

- **iPhone Duo:** a new page; Apple's own change log dates it September 9, 2026. Covers continuity across inner/outer displays, compact/regular layouts, device poses, reserved regions, arrangement views, vertical controls, toolbar prioritization and overflow. [Native source](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/designing-for-iphone-duo.md).
- **Layout:** substantially reorganized and rewritten; September 9 change log. Requires careful review of adaptability, size classes, safe areas, and existing exact specifications. [Native source](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.md).
- **Branding:** September 9 update emphasizes restrained accent color, color in the content layer beneath Liquid Glass, and familiar components/behaviors. [Native source](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/branding.md).
- **SharePlay:** September 9 update expands visionOS guidance and custom spatial templates, including seat/role distinctions and concrete seating constraints. [Native source](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/shareplay.md).
- **App Icons:** adds Parallax Previewer / Parallax Exporter availability through Apple Design Resources. **Wallet:** changes the generic-pass developer reference to poster generic passes. These smaller changes illustrate why change logs alone are insufficient.

Duo integration must preserve exceptions: iOS remains the underlying platform; outer display uses compact width and inner display regular width; vertical bars remain horizontal on the inner display in portrait; vertical hardware-aligned controls stay on the same side in RTL; navigation containers belong outside arrangement views; navigation-focused and task-focused experiences compress different bars. The next version needs explicit routing from Duo terminology to the iOS, layout, toolbar, tab-bar, split-view, and relevant accessibility guidance, with conditions attached rather than flattened into universal rules.

## Inputs to the next planning discussion

The deciding evidence favors a fresh source-grounded distillation with independent fidelity review, using the old corpus as a continuity comparison. Preserve rules, quantities, APIs, exceptions, examples that add information, and recommendation strength. In the subsequent September 12 discussion, Justin accepted approximately 75% word reduction as a corpus-wide heuristic, allowing topic-specific variation, and assigned validation ownership to the implementing agent. The agreement and validation requirements are recorded in `process.md`; the target is not a per-file quota that licenses omissions.

Keep source-fidelity evaluation separate from schema/routing validation and from runtime behavior evaluation. Revisit the 33.6k-token always-loaded floor using observed retrieval quality; don't reduce it by silently discarding useful rules. Include actual Duo scenarios and negative routing cases in future runtime trials.

The requested **enforce mode** is recorded in [enforce-mode-requirements.md](enforce-mode-requirements.md). Scoring details and iteration budgets remain planning decisions. This stage establishes evidence and requirements; it does not select or implement the next release architecture.

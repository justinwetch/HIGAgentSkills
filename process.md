# Apple HIG Update Process

This document is the operating procedure for updating this skill against the current Apple Human Interface Guidelines. The goal is not to summarize the HIG. The goal is to preserve Apple-specific design rules in a compact, triggerable agent reference corpus with verifiable coverage.

## Baseline And Current Status

- Initial repository corpus: 150 distilled files in `distilled/`.
- Current working corpus: 156 distilled files in `distilled/` after adding verified current-source topics.
- Existing skill contract: `SKILL.md` loads tier 1 foundations, platform files, trigger matches, one-hop related files, then on-demand niche files.
- Existing distillation standard: about 75% compression while preserving measurements, API names, platform differences, do/do-not directives, and specific behavioral rules.
- Apple source root: `https://developer.apple.com/design/human-interface-guidelines/`.
- Apple JSON root: `https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json`.
- Apple JSON page pattern: `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/{slug}.json`.
- Live crawl on 2026-06-09 found 176 HIG JSON records: 1 root collection page, 150 records mapped to existing distilled files, 21 unrepresented slugs needing classification, and 4 same-source aliases of existing distilled files.
- Current disposition summary lives in `sources/apple-hig-2026-06-09/dispositions.md`; use `python scripts/report_hig_progress.py sources/apple-hig-2026-06-09/inventory.json --pending --limit 25` for the next queue.
- The 21 unrepresented slugs are:
  `components`, `content`, `controls`, `design-principles`, `foundations`, `getting-started`, `inputs`, `layout-and-organization`, `managing-accounts`, `managing-notifications`, `menus-and-actions`, `navigation-and-search`, `patterns`, `presentation`, `privacy`, `selection-and-input`, `snippets`, `status`, `system-experiences`, `technologies`, `token-fields`.
- The 4 same-source aliases are:
  `components/layout-and-organization/tab-views` -> `tab-views`, `components/presentation/page-controls` -> `page-controls`, `components/system-experiences/complications` -> `complications`, `spatial-interactions` -> `nearby-interactions`.

The 21 unrepresented slugs were not automatically treated as 21 new tiered reference files. Some are collection/category pages. Each received an explicit disposition using the same standard as the existing corpus: include it if it carries reusable guidance, routing value, or rules not fully preserved elsewhere.

## Non-Negotiables

- Do not rely on memory, search snippets, old HIG knowledge, or prior distilled files as source truth.
- Every changed distilled file must be checked against the current Apple JSON source for that exact topic.
- Every new Apple topic must receive an explicit disposition: distilled, merged into an existing file, treated as collection-only, or excluded with reason.
- Do not accept vague summaries. Preserve concrete rules, exact values, platform distinctions, framework/API names, terminology, and prohibitions.
- Do not flatten platform differences into generic advice.
- Do not remove existing guidance unless the current Apple source no longer supports it or it has moved and is preserved elsewhere.
- Do not manually edit `routing-index.md` after the generator exists. Regenerate it from frontmatter.
- Keep an audit trail sufficient for another agent to verify the update without trusting the updater.

## Work Artifacts

Create or maintain these local artifacts during the update. They may be committed if useful for future maintenance.

- `sources/apple-hig-YYYY-MM-DD/raw/*.json`: exact Apple JSON responses.
- `sources/apple-hig-YYYY-MM-DD/rendered/*.md`: deterministic markdown/text rendering of each JSON page.
- `sources/apple-hig-YYYY-MM-DD/inventory.json`: canonical slug inventory, title, URL, role, source hash, status, and mapped distilled file.
- `sources/apple-hig-YYYY-MM-DD/dispositions.md`: decision log for new, removed, renamed, merged, and collection-only pages.
- `sources/apple-hig-YYYY-MM-DD/verification/*.md`: reviewer notes by batch.
- `scripts/crawl_apple_hig.py`: crawl Apple JSON and write raw inventory.
- `scripts/render_apple_hig.py`: render source JSON into reviewable markdown without distilling.
- `scripts/generate_routing_index.py`: generate `routing-index.md` from distilled frontmatter.
- `scripts/validate_corpus.py`: check frontmatter schema, trigger uniqueness, related-file existence, tier counts, and routing consistency.

## Phase 1: Source Crawl

1. Fetch the Apple HIG root JSON.
2. Breadth-first crawl every referenced URL under `/design/human-interface-guidelines`.
3. Normalize paths by lowercasing `Human-Interface-Guidelines`, stripping anchors, and removing trailing slashes.
4. Persist every successful JSON response unmodified.
5. Record failures with URL, status, timestamp, and retry count.
6. Generate `inventory.json` with:
   - slug
   - Apple title
   - Apple URL
   - JSON endpoint
   - source hash
   - role/kind
   - references discovered
   - existing distilled file match, if any
   - disposition status

Acceptance gate: no distillation begins until the crawl has a complete inventory and all fetch failures are retried or explicitly explained.

## Phase 2: Inventory Diff

Compare the live inventory with `distilled/*.md`.

Same slug does not mean same content. Treat every existing distilled file as requiring current-source review unless a prior raw Apple source snapshot exists and its hash matches the current crawl. If no prior snapshot exists, all 150 existing files are in scope.

Classify each slug as:

- `existing-update`: slug has a current distilled file.
- `existing-no-change`: slug has a current distilled file, the current Apple source was reviewed, and no distilled-file change is needed.
- `new-distill`: new Apple page carries durable guidance and deserves its own distilled file.
- `new-merge`: new Apple page carries guidance that belongs in an existing distilled file.
- `collection-only`: page is primarily navigation and does not need a reference file.
- `rename-or-move`: existing topic appears under a changed slug or source structure.
- `removed-upstream`: existing distilled topic no longer appears in the Apple crawl.

Use Apple change history or changelog metadata when present, but only as a triage hint. It is not proof of coverage and does not replace source-to-distilled verification.

Acceptance gate: every Apple slug and every existing distilled file has exactly one classification before editing. Every same-slug file has a source hash comparison or an explicit current-source review note.

## Phase 3: Rendering

Render each Apple JSON page into source markdown before asking any model to distill it.

The renderer must preserve:

- headings and hierarchy
- paragraphs
- lists
- tables
- callouts/asides
- code/API references
- links and referenced topic titles
- image alt text when it contains guidance
- platform labels and availability
- change history if present

Acceptance gate: spot-check rendered markdown against raw JSON for at least one page from each category: foundation, platform, component, technology, pattern, and collection.

## Phase 4: Distillation

For each page, update or create the matching `distilled/{slug}.md`.

Distillation rules:

- Keep the current compact style: direct, dense, reference-like.
- Prefer bullets and tables where they preserve rules more efficiently than prose.
- Preserve exact measurements, sizes, timing values, API names, framework names, and Apple terminology.
- Preserve all do/do-not rules as directives.
- Preserve platform-specific differences under explicit platform headings.
- Remove only framing, marketing prose, redundant explanation, and examples that do not add rules.
- Keep useful cross-topic references in `related`.
- Add triggers that match how an agent or user would ask for the topic.

Special handling:

- `design-principles` should be easy to trigger even when the user asks about general product/interface design without naming Apple. It likely belongs in tier 1 unless token budget analysis says otherwise.
- Collection pages should not become low-value summaries. Include them only if they contain reusable guidance, taxonomy, or trigger-routing value not captured in child pages.
- If a source page splits content into many anchors, keep one distilled topic unless Apple exposes those anchors as true canonical pages.

Acceptance gate for each file: a reviewer can answer the same practical design questions from the distilled file that they could answer from the rendered source.

## Phase 5: Metadata And Routing

For every distilled file:

- Validate YAML frontmatter fields: `topic`, `tier`, `platforms`, `category`, `triggers`, `related`.
- Ensure `topic` matches filename.
- Ensure triggers include:
  - Apple topic title
  - common user phrasing
  - framework/API names
  - platform-specific names where relevant
  - newly introduced terminology
- Ensure `related` points only to existing distilled files.
- Reconsider tiers after adding new topics:
  - tier 1: universal foundations always useful for Apple design work
  - tier 2: platform overview files
  - tier 3: broadly useful components, patterns, and technologies
  - tier 4: niche or narrow platform-specific controls

After metadata edits, regenerate `routing-index.md` from frontmatter.

Acceptance gate: `scripts/validate_corpus.py` passes and no routing entry points to a missing file.

## Phase 6: Independent Verification

Use separate verification passes from the distillation pass. Batch by category or 10 to 15 files at a time. Every existing, changed, and new distilled file must receive either an accepted verification note or an explicit no-change verification note.

Each verifier checks:

- Source coverage: no substantive rule, exact value, API, platform distinction, or prohibition was lost.
- Compression quality: file is distilled, not bloated or tutorial-like.
- Trigger quality: likely user requests route to the file.
- Related quality: one-hop expansion would load necessary adjacent context.
- Drift risk: no stale guidance from the old file remains if Apple changed it.

Verification outcomes:

- `accepted`: no required change.
- `revise`: list exact missing or incorrect items.
- `needs-source-review`: source rendering or crawl may be incomplete.

Acceptance gate: every existing, changed, and new file has an accepted verification note or an explicit no-change verification note.

## Phase 7: Skill-Level Audit

Run a final audit against the whole skill:

- `README.md` counts and tier totals are current.
- `SKILL.md` loading protocol still matches the corpus.
- `routing-index.md` reflects regenerated triggers.
- Token-budget notes are recalculated.
- The design-principles trigger path is explicit in `SKILL.md` and `routing-index.md`.
- Queries for broad design judgment, Apple platform design, components, APIs, and exact measurements route to the expected files.

Suggested smoke tests:

- "What principles should guide a new iOS app design?"
- "Review this interface using Apple design principles."
- "What are the HIG rules for Liquid Glass color?"
- "How should token fields work?"
- "What are the privacy permission request guidelines?"
- "What changed for sidebars/search fields/menus?"

Acceptance gate: smoke tests load the expected files and answer only from loaded distilled sources.

## Phase 8: Final Review

Before calling the update complete:

- Review `git diff` file-by-file.
- Confirm every source inventory item has a disposition.
- Confirm every new or changed distilled file has verification.
- Confirm generated files were regenerated, not hand-edited.
- Confirm no unrelated files changed.
- Summarize:
  - source crawl date
  - pages discovered
  - files added
  - files updated
  - files removed or merged
  - verification coverage
  - known gaps or deferred decisions

## Completed Action Item: Expanded Audit After Remediation

The final random and adjacent audits found a high enough incidence of source-drift, unsupported compression, and related-routing issues that a broader audit pass was required before treating the update as PR-ready. Do not treat `validate_corpus.py` passing as sufficient confidence; it checks structure and routing consistency, not source fidelity.

Completed audit:

- Audited 100% of the corpus, stratified across tier 1, tier 2, tier 3, tier 4, accepted-no-change files, revised files, and new files.
- Prioritize files marked `existing-no-change`, because random audit found that accepted files can still need source-backed remediation.
- For every audit finding, check the current rendered source before patching.
- If a sampled category has more than one substantive issue, audit the adjacent category batch before closing the issue.
- Record sampled slugs, reviewer, verdict, source-drift findings, fixes, and validation results in `sources/apple-hig-2026-06-09/verification/`.
- Completion is recorded in `sources/apple-hig-2026-06-09/verification/full-audit-results.md`: all 156 files received second-pass coverage and all `REVISE` findings were remediated.

## Goal-Mode Strategy: Full Fidelity Audit To Reach 95%+ Quality

Practice audits before the next goal-mode run found a high issue rate: 9 revisions across 15 sampled files. The failures were mostly semantic fidelity and routing issues, not schema errors. Therefore the next goal-mode run should audit every distilled entry, not a sample.

### Objective

Move the corpus from "structurally valid and mostly reviewed" to "source-faithful enough for agent reliance." Treat `validate_corpus.py` as a structural check only. The core quality gate is source-to-distilled fidelity.

### Batch Plan

- Audit all 156 distilled files in batches of 8 to 12 files.
- Stratify early batches to include:
  - `existing-no-change` files first
  - tier 1 foundations
  - new distills
  - recently remediated files
  - tier 4 niche files
- Use read-only subagents for comparison; the main agent integrates findings and patches.
- Keep each subagent prompt concrete: one batch, rendered source path pattern, distilled path pattern, no edits, exact output schema.

### Required Audit Output Schema

Every audited slug must produce one line in this form:

`slug | ACCEPTED/REVISE/NEEDS-SOURCE-REVIEW | P1/P2/P3/Info | source evidence | required fix`

Definitions:

- `ACCEPTED`: distilled file is faithful, compressed, trigger-ready, and related routing is acceptable.
- `REVISE`: source-backed patch needed.
- `NEEDS-SOURCE-REVIEW`: rendered source or raw JSON appears incomplete, mismatched, or ambiguous.
- `P1`: missing/wrong guidance that could materially mislead an agent.
- `P2`: source fidelity or routing issue likely to affect real use.
- `P3`: minor trigger, related, wording, or compression issue.
- `Info`: accepted or intentionally documented overlap.

### What Auditors Must Check

- Source fidelity: every substantive rule, exact value, API, platform distinction, and prohibition is preserved.
- Unsupported old guidance: remove guidance not present in current rendered source unless preserved by an adjacent current source and explicitly routed.
- Over-compression: restore practical rules that an agent would need to answer correctly.
- Over-bloat/unsupported embellishment: remove plausible but unsupported additions.
- Trigger precision: avoid generic triggers that hijack unrelated queries; qualify broad terms.
- Related routing: prefer current source Related links and strong body references; remove unrelated convenience links.
- Platform scope: frontmatter and body must not imply unsupported platforms.
- Measurements/spec tables: preserve exact dimensions unless intentionally deferred with an explicit source reference.

### Expansion Rules

- If a batch has 2 or more `REVISE` findings in the same category, immediately audit adjacent files from that category before calling the batch closed.
- If a file marked `existing-no-change` receives `REVISE`, prioritize the remaining `existing-no-change` files.
- If a routing issue appears in a file, audit the target/source pair on both sides of the route.
- If a spec-table omission appears, audit other spec-heavy files in the same category.

### Integration Rules

- Patch only after checking the current rendered source locally.
- Update `disposition-overrides.json` when a file changes from `existing-no-change` to revised.
- Add or update a verification note for every batch, including accepted files.
- Regenerate `routing-index.md` after trigger/related edits.
- Refresh `inventory.json` and `dispositions.md` after disposition changes.

### Acceptance Gate For Goal Mode

The next goal-mode run is not complete until:

- All 156 distilled files have second-pass audit coverage.
- All `REVISE` findings are patched or explicitly deferred with reason.
- Any adjacent-category expansion triggered by findings is complete.
- `python scripts/generate_routing_index.py --check` passes.
- `python scripts/validate_corpus.py` reports `errors: 0` and no within-file duplicate trigger warnings.
- `python scripts/report_hig_progress.py sources/apple-hig-2026-06-09/inventory.json --pending --limit 100` reports `pending current-source review: 0`.
- Final verification notes summarize defect rate, files audited, files revised, accepted warning classes, and remaining known risks.

### Practice Run Findings To Seed First Batch

Start the next goal-mode run by fixing or re-auditing these practice findings:

- `feedback`: soften multimodal feedback wording; add `playing-audio` related; reconsider `loading`.
- `lists-and-tables`: remove unsupported `swipe actions` trigger; replace `scroll-views` related with `layout`.
- `toolbars`: add `navigation bar` trigger; align related routing with source links.
- `text-fields`: add `text-views` and `combo-boxes`; remove unsupported `search-fields` related.
- `controls`: qualify generic `control`/`controls` triggers to avoid hijacking unrelated control queries.
- `token-fields`: remove or qualify generic `token` trigger.
- `sidebars`: remove or qualify unsupported `inspector` trigger.
- `widgets`: replace `app-clips` related with `layout`; audit omitted iPadOS dimensions.

# September 12 distillation pilot

The completed five-topic pilot supports using the existing **distillation skill unchanged**, with a HIG-specific source and validation workflow. The candidates cover new iPhone Duo guidance, revised Layout and Branding, specification-heavy Typography, and the short Steppers component. Required sampled findings are closed. They are staged locally; this is not the full September release or an installed skill update.

Entry points: candidate files (local `work/distillation-pilot-2026-09-12/drafts/`), staged runtime skill (local `work/distillation-pilot-2026-09-12/runtime/apple-hig/SKILL.md`), and evaluation evidence (local `work/distillation-pilot-2026-09-12/evaluation/`). Local `work/` artifacts are ignored by Git. The captured sources and historical findings are described in [reconnaissance](reconnaissance.md).

## Compression and context

Comparable guidance was measured after removing metadata, resource sections, link destinations and table padding on both sides, adding unique recovered JSON text once. Word counts and named tokenizer counts are separate measurements; neither measures fidelity. See the reproducible measurement script (local `work/distillation-pilot-2026-09-12/scripts/measure_pilot.py`) and metrics (local `work/distillation-pilot-2026-09-12/evaluation/metrics.json`).

| Topic | Source words | Candidate words | Reduction |
|---|---:|---:|---:|
| iPhone Duo | 2,852 | 898 | 68.5% |
| Layout | 3,097 | 920 | 70.3% |
| Typography | 6,521 | 2,987 | 54.2% |
| Branding | 649 | 245 | 62.2% |
| Steppers | 236 | 101 | 57.2% |
| **Total** | **13,355** | **5,151** | **61.4%** |

Comparable guidance uses 21,255 → 9,115 tokens with `o200k_base` (**57.1% reduction**), with a similar result using `cl100k_base`. The five complete candidate files, including frontmatter/resources, use 10,467 `o200k_base` tokens. Named encodings are not a claim about every model's tokenizer.

This deliberately difficult sample does **not** achieve 75% reduction and does not estimate the eventual corpus ratio. Typography contributes nearly half its source words. Retain the user's approximately 75% corpus-wide heuristic and allow dense topics to retain more. The full Typography reference falls from June's 12,409 to 6,705 tokens, about **46% fewer**, while preserving its numerical records and recovering omitted qualifications. Layout's reduction against June also reflects changed source content, so it cannot all be credited to better compression.

The observed Duo runtime request read the skill, index and **27 references**, including all **16 mandatory foundations**. That first invocation loaded 39,083 tokens of file content (`o200k_base`), including 24,639 foundation tokens; wrappers, prompts, previous context and answers are excluded. It avoided false `AR` matches inside “bar” and `AI` inside “explain.” One-hop relationships still pulled some peripheral topics. A full update should measure representative actual loads and reconsider the mandatory loading floor through behavioral comparison, rather than cutting facts to compensate for broad loading.

## Fidelity and behavioral evidence

Independent reviewers compared the candidates with native Markdown, original JSON, generated supplements, metadata and relevant visual evidence. The reference audit caught scope and recommendation-force drift, an omitted API deprecation flag and missing illustration relationships. A separately prepared source exam caught a reversed hover-effect relationship and an example generalized into a rule. These were corrected and independently rechecked. Review files retain exact source and candidate hashes.

The independently authored Typography checker reconstructs **688 records**, compares **1,860 value cells** and **2,064 identity fields**, checks **52 explicit absence cells**, and verifies **11 supplement blocks** against original JSON: zero failures. It does not import or inspect the table generator. Platform-specific 52/53-point tracking exceptions demonstrate why nearly identical tables must be compared fully before factoring shared values.

- Four-topic fidelity review and closure (local `work/distillation-pilot-2026-09-12/evaluation/fidelity-review-v2.md`)
- Typography full review (local `work/distillation-pilot-2026-09-12/evaluation/typography-review-v1.md`), correction closure (local `work/distillation-pilot-2026-09-12/evaluation/typography-correction-review-v2.md`), and numerical reconstruction (local `work/distillation-pilot-2026-09-12/evaluation/typography-table-check.json`)
- Source-derived 35-question exam (local `work/distillation-pilot-2026-09-12/evaluation/source-questions.json`), including seven negative cases. Expected answers were withheld from the answering agent.
- First answer grading (local `work/distillation-pilot-2026-09-12/evaluation/answer-grading-v1.md`): 28 pass, seven partial, zero fail. Partial answers triggered corrections and retesting; incidental illustration subjects and table-header formatting were not treated as required rule retention.
- Observed runtime answer (local `work/distillation-pilot-2026-09-12/evaluation/runtime-behavior-result.json`), actual read log (local `work/distillation-pilot-2026-09-12/evaluation/runtime-read-log.json`), and hash/loading check (local `work/distillation-pilot-2026-09-12/evaluation/runtime-observation-check.json`). The original tested runtime is frozen in `work/distillation-pilot-2026-09-12/runtime-v1/`.

The second full answer run (local `work/distillation-pilot-2026-09-12/evaluation/answer-grading-v2.md`) produced **33 pass, two partial, zero fail**. The residual issues were an imprecise fully-open/partially-folded condition in the Duo Notes example and an answering agent's imperative “Pair” despite the source and Steppers draft saying “consider pairing.” The Duo condition was corrected and independently closed against source (local `work/distillation-pilot-2026-09-12/evaluation/source-correction-closure-v3.md`). Both targeted answer retests pass (local `work/distillation-pilot-2026-09-12/evaluation/targeted-answer-grading-v3.md`): **35 passing sampled cases through v2 plus two targeted retests**, not a fresh full 35-question run. The targeted answers followed correction feedback; they do not establish that an instruction alone prevents future modality drift. Seven negative cases avoided inventing absent rules.

The runtime rerun (local `work/distillation-pilot-2026-09-12/evaluation/runtime-behavior-result-v2.json`) confirms explicit one-hop origins and scoped device-exception precedence resolve the two observed protocol ambiguities. Its provenance (local `work/distillation-pilot-2026-09-12/evaluation/runtime-read-log-v2.json`) distinguishes two new content reads from 27 unchanged files hash-checked and reused from the first run. Both answers satisfy the predeclared orientation, RTL, two-app edge, navigation/task compression and overflow-priority cases. This is a targeted continuation, not a second fresh loading trial.

Structural validation of the 157-file staged corpus passes with zero errors; 38 shared-trigger warnings are cross-topic overlaps. Its generated routing index matches frontmatter. These checks do not establish fidelity for the untouched June topics. Final artifact identities and verification (local `work/distillation-pilot-2026-09-12/evaluation/final-verification.json`) bind the candidates, staged skill and evidence used for this conclusion.

## Workflow decisions for the full update

1. Keep native Markdown as the readable starting point and original JSON as a required companion. Lexical omission detection cannot establish caption-to-image relationships or preserve API deprecation metadata. Inspect original blocks and relevant figures. Captured HIG images resolve under `https://developer.apple.com/tutorials/images/com.apple.HIG/`.
2. Preserve rule force, conditions, actor/object relationships, device states, platform scope and example status explicitly. Source conflicts stay visible; do not invent numerical resolutions. The watchOS recommended minimum versus smaller table entries is one such source tension.
3. Factor repeated tables only when an independent decoder can reconstruct every original record, exception, unit and absence. Audit prose separately; correct numbers alone do not prove faithful guidance.
4. Independently compare source → candidate for loss and candidate → source for invention on every topic. Use old distills for continuity checks, not source truth. Keep changed artifact hashes tied to review and revalidation evidence.
5. Evaluate answer behavior separately. An answering agent can turn a correctly distilled “consider” into an imperative. The staged runtime now explicitly preserves recommendation strength, scopes device exceptions, and expands related references only from the initial selected platform/device/component files.
6. Use source-derived questions with withheld expected answers, exact-value and negative cases, actual file-access evidence, and correction/retest loops. Preserve failed rounds. Full-release runtime evaluation should include independent fresh-context requests, not only this pilot's continuing evaluator.

The pilot's actual runtime test used the same evaluator after direct draft questions, so prior candidate content remained in context. It demonstrates recorded selection, reading and use of staged files, not fresh installation/discovery, device execution or an exhaustive benchmark. Wide specification tables were checked as agent references; narrow-screen visual usability was not tested.

The requested **enforce mode** remains a separate [recorded feature contract](enforce-mode-requirements.md): independent subagents score implementation adherence, require corrections and re-review before a pass. Corpus validation does not by itself implement that product-review mode.

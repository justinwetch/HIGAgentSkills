# September 12 release execution

Status: **in progress**. The June runtime remains the release baseline. No September release is accepted yet.

| Chunk | Status | Evidence / remaining gate |
|---|---|---|
| 1. Source coverage and measurement | pass | 346 source hashes and five pilot candidates verified; 7,642 exact primary blocks. Independent disposition and accounting reviews passed after corrections. |
| 2. Cheaper-drafter calibration | pass | Independent final gate accepted current source fidelity, numeric/compression evidence, behavior and execution provenance. See release-calibration-acceptance.json/.md; all earlier failures remain preserved. |
| 3. Complete corpus | in progress | First two drafting-tier drafting batches dispatched; independent review-tier source-only examination begins before candidate review. Every topic requires source fidelity and behavioral evidence. |
| 4. Runtime and enforce mode | pending | Actual correction/review loops required. |
| 5. README and packaging | pending | Exact manifest, rendered README, reproducible ZIP and clean extraction. |
| 6. Extracted release validation | pending | Fresh actual reads/answers and independent final acceptance. |

Execution contract and extensive working artifacts are in project-local `work/release-2026-09-12/`. Lightweight final identities, coverage/results and reproduction instructions will be retained here. No pending gate is represented as passed.

## Chunk 1 evidence

- [Source freeze](source-freeze.json): 173 pages, both formats, all recorded hashes and byte counts verified.
- [Source dispositions](release-dispositions.md) and [complete mapping](release-dispositions.json): 157 retained topics, one merged source, 15 collection-only pages and four aliases. Notifications requires the full Managing Notifications source in addition to its own page.
- [Independent accounting review](release-accounting-review.md) and [machine-readable review](release-accounting-review.json): raw block bijection and actual rendered-output inspection. Merged-cell table warnings, nested list indentation and duplicate tab headings were corrected before acceptance.
- [Pilot remeasurement](release-pilot-remeasurement.json): 13,756 canonical source words to 5,195 output-body words, **62.235% reduction**. This intentionally differs from the former native-plus-lexical-supplement method (13,355 to 5,151, 61.43%). The new method recovers canonical JSON captions/API labels and includes output resource/comment text. The encodings still count exactly 10,467/10,431 tokens in the same five complete candidate files.

The approved map contains 261,621 source-guidance words before future supported semantic deduplication decisions. This is a source baseline, not a final compression result. Routing-only frontmatter must be independently audited; source coverage and accounting acceptance do not certify candidate fidelity.


## Initial calibration findings and method repairs

Initial full-source audits found recommendation-strength drift, lost conditions, an implied unsupported numeric threshold, and inaccurate writer coverage claims. Independent Keyboards reconstruction confirms all 125 table records, but semantic review still found lost qualifiers. Correction rounds remain subject to final hash-bound review-tier acceptance.

The original 21-case blind run recorded actual reads and answers. Its strict fixed-gold result was 71/87 facts passed, 13 partial and three failed; this is **not a valid question-scope success rate** because nine expected components were not clearly elicited, including all three failed components. Original artifacts are preserved. Eight repaired regression questions now explicitly elicit those nine components; nine separate reserve cases were written source-only before the answers were seen.

Workers now perform an explicit source-strength/condition/coverage verification pass. Examiners must map every expected fact to an eliciting question clause. Candidate/coverage pairs are frozen before review so later edits cannot mutate acceptance inputs. The corpus queue is prepared in 61 bounded batches, but remains undispatched until calibration passes.

Initial drafting elapsed times are not fully evidenced: some writer timestamps were identical report-generation observations. They are not reported as zero-cost or zero-duration work. Actual subsequent dispatch/completion observations and named file-content token measurements are recorded separately from unavailable billed usage.


## Earlier calibration evidence (acceptance subsequently withdrawn)

At this earlier checkpoint, all three references had passed an independent source-first review-tier audit. Keyboards had 125 independently reconstructed records with zero mismatches under that comparison. Historical source-fidelity records and hashes are retained in release-topic-acceptance.json; this was not release acceptance.

That was the finding at this earlier checkpoint. Subsequent cases and the atomic audit below withdrew these acceptances; this paragraph is historical, not a current pass claim.

Accepted-method measurements for these three dense topics are 8,062 source words to 4,835 output words, 40.027% reduction. Independent review explains each below-60% diagnostic variance; this does not predict or relabel the final corpus reduction.

The repaired method/tooling audit passes, including source-set provenance, immutable review pairs, source-first semantic reconstruction, all 126 question/fact bindings, execution-ledger lifecycle checks and fresh-context guards. Round two produced 122 passed facts, three partial and one failed: all 39 facts in nine first-use withheld cases passed, while four regression facts failed through responder omissions or changed recommendation strength. The correct clauses are present in the accepted references. Calibration therefore remains in progress. The next response workflow uses one topic per fresh answerer with explicit question-part and recommendation-strength checks, plus additional independently prepared withheld cases.

The original missing draft timings can now be reconstructed from this task's timestamped dispatch/final-message rollout: initial social drafting 583.618 seconds and initial Keyboards drafting 369.825 seconds of observed wall time. A minimal evidence extraction is retained under work/release-2026-09-12/historical-dispatch-evidence.json; it reports an observed peak of three children. These are tool-observed intervals, not model-compute or billing figures; independent historical reconstruction review remains pending.


### Calibration and tooling continuation (September 13 UTC, September 12 local)

- Single-topic fresh answer runs are now used with explicit question-part, recommendation-strength and state-transition checks. Round-three immutable answers remain preserved; original inputs and gold were not rewritten.
- A new source-derived Privacy case exposed the omitted ability to manage App Store privacy information **at any time**. The earlier fidelity pass was withdrawn. review-tier restored the qualifier; independent re-review and fresh behavioral testing are underway. Final correction is frozen in `work/release-2026-09-12/frozen/calibration-privacy-timing/` with candidate `732f717bb0f69556ce33e5f9e67d1f13f93a99383c6045374ed6d8daee7560b6` and coverage `eacfba70219e4ea8febc884789def545e5cec406117d5957be9d21fb1d2299ae`.
- The Privacy source-first register already contained the timing fact; paragraph-level matching failed to verify it. REVIEWER.md now explicitly requires a separate precise retained clause or supported deduplication destination for each operative fact. Source-first reconstruction alone is insufficient.
- Independent packaging-tool QA found and corrected fixed temporary-path hard-link overwrites and accepted symlink ZIP metadata. Final tool hash `bdfab50cb8d1118eef34ff373f72a8400bb3b3e7f4bb797d6bb5ac9dd394c881` passes 53 independently executed checks, including deterministic builds and write/inspect/replace failure cleanup. These are synthetic tool tests, not release or runtime acceptance. Reproduction and preserved initial/final evidence are under `work/release-2026-09-12/reviews/package-tool/`.
- Actual child tool calls/results and runtime token-usage records are retained using `scripts/capture_hig_agent_evidence.py`, filtered by this task's parent identity. Reasoning text and unrelated task contents are excluded. Runtime-reported tokens, file-content tokenizer measurements and billed usage are separate; invoice/billing data remain unavailable.
- Bounded corpus assignments and extracted-runtime validation tooling are prepared. No remaining corpus batch has been dispatched before the calibration gate. The delivered runtime still has not been assembled or approved.

### Earlier checkpoint: atomic corrections and complete fresh retest

A fresh review-tier (xhigh) audit reconstructed and matched 405 prose facts, 379 data cells plus table headers, and 16 API facts. Its final review found seven substantive correction groups across all three topics. A different review-tier (xhigh) author corrected the 13 affected fact IDs in nine candidate lines; the candidates and coverage maps are frozen under `work/release-2026-09-12/frozen/calibration-final-round6/`. Mechanical checks pass. Independent source re-review and the complete fresh-topic answer suite remain pending.

These corrected calibration files measure **8,062 to 5,007 guidance words, 37.894% reduction**. The fresh suite contains 52 cases and 212 expected facts, including seven finding-targeted regressions and three previously unused source-only reserve cases. Earlier answers and failures remain preserved. No corpus acceptance or 75% compression claim follows from this checkpoint.

The staged enforce protocol passes independent static review after clarifying routing and reviewer/register handoffs. Four browser prototypes now contain actual baseline, defect, regression and repaired behavior. Root browser smoke observations confirmed keyboard access differences and the Cancel regression; these are preparation evidence, not independent enforce-mode execution or native Apple behavior validation. Remaining corpus drafting, full runtime fixtures and release packaging still require their gates.

### Calibration accepted; corpus execution begun

The [independent final calibration gate](release-calibration-acceptance.md) passes C1/C2/C3/C6 within the three-topic scope. It rechecked final source maps, changed clauses, numerical records, metrics, actual tool traces and updated grades. Latest passing behavioral evidence covers SharePlay 21 cases/85 facts, Keyboards 12 cases/47 valid elicited fact items, and Privacy 20 cases/84 facts. Privacy combines 18 passing round-six cases with a focused regression and new source-only case; it is not one clean full-suite rerun. Keyboards explicitly excludes an unasked definition from its scored obligation and preserves the source's uncertainty. Trace/self-report timing and method-read limitations are disclosed in the gate report; billing remains unavailable.

The first eight remaining topics are now assigned to two fresh drafting-tier (high) drafters. A fresh review-tier (high) examiner independently reconstructs the first batch's source facts and freezes withheld questions before seeing candidates. The 61-batch queue preserves the four-topic/20,000-source-guidance-token limits. No remaining topic is accepted merely because drafting started.

### Corpus checkpoint: first three source examinations

Independent source-only examinations are frozen for 11 topics across the first three batches. The second batch's four drafts are frozen and undergoing two-way source review; their initial aggregate reduction is 55.548% (2,992 source words to 1,330 guidance words), not an accepted corpus result. Drafting for the third batch has begun. The first drafter required two native interruption/continuation recoveries after stalled tool progress; saved candidate work is preserved and these recoveries are recorded separately from fidelity correction attempts.

The fresh-answer packet helper passes 42 independently executed synthetic checks after repairing a reference/instructions filename collision and redirected-directory containment. Failed cases and repairs are retained under `work/release-2026-09-12/reviews/blind-packet-tool/`. These checks certify packet construction only; source fairness, actual file use, and answer correctness remain separate gates.

### First corpus corrections and independent re-review

All eleven initial drafts received full independent source review. Eight required substantive corrections; Labels, Column Views and Web Views passed initial fidelity but retained lossless compression opportunities. The original passes apply only to their original bytes. No new corpus topic has completed behavioral acceptance yet.

drafting-tier completed the second and third batches' first corrections and cleanup. Their new immutable pairs are undergoing independent review. Reproducible measurements are 2,992 to 1,519 words (49.231% reduction) for the second batch and 2,500 to 1,616 words (35.36%) for the third. Restoring omitted guidance can increase output despite removing repetition. These partial batches do not establish the eventual corpus ratio.

Recurring modifier, recommendation-strength, purpose and decorative-prose issues are documented in the project-local `CORPUS-LESSONS.md` addendum, with independent method review pending. Its exposure checks cover all eleven initial topics. A source examiner also identified an overbroad Scroll Views question about incidental illustration framing/control details; the original exam is preserved, and a separately recorded candidate-aware fairness repair awaits independent review before use. It is not represented as a newly withheld source-only case.


### Corpus checkpoint: September13 04:00 UTC

All twenty initial batch01 fidelity findings are closed. Column views passes source/coverage/compression review; Charts needs coverage/response errata plus specified consolidation, Collections and Image views need concrete duplicate removal. Second cheaper corrections for batches02/03 are frozen and independently re-reviewed. Labels final source pass is bound to 8cd016d7...; its first fresh blind answering is running. No additional corpus topic has full blind-answer acceptance yet. Batch02 final candidate measurement is 2992 → 1462 guidance words (51.136% reduction); batch03 is 2500 → 1569 (37.24%). These are subset results, not corpus claims. All eleven exposed topics require the independently reviewed CORPUS-LESSONS check.


### Corpus checkpoint: September13 04:12 UTC

Batch02 all four topics pass final-byte source, coverage and topic compression review (summary b6d7358e...). Five first-use Labels answers are grading independently; full packet reads are observed, with a separately retained self-reported manifest-hash typo erratum. Other three first-use packets are ready. Batch03 second correction introduced an NSScrollView object-role error and edge-effect URL typos; final report pending and review-tier escalation required. Source-internal doc IDs and site-relative links in batch01 also require portable serialization before runtime acceptance. The lead CommonMark exposure check covered all eleven initial topics; only batch01 has those source-internal link forms. LINK-PORTABILITY.md records exact frozen JSON URL resolution, without changing source accounting. Column views blind packet remains unused pending link correction; its source-content pass is not a final delivery pass.


### Corpus checkpoint: September13 04:24 UTC

Labels is the fourth topic accepted for corpus integration after three calibration topics: full source pass plus5/5 first-use cases and29/29 elicited facts. Batches01/02/03 latest immutable candidates measure4579→2585 (43.547%),2992→1462 (51.136%),2500→1586 (36.56%) words respectively; these remain subsets. A distinct review-tier corrected Scroll Views, and its independent round3 reviewer accepts all three batch03 references including topic C3; no corpus-wide75% claim. All83 current links across the initial eleven topics match literal mapped frozen source destinations under the lead CommonMark diagnostic. Batch01 final review still flags stale Charts coverage line references; no final pass inferred from correct runtime prose. LT/LP first answers completed and inspected with complete four-file read evidence, awaiting independent grading; Outline and Text fresh answering running. Four accepted topic records remain separate from final runtime/package acceptance.


Checkpoint 2026-09-13 04:48 UTC: first-use corpus answers exposed two reference defects after source review: Lists and Tables changed possible difficulty to certainty; Outline Views dropped explicit consider guidance for alternating colors. Affected source passes withdrawn prospectively in corpus-02/answer1/summary.json; all original records preserved. Three fresh review-tier (xhigh) source-first force audits now cover all eleven drafted corpus topics, with 22 additional withheld questions frozen before candidate access. Labels and Live Photos first-use answers passed; LT/Outline need corrections and regression plus new cases. All three corpus-03 first-use answer artifacts are complete and awaiting independent grading. No complete-corpus, runtime or package pass is claimed.


Checkpoint 2026-09-13T05:11:39.980782+00:00: independent review-tier (xhigh) precision audit completed all eleven initial corpus topics. Column Views, Labels, Text Views and Web Views passed the supplementary check. Fourteen source-fidelity findings affected the other seven topics, plus one Charts coverage locator. Different review-tier authors corrected them; immutable snapshots force-round1-a and force-round1-b await renewed independent acceptance. First corpus-03 answering passed Text/Web; Scroll S02/S06 failed four fact checks (two inherited candidate errors, two responder omissions). Original defective gold wording was explicitly qualified against source, not silently rewritten. Eleven prepared blind packets contain 70 cases, with first-use/source-only versus regression lineage retained outside packets. Actual trace decoding verifies complete native sources before all three source-only freezes; a preliminary helper false negative and its correction are preserved. No full-corpus or release acceptance is claimed.

## 2026-09-13T05:40:52.713084+00:00 checkpoint

All eleven initial corpus topics completed independent source precision acceptance on frozen bytes. Subsequent fresh answers exposed two ambiguous Outline Views interaction mappings, independently confirmed; those clauses return to correction and review. A new source-only examiner froze two cases before revision. Lists and Tables now has seven passing cases and 44 passing scoped fact records, with five regressions and two first-use cases explicitly distinguished; it is the fifth topic acceptance record including three calibration topics and Labels. Other fresh grades remain pending. No full-corpus, runtime or release acceptance is claimed.

## 2026-09-13T06:12:44.217758+00:00 checkpoint

Eight topic acceptance records now combine final source and actual-answer evidence. Outline interaction repair passed independent source review, and its nine-case answers await grading. A new Charts rationale omission was found by independent behavioral grading and confirmed against the raw source; affected C2 returns to correction. Scroll's reminder-only targeted retest still has observed responder errors; no successful method effect is claimed. A proposed literal-clause/line audit checkpoint is under independent review. drafting-tier (high) drafting resumed for the four-topic controls batch after calibration and prospective method clarification approval; all new drafts remain subject to full independent source and behavioral QA.


## 2026-09-13T06:40:27.485648+00:00 checkpoint

Nine topic records now bind source and actual-answer acceptance to current bytes. Charts rationale repair is frozen (3427 to1803 guidance words;47.388% topic reduction) and independently reviewed. Controls batch04 is in full independent source QA after source-only facts and18questions froze. Scroll reminder-only retest failed four of five response/audit checks; a literal quote/line checkpoint is approved only for a bounded prospective trial with new source-only questions. No full-corpus, runtime or package acceptance is claimed.

# September Apple HIG reference corpus

**Revision 2026-09-24:** 106 topics changed. Topics rewritten from Apple's source for fidelity-first compression were each independently re-reviewed against the capture; others received only a narrow removal of source-narration lines that kept every operative fact. The remaining 51 are unchanged. Corpus totals are now **261,621 → 90,027 words (65.589%)**, **163,033 o200k / 162,491 cl100k** full-file tokens, and **27,096 / 26,936** for the 16 foundations. Median topic reduction is 63.903%, range 20.661–83.077%. `topics.csv` holds the current per-topic hashes and counts. An earlier 2026-09-23 revision restored source qualifiers in `designing-for-iphone-duo` and removed over-broad Duo triggers. The figures below record the original September 13 acceptance. `work/` paths are local maintainer evidence and are not published.

All **157 references** passed independent source review against the September 12 capture, with no open findings; drafting, corrections and review were done by separate agents. June was checked afterward for continuity. This completes reference distillation and source QA; runtime integration, observed agent behavior, enforce mode, README integration, and the release ZIP remain separate work.

Accepted references (local `work/remaining-2026-09-13/combined/references`) · Manifest and review linkage (local `work/remaining-2026-09-13/combined/manifest.json`) · Independent assembly check (local `work/remaining-2026-09-13/combined/assembly-check.json`) · [Per-topic measurements and hashes](topics.csv)

The 177 discovered paths comprise 157 retained topics, one source merged into Notifications, 15 collection-only pages, and four obsolete aliases: 173 captured pages, 158 mapped guidance pages. Native Markdown and JSON representations count once.

**261,621 → 108,104 guidance words; 58.679% reduction.** This is the ratio of totals, below the approximately 75% heuristic. Dense specifications, conditional recommendations, meaningful figure relationships, and API details limit compression; unresolved omissions were fixed rather than accepted for a percentage. Median topic reduction is 55.913%, range 20–83.049%; 109 topics fall below 60%, none above 85%. Largest retained topics are Typography (3,154 words), Widgets (3,004), and Wallet (2,300).

| Complete reference-file tokens | June | September |
|---|---:|---:|
| o200k_base | 135,029 | 199,915 |
| cl100k_base | 134,586 | 198,479 |
| 16 foundations, o200k_base | 32,737 | 29,822 |
| 16 foundations, cl100k_base | 32,574 | 29,669 |

The full corpus grew 53.3% in guidance words and 48.1% in o200k tokens over June; the mandatory foundations shrank 8.9% in o200k tokens. These are static file counts, **not observed loads or billed usage**. All 156 June files remain unchanged; Duo is the additional topic.

The `canonical-blocks-v1` method counts complete output bodies, including comments/resources, excluding only the six routing fields and link destinations. Source exclusions and all per-topic counts are in the full measurements (local `work/remaining-2026-09-13/combined/measurements.json`). Tokenizers use tiktoken 0.14.0. Review covered saved text, tables, captions, alt text, relationships, and API metadata; it did not validate image pixels, video footage, or runtime behavior.

Reproduce in the existing project workspace with its captured sources, block register, and tokenizer dependencies:

```powershell
Set-Location <repository-root>
python -X utf8 scripts/measure_hig_release.py --candidates work/remaining-2026-09-13/combined/references --output work/remaining-2026-09-13/reproduced-measurements.json
```

Compare the complete JSON with `combined/measurements.json`. The independent assembly check also reproduces June measurements, checks final acceptance/hash linkage, and verifies source dispositions, routing schema, and exact membership. Historical checkpoint exceptions remain recorded; their 24 independently accepted repairs supersede them in the combined manifest.

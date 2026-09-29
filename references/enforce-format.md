# Enforce JSON format

`hig_enforce.py` reads one frozen register and two independent review files. A
review is bound to the current artifact by its revision and by SHA-256 hashes
of every listed artifact file. Paths are relative, normalized paths under the
named `--artifact-root`; traversal and absolute paths are rejected. Code
evidence must also appear in that review's `artifact_files` map. Render and
behavior evidence may be separate saved files under `--artifact-root`, so
independent reviewers can use different captures while binding to the same
artifact hashes. HIG source text is used only through the register's `source`
field. The helper reads no reviewer-provided score.

Each evidence array must include the check's required `evidence_kind`; it may
also include supporting code, render, or behavior observations. Supporting
screenshots or source never substitute for required executed behavior.

Register checks have these required fields:

```json
{
  "artifact_revision": "demo-1",
  "checks": [{
    "id": "layout-1", "owner": "A", "dimension": "layout",
    "applies": true, "strength": "must",
    "source": {"path": "references/hig/voiceover.md", "quote": "Provide alternative labels for all key interface elements."},
    "expected_behavior": "The primary action has an accessible name.",
    "evidence_kind": "code"
  }]
}
```

`owner` is exactly `A` or `B`; `strength` is `must`, `prohibition`, `prefer`,
`consider`, `should`, `recommendation`, `recommend`, `may`, `optional`, or
`example`. `must` and `prohibition` are mandatory. An excluded check has
`applies: false` and a non-empty, source-backed `exclusion_reason`; it remains
in the frozen register but contributes no points. A preference or consideration
cannot be upgraded with `mandatory: true`. `source.path` must be
`references/hig/<topic>.md` with topic frontmatter, and `source.quote`
must occur exactly in that local file below `--skill-root`.

Each review has `reviewer_id`, `completed: true`, matching
`artifact_revision`, non-empty `artifact_files`, and exactly the applicable
checks owned by that reviewer:

```json
{
  "reviewer_id": "reviewer-a", "completed": true,
  "artifact_revision": "demo-1",
  "artifact_files": [{"path": "app/main.swift", "sha256": "<64 hex chars>"}],
  "cross_cutting": [{"id": "layout-1", "evidence": [{
    "file": "app/main.swift", "sha256": "<same hash>", "kind": "code",
    "observation": "The label is present in the inspected source."
  }]}],
  "checks": [{"id": "layout-1", "result": "met", "evidence": [{
    "file": "app/main.swift", "sha256": "<same hash>", "kind": "code",
    "observation": "The inspected implementation supplies the accessible name."
  }]}]
}
```

The four results are `met`, `partial`, `violated`, and `missing`, scoring 2, 1,
0, and 0 points respectively. `missing` cannot claim evidence and blocks the
run. `partial` and `violated` require a finding with `observed`, `fix_location`,
`action`, `verify`, and boolean `material`. A mandatory or material failure
keeps the result at `needs changes`; nonmaterial recommendation shortfalls
remain visible and reduce the score without independently blocking a pass.
Optional `finding`/`findings` and `challenges` are supported.
A challenge that disagrees with the owner result must include `resolved: true`
and a non-empty evidence-backed `resolution` after reconciliation, otherwise it
is an open disagreement. Both reviewers
must provide evidence for every mandatory check through `cross_cutting`.
They may also include other applicable checks there to document independent
inspection of material risks; each cross-cutting ID must be unique.

Use the available Python 3.10+ executable in place of `<python>` below. Resolve
`<skill-root>` to the installed skill and `<app-root>` to the reviewed project.
Paths inside review JSON remain relative to `<app-root>`. Keep each cycle's input
JSON, artifact snapshots and result under `<app-root>/work/hig-enforce/`.
Create the cycle directories before running the helper. Commands use distinct
output files so they never overwrite previous evidence.

```text
<python> "<skill-root>/scripts/hig_enforce.py" --register "<app-root>/work/hig-enforce/cycle-0/register.json" --review-a "<app-root>/work/hig-enforce/cycle-0/review-a.json" --review-b "<app-root>/work/hig-enforce/cycle-0/review-b.json" --artifact-root "<app-root>" --skill-root "<skill-root>" --cycle 0 --output "<app-root>/work/hig-enforce/cycle-0/result.json"
<python> "<skill-root>/scripts/hig_enforce.py" --register "<app-root>/work/hig-enforce/cycle-1/register.json" --review-a "<app-root>/work/hig-enforce/cycle-1/review-a.json" --review-b "<app-root>/work/hig-enforce/cycle-1/review-b.json" --artifact-root "<app-root>" --skill-root "<skill-root>" --cycle 1 --previous "<app-root>/work/hig-enforce/cycle-0/result.json" --output "<app-root>/work/hig-enforce/cycle-1/result.json"
```

For cycles 2–3, use their own directories and the immediately preceding result.
Exit 0 means `pass`; exit 1 means `needs changes` or `blocked`. Usage/output-path
errors exit 2 with an explanation on stderr and may not produce a result file.

The helper compares the complete
normalized frozen register, so removing or weakening a failed check cannot
raise the score. Start an explicitly new run for a real rescope. A pass needs
at least 90 points, complete evidence, two distinct completed reviewers, no
unresolved disagreement, no mandatory violation, and no open material finding.
The result preserves the verified `artifact_files` map and register hash for
reproduction. The helper can verify bytes and arithmetic; it cannot prove honesty,
completeness, semantic source interpretation, reviewer independence, or actual
behavior beyond the observations supplied by the agents.

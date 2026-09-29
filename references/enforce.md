# Enforce mode

Use only when the user explicitly asks to apply apple-hig in enforce mode. Review the requested artifact, fix actionable defects within scope, and independently inspect the result. Ordinary guidance and questions about enforce mode do not activate this procedure.

## Establish scope and checks

First check for Python 3.10+, two independent reviewers and the observation tools needed for the requested artifact. If a required capability is unavailable, explain the concrete blocker before edits or lengthy loading. Use project files and the conversation directly; no browser intake, dashboard or setup server is required. Then follow the entry point's reference loading protocol. Identify the actual project components, their defining files, platforms/devices, requested tasks, important states, and available code/render/interaction evidence. Prefer existing components and APIs when repairing the app. Use existing linters, accessibility inspection, and runtime tests where useful; do not mistake their success for complete HIG adherence.

Use two independent subagents: **A** covers platform conventions, layout/navigation, and components/materials; **B** covers accessibility/input, content/state continuity, and device adaptation. Both inspect cross-cutting mandatory and material risks. Give them actual artifacts, evidence access, and relevant loaded references, without another reviewer's findings or suggested answers. If two reviewers or required evidence are unavailable, return `blocked` with the concrete missing capability.

Each reviewer proposes applicable source-backed checks for their assignment. Merge and deduplicate them, preserving independently testable conditions. Have both confirm coverage before scoring. Keep a compact register with stable IDs, one owner and dimension per check, exact source clause, Apple recommendation strength, applicability, observable expectation, and required evidence kind. Source locations refer to `references/hig/`; reuse the HIG rather than writing a second rule corpus. Check all relevant guidance, not just a convenient selection of easy-to-pass rules.

An explicit device/state exception qualifies a broader rule only within that scope. Preserve must, prefer, consider, conditions, alternatives, and examples. A pure optional alternative need not be implemented; record why it is inapplicable. For a recommendation to consider an option, assess the relevant consideration rather than demanding that option. Do not invent numerical targets or elevate a preference into an Apple requirement. A source conflict remains visible until resolved against actual source evidence.

Freeze the register for this review run. Failed checks cannot be removed or weakened to raise the score. A genuine scope change requires an explicit new run and an explanation of which old findings remain outside its scope; it cannot claim completion of the original scope.

**Before editing the artifact:** obtain both independent reviews of the original revision and run the helper for cycle 0. Save the original artifact bytes and evidence. Do not repair first and reconstruct an initial review afterward. If this gate cannot be completed, return `blocked` before making changes.

## Inspect and return actionable findings

Use [the compact data format](enforce-format.md) for the register and two separate review files. Put working evidence in the reviewed project's `work/hig-enforce/` directory. Bind both reviews to the same artifact revision and identify each actual reviewer. Reviewers must read and observe the artifact themselves; another review's conclusions are not evidence.

For every applicable check, record `met`, `partial`, `violated`, or `missing`, with evidence and any material consequence. Evidence identifies a file/state/interaction, its saved file hash, and what was observed. A code-only check can use source inspection. A rendered design check needs the rendered state. A behavioral check needs an executed interaction and observed result; code presence or screenshots cannot establish state continuity, keyboard focus, or assistive-technology operation. Prototype viewport resizing is not proof of native device folding behavior.

A failed check's diagnostic should let the implementer act immediately:

```text
hig/state-continuity — material
Observed: Opening the inner display resets the selected message.
Source: designing-for-iphone-duo, Displays, poses, and continuity.
Fix: Preserve selection outside the display-specific view branches.
Verify: Select a message, open and close the device, confirm selection persists.
```

This is an illustrative finding, not evidence about the user's app. Actual diagnostics include the repair file/location and observed artifact evidence. Suggest existing components/variants and exact defining files when available. The HIG establishes the obligation; the proposed implementation remains a design choice. Never suggest changing policy, suppressing a finding, or deleting functionality merely to obtain a pass.

Reviewers submit their scores and challenges independently. Reconcile disagreements against the HIG and artifact evidence, not by averaging or choosing the more confident reviewer. Resolve each challenge, or retain it as an open finding. Reviewers confirm the reconciliation without copying another reviewer's unexamined claims.

## Score, fix, recheck

Run the packaged `scripts/hig_enforce.py` helper using the command in the format reference. It derives points: **met=2, partial=1, violated/missing=0**. Every applicable check contributes two possible points. Excluded checks need source-supported reasons; no applicable checks is `blocked`. The helper validates inputs, source/evidence references, artifact hashes, register continuity, and arithmetic. It cannot prove truthful observations, complete scope, source interpretation, or reviewer independence; the coordinator and independent reviewers own those judgments.

Pass requires **at least 90/100**, complete evidence, both independent reviews, no unresolved mandatory-rule violation, no material finding, and resolved disagreements. A material finding impairs task completion, accessibility, navigation, state continuity, or applicable platform/device behavior. A preference can have a material impact without becoming a mandatory Apple rule. An approved exception remains explicit and cannot yield an unqualified pass with mandatory or material issues outstanding.

The coordinator or a separate implementer fixes the findings. Perform the initial review and at most **three correction/re-review cycles**. After each edit, rerun affected checks and inspect the actual result, including previously passing behavior that might regress. Preserve the user's intended appearance and functionality. Both reviewers independently re-review their affected scope and cross-cutting risks on the same new revision. A reviewer who authored a correction must be replaced for its acceptance.

Carry unchanged evidence forward only when its artifact and behavioral dependencies are unchanged and the reviewer states why. Changed dependencies invalidate earlier evidence. Re-run the helper with the previous result to preserve the frozen check set and cycle continuity. A claimed fix without reinspection does not close a finding. Missing evidence/capability returns `blocked`; unresolved failures at the cycle limit return `needs changes`.

## Deliver

Report the status, scope/revision, actual fixes, remaining findings, overall and dimension points/scores, evidence coverage, reviewer identities, and correction count. Keep the register and evidence available locally; present a concise result to the user. Distinguish design conclusions from observed runtime behavior. Do not call the artifact good solely because its score is high.

# Enforce mode: requirement captured September 12, 2026

Justin requested an explicit `enforce` mode requiring subagents to score adherence to the HIG and require changes to fix nonadherence. This is a next-version feature requirement, not a claim that the current runtime implements enforcement.

## Requested behavior

When enforce mode is active, the implementing agent must obtain independent subagent reviews of the actual design/implementation, receive HIG adherence scores and source-backed findings, make required corrections, and have the revised result reviewed again before reporting a pass. An advisory review that merely lists issues does not fulfill enforce mode.

## Proposed contract for planning

- Scope the review to the target platforms, features, device states, and applicable HIG pages. For Duo work, include compact/regular layouts, opening/folding continuity, orientation exceptions, reserved regions, vertical bars, overflow, and RTL behavior where relevant.
- Require separate reviewer subagents; the implementer cannot satisfy independence by writing its own reviewer personas. Decide the minimum reviewer count and domain assignments during planning. If subagent capability is unavailable, state that enforcement cannot complete rather than silently substituting self-review.
- Give reviewers the relevant current sources and actual artifact evidence. Reviews must identify the inspected version, code/UI locations, screenshots or interaction observations as applicable. An intended design description alone cannot establish implementation adherence.
- For each finding, record the source page and section, relevant recommendation strength and conditions, observed violation, severity, required correction, and the evidence needed to verify the fix. Preserve “must,” “avoid,” “prefer,” “consider,” and platform exceptions accurately; don't turn every preference into an Apple requirement.
- Produce per-dimension adherence scores with an explicit rubric and denominator, alongside coverage and unverified items. Suggested dimensions for evaluation: platform conventions, layout/navigation, components/materials, accessibility/input, content/state continuity, and relevant device adaptation. The score is this skill's assessment, not an Apple certification.
- Require correction of applicable, substantiated findings within the user's constraints. A strong overall score must never cancel an unresolved mandatory-rule violation or a material issue. Reviewer disagreements should be resolved against source and artifact evidence, not by averaging scores or changing weights until the artifact passes.
- Re-review the changed artifact and affected adjacent behavior. Keep before/after findings and scores; reviewers must check the correction rather than accepting the implementer's assertion that it was fixed.
- A pass requires both the agreed score threshold and closure of required findings, with required review coverage complete. Unverified behavior remains unverified, never counted as passing. User-approved exceptions remain explicit exceptions rather than silently compliant items.
- Bound revision rounds to avoid an endless loop. On inability to inspect, unavailable tooling, irreconcilable constraints, or exhausted rounds, return a concrete non-pass status and remaining findings. Do not lower the quality bar to force completion.

## Decisions still open

Invocation syntax; default versus opt-in behavior; reviewer count; score scale and anchors; domain weights; pass threshold; severity definitions; required evidence by artifact type; revision budget; handling of approved exceptions; and the cost/latency budget.

Validate the mode with known-good and deliberately defective implementations, including subtle platform exceptions and regressions after a fix. Check that reviewers find real violations, avoid inventing requirements, and refuse to pass unresolved required findings. Keep this runtime product review distinct from the independent review used to create the distilled HIG corpus itself.

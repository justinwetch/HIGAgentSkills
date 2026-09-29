#!/usr/bin/env python3
"""Deterministic, evidence-bound scorer for Apple HIG enforce reviews.

The program deliberately scores only the frozen register and independently
verified observations.  It does not try to decide whether a reviewer was
honest, whether a source was interpreted correctly, or whether an observation
is semantically complete.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

SCHEMA = "apple-hig-enforce/v1"
RESULTS = {"met": 2, "partial": 1, "violated": 0, "missing": 0}
STRENGTHS = {"must", "prohibition", "prefer", "consider", "should", "recommendation", "recommend", "may", "optional", "example"}
KINDS = {"code", "render", "behavior"}


class Invalid(Exception):
    """Input or environment is not sufficient for a trustworthy result."""


def _obj(value: Any, where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise Invalid(f"{where} must be an object")
    return value


def _str(value: Any, where: str, *, nonempty: bool = True) -> str:
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise Invalid(f"{where} must be a non-empty string")
    return value


def _bool(value: Any, where: str) -> bool:
    if not isinstance(value, bool):
        raise Invalid(f"{where} must be boolean")
    return value


def _sha(value: Any, where: str) -> str:
    value = _str(value, where).lower()
    if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise Invalid(f"{where} must be a SHA-256 hex digest")
    return value


def _list(value: Any, where: str) -> list[Any]:
    if not isinstance(value, list):
        raise Invalid(f"{where} must be an array")
    return value


def _safe_relative(value: Any, where: str) -> str:
    raw = _str(value, where)
    p = Path(raw)
    # PureWindowsPath catches drive-qualified paths even when tested elsewhere.
    from pathlib import PureWindowsPath

    if p.is_absolute() or PureWindowsPath(raw).is_absolute() or "\x00" in raw:
        raise Invalid(f"{where} must be relative")
    parts = Path(raw.replace("\\", "/")).parts
    if not parts or any(part in ("", ".", "..") for part in parts):
        raise Invalid(f"{where} must be a normalized relative path")
    return "/".join(parts)


def _under(root: Path, relative: str, where: str) -> Path:
    root = root.resolve()
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise Invalid(f"{where} escapes its named root") from exc
    return candidate


def _file_sha(path: Path, where: str) -> str:
    if not path.is_file():
        raise Invalid(f"{where} does not name an existing file")
    digest = hashlib.sha256()
    try:
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise Invalid(f"cannot read {where}: {exc}") from exc
    return digest.hexdigest()


def _reference(source: Any, where: str, skill_root: Path) -> dict[str, str]:
    source = _obj(source, where)
    path = _safe_relative(source.get("path"), f"{where}.path")
    if not (path.startswith("references/hig/") and path.endswith(".md") and len(Path(path).parts) == 3):
        raise Invalid(f"{where}.path must be a local references/hig/<topic>.md file")
    quote = _str(source.get("quote"), f"{where}.quote")
    local = _under(skill_root, path, f"{where}.path")
    if not local.is_file():
        raise Invalid(f"{where}.path does not name an existing local reference")
    try:
        contents = local.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise Invalid(f"cannot read {where}.path: {exc}") from exc
    if quote not in contents:
        raise Invalid(f"{where}.quote is not an exact substring of {path}")
    frontmatter = contents.split("---", 2)
    if len(frontmatter) < 3 or not any(line.startswith("topic:") for line in frontmatter[1].splitlines()):
        raise Invalid(f"{where}.path is not an accepted HIG reference with topic frontmatter")
    return {"path": path, "quote": quote}


def normalize_register(raw: Any, skill_root: Path) -> dict[str, Any]:
    raw = _obj(raw, "register")
    revision = _str(raw.get("artifact_revision"), "register.artifact_revision")
    checks = _list(raw.get("checks"), "register.checks")
    if not checks:
        raise Invalid("register.checks cannot be empty")
    normalized: list[dict[str, Any]] = []
    ids: set[str] = set()
    for i, item in enumerate(checks):
        where = f"register.checks[{i}]"
        item = _obj(item, where)
        ident = _str(item.get("id"), f"{where}.id")
        if ident in ids:
            raise Invalid(f"duplicate check id: {ident}")
        ids.add(ident)
        owner = _str(item.get("owner"), f"{where}.owner")
        if owner not in {"A", "B"}:
            raise Invalid(f"{where}.owner must be A or B")
        dimension = _str(item.get("dimension"), f"{where}.dimension")
        applies = _bool(item.get("applies"), f"{where}.applies")
        exclusion = item.get("exclusion_reason", "")
        if not isinstance(exclusion, str):
            raise Invalid(f"{where}.exclusion_reason must be a string")
        if not applies and not exclusion.strip():
            raise Invalid(f"{where}.exclusion_reason is required when applies is false")
        if applies and exclusion.strip():
            raise Invalid(f"{where}.exclusion_reason is only for excluded checks")
        strength = _str(item.get("strength"), f"{where}.strength").lower()
        if strength not in STRENGTHS:
            raise Invalid(f"{where}.strength must be must, prohibition, prefer, or consider")
        derived_mandatory = strength in {"must", "prohibition"}
        if "mandatory" in item:
            mandatory = _bool(item.get("mandatory"), f"{where}.mandatory")
            if mandatory != derived_mandatory:
                raise Invalid(f"{where}.mandatory must be derived from Apple strength")
        else:
            mandatory = derived_mandatory
        if mandatory and strength not in {"must", "prohibition"}:
            raise Invalid(f"{where} upgrades an optional Apple recommendation to mandatory")
        expected = item.get("evidence_kind", item.get("expected_evidence_kind"))
        expected = _str(expected, f"{where}.evidence_kind").lower()
        if expected not in KINDS:
            raise Invalid(f"{where}.evidence_kind must be code, render, or behavior")
        reference = _reference(item.get("source"), f"{where}.source", skill_root)
        normalized.append(
            {
                "id": ident,
                "owner": owner,
                "dimension": dimension,
                "applies": applies,
                "exclusion_reason": exclusion if not applies else "",
                "strength": strength,
                "mandatory": mandatory,
                "source": reference,
                "expected_behavior": _str(item.get("expected_behavior"), f"{where}.expected_behavior"),
                "evidence_kind": expected,
            }
        )
    return {"artifact_revision": revision, "checks": normalized}


def _canonical_register(register: dict[str, Any]) -> str:
    checks = sorted(register["checks"], key=lambda c: c["id"])
    # The artifact revision is expected to change during a correction cycle;
    # only the check definitions are frozen.
    return json.dumps({"checks": checks}, sort_keys=True, separators=(",", ":"))


def _artifact_map(review: dict[str, Any], artifact_root: Path, where: str) -> dict[str, str]:
    entries = _list(review.get("artifact_files"), f"{where}.artifact_files")
    if not entries:
        raise Invalid(f"{where}.artifact_files cannot be empty")
    result: dict[str, str] = {}
    for i, raw in enumerate(entries):
        item = _obj(raw, f"{where}.artifact_files[{i}]")
        path = _safe_relative(item.get("path"), f"{where}.artifact_files[{i}].path")
        if path in result:
            raise Invalid(f"duplicate artifact file path: {path}")
        expected = _sha(item.get("sha256"), f"{where}.artifact_files[{i}].sha256")
        actual = _file_sha(_under(artifact_root, path, f"{where}.artifact_files[{i}].path"), f"{where}.artifact_files[{i}].path")
        if actual != expected:
            raise Invalid(f"stale artifact hash for {path}")
        result[path] = expected
    return result


def _evidence(raw: Any, where: str, check: dict[str, Any], artifact_root: Path, skill_root: Path, artifact_files: dict[str, str]) -> list[dict[str, Any]]:
    entries = _list(raw, where)
    out: list[dict[str, Any]] = []
    for i, value in enumerate(entries):
        item = _obj(value, f"{where}[{i}]")
        path = _safe_relative(item.get("file"), f"{where}[{i}].file")
        supplied = _sha(item.get("sha256"), f"{where}[{i}].sha256")
        kind = _str(item.get("kind"), f"{where}[{i}].kind").lower()
        if kind not in KINDS:
            raise Invalid(f"{where}[{i}].kind must be code, render, or behavior")
        observation = _str(item.get("observation"), f"{where}[{i}].observation")
        artifact_path = _under(artifact_root, path, f"{where}[{i}].file")
        if artifact_path.is_file():
            actual = _file_sha(artifact_path, f"{where}[{i}].file")
            if kind == "code" and path not in artifact_files:
                raise Invalid(f"artifact evidence {path} is absent from artifact_files")
            if (path in artifact_files and artifact_files[path] != supplied) or actual != supplied:
                raise Invalid(f"stale evidence hash for {path}")
        else:
            raise Invalid(f"evidence file does not exist under artifact-root: {path}")
        out.append({"file": path, "sha256": supplied, "kind": kind, "observation": observation})
    if out and not any(item["kind"] == check["evidence_kind"] for item in out):
        raise Invalid(f"{where}: check requires {check['evidence_kind']} evidence")
    return out


def _finding(raw: Any, where: str) -> dict[str, Any]:
    item = _obj(raw, where)
    result = {
        "observed": _str(item.get("observed"), f"{where}.observed"),
        "fix_location": _str(item.get("fix_location"), f"{where}.fix_location"),
        "action": _str(item.get("action"), f"{where}.action"),
        "verify": _str(item.get("verify"), f"{where}.verify"),
        "material": _bool(item.get("material"), f"{where}.material"),
        "closed": item.get("closed", item.get("resolved", False)),
    }
    if not isinstance(result["closed"], bool):
        raise Invalid(f"{where}.closed must be boolean")
    return result


def _findings(raw: Any, where: str) -> list[dict[str, Any]]:
    if raw is None:
        return []
    if isinstance(raw, dict):
        raw = [raw]
    entries = _list(raw, where)
    return [_finding(item, f"{where}[{i}]") for i, item in enumerate(entries)]


def _review(review_raw: Any, label: str, register: dict[str, Any], artifact_root: Path, skill_root: Path) -> dict[str, Any]:
    where = f"review-{label}"
    review = _obj(review_raw, where)
    reviewer_id = _str(review.get("reviewer_id"), f"{where}.reviewer_id")
    if not _bool(review.get("completed"), f"{where}.completed"):
        raise Invalid(f"{where}.completed must be true")
    if _str(review.get("artifact_revision"), f"{where}.artifact_revision") != register["artifact_revision"]:
        raise Invalid(f"{where}.artifact_revision does not match register")
    artifacts = _artifact_map(review, artifact_root, where)
    by_id = {c["id"]: c for c in register["checks"] if c["applies"]}
    assigned = {c["id"] for c in by_id.values() if c["owner"] == label}
    entries = _list(review.get("checks"), f"{where}.checks")
    seen: set[str] = set()
    scored: dict[str, dict[str, Any]] = {}
    for i, raw in enumerate(entries):
        item = _obj(raw, f"{where}.checks[{i}]")
        ident = _str(item.get("id"), f"{where}.checks[{i}].id")
        if ident in seen:
            raise Invalid(f"{where} contains duplicate check id: {ident}")
        seen.add(ident)
        if ident not in by_id:
            raise Invalid(f"{where} contains unknown or excluded check: {ident}")
        check = by_id[ident]
        if check["owner"] != label:
            raise Invalid(f"{where} cannot score check owned by {check['owner']}: {ident}")
        result = _str(item.get("result"), f"{where}.checks[{i}].result").lower()
        if result not in RESULTS:
            raise Invalid(f"invalid result for {ident}: {result}")
        evidence = []
        if result != "missing":
            evidence = _evidence(item.get("evidence"), f"{where}.checks[{i}].evidence", check, artifact_root, skill_root, artifacts)
            if not evidence:
                raise Invalid(f"{ident} has no evidence")
        elif item.get("evidence") not in (None, []):
            raise Invalid(f"missing result for {ident} cannot claim evidence")
        fs = _findings(item.get("findings", item.get("finding")), f"{where}.checks[{i}].findings")
        if result in {"partial", "violated"} and not fs:
            raise Invalid(f"{ident} requires a structured finding")
        scored[ident] = {"id": ident, "result": result, "evidence": evidence, "findings": fs}
    if seen != assigned:
        missing = sorted(assigned - seen)
        extra = sorted(seen - assigned)
        raise Invalid(f"{where} must score each exact owner-assigned check (missing={missing}, extra={extra})")

    mandatory_ids = {c["id"] for c in by_id.values() if c["mandatory"]}
    cross_raw = review.get("cross_cutting", review.get("cross_cutting_checks"))
    if mandatory_ids or cross_raw is not None:
        if cross_raw is None:
            raise Invalid(f"{where}.cross_cutting must identify every mandatory check")
        cross = _list(cross_raw, f"{where}.cross_cutting")
        cross_ids: set[str] = set()
        for i, value in enumerate(cross):
            item = _obj(value, f"{where}.cross_cutting[{i}]")
            ident = _str(item.get("id", item.get("check_id")), f"{where}.cross_cutting[{i}].id")
            check = by_id.get(ident)
            if not check:
                raise Invalid(f"unknown cross-cutting check: {ident}")
            if not _evidence(item.get("evidence"), f"{where}.cross_cutting[{i}].evidence", check, artifact_root, skill_root, artifacts):
                raise Invalid(f"cross-cutting inspection for {ident} has no evidence")
            if ident in cross_ids:
                raise Invalid(f"{where}.cross_cutting contains a duplicate check")
            cross_ids.add(ident)
        if not mandatory_ids <= cross_ids:
            raise Invalid(f"{where}.cross_cutting is incomplete")

    challenges = []
    for i, raw in enumerate(_list(review.get("challenges", []), f"{where}.challenges")):
        item = _obj(raw, f"{where}.challenges[{i}]")
        ident = _str(item.get("check_id", item.get("id")), f"{where}.challenges[{i}].check_id")
        check = by_id.get(ident)
        if not check:
            raise Invalid(f"unknown challenge check: {ident}")
        challenge_result = _str(item.get("result"), f"{where}.challenges[{i}].result").lower()
        if challenge_result not in RESULTS:
            raise Invalid(f"invalid challenge result for {ident}")
        if challenge_result != "missing":
            ev = _evidence(item.get("evidence"), f"{where}.challenges[{i}].evidence", check, artifact_root, skill_root, artifacts)
            if not ev:
                raise Invalid(f"challenge for {ident} has no evidence")
        else:
            ev = []
        resolved = item.get("resolved", False)
        if not isinstance(resolved, bool):
            raise Invalid(f"{where}.challenges[{i}].resolved must be boolean")
        resolution = item.get("resolution", "")
        if not isinstance(resolution, str):
            raise Invalid(f"{where}.challenges[{i}].resolution must be a string")
        if resolved and not resolution.strip():
            raise Invalid(f"{where}.challenges[{i}] needs an evidence-backed resolution")
        challenges.append({"check_id": ident, "result": challenge_result, "evidence": ev, "finding": _findings(item.get("findings", item.get("finding")), f"{where}.challenges[{i}].findings"), "resolved": resolved, "resolution": resolution})
    return {"reviewer_id": reviewer_id, "artifact_revision": register["artifact_revision"], "artifact_files": artifacts, "checks": scored, "challenges": challenges}


def _load(path: str, label: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise Invalid(f"cannot read {label} JSON: {exc}") from exc


def _guard_output(path: str, artifact_root: Path, skill_root: Path, inputs: list[str]) -> Path:
    target = Path(path).resolve()
    for root, label in ((artifact_root, "artifact-root"), (skill_root, "skill-root")):
        try:
            target.relative_to(root.resolve())
        except ValueError:
            continue
        if label == "artifact-root" and target.is_file():
            raise Invalid("output must not overwrite an artifact file")
        if label == "skill-root" and target.is_file():
            raise Invalid("output must not overwrite a HIG source file")
    if target in {Path(value).resolve() for value in inputs if value}:
        raise Invalid("output must not overwrite an input JSON file")
    return target


def evaluate(register_raw: Any, review_a_raw: Any, review_b_raw: Any, artifact_root: Path, skill_root: Path, cycle: int, previous_raw: Any = None) -> dict[str, Any]:
    errors: list[str] = []
    reasons: list[str] = []
    if not isinstance(cycle, int) or isinstance(cycle, bool) or cycle not in range(4):
        return {"schema": SCHEMA, "status": "blocked", "cycle": cycle, "score": {"earned": 0, "possible": 0, "percent": None}, "evidence_complete": False, "errors": ["cycle must be an integer from 0 through 3"], "limits": ["Verified hashes and scores cannot establish reviewer honesty or completeness.", "They cannot establish semantic source interpretation, reviewer independence, or behavior beyond the observations supplied by agents.", "Agents remain responsible for actual observation; tooling metadata is not proof."]}
    try:
        if cycle > 0 and previous_raw is None:
            raise Invalid("cycles 1-3 require --previous result.json")
        if cycle == 0 and previous_raw is not None:
            raise Invalid("--previous is only valid for correction cycles 1-3")
        register = normalize_register(register_raw, skill_root)
        if not artifact_root.is_dir():
            raise Invalid("artifact-root must be an existing directory")
        if not skill_root.is_dir():
            raise Invalid("skill-root must be an existing directory")
        review_a = _review(review_a_raw, "A", register, artifact_root, skill_root)
        review_b = _review(review_b_raw, "B", register, artifact_root, skill_root)
        if review_a["reviewer_id"] == review_b["reviewer_id"]:
            raise Invalid("reviewer identities must be distinct")
    except Invalid as exc:
        errors.append(str(exc))
        register = locals().get("register", {"artifact_revision": None, "checks": []})
        review_a = review_b = None

    if previous_raw is not None and not errors:
        try:
            previous = _obj(previous_raw, "previous result")
            prior_cycle = previous.get("cycle")
            if not isinstance(prior_cycle, int) or isinstance(prior_cycle, bool) or prior_cycle != cycle - 1:
                raise Invalid("previous result must be from the immediately preceding cycle")
            prior_register = previous.get("register")
            if not isinstance(prior_register, dict) or not isinstance(prior_register.get("checks"), list):
                raise Invalid("previous result has no frozen register")
            if not isinstance(previous.get("outcomes", {}), dict):
                raise Invalid("previous result outcomes must be an object")
            prior_hash = previous.get("register_hash")
            if prior_hash is not None:
                expected_hash = hashlib.sha256(_canonical_register(prior_register).encode("utf-8")).hexdigest()
                if prior_hash != expected_hash:
                    raise Invalid("previous result register hash does not match its frozen register")
            if _canonical_register(register) != _canonical_register(prior_register):
                raise Invalid("frozen register changed; start an explicit new run to rescope")
        except Invalid as exc:
            errors.append(str(exc))
        except (TypeError, KeyError, AttributeError) as exc:
            errors.append(f"malformed previous result: {exc!r}")

    applicable = [c for c in register.get("checks", []) if c.get("applies")]
    excluded = [c for c in register.get("checks", []) if not c.get("applies")]
    scores: dict[str, int] = {}
    outcomes: dict[str, str] = {}
    findings: list[dict[str, Any]] = []
    disagreements: list[dict[str, Any]] = []
    evidence_complete = not errors
    regressions: list[str] = []
    if review_a and review_b:
        for check in applicable:
            ident = check["id"]
            entry = (review_a["checks"] if check["owner"] == "A" else review_b["checks"])[ident]
            outcomes[ident] = entry["result"]
            scores[ident] = RESULTS[entry["result"]]
            if entry["result"] == "missing":
                evidence_complete = False
                reasons.append(f"required evidence missing for {ident}")
            elif entry["result"] in {"partial", "violated"}:
                # The current result remains authoritative: a finding marked
                # closed cannot turn a current mandatory/material failure into
                # a pass.  Nonmaterial optional findings may be residual when
                # the score still meets the threshold.
                if check["mandatory"]:
                    reasons.append(f"mandatory check is {entry['result']}: {ident}")
                if any(f["material"] for f in entry["findings"]):
                    reasons.append(f"material {entry['result']} finding for {ident}")
            for finding in entry["findings"]:
                findings.append({"check_id": ident, "reviewer": review_a["reviewer_id"] if check["owner"] == "A" else review_b["reviewer_id"], **finding})
                if finding["material"] and not finding["closed"]:
                    reasons.append(f"open material finding for {ident}")
                if check["mandatory"] and entry["result"] == "violated":
                    reasons.append(f"mandatory check violated: {ident}")
        if review_a["artifact_files"] != review_b["artifact_files"]:
            errors.append("reviewers are bound to different artifact file hashes")
        for reviewer, other in ((review_a, review_b), (review_b, review_a)):
            for challenge in reviewer["challenges"]:
                if challenge["result"] == "missing":
                    evidence_complete = False
                    reasons.append(f"required challenge evidence missing for {challenge['check_id']}")
                primary = other["checks"].get(challenge["check_id"])
                if primary and primary["result"] != challenge["result"]:
                    resolved = bool(challenge.get("resolved", False))
                    disagreements.append({"check_id": challenge["check_id"], "reviewer": reviewer["reviewer_id"], "primary_result": primary["result"], "challenge_result": challenge["result"], "resolved": resolved, "resolution": challenge["resolution"]})
                    if not resolved:
                        reasons.append(f"unresolved reviewer disagreement for {challenge['check_id']}")
                for finding in challenge["finding"]:
                    findings.append({"check_id": challenge["check_id"], "reviewer": reviewer["reviewer_id"], **finding})
                    if finding["material"] and not finding["closed"]:
                        reasons.append(f"open material challenge for {challenge['check_id']}")

    if previous_raw is not None and not errors:
        prior_outcomes = previous_raw.get("outcomes", {}) if isinstance(previous_raw, dict) else {}
        for ident, old in prior_outcomes.items():
            if old == "met" and outcomes.get(ident) in {"partial", "violated", "missing"}:
                regressions.append(ident)
        if regressions:
            reasons.append("regression in previously met checks: " + ", ".join(sorted(regressions)))

    dimensions: dict[str, dict[str, Any]] = {}
    for check in register.get("checks", []):
        dimensions.setdefault(check["dimension"], {"earned": 0, "possible": 0})
    for check in applicable:
        bucket = dimensions.setdefault(check["dimension"], {"earned": 0, "possible": 0})
        bucket["possible"] += 2
        bucket["earned"] += scores.get(check["id"], 0)
    for bucket in dimensions.values():
        bucket["score"] = round(100 * bucket["earned"] / bucket["possible"], 2) if bucket["possible"] else None
    earned = sum(scores.values())
    possible = 2 * len(applicable)
    percent = round(100 * earned / possible, 2) if possible else None
    if not applicable:
        reasons.append("no applicable checks")
    if errors:
        status = "blocked"
    elif not evidence_complete:
        status = "blocked"
    elif not applicable:
        status = "blocked"
    elif reasons:
        status = "needs changes"
    elif percent is not None and earned * 100 < possible * 90:
        status = "needs changes"
    elif percent is not None and len(outcomes) == len(applicable) and not any(not d["resolved"] for d in disagreements):
        status = "pass"
    else:
        status = "blocked"
    return {
        "schema": SCHEMA,
        "status": status,
        "cycle": cycle,
        "artifact_revision": register.get("artifact_revision"),
        "reviewers": ([review_a["reviewer_id"], review_b["reviewer_id"]] if review_a and review_b else []),
        "artifact_files": (review_a["artifact_files"] if review_a else {}),
        "register": register,
        "register_hash": hashlib.sha256(_canonical_register(register).encode("utf-8")).hexdigest(),
        "applicable_count": len(applicable),
        "excluded_count": len(excluded),
        "dimensions": dimensions,
        "score": {"earned": earned, "possible": possible, "percent": percent},
        "evidence_complete": evidence_complete,
        "outcomes": outcomes,
        "findings": findings,
        "disagreements": disagreements,
        "regressions": regressions,
        "errors": errors,
        "reasons": sorted(set(reasons)),
        "limits": [
            "Verified hashes and scores cannot establish reviewer honesty or completeness.",
            "They cannot establish semantic source interpretation, reviewer independence, or behavior beyond the supplied observations.",
            "Agents remain responsible for inspecting the actual artifact and recording truthful observations; tooling metadata is not accepted as proof.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score two evidence-bound Apple HIG enforce reviews")
    parser.add_argument("--register", required=True)
    parser.add_argument("--review-a", required=True)
    parser.add_argument("--review-b", required=True)
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--skill-root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--cycle", required=True, type=int, choices=range(4))
    parser.add_argument("--previous")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        output_path = _guard_output(args.output, Path(args.artifact_root), Path(args.skill_root), [args.register, args.review_a, args.review_b, args.previous or ""])
    except Invalid as exc:
        print(f"invalid output path: {exc}", file=sys.stderr)
        return 2
    try:
        previous = _load(args.previous, "previous result") if args.previous else None
        result = evaluate(_load(args.register, "register"), _load(args.review_a, "review-a"), _load(args.review_b, "review-b"), Path(args.artifact_root), Path(args.skill_root), args.cycle, previous)
    except Invalid as exc:
        result = {"schema": SCHEMA, "status": "blocked", "cycle": args.cycle, "score": {"earned": 0, "possible": 0, "percent": None}, "evidence_complete": False, "errors": [str(exc)], "limits": ["Verified hashes and scores cannot establish reviewer honesty or completeness.", "They cannot establish semantic source interpretation, reviewer independence, or behavior beyond the supplied observations.", "Agents remain responsible for actual observation; tooling metadata is not proof."]}
    try:
        output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 2
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

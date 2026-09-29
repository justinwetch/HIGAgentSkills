import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "hig_enforce.py"
spec = importlib.util.spec_from_file_location("hig_enforce", SCRIPT)
enforce = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(enforce)


class EnforceTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).parents[1] / "work" / "enforce-2026-09-14" / "unit-tmp"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.artifact = root / "artifact"
        self.skill = root / "skill"
        self.artifact.mkdir()
        self.skill.mkdir()
        (self.artifact / "app.txt").write_text("accessible action\n", encoding="utf-8")
        (self.skill / "references" / "hig").mkdir(parents=True)
        (self.skill / "references" / "hig" / "hig.md").write_text("---\ntopic: demo\n---\nSource clause: use accessible action.\n", encoding="utf-8")
        digest = self.sha(self.artifact / "app.txt")
        self.register = {
            "artifact_revision": "r1",
            "checks": [
                {"id": "a-1", "owner": "A", "dimension": "layout", "applies": True, "strength": "must", "source": {"path": "references/hig/hig.md", "quote": "use accessible action"}, "expected_behavior": "The action is present.", "evidence_kind": "code"},
                {"id": "b-1", "owner": "B", "dimension": "accessibility", "applies": True, "strength": "prefer", "source": {"path": "references/hig/hig.md", "quote": "use accessible action"}, "expected_behavior": "The action is usable.", "evidence_kind": "code"},
            ],
        }
        self.a = self.review("A", "alice", {"a-1": "met"}, digest)
        self.b = self.review("B", "bob", {"b-1": "met"}, digest)

    @staticmethod
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def evidence(self, digest, observation="observed source"):
        return [{"file": "app.txt", "sha256": digest, "kind": "code", "observation": observation}]

    def review(self, owner, identity, outcomes, digest):
        checks = []
        for ident, result in outcomes.items():
            item = {"id": ident, "result": result, "evidence": self.evidence(digest)}
            if result in {"partial", "violated"}:
                item["finding"] = {"observed": "defect", "fix_location": "app.txt:1", "action": "repair action", "verify": "repeat task", "material": result == "violated"}
            if result == "missing":
                item["evidence"] = []
            checks.append(item)
        cross = []
        for check in self.register["checks"]:
            if check["mandatory"] if "mandatory" in check else check["strength"] == "must":
                cross.append({"id": check["id"], "evidence": self.evidence(digest, "cross-cutting observation")})
        return {"reviewer_id": identity, "completed": True, "artifact_revision": "r1", "artifact_files": [{"path": "app.txt", "sha256": digest}], "cross_cutting": cross, "checks": checks}

    def evaluate(self, register=None, a=None, b=None, previous=None, cycle=0):
        return enforce.evaluate(register or self.register, a or self.a, b or self.b, self.artifact, self.skill, cycle, previous)

    def test_valid_pass_uses_derived_points(self):
        result = self.evaluate()
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["score"], {"earned": 4, "possible": 4, "percent": 100.0})
        self.assertEqual(result["dimensions"]["layout"]["score"], 100.0)

    def test_user_supplied_score_is_ignored(self):
        a = copy.deepcopy(self.a)
        a["score"] = {"percent": "not-a-number"}
        result = self.evaluate(a=a)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["score"]["earned"], 4)

    def test_partial_or_violation_needs_changes(self):
        a = self.review("A", "alice", {"a-1": "partial"}, self.sha(self.artifact / "app.txt"))
        result = self.evaluate(a=a)
        self.assertEqual(result["status"], "needs changes")
        self.assertIn("a-1", result["outcomes"])

    def test_missing_evidence_blocks(self):
        a = self.review("A", "alice", {"a-1": "missing"}, self.sha(self.artifact / "app.txt"))
        result = self.evaluate(a=a)
        self.assertEqual(result["status"], "blocked")
        self.assertFalse(result["evidence_complete"])

    def test_stale_artifact_hash_blocks(self):
        self.a["artifact_files"][0]["sha256"] = "0" * 64
        result = self.evaluate()
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(result["errors"])

    def test_same_reviewer_identity_blocks(self):
        b = copy.deepcopy(self.b)
        b["reviewer_id"] = "alice"
        result = self.evaluate(b=b)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("distinct" in e for e in result["errors"]))

    def test_missing_owner_check_blocks(self):
        a = copy.deepcopy(self.a)
        a["checks"] = []
        result = self.evaluate(a=a)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("owner-assigned" in e for e in result["errors"]))

    def test_duplicate_register_id_blocks(self):
        register = copy.deepcopy(self.register)
        register["checks"][1]["id"] = "a-1"
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("duplicate" in e for e in result["errors"]))

    def test_source_quote_must_be_local_exact_text(self):
        register = copy.deepcopy(self.register)
        register["checks"][0]["source"]["quote"] = "not in source"
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("exact substring" in e for e in result["errors"]))

    def test_optional_exclusion_is_counted_and_does_not_become_mandatory(self):
        register = copy.deepcopy(self.register)
        register["checks"].append({"id": "optional", "owner": "A", "dimension": "layout", "applies": False, "exclusion_reason": "The artifact has no animation.", "strength": "consider", "source": {"path": "references/hig/hig.md", "quote": "use accessible action"}, "expected_behavior": "Consider animation.", "evidence_kind": "render"})
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["excluded_count"], 1)
        self.assertEqual(result["score"]["possible"], 4)

    def test_arbitrary_supplement_is_not_a_hig_source(self):
        register = copy.deepcopy(self.register)
        register['checks'][0]['source']['path'] = 'references/supplement.json'
        with self.assertRaises(enforce.Invalid):
            enforce.normalize_register(register, self.skill)

    def test_malformed_previous_result_blocks_without_crashing(self):
        valid = self.evaluate()
        for mutate in (lambda p: p["register"].update(checks=[1]),
                       lambda p: p["register"]["checks"][0].pop("id"),
                       lambda p: p.update(outcomes=[])):
            previous = copy.deepcopy(valid)
            mutate(previous)
            result = self.evaluate(previous=previous, cycle=1)
            self.assertEqual(result["status"], "blocked")

    def test_json_input_with_byte_order_mark_loads(self):
        path = Path(self.tmp.name) / "bom.json"
        path.write_text('{"ok": true}', encoding="utf-8-sig")
        self.assertEqual(enforce._load(str(path), "register"), {"ok": True})

    def test_previous_result_freezes_register(self):
        previous = self.evaluate()
        register = copy.deepcopy(self.register)
        register["checks"][0]["expected_behavior"] = "weakened"
        result = self.evaluate(register=register, previous=previous, cycle=1)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("frozen register changed" in e for e in result["errors"]))

    def test_unresolved_challenge_is_needs_changes(self):
        b = copy.deepcopy(self.b)
        b["challenges"] = [{"check_id": "a-1", "result": "partial", "evidence": self.evidence(self.sha(self.artifact / "app.txt")), "resolved": False, "finding": {"observed": "different result", "fix_location": "app.txt:1", "action": "inspect", "verify": "repeat", "material": False}}]
        result = self.evaluate(b=b)
        self.assertEqual(result["status"], "needs changes")
        self.assertTrue(result["disagreements"])

    def test_resolved_challenge_requires_resolution_and_can_pass(self):
        b = copy.deepcopy(self.b)
        b["challenges"] = [{"check_id": "a-1", "result": "partial", "evidence": self.evidence(self.sha(self.artifact / "app.txt")), "resolved": True, "resolution": "A reinspection confirmed the primary met result.", "finding": {"observed": "initial disagreement", "fix_location": "app.txt:1", "action": "reconcile against source", "verify": "repeat inspection", "material": False, "closed": True}}]
        result = self.evaluate(b=b)
        self.assertEqual(result["status"], "pass")
        self.assertTrue(result["disagreements"][0]["resolved"])

    def test_cycle_requires_immediately_prior_result(self):
        result = self.evaluate(cycle=1)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("require --previous" in e for e in result["errors"]))
        previous = self.evaluate()
        result = self.evaluate(previous=previous, cycle=3)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("immediately preceding" in e for e in result["errors"]))

    def test_must_cannot_be_downgraded_with_mandatory_false(self):
        register = copy.deepcopy(self.register)
        register["checks"][0]["mandatory"] = False
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("derived" in e for e in result["errors"]))

    def test_score_below_threshold_is_needs_changes(self):
        b = self.review("B", "bob", {"b-1": "partial"}, self.sha(self.artifact / "app.txt"))
        b["checks"][0]["finding"]["closed"] = True
        result = self.evaluate(b=b)
        self.assertEqual(result["score"]["percent"], 75.0)
        self.assertEqual(result["status"], "needs changes")

    def test_path_traversal_blocks(self):
        register = copy.deepcopy(self.register)
        register["checks"][0]["source"]["path"] = "../hig.md"
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "blocked")

    def test_nonmaterial_recommendation_can_remain_at_95(self):
        register = copy.deepcopy(self.register)
        for i in range(8):
            check = copy.deepcopy(register["checks"][1])
            check["id"] = f"b-extra-{i}"
            register["checks"].append(check)
        outcomes = {c["id"]: "met" for c in register["checks"] if c["owner"] == "B"}
        outcomes["b-1"] = "partial"
        b = self.review("B", "bob", outcomes, self.sha(self.artifact / "app.txt"))
        result = self.evaluate(register=register, b=b)
        self.assertEqual(result["score"]["percent"], 95.0)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(len(result["findings"]), 1)
        b["checks"][0]["finding"]["material"] = True
        self.assertEqual(self.evaluate(register=register, b=b)["status"], "needs changes")

    def test_real_correction_can_change_artifact_revision(self):
        previous = self.evaluate()
        (self.artifact / "app.txt").write_text("corrected accessible action\n", encoding="utf-8")
        digest = self.sha(self.artifact / "app.txt")
        register = copy.deepcopy(self.register)
        register["artifact_revision"] = "r2"
        a = self.review("A", "alice", {"a-1": "met"}, digest)
        b = self.review("B", "bob", {"b-1": "met"}, digest)
        a["artifact_revision"] = b["artifact_revision"] = "r2"
        result = self.evaluate(register=register, a=a, b=b, previous=previous, cycle=1)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["register_hash"], previous["register_hash"])

    def test_unavailable_reviewer_blocks(self):
        b = copy.deepcopy(self.b)
        b["completed"] = False
        self.assertEqual(self.evaluate(b=b)["status"], "blocked")
        result = enforce.evaluate(self.register, self.a, None, self.artifact, self.skill, 0)
        self.assertEqual(result["status"], "blocked")

    def test_code_cannot_substitute_for_behavior(self):
        register = copy.deepcopy(self.register)
        register["checks"][1]["evidence_kind"] = "behavior"
        result = self.evaluate(register=register)
        self.assertEqual(result["status"], "blocked")
        self.assertTrue(any("requires behavior" in e for e in result["errors"]))

    def test_regression_is_retained_and_cycle_limit_is_enforced(self):
        previous = self.evaluate()
        a = self.review("A", "alice", {"a-1": "violated"}, self.sha(self.artifact / "app.txt"))
        result = self.evaluate(a=a, previous=previous, cycle=1)
        self.assertEqual(result["status"], "needs changes")
        self.assertEqual(result["regressions"], ["a-1"])
        for cycle in (2, 3):
            result = self.evaluate(a=a, previous=result, cycle=cycle)
            self.assertEqual(result["status"], "needs changes")
        self.assertEqual(self.evaluate(a=a, previous=result, cycle=4)["status"], "blocked")

    def test_supplemental_evidence_keeps_required_kind(self):
        register = copy.deepcopy(self.register)
        register["checks"][1]["evidence_kind"] = "behavior"
        b = copy.deepcopy(self.b)
        (self.artifact / "runtime.json").write_text('{"observed":true}', encoding="utf-8")
        b["checks"][0]["evidence"].append({"file": "runtime.json", "sha256": self.sha(self.artifact / "runtime.json"), "kind": "behavior", "observation": "Executed interaction."})
        self.assertEqual(self.evaluate(register=register, b=b)["status"], "pass")

    def test_extra_cross_cutting_inspection_does_not_replace_mandatory(self):
        a = copy.deepcopy(self.a)
        a["cross_cutting"].append({"id": "b-1", "evidence": self.evidence(self.sha(self.artifact / "app.txt"))})
        self.assertEqual(self.evaluate(a=a)["status"], "pass")
        a["cross_cutting"] = a["cross_cutting"][1:]
        self.assertEqual(self.evaluate(a=a)["status"], "blocked")


if __name__ == "__main__":
    unittest.main()

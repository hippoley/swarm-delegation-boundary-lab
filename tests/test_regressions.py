"""Regression vectors for synthetic conformance semantics."""
import copy
import json
import unittest
from pathlib import Path
from delegation_conformance import evaluate

BASE = json.loads((Path(__file__).resolve().parents[1] / "examples/allow.json").read_text())


class RegressionTests(unittest.TestCase):
    def case(self):
        return copy.deepcopy(BASE)

    def test_multihop_scope_intersection(self):
        case = self.case()
        case["delegations"].append({"id": "d2", "parent": "worker", "child": "subagent", "scope": ["read", "write"]})
        case["request"].update({"principal": "subagent", "delegation_path": ["d1", "d2"], "permission": "write"})
        case["observed_decision"] = "allow"
        self.assertEqual(evaluate(case)["status"], "FAIL")

    def test_multihop_legitimate_read(self):
        case = self.case()
        case["delegations"].append({"id": "d2", "parent": "worker", "child": "subagent", "scope": ["read"]})
        case["request"].update({"principal": "subagent", "delegation_path": ["d1", "d2"]})
        self.assertEqual(evaluate(case)["status"], "PASS")

    def test_broken_chain_cannot_authorize(self):
        case = self.case()
        case["delegations"][0]["parent"] = "unrelated"
        self.assertEqual(evaluate(case)["expected"], "deny")

    def test_root_may_act_without_delegation(self):
        case = self.case()
        case["request"].update({"principal": "root", "delegation_path": []})
        self.assertEqual(evaluate(case)["status"], "PASS")

    def test_empty_path_cannot_claim_other_principal(self):
        case = self.case()
        case["request"]["delegation_path"] = []
        self.assertEqual(evaluate(case)["status"], "FAIL")

    def test_duplicate_edge_ids_indeterminate(self):
        case = self.case()
        case["delegations"].append(dict(case["delegations"][0]))
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")

    def test_non_boolean_observation_indeterminate(self):
        case = self.case()
        case["observed_decision"] = True
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")


if __name__ == "__main__":
    unittest.main()

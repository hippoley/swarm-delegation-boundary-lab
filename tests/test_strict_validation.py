import copy
import json
import unittest
from pathlib import Path
from delegation_conformance import evaluate
from delegation_conformance.core import validate

BASE = json.loads((Path(__file__).resolve().parents[1] / "examples/allow.json").read_text())

class StrictValidationTests(unittest.TestCase):
    def case(self):
        return copy.deepcopy(BASE)

    def test_baseline_valid(self):
        validate(self.case())

    def test_top_level_extra(self):
        c = self.case(); c["unexpected"] = "x"
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_nested_request_extra(self):
        c = self.case(); c["request"]["unexpected"] = "x"
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_edge_extra(self):
        c = self.case(); c["delegations"][0]["unexpected"] = "x"
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_missing_required(self):
        c = self.case(); del c["root_scope"]
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_duplicate_scope(self):
        c = self.case(); c["root_scope"] = ["read", "read"]
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_invalid_observation(self):
        c = self.case(); c["observed_decision"] = True
        self.assertEqual(evaluate(c)["reason"], "INVALID_INPUT")

    def test_missing_observation_is_distinct(self):
        c = self.case(); del c["observed_decision"]
        validate(c)
        self.assertEqual(evaluate(c)["reason"], "MISSING_OBSERVATION")

if __name__ == "__main__":
    unittest.main()

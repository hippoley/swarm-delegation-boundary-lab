import json
import unittest
from pathlib import Path
from delegation_conformance import evaluate

ROOT = Path(__file__).resolve().parents[1]


class ConformanceTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "examples" / name).read_text())

    def test_valid_read(self):
        self.assertEqual(evaluate(self.load("allow.json"))["status"], "PASS")

    def test_widening_detected(self):
        result = evaluate(self.load("violation.json"))
        self.assertEqual((result["status"], result["expected"]), ("FAIL", "deny"))

    def test_no_observation(self):
        case = self.load("allow.json")
        del case["observed_decision"]
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")

    def test_wrong_principal(self):
        case = self.load("allow.json")
        case["request"]["principal"] = "impostor"
        self.assertEqual(evaluate(case)["status"], "FAIL")

    def test_missing_edge(self):
        case = self.load("allow.json")
        case["request"]["delegation_path"] = ["missing"]
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")

    def test_malformed_scope(self):
        case = self.load("allow.json")
        case["root_scope"] = "read"
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")

    def test_cycle_repeated_edge(self):
        case = self.load("allow.json")
        case["request"]["delegation_path"] = ["d1", "d1"]
        self.assertEqual(evaluate(case)["status"], "INDETERMINATE")


if __name__ == "__main__":
    unittest.main()

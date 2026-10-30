"""Usage: python -m delegation_conformance path/to/scenario.json"""
import json
import sys
from pathlib import Path
from .core import evaluate


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python -m delegation_conformance SCENARIO.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "INDETERMINATE", "reason": "UNREADABLE_INPUT", "detail": str(exc)}))
        return 2
    result = evaluate(data)
    print(json.dumps(result, sort_keys=True))
    return {"PASS": 0, "FAIL": 1, "INDETERMINATE": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())

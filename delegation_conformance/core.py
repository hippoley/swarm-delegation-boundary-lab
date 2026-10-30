"""Deterministic, dependency-free, offline delegation trace checker.

This checks a deliberately narrow synthetic contract, NOT cryptographic identity.
It does not verify external agent claims or production authorization systems.
"""
from __future__ import annotations

from typing import Any


class InvalidScenario(ValueError):
    pass


def _strings(value: Any, field: str) -> set[str]:
    if not isinstance(value, list) or any(not isinstance(x, str) or not x for x in value):
        raise InvalidScenario(f"{field} must be a list of nonempty strings")
    if len(set(value)) != len(value):
        raise InvalidScenario(f"{field} contains duplicates")
    return set(value)


def _check_keys(obj: Any, required: set[str], optional: set[str], name: str) -> None:
    if not isinstance(obj, dict):
        raise InvalidScenario(f"{name} must be an object")
    missing = required - obj.keys()
    unknown = obj.keys() - required - optional
    if missing or unknown:
        raise InvalidScenario(f"{name}: missing={sorted(missing)}, unknown={sorted(unknown)}")


def validate(data: Any) -> None:
    _check_keys(data, {"schema_version", "scenario_id", "root_principal", "root_scope", "delegations", "request"}, {"observed_decision"}, "scenario")
    if data.get("schema_version") != "0.1":
        raise InvalidScenario("schema_version must be 0.1")
    for field in ("scenario_id", "root_principal"):
        if not isinstance(data.get(field), str) or not data[field]:
            raise InvalidScenario(f"{field} must be a nonempty string")
    _strings(data.get("root_scope"), "root_scope")
    edges = data.get("delegations")
    if not isinstance(edges, list):
        raise InvalidScenario("delegations must be a list")
    ids = set()
    for i, edge in enumerate(edges):
        _check_keys(edge, {"id", "parent", "child", "scope"}, set(), f"delegations[{i}]")
        for key in ("id", "parent", "child"):
            if not isinstance(edge.get(key), str) or not edge[key]:
                raise InvalidScenario(f"delegations[{i}].{key} invalid")
        if edge["id"] in ids:
            raise InvalidScenario("duplicate delegation id")
        ids.add(edge["id"])
        _strings(edge.get("scope"), f"delegations[{i}].scope")
    req = data.get("request")
    _check_keys(req, {"principal", "permission", "delegation_path"}, set(), "request")
    for field in ("principal", "permission"):
        if not isinstance(req.get(field), str) or not req[field]:
            raise InvalidScenario(f"request.{field} invalid")
    path = req.get("delegation_path")
    if not isinstance(path, list) or any(not isinstance(x, str) for x in path):
        raise InvalidScenario("request.delegation_path must be string list")
    if len(path) != len(set(path)):
        raise InvalidScenario("delegation_path repeats an edge")
    if "observed_decision" in data and data["observed_decision"] not in ("allow", "deny"):
        raise InvalidScenario("observed_decision must be allow or deny")


def evaluate(data: Any) -> dict[str, Any]:
    """Return PASS/FAIL/INDETERMINATE for a synthetic observed decision.

    PASS means observed decision agrees with the limited reference oracle.
    FAIL means it disagrees. INDETERMINATE means evidence is missing/ambiguous.
    """
    try:
        validate(data)
    except InvalidScenario as exc:
        return {"status": "INDETERMINATE", "reason": "INVALID_INPUT", "detail": str(exc), "expected": None}
    observed = data.get("observed_decision")
    if observed not in ("allow", "deny"):
        return {"status": "INDETERMINATE", "reason": "MISSING_OBSERVATION", "expected": None}
    edges = {e["id"]: e for e in data["delegations"]}
    principal = data["root_principal"]
    effective = _strings(data["root_scope"], "root_scope")
    for edge_id in data["request"]["delegation_path"]:
        edge = edges.get(edge_id)
        if edge is None:
            return {"status": "INDETERMINATE", "reason": "UNKNOWN_EDGE", "expected": None}
        if edge["parent"] != principal:
            expected = "deny"
            return _compare(observed, expected, "BROKEN_CHAIN")
        principal = edge["child"]
        effective &= set(edge["scope"])
    if principal != data["request"]["principal"]:
        return _compare(observed, "deny", "PRINCIPAL_MISMATCH")
    expected = "allow" if data["request"]["permission"] in effective else "deny"
    return _compare(observed, expected, "SCOPE_CHECK")


def _compare(observed: str, expected: str, reason: str) -> dict[str, Any]:
    return {"status": "PASS" if observed == expected else "FAIL",
            "reason": reason, "expected": expected, "observed": observed}

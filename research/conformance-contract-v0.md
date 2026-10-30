# Portable Delegation Conformance Contract v0 — PROPOSAL ONLY

A vendor-neutral *test artifact* contract, not a credential or authorization protocol.

## Inputs

1. Scenario: principal identities, original authorization, delegation edges, action requests, event order, revocation visibility assumptions.
2. Trace: observed identity claims, delegated scopes, tool decisions, timestamps, and supporting evidence references.
3. Adapter metadata: source framework, version, mapping limitations, unsupported fields.

## Output

- `PASS`: all evaluated invariants supported by sufficient evidence.
- `FAIL`: counterexample with path, event, invariant, and expected/observed behavior.
- `INDETERMINATE`: missing evidence, ambiguous semantics, or unsupported feature; **never silently PASS**.

## Invariants (candidate)

- I1: Effective scope cannot widen across a valid delegation edge.
- I2: Display-name changes cannot change the principal being authorized.
- I3: Credential claims alone do not prove possession or authorization.
- I4: Post-revocation actions must be judged against an explicitly stated revocation visibility model.
- I5: Replay evaluation distinguishes reusable grants from single-use execution requests.
- I6: Evidence hash verification proves bytes unchanged relative to a trusted anchor, not that events were truthful.

## Versioning and evidence

Each test vector carries schema version, scenario ID, provenance, fixture digest, expected invariant, and reviewer status. Conformance reports include implementation version, adapter version, tested invariant set, evidence availability and reproducible commands.

## Boundaries

No real endpoints, live credentials, devices, or claims of formal verification. This contract has no implementation or external adopters yet. The first viable post-sprint milestone is one independent third-party trace mapped into the contract and verified without manual interpretation.

# Schema semantics and implementation gaps (pre-sprint)

The JSON Schema in `schemas/scenario-v0.1.schema.json` documents the **synthetic** input envelope. It is not a replacement for the Python semantic validator, which additionally checks unique delegation IDs. The schema does not independently validate delegation chain continuity, principal authentication, revocation, replay, signature integrity, or time semantics.

**Known mismatch:** the JSON Schema rejects additional properties, while the current Python validator ignores them. The schema is a proposed stricter input contract, not yet an enforced runtime contract. Do not advertise strict JSON Schema conformance until the parser and validator agree and are tested against the same fixtures.

Unknown delegation IDs currently yield INDETERMINATE (missing chain evidence), while a known but broken parent-child link yields expected DENY. This distinction is deliberate for incomplete traces but may need refinement for complete-trace scenarios.

The PASS result means the observed decision matches this narrow oracle. It does not establish cryptographic identity, trace authenticity, revocation enforcement or general security.

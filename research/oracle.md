# Independent decision oracle (pre-sprint design)

The oracle is independent of all three evaluated policies. It computes the expected decision from an immutable scenario specification, not from any evaluated policy's output.

## Scenario fields

- scenario_id, seed, root_principal_id, root_authority
- delegation_edges: parent_id, child_id, requested_scope, issued_at, expires_at, delegation_id
- identity_events: rename, clone, key rotation
- revocations: delegation_id, effective_at
- action: actor_id, resource, operation, timestamp, presented_credential_id
- expected_decision and expected_reason (human-reviewed test fixture)

## Oracle rule

An action is allowed iff there is a valid chain from the root principal to the actor; every delegation is bound to the intended principal, unexpired, and not revoked at action time; and the action belongs to the intersection of all authority scopes along the chain. Renaming a display name does not change principal identity. Cloning a display name does not grant identity. Replayed or revoked credentials do not restore authority.

The oracle specification is a normative test definition, not an empirical finding. Include a separate review of the oracle and adversarial cases where the oracle itself may be wrong.

## Avoid circularity

1. Freeze scenario fixtures and expected decisions before executing A/B/C.
2. Run a standalone reference oracle and compare it with hand-reviewed fixtures.
3. Never derive ground truth from the output of treatment C.
4. Keep oracle version, fixture hashes, reviewer notes, and disagreements.
5. Report invalid or ambiguous fixtures separately rather than silently excluding them.

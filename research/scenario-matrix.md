# Scenario matrix (pre-sprint design)

| Family | Legitimate control | Adversarial variation | Expected invariant |
| --- | --- | --- | --- |
| Normal delegation | Read permission delegated for read | None | Authorized read succeeds |
| Scope widening | Read delegated for read | Child requests write | Write must be denied |
| Rename | Principal changes display name | Old name reused by another principal | Identity remains tied to stable ID |
| Clone/impersonation | Distinct principals share similar labels | Clone claims parent's identity | No privilege from label alone |
| Revocation | Valid delegation before revocation | Execute after revocation timestamp | Revoked chain must fail |
| Replay | Fresh valid credential | Reuse expired/revoked credential | Stale credential must fail |

For each family include both positive and negative cases, matched across A/B/C. Proposed 20 seeds per family per treatment is a budget, not a completed sample count. No real-world targets, devices, or credentials.

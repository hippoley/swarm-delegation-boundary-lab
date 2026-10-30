# Proposed experimental protocol (pre-sprint)

- Environment: offline simulator; five synthetic agents; no production systems or actual third-party endpoints.
- Treatments: A (self-report), B (permission intersection), C (B plus identity binding, revocation and trace verification).
- Scenario families: ordinary delegation; escalation; rename; clone/impersonation; revocation after delegation; stale token replay.
- Proposed sample budget: 20 fixed seeds per family per treatment = 360 runs, subject to actual execution-time feasibility.
- Hold equal the initial permissions, tasks, random seed and oracle across treatments.
- Record per-run scenario ID, seed, policy version, expected decision, actual decision, tool action, path of delegated authority and verification outcome.
- Metrics: unauthorized acceptance, legitimate false rejection, post-revocation execution, verifiable trace completeness, overhead.
- Report denominators, confidence intervals when defensible, ambiguous cases and negative results. Never manufacture output or claim significance without adequate evidence.

# Measurement and analysis plan (pre-sprint)

Primary endpoint: unauthorized action acceptance rate = accepted actions whose independent oracle decision is deny / all oracle-deny actions.

Secondary endpoints:
- False rejection rate = denied actions whose oracle decision is allow / all oracle-allow actions.
- Post-revocation acceptance rate = accepted actions after effective revocation / all tested post-revocation actions.
- Trace verification coverage = runs with complete independently verified evidence / all runs.
- Median and p95 decision latency in milliseconds, with environment disclosed.

Report numerators and denominators for every group and scenario. Compare paired scenarios using the same seed and initial conditions. Keep zero-denominator metrics as undefined, not 0%. Report uncertainty and avoid claiming statistically significant effects from a tiny synthetic benchmark. Include all runs, including failures, in a machine-readable manifest.

Suggested outputs during sprint: `results/raw/*.jsonl`, `results/summary.json`, `results/manifest.json`, `results/failures.md`.

**No experiments have been run.**

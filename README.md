# Delegation Boundary Lab

Pre-sprint research planning for **Apart Research Swarm Alignment Hackathon (November 6–8, 2026)**, Track 3: Strengthening Agent Infrastructure.

**Research question:** Does an agent's effective authority remain bounded when tasks pass through multiple delegates, including renaming, cloning, revocation, and replay?

**Status:** Planning only (October 30, 2026). No simulator, experiments, evaluation results, or competition submission are claimed here.

## Proposed comparisons

- A: self-reported downstream permissions (baseline)
- B: effective permissions constrained by the intersection of parent authority and delegation scope
- C: B plus stable identity binding, revocation checks, and independently checkable evidence

All tools and agents will be simulated offline. Findings, including negative findings, will be reported after experiments are actually run.

See `research/` for the pre-registration plan, `PREEXISTING_WORK.md` for prior-work disclosure, and `report/report_draft.md` for the empty report outline.

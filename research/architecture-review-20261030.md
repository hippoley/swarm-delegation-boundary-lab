# Architecture audit — 2026-10-30 (pre-sprint)

## Verdict

The repository contains a research plan, not a runnable conformance infrastructure. The original A/B/C design conflates authorization attenuation, identity authentication, revocation consistency, replay prevention, and evidence integrity. It cannot causally attribute improvements to any one primitive without additional controlled comparisons.

## User stories and status

| Story | Status | Gap | Closure evidence |
|---|---|---|---|
| Root delegation | design | no canonical data model | schema + independent parser tests |
| Scope attenuation | design | no operation/resource/constraint semantics | fixed vectors and implementation |
| Rename | design | display name confused with principal | stable ID vectors |
| Clone | design | no proof-of-possession trust model | authentication test doubles |
| Revocation | design | no propagation or observation model | time-stamped vectors |
| Replay | design | no unique message consumption state | replay vectors |
| Independent oracle | design | no implementation or human review | frozen fixtures and separate review |
| Evidence verification | design | no envelope/verifier | corruption-detection tests |
| Framework adapter | missing | no external trace mapping | independently runnable adapter |
| External adoption | missing | no third-party integration | external issue/PR/use report |
| Sprint paper | outline | no empirical results | actual report and raw data |
| Compatibility | missing | no schema/version policy | versioned fixtures and changelog |

## Methodology corrections

- Separate *policy decision correctness* from *identity proof*, *revocation visibility*, *replay protection*, and *evidence integrity*.
- Use matched scenarios and independent oracle decisions. Include authorized positive controls.
- Define a trusted enforcement point explicitly. Never equate signed events with truthful events.
- Compare incremental ablations (scope-only; scope+identity; scope+revocation; scope+replay; scope+evidence), rather than treating C as a single unexplained bundle.
- Mark oracle assumptions and ambiguities. Define what a replay is (one-time-use request vs reusable authorization grant).

## Decision

Keep the sprint research question narrow: privilege attenuation under delegation. Treat a portable conformance verifier as a *post-sprint hypothesis* until a third-party trace and independent integration exist.

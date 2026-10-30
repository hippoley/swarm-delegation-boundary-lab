# Investment / pivot gates

## Gate 0 — sprint research integrity

Finish an honestly reproducible offline comparison with raw data, explicit assumptions and a report. No synthetic result may be passed off as measured.

## Gate 1 — independently usable contract

At least one external contributor can run the verifier from instructions without author intervention. If this fails, improve ergonomics before adding protocols.

## Gate 2 — real external integration

At least one third-party framework trace is mapped through a documented adapter, with explicit unsupported fields. If absent, do not claim interoperability.

## Gate 3 — demand signal

At least one non-author user files an issue, references a test vector, contributes an adapter, or uses the verifier in CI. Stars and page views alone are insufficient.

## Pivot rule

If no independently reproduced run or external integration materializes after a focused 4–6 week post-sprint probe, stop adding custom protocol features. Reassess upstream contribution to existing identity/conformance projects or shift to a narrower adapter that an active maintainer explicitly requests.

## Cost control

Offline, standard-library-first, no paid model or cloud infrastructure required for the initial probe.

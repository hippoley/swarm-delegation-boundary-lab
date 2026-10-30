# Pre-sprint prototype disclosure

This implementation was created **before** the November 6–8, 2026 sprint and must not be claimed as sprint-original code. It is a tiny, standard-library-only reference checker for synthetic permission attenuation along an explicitly supplied delegation path.

Run: `python -m unittest discover -s tests -v`

CLI examples:

```sh
python -m delegation_conformance examples/allow.json
python -m delegation_conformance examples/violation.json
```

The second command should exit 1 with FAIL because observed allow contradicts the reference oracle's deny.

**Limitations:** no JSON Schema file yet, no cryptographic principal verification, no revocation, replay, concurrency, signed evidence, trace adapter, external framework integration, CI, or independently validated human oracle. The checker compares observed decisions against a deliberately narrow normative model; it does not establish a real system's security. No contest experiment results are claimed.

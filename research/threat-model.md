# Proposed threat model (pre-sprint)

The attacker controls only a synthetic downstream agent's claimed identity, requested delegated scope, and simulated action requests. A trusted local reference monitor is assumed for B/C, and that assumption will be called out explicitly.

Threats: authorization widening, confused deputy, identity renaming, identity cloning, stale delegation after revocation and replay.

Out of scope: real-world penetration testing, malware, attacks on public services, credential theft, or physical devices.

Audit logs alone do not establish tamper resistance. Any evidence-integrity claim requires a real verification procedure.

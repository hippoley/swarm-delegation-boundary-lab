# Standards and adjacent work — verified starting points (2026-10-30)

This is a comparison baseline, not a claim of novelty or endorsement.

| Source | Established/relevant capability | Gap to investigate, not yet proven |
|---|---|---|
| IETF RFC 8693 | Token exchange, delegation vs impersonation | multi-framework trace conformance evidence |
| IETF draft-sweeney-wimse-credential-delegation-00 (July 2026, Internet-Draft) | attenuated credentials, cascading revocation, audit-chain proposal | independent implementation-level test vectors |
| IETF draft-sharif-openid-agent-identity-02 (Oct 2026, Internet-Draft) | agent identity claims | implementation-level identity/delegation testing |
| OWASP AI Agent Security Cheat Sheet | multi-agent trust boundaries, least privilege, anti-replay | reproducible portable test artifacts |
| MCP authorization security considerations (2026-07-28) | token audience validation, no token passthrough | delegated chains crossing MCP and other runtimes |

Primary links:
- https://www.rfc-editor.org/rfc/rfc8693.html
- https://datatracker.ietf.org/doc/html/draft-sweeney-wimse-credential-delegation-00
- https://datatracker.ietf.org/doc/draft-sharif-openid-agent-identity/
- https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx

**Novelty status:** Unverified. Do not claim invention of delegation attenuation, identity binding, revocation, or tamper-evident logs. Focus on evidence-backed conformance and interoperability gaps.

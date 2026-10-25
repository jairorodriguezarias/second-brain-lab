# Area — AI Security Research

Ongoing responsibility (no end date). The AISB track + the chaos-monkey project (AI red teaming for voice contact centers).

## Scope
- OWASP Top 10 LLMs (LLM01 prompt injection → LLM10 model DoS)
- NIST AI RMF + ATLAS (adversarial tactics against ML)
- Supply-chain risks (model provenance, vector-DB reversal, MCP server exploits)
- chaos-monkey (ia2sip): AI-driven red teaming of voice — the hero project for the AISB interview

## Active threads
- AISB Part 2 practice (post-interview)
- chaos-monkey design: intent-induction → jailbreak → exfiltration over the voice channel
- RAG security: vector DB breach → embedding reversal → original-text leak (see [[RAG — Retrieval-Augmented Generation]])

## Reusable assets
- [[AISB — OWASP & AI Security Knowledge]]
- [[AISB Use case — Chaos Monkey (ia2sip)]]
- The lab's human-gate pattern IS a security control (the only write edge into Resources is gated)

## Notes
- Honest failure (R1) is a security property too: a model that says "not in the notes" is safer than one that invents.
- The gate (R4) is the lab's access-control on the second brain.

---
SOURCE: 2 - Areas/Area — AI Security Research.md
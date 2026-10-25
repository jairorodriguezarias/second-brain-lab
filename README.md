# Second Brain Lab — a minimal local starter

[![License: MIT](https://img.shields.io/badge/license-MIT-A51C30)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/ollama-local-5DB28B)](https://ollama.com/)
![Keys](https://img.shields.io/badge/API_keys-none-000000)
![Cloud](https://img.shields.io/badge/cloud-none-000000)

> **The minimum to start:** one small local model — `gemma4:e2b-it-qat` on ollama — reading
> your own PARA notes. No keys, no cloud, no pip. That's the whole product. Everything else
> (context engineering, research loops, routing, the human gate) we **grow together in class**.

A 2B model on its own forgets everything between calls and invents facts. The fix is not a
bigger model — it's **files**: your to-do and your notes go into the prompt each turn, and the
model's memory lives in those files, not in its weights. This repo is the smallest setup that
makes that work — a **PARA vault template** plus the agent's contract. The runner (the code that
talks to the local model) is **built live in class**, one function per phase; the instructor's
finished version lives in the `second-brain-lab` skill (`brain_agent.py` · `brain_research.py` ·
`brain_graph.py`). The vault you build is **PARA-native** — the same triage methodology
professionals use.

## Requirements

- [ollama](https://ollama.com/) ≥ 0.34.4 (`brew install ollama` — macOS · no keys, no cloud)
- the model: `ollama pull gemma4:e2b-it-qat` (~4.3 GB)
- Python 3.9+ — **stdlib only: no pip, no venv, no internet during class**

## Start in 4 commands

```bash
git clone https://github.com/jairorodriguezarias/second-brain-lab.git   # or Code → Download ZIP → unzip
cd second-brain-lab
bash new_lab_vault.sh alfa        # your working vault → lab-vault-alfa/ (+ Obsidian opens it)
```

Your team vault is ready in Obsidian. In class we build the runner together — three functions,
one per phase (A · harness → B · loop → C · graph). Each function is a small, nameable fix; we
introduce the concept behind each one live, then you write it.

| Phase | What your function does when it's done |
|---|---|
| **A — harness** | bare model → the amnesia receipt · files in the prompt → it KNOWS · typed contract `{"action":"ADD\|DONE\|MOVE\|DELETE","item":...,"cite":"SOURCE: 1 - Projects/Inbox.md"}` · DONE moves the line to `4 - Archive/`, dated |
| **B — loop** | draft → self-critique → refine · evidence checks (≥2 SOURCE lines + OPEN QUESTION, no invented numbers) · an honest-fail exit · your own rule R6 |
| **C — graph** | cold router misroutes → few-shot + § catalog fix · TASK / FACT / NEW · NEW = draft → 👤 human gate → only write path into `3 - Resources/` |

## What's inside (the lab vault, per team)

| Folder / file | Role |
|---|---|
| `1 - Projects/` | to-do folder — things with an end (the agent writes `Inbox.md` via the typed contract) |
| `2 - Areas/` | ongoing responsibilities — the agent READS, never writes |
| `3 - Resources/` | the second brain — one `.md` note per topic, each starting with `§ <Topic>`; writes ONLY via the human gate (a new note file) |
| `4 - Archive/` | done things, dated (`- [x] <item> - done <date>` in a monthly `Archive — <YYYY-MM>.md`) — the runner's DONE appends here |
| `rules.md` | the model's contract: PARA folder map + rules R1–R4 |
| `AGENTS.md` | the guide for coding agents (Claude Code, Codex, pi, …) |
| `new_lab_vault.sh` | makes the team copies + configures Obsidian + warms the model |

## Ground rules

- **Never hand-edit the data files to fake a pass** — the runner and the gate must produce every change.
- Test in a copy when exploring; log it anyway.
- Every claim ends with `SOURCE: …` (R2). Honest failure beats a confident invention (R1).
- Contradictions go to the **human gate** (R4) — never pick a side.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Empty answer | `"think": false` missing — gemma4's default thinking eats the token budget |
| 60-second timeouts | no `num_predict` cap — uncapped generation |
| Everything routes to TASK | the router prompt lost its few-shot examples + § catalog |
| `.txt` files invisible in Obsidian | the launcher pre-enables "Detect all file extensions"; check `.obsidian/app.json` |
| Cold calls take 5–6 s | normal; warm calls are 0.3–1 s — `keep_alive` is set to 30 m |

## Instructor notes

The full run-sheet (75-minute format, three phases, roles, rubric, QA drill) lives in the
course kit — *AI Novelties Masterclass, ISDI*. The instructor scripts (the finished versions of
the three functions, with all quirks pre-fixed) live in the `second-brain-lab` skill
(`brain_agent.py` · `brain_research.py` · `brain_graph.py`). **This repo is deliberately the
minimum** — the concepts land when we build them live, not when students read a README.

## License

MIT © 2026 [Jairo Rodriguez Arias](https://github.com/jairorodriguezarias) — *AI Novelties
Masterclass, ISDI.*

---

*Start small. The model is wrong on purpose at least twice today — every fix is a line you can
name, not luck.*
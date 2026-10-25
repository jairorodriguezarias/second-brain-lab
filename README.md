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
makes that work, plus a runner with marked `TODO`s that become the path we walk during the
session. The vault you build is **PARA-native** — the same triage methodology professionals use.

## Requirements

- [ollama](https://ollama.com/) ≥ 0.34.4 (`brew install ollama` — macOS · no keys, no cloud)
- the model: `ollama pull gemma4:e2b-it-qat` (~4.3 GB)
- Python 3.9+ — **stdlib only: no pip, no venv, no internet during class**

## Start in 5 commands

```bash
git clone https://github.com/jairorodriguezarias/second-brain-lab.git   # or Code → Download ZIP → unzip
cd second-brain-lab
bash new_lab_vault.sh alfa        # your working vault → lab-vault-alfa/ (+ Obsidian opens it)
python3 lab_runner.py             # the opening demo: a research pass + one routed question
```

Then open `lab_runner.py` and work the **TODOs in order** (they live in the file as comments) —
one TODO per pass, two lines in `if __name__ == "__main__":` swapped as you go. Each TODO is a
small, nameable fix; we introduce the concept behind each one live in class.

| TODOs | What happens when you finish them |
|---|---|
| **A1–A4** | bare model → the amnesia receipt · files in the prompt → it KNOWS · typed contract `{"action":"ADD\|DONE\|MOVE\|DELETE","item":...,"cite":"SOURCE: 1 - Projects.md"}` · DONE moves the line to `4 - Archive.md`, dated |
| **B1–B4** | draft → self-critique → refine · evidence checks (≥2 SOURCE lines + OPEN QUESTION, no invented numbers) · an honest-fail exit · your own rule R6 |
| **C1–C2** | cold router misroutes → few-shot + § catalog fix · TASK / FACT / NEW · NEW = draft → 👤 human gate → only write path into `3 - Resources.md` |

## What's inside (the lab vault, per team)

| File | Role |
|---|---|
| `1 - Projects.md` | to-do — things with an end (the agent writes via the typed contract) |
| `2 - Areas.md` | ongoing responsibilities — the agent READS, never writes |
| `3 - Resources.md` | the second brain (sections start with `§ Name`) — writes ONLY via the human gate |
| `4 - Archive.md` | done things, dated (`- [x] <item> - done <date>`) — the runner's DONE appends here |
| `rules.md` | the model's contract: PARA file map + rules R1–R4 |
| `AGENTS.md` | the guide for coding agents (Claude Code, Codex, pi, …) |
| `lab_runner.py` | the starter runner you grow during class |
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
| `.py` files invisible in Obsidian | the launcher pre-enables "Detect all file extensions"; check `.obsidian/app.json` |
| Cold calls take 5–6 s | normal; warm calls are 0.3–1 s — `keep_alive` is set to 30 m |

## Instructor notes

The full run-sheet (75-minute format, three phases, roles, rubric, QA drill) lives in the
course kit — *AI Novelties Masterclass, ISDI*. The instructor scripts (finished versions of these
TODOs, with all quirks pre-fixed) mirror this repo. **This repo is deliberately the minimum** —
the concepts land when we build them live, not when students read a README.

## License

MIT © 2026 [Jairo Rodriguez Arias](https://github.com/jairorodriguezarias) — *AI Novelties
Masterclass, ISDI.*

---

*Start small. The model is wrong on purpose at least twice today — every fix is a line you can
name, not luck.*
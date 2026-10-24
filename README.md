# Second Brain Lab — harness · loop · graph on a 2B model

[![License: MIT](https://img.shields.io/badge/license-MIT-A51C30)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/ollama-local-5DB28B)](https://ollama.com/)
![Keys](https://img.shields.io/badge/API_keys-none-000000)
![Cloud](https://img.shields.io/badge/cloud-none-000000)

Make a small model behave like a real assistant. One local model — `gemma4:e2b-it-qat`
on ollama — becomes your personal second brain because its **memory lives in files, not in the
model**. In one session you build the three engineering layers that turn a failing chatbot into a
harnessed, honest, routed assistant:

1. **Harness** — a to-do and a second brain that survive new sessions (files in the prompt, always)
2. **Loop** — research one topic with a draft → self-critique → refine cycle that can honest-fail
3. **Graph** — route each request (TASK / FACT / NEW); a 👤 **human gate** is the only way anything
   gets written into the second brain

The vault students build is **PARA-native** — the same triage methodology professionals use.

## Requirements

- [ollama](https://ollama.com/) ≥ 0.34.4 (`brew install ollama` — macOS · no keys, no cloud)
- the model: `ollama pull gemma4:e2b-it-qat` (~4.3 GB)
- Python 3.9+ — **stdlib only: no pip, no venv, no internet during class**

## Start in 5 commands

```bash
git clone https://github.com/<you>/second-brain-lab.git   # or Code → Download ZIP → unzip
cd second-brain-lab
bash new_lab_vault.sh alfa        # your working vault → lab-vault-alfa/ (+ Obsidian opens it)
python3 lab_runner.py             # the opening demo: honest research loop + one routed question
```

Then open `lab_runner.py` and work the **TODOs in order** (they live in the file as comments) —
one TODO per pass, two lines in `if __name__ == "__main__":` swapped as you go:

| Layer | TODOs | What happens |
|---|---|---|
| **A · Harness** | A1–A4 | bare model → amnesia receipt · files in prompt → it KNOWS · typed contract `{"action":"ADD\|DONE\|MOVE\|DELETE","item":...,"cite":"SOURCE: 1 - Projects.md"}` · DONE moves the line to `4 - Archive.md`, dated |
| **B · Loop** | B1–B4 | draft → self-critique → refine · evidence checks (≥2 SOURCE lines + OPEN QUESTION, no invented numbers) · fail-on-purpose confidence exit · your own rule R6 |
| **C · Graph** | C1–C2 | cold router misroutes → few-shot + § catalog fix · TASK / FACT / NEW · NEW = draft → 👤 human gate → only write path into `3 - Resources.md` |

Log **every** model call in `00 - Lab Notebook.md` — append-only evidence.

## What's inside (the lab vault, per team)

| File | Role |
|---|---|
| `1 - Projects.md` | to-do — things with an end (the agent writes via the typed contract) |
| `2 - Areas.md` | ongoing responsibilities — the agent READS, never writes |
| `3 - Resources.md` | the second brain (sections start with `§ Name`) — writes ONLY via the human gate |
| `4 - Archive.md` | done things, dated (`- [x] <item> - done <date>`) — the runner's DONE appends here |
| `rules.md` | the model's contract: PARA file map + rules R1–R4 |
| `AGENTS.md` | the guide for coding agents (Claude Code, Codex, pi, …) |
| `lab_runner.py` | the starter runner you build on |
| `00 – 03` notes | team lab log + one note per layer (A Harness · B Loop · C Graph) |
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

The full run-sheet (75-minute format, three phases, roles B/R/T/F, rubric, QA drill) lives in the
course kit — *AI Novelties Masterclass, ISDI*. The instructor scripts (finished versions of these
TODOs, with all quirks pre-fixed) mirror this repo.

## License

MIT © 2026 [Jairo Rodriguez Arias](https://github.com/) — *AI Novelties Masterclass, ISDI.*

---

*The model answers wrong on purpose at least twice today. That's the point — every fix is a line
you can name, not luck.*
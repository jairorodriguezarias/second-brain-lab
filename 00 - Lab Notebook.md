---
type: lab-notebook
course: "[[00 - Hub — AI Novelties Masterclass]]"
note: lab-vault team template — duplicate this whole folder per team
---
# Team ☐☐ — Lab Notebook

**Roles:** B ___ · R ___ · T ___ · F ___ · **Model:** `gemma4:e2b-it-qat` (fallback `gemma3:4b`) · **Runner laptop:** ____

> **Minute 0:** `bash new_lab_vault.sh <team-name>` — the script clones this vault, makes the `.py`/`.txt` visible in Obsidian, warms the model and opens it for you. Then fill the roles below.

> *"Mismo modelo todo el día. Lo que cambia es lo que ustedes construyen alrededor."*
> The notebook is part of the lab: **append-only** — mistakes stay, reverted entries get ✂.

## Progress

- [ ] A — **bare run**: *"what's on my list?"* → the amnesia receipt → [[01 - A Harness]]
- [ ] A — **harnessed run**: files in the prompt → it KNOWS → [[01 - A Harness]]
- [ ] A — one reminder **survives** (ADD via typed contract → applied to `todo.md` → re-ask) → [[01 - A Harness]]
- [ ] B — research loop with **evidence checks** (2 sources + open question) → [[02 - B Loop]]
- [ ] B — confidence exit (fail-on-purpose, ✂ kept) → [[02 - B Loop]]
- [ ] C — route graph: TASK / FACT / NEW + 👤 gate → [[03 - C Graph]]
- [ ] C — a NEW note enters `brain.md` **only through the gate** → [[03 - C Graph]]

## Files (on disk, next to this note — enable *Detect all file extensions* in Obsidian settings)

- `lab_runner.py` — starter; B marks all TODOs `[done]`
- `1 - Projects.md` · `3 - Resources.md` · `rules.md` — R applies changes; T owns the stale section; F guards the gate

## One-page report (the notebook IS the report)

| Layer | What it stores | First failure | Patch | Evidence |
|---|---|---|---|---|
| harness (A) | your list + notes, given to the model each time | | | |
| loop (B) | the research log, honest exits | | | |
| graph (C) | where info may come from; the gate into brain | | | |
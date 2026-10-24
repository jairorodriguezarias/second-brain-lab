# AGENTS.md — Lab vault "Second Brain Lab"

Guide for AI agents (and humans acting like one) working inside this lab vault.

## What this vault is

A **mini-PARA vault** used in the **Harness · Loop · Graph lab** (AI Novelties Masterclass, ISDI).
The idea of the lab: an agent's memory lives OUTSIDE the model — in these files — and the team
builds the three engineering layers that make a small 2B model behave like a real assistant:

1. **Harness** — maintain the to-do / second brain (context engineering: files → prompt)
2. **Loop** — research ONE topic against the own notes (draft → critique → refine, with evidence rules)
3. **Graph** — route each question (TASK / FACT / NEW) and act accordingly; the 👤 human gate is the
   ONLY write path into the second brain

## The map (do NOT rename — rules.md and lab_runner.py reference these exact names)

- `1 - Projects.md` — open tasks (things with an end). The agent's ADDs land here.
- `2 - Areas.md` — ongoing responsibilities. The assistant READS these, never writes.
- `3 - Resources.md` — the second brain. Every section starts with `§ Name`.
- `4 - Archive.md` — completed tasks, dated. The runner's DONE moves lines from Projects here.
- `rules.md` — the model's contract: PARA file map + rules R1–R4 (Markdown, so it renders in Obsidian too). **Source of truth.**
- `lab_runner.py` — the student's runner (fill the TODOs: A1–A4 harness · B2–B4 loop · C1–C2 graph)
- `new_lab_vault.sh` — creates a team copy of this vault (`lab-vault-<team>`)
- `AGENTS.md` — the guide for coding agents (this file — they read it automatically)
- `README.md` — the students' quickstart (humans start here)
- `00–03` numbered notes — team lab notebook + one note per layer (A, B, C)

## The contract chain (who does what)

1. `rules.md` defines WHAT the agent may say (R1 no invention · R2 always cite SOURCE ·
   R3 questions = one text line, commands = typed JSON only when the script asks ·
   R4 contradictions → say "CONTRADICTION: <which>" and route to the human gate).
2. `lab_runner.py` decides HOW the model is called (ollama local, gemma4:e2b-it-qat).
3. The typed contract `{"action":"ADD|DONE|MOVE|DELETE","item":"...","cite":"SOURCE: 1 - Projects.md"}`
   is the ONLY way the agent writes to Projects. DONE is executed BY THE RUNNER (Projects → Archive).
4. Nothing writes to `3 - Resources.md` unless the human accepts it at the gate.

## Model facts (already baked into lab_runner.py — do not "fix" them)

- `"think": false` — gemma4 thinks by default and eats the token budget → empty answers.
- `num_predict` caps — uncapped generation = 60-second timeouts.
- `"keep_alive": "30m"` — cold first call ≈ 5–6 s, warm calls ≈ 0.3–1 s.
- `"temperature": 0.0` for contracts and routing. No internet, no API keys — all local.

## For coding agents (Claude Code, Codex, pi, …) helping the team

- Work ONLY on the TODOs in `lab_runner.py` (A1–A4 · B2–B4 · C1–C2). One TODO per pass.
- Test in a COPY, never inside the template: `cp -R . /tmp/<team>` and run there.
- NEVER hand-edit the data files to fake a pass — the runner + the gate must produce the change.
- Do not change file names, the cite format ("SOURCE: …"), or the § section convention.
- If a run misbehaves: empty answer → check `think:false` · timeout → check `num_predict` ·
  route collapses to one bucket → strengthen the router's few-shot examples.
- Do not invent facts (R1). If the information is NOT in the files, say so — the graph routes it
  as NEW → draft → human gate. Honest failure beats a confident invention.

## Lab phases (read the numbered notes in order)

- `00 - Lab Notebook.md` — team log; append-only evidence (EVERY model call gets logged)
- `01 - A Harness.md` — context engineering; compare "bare model" vs "files in prompt"
- `02 - B Loop.md` — draft → self-critique → refine, with the evidence rules
- `03 - C Graph.md` — router TASK/FACT/NEW + `search_brain` + gated write

## Acceptance criteria (what "done" means)

- **A**: a question → ONE line + SOURCE from the files; a command → JSON applied by the runner;
  DONE lands in `4 - Archive.md` dated.
- **B**: the note exits as EVIDENCE — ≥2 SOURCE lines to real § sections + an explicit
  `OPEN QUESTION:` line + no invented numbers — or EXHAUSTION (the loop honest-fails).
- **C**: "what's for dinner Friday?" → FACT + §Recipes · "next pending task?" → TASK ·
  "gift ideas for my sister?" → NEW → draft → 👤 gate decides.

## Language

Template and contract files are English (as shipped). Team notes and student writing can be
English or Spanish — keep the citations in the contract's format either way.
# AGENTS.md — Lab vault "Second Brain Lab"

Guide for AI agents (and humans acting like one) working inside this lab vault.

## What this vault is

A **mini-PARA vault** — the minimal starter for the *AI Novelties Masterclass* lab (ISDI).
The core idea: an agent's memory lives OUTSIDE the model — in these files. This repo ships the
smallest setup that makes that work (a local 2B model reading the PARA notes each turn) as a
**vault template + contract**. The runner (the code that talks to the model) is **built live in
class**, one function per phase. The engineering layers behind those functions — **harness**
(context engineering: files → prompt), **loop** (draft → critique → refine with evidence rules),
and **graph** (route TASK / FACT / NEW; the 👤 human gate is the only write path into the second
brain) — are introduced and built live, not pre-pitched in the kit.

## The map (do NOT rename — rules.md references these exact names)

- `1 - Projects.md` — open tasks (things with an end). The agent's ADDs land here.
- `2 - Areas.md` — ongoing responsibilities. The assistant READS these, never writes.
- `3 - Resources.md` — the second brain. Every section starts with `§ Name`.
- `4 - Archive.md` — completed tasks, dated. The runner's DONE moves lines from Projects here.
- `rules.md` — the model's contract: PARA file map + rules R1–R4 (Markdown, so it renders in Obsidian too). **Source of truth.**
- `new_lab_vault.sh` — creates a team copy of this vault (`lab-vault-<team>`)
- `AGENTS.md` — the guide for coding agents (this file — they read it automatically)
- `README.md` — the students' quickstart (humans start here)

> The runner is not shipped — the team writes it in class (three functions: `agent` · `research`
> · `route`, plus the `gate_write` edge). The instructor's finished version lives in the
> `second-brain-lab` skill (`brain_agent.py` · `brain_research.py` · `brain_graph.py`).

## The contract chain (who does what)

1. `rules.md` defines WHAT the agent may say (R1 no invention · R2 always cite SOURCE ·
   R3 questions = one text line, commands = typed JSON only when the script asks ·
   R4 contradictions → say "CONTRADICTION: <which>" and route to the human gate).
2. The runner (built in class) decides HOW the model is called (ollama local, gemma4:e2b-it-qat).
3. The typed contract `{"action":"ADD|DONE|MOVE|DELETE","item":"...","cite":"SOURCE: 1 - Projects.md"}`
   is the ONLY way the agent writes to Projects. DONE is executed BY THE RUNNER (Projects → Archive).
4. Nothing writes to `3 - Resources.md` unless the human accepts it at the gate.

## Model facts (bake these into the runner — do not "fix" them)

- `"think": false` — gemma4 thinks by default and eats the token budget → empty answers.
- `num_predict` caps — uncapped generation = 60-second timeouts.
- `"keep_alive": "30m"` — cold first call ≈ 5–6 s, warm calls ≈ 0.3–1 s.
- `"temperature": 0.0` for contracts and routing. No internet, no API keys — all local.

## For coding agents (Claude Code, Codex, pi, …) helping the team

- Build the runner WITH the team — one function per phase (A `agent` · B `research` · C `route`
  + `gate_write`), following the run-sheet. The instructor's finished reference is the
  `second-brain-lab` skill (`brain_agent.py` · `brain_research.py` · `brain_graph.py`).
- Test in a COPY, never inside the template: `cp -R . /tmp/<team>` and run there.
- NEVER hand-edit the data files to fake a pass — the runner + the gate must produce the change.
- Do not change file names, the cite format ("SOURCE: …"), or the § section convention.
- If a run misbehaves: empty answer → check `think:false` · timeout → check `num_predict` ·
  route collapses to one bucket → strengthen the router's few-shot examples.
- Do not invent facts (R1). If the information is NOT in the files, say so — the graph routes it
  as NEW → draft → human gate. Honest failure beats a confident invention.

## The growth path (the three functions, built in class)

The runner is grown in three passes. The concept behind each pass is introduced in class; the
function is the concrete fix the team writes.

- **A · harness** — context engineering: compare "bare model" vs "files in the prompt";
  the typed contract; DONE → Archive.
- **B · loop** — draft → self-critique → refine; the evidence checks; an honest-fail exit;
  one line of the log becomes rule R6.
- **C · graph** — router TASK / FACT / NEW; `search_brain`; the 👤 human gate as the only
  write edge into `3 - Resources.md`.

## Acceptance criteria (what "done" means)

- **A**: a question → ONE line + SOURCE from the files; a command → JSON applied by the runner;
  DONE lands in `4 - Archive.md` dated.
- **B**: the note exits as EVIDENCE — ≥2 SOURCE lines to real § sections + an explicit
  `OPEN QUESTION:` line + no invented numbers — or EXHAUSTION (the loop honest-fails).
- **C**: "what's for dinner Friday?" → FACT + §Recipes · "next pending task?" → TASK ·
  "gift ideas for a friend's birthday?" → NEW → draft → 👤 gate decides.

## Language

Template and contract files are English (as shipped). Team notes and student writing can be
English or Spanish — keep the citations in the contract's format either way.
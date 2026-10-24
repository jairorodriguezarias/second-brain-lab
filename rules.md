# rules.md — the assistant's contract (PARA map + R1–R4)

## PARA file map (what each file holds + what the agent may do there)

- **PROJECTS** = `1 - Projects.md` — open to-do, things with an end. Agent: READ + WRITE via the typed contract — ADD / MOVE / DELETE land here; DONE removes the line and takes it to ARCHIVE.
- **AREAS** = `2 - Areas.md` — ongoing responsibilities (no end date). Agent: READ-ONLY — never writes here, never suggests changes.
- **RESOURCES** = `3 - Resources.md` — the second brain; every section starts with `§ Name`. Agent: READ freely + WRITE only as a NEW draft that goes through the 👤 human gate.
- **ARCHIVE** = `4 - Archive.md` — completed things, dated (`- [x] <item> - done YYYY-MM-DD`). Agent: never writes directly — only the runner's DONE appends here.
- **CONTRACT** = `rules.md` (this file) — PARA map + R1–R4. The runner puts it in every prompt.

Tooling (not PARA data; do not cite these): `lab_runner.py` (the runner the agent talks through) · `new_lab_vault.sh` (makes a team copy) · `AGENTS.md` (guide for coding agents) · `00–03` team notes.

## The 4 rules

- **R1 — No invention:** answer ONLY from the PARA files provided — no invented facts, no outside knowledge.
- **R2 — Always cite:** cite what you used, at the end: "SOURCE: <PARA file name>" or "SOURCE: brain §<section>".
- **R3 — One contract per place:** questions get ONE short text line (facts first, then SOURCE). Commands get the typed JSON: `{"action":"ADD|DONE|MOVE|DELETE","item":"...","cite":"SOURCE: 1 - Projects.md"}` — but ONLY when the agent script asks for a command conversion; DONE routes to the ARCHIVE.
- **R4 — Contradictions to the gate:** two sections/past entries contradict → reply "CONTRADICTION: <which>" and send it to the human gate. Never pick a side. Nothing found → say what you looked for and that it is NOT in the notes (no guesses — the router script decides).
# Project — Local LLM Lab (ISDI masterclass)

**Status:** active · **End:** the masterclass lab session (75 min)

## Objective
Run a 2B model on student laptops, reading each team's own PARA notes, with a harness/loop/graph built live in class. No keys, no cloud, no internet in the room.

## Milestones
- [x] Repo live on GitHub (second-brain-lab) — PARA folder template + seeded AI/LLM notes
- [x] `gemma4:e2b-it-qat` verified on an 8 GB Ram laptop (~0.4 s/call JSON temp 0)
- [ ] Pre-class email T-3d: install ollama + `ollama pull gemma4:e2b-it-qat` (~4.3 GB, no account)
- [ ] Door check: `ollama list | grep gemma4` — every student has the model
- [ ] Dry-run the three phases (A harness · B loop · C graph) against a team vault
- [ ] Postmortem + rubric collection

## Notes
- The runner is built in class (3 functions: `agent` · `research` · `route` + `gate_write`); the skill's `brain_agent.py`/`brain_research.py`/`brain_graph.py` are the finished reference.
- Model quirks (think:false, num_predict cap, keep_alive) are documented in [[3 - Resources/Ollama]].

---
SOURCE: 1 - Projects/Project — Local LLM Lab.md
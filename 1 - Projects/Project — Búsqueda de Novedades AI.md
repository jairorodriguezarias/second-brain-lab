# Project — Búsqueda de Novedades AI

**Status:** active · **End:** a daily AI-news scan the student can run to stay current

## Objective
A small, stdlib-only news scan: given a list of AI sources (arXiv listings, lab blogs, a few RSS feeds), pull the last 24 h of headlines into one dated note the student can skim each morning. No framework, no pip — the same stdlib-only ethos as the rest of the lab.

## Why
The field moves too fast to track by hand, and the frontier labs publish faster than any one person can read. A daily scan turns "stay current" from an aspiration into a 5-minute morning habit. It is the news-layer counterpart to the lab's research loop.

## Milestones
- [ ] Pick the sources (arXiv `cs.AI` + `cs.CL` new listings, 5–8 lab blogs, 2–3 RSS feeds: Anthropic, OpenAI, Google DeepMind, Meta, DeepSeek, Hugging Face, arXiv)
- [ ] Write the scan (`urllib` + `json` — fetch each source, dedupe, sort by recency, render one dated Markdown digest)
- [ ] Schedule it (cron / launchd daily 08:30, or a `--since` flag for manual runs)
- [ ] Wire it into the lab vault: the digest lands in `3 - Resources/` as a gated note (a human curates before it enters the second brain)
- [ ] Tune the noise floor (blacklists, keyword filters, dedupe across sources)

## Notes
- This is the news analog of the lab's research loop (`brain_research.py`): where the loop researches ONE question in depth, this scan skims MANY headlines per day.
- Output note format mirrors the lab's cite convention: every headline ends with `SOURCE: <feed>`, so the model can trace each item back to its origin.
- The human gate (R4) applies: a human skimms the digest before it enters `3 - Resources/` — the scan proposes, the human disposes.
- Pairs with the main vault's `22 - Areas/Watchlist.md` (the grown-up version) and `skills/research` `watch` mode.

---
SOURCE: 1 - Projects/Project — Búsqueda de Novedades AI.md
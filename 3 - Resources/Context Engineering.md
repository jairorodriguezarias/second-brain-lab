§ Context Engineering

# Context Engineering

Context engineering is the natural successor to prompt engineering. Where prompt engineering optimizes a static instruction string, context engineering curates the **whole token set** the model sees at inference — system prompt, tools, retrieved knowledge, message history, memory, runtime state — as a dynamic, structured, finite resource.

## The core idea
An autoregressive LLM samples `P(Y|C)`. Old view: `C = prompt` (one string). New view: `C = A(c_instr, c_know, c_tools, c_mem, c_state, c_query)` — an assembly function over sourced/filtered/formated components. The job: find the smallest high-signal token set that maximizes the likelihood of the desired output, under the hard constraint `|C| ≤ L_max` (the context window).

## Why context is finite
- **Context rot** — recall accuracy drops as the window fills (needle-in-a-haystack studies).
- **n² attention** — every token attends to every token; pairwise relationships stretch thin at long context.
- **Training distribution** — models see shorter sequences far more than long ones, so they have weaker long-range attention.
- **Attention budget** — like human working memory; every extra token depletes it.

## The four strategies (LangChain taxonomy)
- **Write** — save context outside the window (scratchpads, long-term memory/notes) for later use.
- **Select** — pull the right context back in (RAG over files/memories/tools; embedding + knowledge-graph indexes).
- **Compress** — summarization (auto-compact à la Claude Code) and trimming (drop old tool results, stale messages).
- **Isolate** — split context across sub-agents (each with its own window) or sandboxes/state fields so heavy objects never enter the LLM's window.

## Anatomy of good context
- **System prompt** — clear, simple, right altitude (not brittle if-else, not vague). XML/Markdown sections.
- **Tools** — minimal viable set; self-contained; descriptive arg names; no overlapping descriptions (or the model can't pick).
- **Examples** — few-shot, but curated and diverse, not a laundry list of edge cases.
- **Just-in-time retrieval** — keep lightweight references (file paths, stored queries) and load data on demand (Claude Code's glob/grep/head/tail pattern).

## Long-horizon techniques
- **Compaction** — near-window → summarize → restart with the summary + recent files.
- **Structured note-taking** — agent writes NOTES.md / to-do and re-reads after resets (Claude playing Pokémon, multi-hour coherence).
- **Sub-agents** — focused sub-tasks in clean windows; return a distilled 1-2K-token summary to the lead agent.

## Lab connection
The lab's harness (rules.md + the PARA files INSIDE the system prompt each turn) IS context engineering in its simplest form: write = the vault files, select = which folder to read, compress = the § section convention, isolate = the human gate. The skill's brain_*.py are the "finished" version of the same loop.

---
SOURCE: web — Anthropic "Effective context engineering for AI agents" (Sep 2025); Mei et al. "A Survey of Context Engineering for LLMs" (arXiv:2507.13334); LangChain docs/blog (2025). Synthesized for the Second Brain Lab seed.
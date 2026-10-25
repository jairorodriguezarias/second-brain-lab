# Area — Líneas Futuras de la AI

Ongoing responsibility (no end date). Watch where AI is heading — the directions already visible in shipping products and the open questions where honest experts still disagree.

## Directions already underway (near-term)
Five directions are visible in today's systems — none is speculation:

| Direction | What it is |
|---|---|
| **Agents** | systems that take actions and use tools (browse, run code, call APIs), not just return text. Still most reliable on narrow tasks with human checkpoints. |
| **Reasoning models** | work through a problem in explicit intermediate steps; spend more compute on harder questions. Better math/coding/logic at some cost in speed + price. |
| **Multimodality** | one model handles text, images, audio, video together — blurring the line between formerly separate tools. |
| **Smaller, on-device models** | compact models on phones/laptops: cheaper, faster, more private (data stays local), though less capable than the largest frontier models. |
| **Ambient integration** | AI moves out of standalone chat windows into email, docs, search, coding tools, OS — present where work already happens, not a separate destination. |

The through-line: AI is moving from **something you consult** to **something that acts on your behalf**. That makes **reliability** the open question that matters most.

## Open questions (genuinely contested)
- **Reliability + hallucination** — can confident fluent errors be eliminated, or only reduced? Grounding in sources, tools to self-check, citations, and training all lower error rates, but residual confident error may be intrinsic to the current paradigm. For anything high-stakes, verification + human oversight remain necessary.
- **Alignment + safety** — near-term: misuse (fraud, disinformation, cyber/bio harm), biased outputs, agents taking unintended actions. Longer-term (contested): could highly capable goal-directed systems become hard to control or act in unintended ways at scale? Both camps increasingly agree on practical measures (evaluation, red-teaming, monitoring, staged deployment, independent safety institutes).
- **Work, wages, economy** — AI automates parts of cognitive work (writing, coding, analysis, support, design). Near-term likely augmentation more than wholesale replacement (most jobs are bundles of tasks, only some automatable). Economy-wide effects are mixed and hard to isolate. How gains are distributed may matter more than the aggregate.
- **Regulation + governance** — EU: risk-based regime, phased by use. US: sectoral rules + executive action + voluntary commitments, no comprehensive federal law yet. UK + China: their own approaches. No global consensus. Tensions are structural (fast tech vs slow law, innovation vs precaution, national competition vs international coordination).
- **Energy, compute, cost** — training + running large models consumes significant electricity + specialized hardware; data centers strain power grids + water. But the cost per given capability has fallen sharply. Efficiency gains lower cost/task, but cheaper capability → more usage → total demand can rise even as each unit gets more efficient.
- **AGI debate** — no agreed definition, no consensus on timing. Estimates range from a few years to many decades to "not with current methods." Definitions vary, timelines vary, method varies (will scaling suffice, or are breakthroughs needed?). Progress is jagged — superhuman at some tasks, failing at things a child manages.

## The through-line: AI as a decision layer
Beneath the directions and debates: AI is increasingly the layer through which people find information, filter options, and decide — from search (returns a list of links to evaluate) to answers (returns a synthesized recommendation to act on). Influence concentrates in a few systems; the reasons behind an answer are often opaque; questions of bias, accountability, and who gets included become questions about the public information environment. Being legible to these systems — findable, understandable, trustworthy to a machine — starts to matter as much as being findable to a person once did.

## Notes
- The lab's harness (rules + PARA files inside the system prompt each turn) IS the near-term directions in their simplest form: write = the vault files, select = which folder, compress = the § convention, isolate = the human gate.
- The open questions are the lab's pedagogical hook — the model that "knows" everything but invents facts (hallucination) is the fail-on-purpose demo; the model that says "not in the notes" (honest failure) is the safer one.
- See [[Context Engineering]] for the assembly-function framing; [[SLMs — Small Language Models]] for the on-device direction; [[LLM grandes]] for the frontier this Area watches.

---
SOURCE: web — highlevel.ai "Where AI is heading"; IBM "The trends that will shape AI in 2026"; State of AI Report 2026 (Nathan Benaich, Air Street Capital). Synthesized for the Second Brain Lab seed.
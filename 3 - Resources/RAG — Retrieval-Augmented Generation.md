§ RAG — Retrieval-Augmented Generation

# RAG — Retrieval-Augmented Generation

RAG extends an LLM with an external knowledge base it can query at inference time, so answers come from current/authoritative sources instead of only the model's static training data. The model retrieves, augments its prompt with the retrieved context, then generates.

## The five-stage flow
1. User submits a prompt.
2. Retriever queries the knowledge base for relevant chunks.
3. Relevant chunks return to the integration layer.
4. The prompt is augmented with the retrieved context.
5. The LLM generates an answer (ideally with citations).

## Core components
- **Knowledge base** — the external store (PDFs, docs, databases). Content is chunked and embedded into vectors.
- **Embedding model** — vectorizes chunks and queries into a shared semantic space.
- **Retriever** — matches the query vector to chunk vectors (cosine similarity / top-k).
- **Integration layer** — assembles the augmented prompt (query + retrieved context).
- **Generator** — the LLM that produces the final answer.
- Optional **ranker** — re-orders retrieved chunks by relevance.

## Why use it
- **Cost** — no retraining/fine-tuning to add new knowledge.
- **Currency** — connect live data sources; beats the training cutoff.
- **Trust** — citations let users verify answers.
- **Control** — swap/edit the knowledge base without touching model weights.
- **Security** — data stays outside the model (but vector DBs themselves must be secured).

## Failure modes
- Retrieval quality: noisy index → wrong chunks → wrong answers.
- Hallucination persists if retrieved context is incomplete/contradictory.
- Latency: real-time retrieval adds round-trips.
- Lost-in-the-middle: LLMs underweight context placed mid-window.

## Evolution
Naive RAG → Advanced RAG (query rewriting, reranking, chunking strategy) → Modular RAG (reconfigurable pipelines: Rewrite-Retrieve-Read, RAGFusion, routing) → Agentic RAG (the LLM decides when/what to retrieve, with reflection + planning) → Graph-Enhanced RAG (GraphRAG, LightRAG, HippoRAG — knowledge graphs for multi-hop).

## Classic vs fine-tuning
RAG = query-time retrieval (no weight change). Fine-tuning = bake domain data into weights. They compose: fine-tune for domain/style, RAG for fresh facts.

---
SOURCE: web — AWS, IBM, Microsoft Learn, GOV.UK (2024-2026); synthesized for the Second Brain Lab seed.
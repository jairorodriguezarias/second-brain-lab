§ LLM grandes

# LLM grandes — Large Language Models

A large language model (LLM) is a transformer-based neural net trained on vast amounts of unlabeled text to predict the next token. Scale (parameters), training data, and compute together set the capability; the recipe still matters more than raw size.

## Total vs active parameters (the MoE twist)
A **dense** model uses every parameter on every token: "size" is one number (e.g. Gemma 4 31B = 31B on the main path).
A **mixture-of-experts (MoE)** model has many parallel "expert" feedforward blocks; a router sends each token to one or a few. Cards list **total** (all experts) and **active** (what runs per token) — active width is the better handle on per-step compute.

## The frontier (closed, undisclosed sizes)
None of the frontier vendors publish parameter counts. Every number you see for GPT/Claude/Gemini is an estimate or a leak — never a confirmed spec.
- **GPT-5.x** (OpenAI) — undisclosed; best-supported public estimate ≈ **100B active** (Epoch AI, from API pricing + throughput). GPT-5.4 is the current flagship; a `pro` variant adds test-time scaling.
- **Claude Opus / Sonnet / Haiku** (Anthropic) — undisclosed; no credible estimate exists. Opus 5 is the top tier.
- **Gemini 3 Pro / Flash** (Google DeepMind) — undisclosed; no credible estimate.

## The largest open-weight models (disclosed, downloadable)
Every figure below is on the model card or HuggingFace `config.json` and verifiable.

| Model | Lab | Total | Active | Architecture |
|---|---|---|---|---|
| DeepSeek V4-Pro | DeepSeek | **1.6T** | 49B | MoE (384 exp) |
| Kimi K2.6 | Moonshot AI | **1T** | 32B | MoE (384 exp) |
| GLM-5.2 | Z.ai | 744B | 40B | MoE (256 exp) |
| Mistral Large 3 | Mistral AI | 675B | 41B | MoE |
| DeepSeek V3 | DeepSeek | 671B | 37B | MoE (256 exp) |
| Llama 4 Maverick | Meta | 400B | 17B | MoE (128 exp) |
| Qwen3.5-397B | Alibaba | 397B | 17B | MoE |
| Gemma 4 (31B) | Google | 30.7B | — | Dense |

## So what is "biggest"?
- **Largest disclosed + downloadable:** DeepSeek V4-Pro (1.6T total / 49B active).
- **Largest vendor claim ever:** ERNIE 5.0 (Baidu, ~2.4T, proprietary, unverifiable).
- **Largest announced as open weights, never shipped:** Llama 4 Behemoth (Meta, ~2T, paused).
- **Frontier chatbot (ChatGPT/Claude/Gemini):** none publish a count — every number is an estimate.

A 1T MoE like Kimi K2.6 can be **cheaper to serve** than a 123B dense model despite 8× the parameters, because only 32B run per token. Comparing raw totals across dense and MoE models misleads.

## Context windows (the 2026 frontier)
GPT-5 ≈ 1M · Claude Opus ≈ 1M · Gemini 2.5 Pro ≈ **2M** · Gemini 2.5 Flash ≈ 1M · Llama 3.3 405B ≈ 128K.
Longer context costs more (memory + latency) and can weaken other skills — the "lost-in-the-middle" effect.

## Why scale still matters
- **Capacity:** with similar data + training, a larger weight budget can represent richer patterns.
- **Serving cost:** more active params per forward pass → more FLOPs + memory at inference (quantization + hardware matter).
- **Economics:** the price of a given capability has fallen sharply (inference ≫ cheaper), but cheaper capability invites far more usage → total demand can rise even as each unit gets more efficient.

## Lab connection
The lab's `gemma4:e2b-it-qat` is the **SLM** answer to "why not just use a bigger model?" — a 2B-effective model on an 8 GB laptop. The frontier LLMs ([[Context Engineering]]'s assembly function over sourced components) are the "finished" version of the same scaling story, at the datacenter end. See [[SLMs — Small Language Models]] for the on-device end.

---
SOURCE: web — Epoch AI (GPT-5 estimate); AI Wiki (llm_parameter_comparison); IBM (LLM list); explainx.ai (parameters explainer). Synthesized for the Second Brain Lab seed.
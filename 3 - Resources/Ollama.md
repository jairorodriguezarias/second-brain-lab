§ Ollama

# Ollama

Ollama is a single binary that runs LLMs locally. No API keys, no cloud, no pip — `ollama pull gemma4:e2b-it-qat` and you have a model on your laptop. It is the runtime this lab's model runs on.

## The three-process architecture
- **CLI** (`ollama`) — the user-facing command (cobra tree: `serve`, `run`, `pull`, `create`, `ps`, `launch`…). Talks to the daemon over local HTTP on port 11434.
- **Daemon** (`ollama serve`) — a Gin HTTP server. Native API (`/api/chat`, `/api/generate`, `/api/embed`…) + OpenAI-compat (`/v1/chat/completions`…) + Anthropic-compat (`/v1/messages`…). Schedules runners.
- **Runner subprocess** — one per loaded model. The daemon forks `ollama runner …`, which dispatches to:
  - `llamarunner` — llama.cpp via CGO (the default for GGUF models),
  - `ollamarunner` — pure-Go inference runtime (`--ollama-engine`),
  - `mlxrunner` — Apple MLX on Apple Silicon (`--mlx-engine`),
  - `imagegen` — image-generation models.
  The runner exposes a tiny HTTP API (`/completion`, `/embedding`, `/tokenize`, `/detokenize`, `/health`) on an ephemeral port; the daemon proxies to it.

## Scheduler
One model loads at a time (`activeLoading`); already-loaded models serve concurrent requests. Load → fork runner → `WaitUntilRunning` (polls `/health`) → serve. Runners expire after `OLLAMA_KEEP_ALIVE` (default 5 m) of idle and are reaped via `expiredCh`.

## Model store
Models live as content-addressed blobs under `~/.ollama/models`. A manifest references the blobs (GGUF weights, projector, license, params, template). `ollama create` walks a Modelfile's `FROM`/`ADAPTER`/`MESSAGE`/`TEMPLATE` directives and uploads blobs through `/api/blobs/:digest`.

## The lab's model: `gemma4:e2b-it-qat`
- Gemma 4, E2B-effective, QAT-quantized → ~4.3 GB on disk.
- Runs on an 8 GB-Ram laptop (uses system RAM if VRAM is tight; slower but works).
- Pulled once before class: `ollama pull gemma4:e2b-it-qat`. Fallback `gemma3:4b` (instructor laptop only).

## Quirks the lab bakes in (all verified live 2026-10-24)
- `think: false` — gemma4's thinking channel is ON by default and eats the token budget → `content` comes back empty.
- `num_predict` cap — uncapped generation >60 s; cap per call type (90 contract · 120 route · 320 research).
- `keep_alive: "30m"` — cold first call ≈5–6 s; warm calls ≈0.3–1 s.
- `temperature: 0.0` for contracts and routing.

## Warm-up curl (T-5 before class)
```bash
curl http://localhost:11434/api/chat -d '{"model":"gemma4:e2b-it-qat","messages":[{"role":"user","content":"Reply OK"}],"stream":false}'
```

## Cloud proxy
Some models are too big for any single machine; Ollama Cloud forwards `/api/chat` to `ollama.com` (SSH-key-signed requests). Same path serves the experimental `/api/experimental/web_search` and `/web_fetch`. Not used in this lab — everything is local.

---
SOURCE: web — Ollama docs (Quickstart), factory.com architecture wiki, ollama/ollama codebase (llm/server.go). Synthesized for the Second Brain Lab seed.
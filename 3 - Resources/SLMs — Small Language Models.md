§ SLMs — Small Language Models

# SLMs — Small Language Models

Small Language Models (SLMs) are decoder-only transformers in roughly the 100M-5B parameter range, built to run on consumer/edge hardware (phones, laptops, Jetson-class boards) instead of data-center GPUs. They trade raw capability for privacy, latency, and cost.

## Why on-device
- **Privacy** — inference stays local (GDPR/HIPAA-friendly; no data egress).
- **Latency** — no cloud round-trip; sub-second interaction (ITU-T G.114: ≤150 ms one-way for voice quality).
- **Offline** — works with no/weak connectivity.
- **Cost/energy** — no per-token API spend; battery-friendly.

## The memory wall
The defining bottleneck is the **memory subsystem**, not FLOPs. A 7B model is ~28 GB in FP32 — exceeds phone DRAM. Even when it fits, autoregressive **decode** is memory-bandwidth-bound: every generated token reads the whole model from DRAM, so bandwidth (not compute) sets tokens/sec. Prefill (prompt eval) is compute-bound and parallelizes well.

## Compression toolkit (A-L-E-M)
- **Quantization** — FP32→INT4/INT8. First lever: shrinks memory + TTFT. Methods: GPTQ, AWQ, SmoothQuant, LLM.int8, QLoRA, KVQuant, KIVI.
- **Pruning** — remove heads/channels/layers. Structured = dense sub-graphs (hardware-friendly); unstructured = irregular sparsity. SparseGPT, Wanda, ShearedLLaMA, SlimLLM.
- **Knowledge distillation** — small student mimics large teacher (logits, CoT, process). DSS, Orca, MAmmoTH.
- **Low-rank** — LoRA/DoRA/PiSSA adapters; SVD-LLM; linear attention (Linformer, Performer, Mamba).
- **Hybrid** — quantization+sparsity (SpQR), quantization+low-rank (LQ-LoRA, CALDERA), distillation+pruning (Compact LMs).

## Representative families
Phi (1-3.8B, Microsoft — top capability per parameter), Gemma/Gemma 2 (2B, Google), Qwen 2/2.5 (0.5-4B, Alibaba), Llama 3.2 (1B/3B, Meta), SmolLM (135M-1.7B, HuggingFace), MobileLLM (sub-1B, Meta), OpenELM (Apple), MiniCPM, TinyLlama.

## Key findings (Lu et al. 2025, 68 SLMs)
- State-of-the-art SLMs surpass 7B models on general tasks (Phi-3.5 mini ≈ LLaMA 3.1 8B).
- **Data quality > data quantity** (FineWeb-Edu, DCLM beat raw scale).
- SLMs are **over-trained** (≫ Chinchilla 1:20; often >1.5T tokens) to spend compute at training time, save it at inference.
- In-context learning gains are limited and uneven below ~2B.
- GQA + gated FFN + SiLU + RMSNorm + vocab >50K is the 2024-era default architecture.

## Lab connection
This lab's `gemma4:e2b-it-qat` is a 2B-effective SLM — exactly the class where these trade-offs bite. The harness (files in the prompt) is the fix for the amnesia + bandwidth walls.

---
SOURCE: web — Lu et al. "Demystifying SLMs for Edge Deployment" (ACL 2025); Chen et al. on-device LLMs survey (AI Review 2026); Patra et al. on-device SLM survey (IEEE 2026). Synthesized for the Second Brain Lab seed.
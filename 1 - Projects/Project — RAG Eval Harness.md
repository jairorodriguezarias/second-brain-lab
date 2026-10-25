# Project — RAG Eval Harness

**Status:** active · **End:** a reusable eval script + a 20-question golden set

## Objective
A tiny, stdlib-only eval harness for RAG: given a knowledge base (a folder of notes) and 20 question/answer pairs, measure retrieval recall + answer faithfulness. No framework, no pip.

## Milestones
- [ ] Write the golden set (20 Q/A pairs over the Resources notes)
- [ ] Implement retrieval recall@5 (do the top-5 chunks contain the answer's source?)
- [ ] Implement answer faithfulness (does every claim cite a real `SOURCE:` line?)
- [ ] Run it against `gemma4:e2b-it-qat` local
- [ ] Compare naive RAG vs §-catalog routing (the lab's C-fix as a retriever)

## Notes
- Cite format: `SOURCE: 3 - Resources/<note>.md §<Topic>`.
- Honest failure beats confident invention (R1). The harness must flag invented numbers.
- See [[3 - Resources/RAG — Retrieval-Augmented Generation]] for the RAG taxonomy this evals.

---
SOURCE: 1 - Projects/Project — RAG Eval Harness.md
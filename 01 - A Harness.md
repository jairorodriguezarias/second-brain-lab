---
type: lab-notebook
course: "[[00 - Hub — AI Novelties Masterclass]]"
note: Phase A — the assistant's memory lives OUTSIDE the model
---
# 01 - A Harness — to-do + second brain

## The two runs

| Ask the same question twice: *"what's on my list?"* | What it says | Cites files? |
|---|---|---|
| **BARE** agent (no files in the prompt) — TODO A1 | | |
| **HARNESSED** agent (todo.md + brain.md in the prompt) — TODO A2 | | |

> [!failure] The amnesia receipt (bare run, paste exact answer — KEEP)
>

## Then make one reminder SURVIVE (A3)

1. command the assistant: *"add: send the rent payment"*
2. it must reply with the typed contract: `{"action":"ADD","item":"...","cite":"..."}`
3. role **R** applies it to `todo.md` → re-ask *"what's on my list?"* → ☑ it's there
4. fresh session → **still there** (the memory was never in the model)

## Receipt table

| Command | Contract returned ✓/✗ | todo.md changed | Re-ask confirms |
|---|---|---|---|
| add the rent payment | | | |
| mark the dentist done | | | |
| move group-project email to tomorrow | | | |

> [!question] Say it out loud: where does the memory live — in the model, or in the files? What, then, is a "second brain" in engineering terms?
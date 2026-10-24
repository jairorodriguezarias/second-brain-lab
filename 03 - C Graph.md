---
type: lab-notebook
course: "[[00 - Hub — AI Novelties Masterclass]]"
note: Phase C — where is the information ALLOWED to come from?
---
# 03 - C Graph — find information (the routing graph)

## The graph (edit the Mermaid as you decide — live render)

```mermaid
flowchart TD
  Q[question] --> ROUTE{route<br>TASK | FACT | NEW}
  ROUTE -->|TASK| TODO[read todo.md]
  ROUTE -->|FACT| BRAIN[search_brain · cite §]
  ROUTE -->|NEW| DRAFT[draft note + OPEN QUESTION]
  TODO --> ANS[answer + SOURCE]
  BRAIN --> ANS
  DRAFT --> GATE{👤 HUMAN}
  GATE -->|yes| BRAINW[write into brain.md]
  GATE -->|no| DISCARD[discard, logged]
  BRAINW --> ANS
  ANS --> OUT[user gets answer + route receipt]
```

## Question cards (run each through the graph; log route + receipt)

| # | Question | Route (TASK/FACT/NEW) | Sources used § | Gate? |
|---|---|---|---|---|
| 1 | "what's for dinner Friday?" | | | |
| 2 | "what's my next pending task?" | | | |
| 3 | **"how much is the night train to Lisbon?"** | | ⚠️ | |
| 4 | "should I change my phone plan?" | | | |

## The Lisbon contradiction (the designed trap)

`brain.md` says train ~34€ (September) — T's stale-vs-UPDATE section says ✗ cancelled, flight 89€.
**Two sections, one truth problem.** What does your graph do? (route → the gate decides which section is current — or flags the whole topic NEW)

> [!check] The Lisbon question receipt: route = ___ · gate decision by (name): ___ · what entered brain.md (if anything): ___

## The rule (say it aloud)

> *The ONLY edge that writes into your second brain is the 👤 human gate. Everything else just reads.*
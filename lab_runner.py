#!/usr/bin/env python3
# lab_runner.py — Harness · Loop · Graph lab (PARA starter) — stdlib only, no pip, no keys
# Build three layers around ONE local model (gemma4:e2b-it-qat) over YOUR OWN mini-PARA vault:
#   A · Harness — keep 1 - Projects.md (a reminder that survives reboots)
#   B · Loop    — research one topic from 3 - Resources.md with honest exits
#   C · Graph   — route questions TASK|FACT|NEW; only a HUMAN GATE writes into Resources
import json, time, urllib.request
from datetime import date

OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "gemma4:e2b-it-qat"          # fallback (instructor laptop only): "gemma3:4b"
PROJECTS, AREAS = "1 - Projects.md", "2 - Areas.md"
RESOURCES, ARCHIVE = "3 - Resources.md", "4 - Archive.md"

def chat(messages, num_predict=160):
    body = {"model": MODEL, "messages": messages, "stream": False,
            "options": {"temperature": 0.0, "num_predict": num_predict},
            "think": False,           # gemma4 default thinking ON eats the budget -> content empty
            "keep_alive": "30m"}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.load(r)["message"]["content"].strip()
    except Exception as e:            # transport error -> failed attempt (evidence rejects it), loop retries
        return json.dumps({"transport_error": str(e)[:100]})

def read(p):
    return open(p, encoding="utf-8").read().rstrip("\n")

# ---- A · HARNESS: maintain 1 - Projects.md ----------------------------------
ADD_CONTRACT = ('{"action":"ADD|DONE|MOVE|DELETE","item":"<short task>",'
                '"cite":"SOURCE: 1 - Projects.md"}')

def agent(memory_on, question):
    if memory_on:   # TODO A2: the harness = PARA files INSIDE the prompt, rules first
        sys = ("You are the user's personal assistant. RULES:\n" + read("rules.md")
               + "\n\nPROJECTS:\n" + read(PROJECTS)
               + "\n\nAREAS:\n" + read(AREAS)
               + "\n\nRESOURCES:\n" + read(RESOURCES))
    else:           # TODO A1: the bare run — add NOTHING. Ask "what's on my list?" -> amnesia receipt.
        sys = "You are the user's personal assistant."
    return chat([{"role": "system", "content": sys}, {"role": "user", "content": question}])
    # TODO A3: questions -> ONE line ending 'SOURCE: ...'; commands (add/done/move/delete:)
    #   -> the ADD_CONTRACT JSON. Then R (a human) applies it below:

def apply(contract, yes=True):
    """DONE = the PARA move: the line leaves Projects and gets archived, dated."""
    c = json.loads(contract)
    todo = read(PROJECTS) + "\n"
    if c["action"] == "ADD" and c["item"][:12].lower() not in todo.lower():
        todo = todo.rstrip("\n") + "\n- [ ] " + c["item"] + "\n"
    elif c["action"] == "DONE":
        line = next((l for l in todo.splitlines() if c["item"][:12].lower() in l.lower()), None)
        if line:
            todo = todo.replace(line, "")
            open(ARCHIVE, "a", encoding="utf-8").write(
                "- [x] " + c["item"] + " - done " + str(date.today()) + "\n")
    elif c["action"] in ("MOVE", "DELETE"):
        pass                          # TODO A4: implement MOVE (reschedule) / DELETE (drop the line)
    open(PROJECTS, "w", encoding="utf-8").write(todo.rstrip("\n") + "\n")   # newline discipline
    return c

# ---- B · LOOP: research ONE topic from 3 - Resources.md, honest exits -------
def evidence_fn(answer):
    """TODO B2: the checks -> ok only if ALL pass:
       (1) >= 2 citations 'SOURCE: brain <section>' (2) a final 'OPEN QUESTION:' line
       (3) 'no invented facts': every number in the answer appears in Resources/Projects"""
    ok, why = False, "TODO: checks not implemented"
    return {"ok": ok, "why": why}

def research(question, attempts=4, max_seconds=240):
    t0, log = time.time(), []
    answer = chat([{"role": "user", "content": "Answer with: 3-block note (ANSWER / SOURCES 'SOURCE: brain <section>' x2+ / OPEN QUESTION:),"
                   + " only from these notes:\n" + read(RESOURCES) + "\n\n" + question}])
    for i in range(1, attempts + 1):
        if time.time() - t0 > max_seconds:
            break
        ev = evidence_fn(answer)
        log.append({"attempt": i, "raw": answer[:300], "evidence": ev, "t": round(time.time() - t0, 1)})
        if ev["ok"]:
            return {"exited": "EVIDENCE", "attempts": i, "answer": answer, "log": log}
        if i == attempts:
            break
        cr = chat([{"role": "user", "content": "In 3 short bullets: which SOURCE lines are missing? is there an OPEN QUESTION line? any invented fact?\n\nNOTE:\n" + answer}])
        answer = chat([{"role": "user", "content": "Fix every bullet from the critique, keep the 3-block format.\n\nCRITIQUE:\n" + cr
                        + "\n\nPREVIOUS NOTE:\n" + answer
                        + "\n\nNotes:\n" + read(RESOURCES) + "\n\n" + question}])
    return {"exited": "EXHAUSTION", "attempts": attempts, "answer": answer, "log": log}
    # TODO B3 (fail-on-purpose): one bare call, no checks -> CONFIDENCE exit -> paste into your team notebook (kept)
    # TODO B4 (4th loop): pick ONE line of the log -> it becomes rule R6 in rules.md

# ---- C · GRAPH: TASK | FACT | NEW -> only the GATE writes into Resources ----
def route(question):
    """TODO C1 (the lab's known failure): ask the model for a bucket WITHOUT context
       -> it misroutes (dinner -> TASK). FIX: put the section catalog + 3 few-shot
       examples in the prompt; reply ONLY {"bucket":"...","section":"..."}. Then test again."""
    out = chat([{"role": "user", "content":
                 'Classify into ONE of ["TASK","FACT","NEW"]: ' + question
                 + '\nReply ONLY JSON: {"bucket":"...","section":"<brain section or none>"}'}])
    try:
        return json.loads(out)
    except Exception:
        return {"bucket": "NEW", "section": "none"}

def gate_write(question, yes=True):
    """TODO C2: the ONLY edge that writes into 3 - Resources.md — a HUMAN says yes first."""
    draft = chat([{"role": "user", "content": "Draft a note: first line '<section' + 2 bullets (mark unknowns 'open'), from the user's words only:\n" + question}])
    if not yes and input("👤 HUMAN GATE — write into " + RESOURCES + "? (y/N) ").strip().lower() != "y":
        return "GATE: declined — logged."
    open(RESOURCES, "a", encoding="utf-8").write("\n\n" + draft.rstrip("\n") + "\n")
    return "WRITTEN (gated): " + draft[:60]

if __name__ == "__main__":
    t0 = time.time()
    r = research("What do I have planned for the Lisbon trip?")
    print(json.dumps({"exited": r["exited"], "log": [x["evidence"]["why"] for x in r["log"]]}, ensure_ascii=False))
    print("route:", route("what's for dinner Friday?"), f"[{round(time.time()-t0,1)}s]")
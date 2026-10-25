#!/usr/bin/env python3
# brain_research.py — B · LOOP: research ONE question from 3 - Resources/, honest exits
# drift fix: the vault sits in the SYSTEM message (ollama prompt-caches it -> retries fast),
# one job per call, and refinement keeps the draft INSIDE one call's shape.
# usage:
#   python3 brain_research.py "What do I have planned for the weekend trip?" [--attempts 3] [--out "02 - B Loop.md"]
import re, sys, argparse, json, time, urllib.request
OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "gemma4:e2b-it-qat"          # fallback: "gemma3:4b"
RESOURCES = "3 - Resources"

import os

def read_folder(folder):
    """Concatenate every .md file in a PARA folder, each prefixed with '### <path>'."""
    parts = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md"):
            rel = folder + "/" + name
            parts.append("### " + rel + "\n" + open(rel, encoding="utf-8").read().rstrip("\n"))
    return "\n\n".join(parts)

def chat(user, num_predict=320, sys=None):
    msgs = ([{"role": "system", "content": sys}] if sys else []) + [{"role": "user", "content": user}]
    body = {"model": MODEL, "messages": msgs, "stream": False,
            "options": {"temperature": 0.0, "num_predict": num_predict},
            "think": False,           # gemma4 thinking ON ate the budget in run 1 -> empty content
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

SYSTEM = (
    "You write a short research note from the user's second brain, which follows.\n"
    "HARD FORMAT (else the note is rejected): 3 blocks separated by blank lines:\n"
    "  Block 1 ANSWER: at most 6 lines, ONLY facts from the notes.\n"
    "  Block 2 SOURCES: one line per used section, exactly 'SOURCE: brain §<section name>' with the real section name, at least 2 lines.\n"
    "  Block 3 starts with the words OPEN QUESTION: what the notes do not answer (one line).\n"
    "Never invent: every number/name must appear in the notes.\n"
    "NOTES (3 - Resources):\n" + read_folder(RESOURCES)
)

def evidence_fn(answer):
    """The three+1 checks — implement your own variant in the lab runner."""
    brain = read_folder(RESOURCES)
    sources = re.findall(r"SOURCE:\s*brain\s*§\s*(.+)", answer)
    checks = {
        "sources>=2": len([s for s in sources if s.strip()]) >= 2,
        "sections_exist": all(n.strip() in brain for n in sources),
        "open_question": "OPEN QUESTION" in answer,
        "no_invented": all(n in brain for n in re.findall(r"\d+", answer)),
    }
    bad = [k for k, v in checks.items() if not v]
    return {"ok": not bad, "why": bad or "ALL-VALID"}

def research(question, attempts=3):
    t0, log = time.time(), []
    answer = chat(question, sys=SYSTEM)
    for i in range(1, attempts + 1):
        ev = evidence_fn(answer)
        log.append({"attempt": i, "evidence": ev["why"], "secs": round(time.time() - t0, 1)})
        if ev["ok"]:
            return {"exited": "EVIDENCE", "attempts": i, "answer": answer, "log": log}   # the note IS the evidence
        if i == attempts:
            break
        cr = chat("Critique this note against the format rules: missing/invalid SOURCE lines? no OPEN QUESTION line? "
                  "invented facts? Reply 3 short bullets only.\n\nNOTE:\n" + answer, num_predict=120)
        answer = chat("CRITIQUE (fix every bullet, keep the format):\n" + cr + "\n\nPREVIOUS NOTE:\n" + answer,
                      num_predict=320, sys=SYSTEM)
    return {"exited": "EXHAUSTION", "attempts": attempts, "answer": answer, "log": log}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--out", help="append the final note + log to this file (the lab notebook)")
    a = ap.parse_args()
    r = research(a.question, a.attempts)
    for row in r["log"]:
        print("  attempt", row["attempt"], "->", row["evidence"], "-", row["secs"], "s")
    print("EXIT:", r["exited"], "(" + str(r["attempts"]) + " attempts)\n")
    print(r["answer"])
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n## " + a.question + "  (exit: " + r["exited"] + ", " + str(r["attempts"]) + " attempts)\n"
                    + r["answer"] + "\n")
        print("\n-> appended to", a.out)
    sys.exit(0 if r["exited"] == "EVIDENCE" else 1)   # the loop's verdict, scriptable
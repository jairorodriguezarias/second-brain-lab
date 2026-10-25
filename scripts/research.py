#!/usr/bin/env python3
# research.py — minimal research starter: ask ONE question against 3 - Resources/, get an answer + SOURCE
# "arrancar": run this, then grow it (evidence loop, attempts, output file) in class
# usage:
#   python3 scripts/research.py "What's the deal with RAG?"
import json, sys, urllib.request, os

OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "gemma4:e2b-it-qat"
RESOURCES = "3 - Resources"

def read_folder(folder):
    parts = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md"):
            rel = folder + "/" + name
            parts.append("### " + rel + "\n" + open(rel, encoding="utf-8").read().rstrip("\n"))
    return "\n\n".join(parts)

def research(question):
    sys = ("You are the assistant over the user's second brain.\n"
            "RULES: R1 answer only from the materials below, no invention. "
            "R2 cite at the end: 'SOURCE: <file or section>'.\n"
            "Reply ONE text line ending with 'SOURCE: ...'.\n"
            "NOTES (3 - Resources):\n" + read_folder(RESOURCES))
    body = {"model": MODEL,
            "messages": [{"role": "system", "content": sys},
                          {"role": "user", "content": question}],
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": 320},
            "think": False, "keep_alive": "30m"}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["message"]["content"].strip()

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What's new in AI this week?"
    print(research(q))
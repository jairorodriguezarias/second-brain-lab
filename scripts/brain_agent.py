#!/usr/bin/env python3
# brain_agent.py — A · HARNESS: questions get ANSWERS, commands get CONTRACTS
# dispatch happens in PYTHON (a 2B model must never choose the mode)
# PARA: maintains 1 - Projects/ (Inbox.md is the to-do list); DONE moves lines to 4 - Archive/Archive — <YYYY-MM>.md, dated
# usage:
#   python3 brain_agent.py "what's my next pending task?"
#   python3 brain_agent.py "add: buy groceries"
#   python3 brain_agent.py --apply '{"action":"ADD","item":"...","cite":"SOURCE: ..."}' [--yes]
import json, sys, re, urllib.request
from datetime import date

OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "gemma4:e2b-it-qat"        # fallback: "gemma3:4b"
PROJECTS, AREAS = "1 - Projects", "2 - Areas"
RESOURCES, ARCHIVE = "3 - Resources", "4 - Archive"
INBOX = PROJECTS + "/Inbox.md"        # the typed-contract to-do list

def chat(system, user, num_predict=140):
    body = {"model": MODEL,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": num_predict},
            "think": False,           # gemma4 default thinking ON eats the budget -> content empty
            "keep_alive": "30m"}      # stay warm through the lab
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.load(r)["message"]["content"].strip()
    except Exception as e:            # transport error is not a crash -> evidence failure, not a stack trace
        return json.dumps({"transport_error": str(e)[:100]})

def read(p):
    return open(p, encoding="utf-8").read().rstrip("\n")

def read_folder(folder):
    """Concatenate every .md file in a PARA folder, each prefixed with a header
    so the model can cite the exact note: '### <relative path>'. Sorted for stability."""
    import os
    parts = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md"):
            rel = folder + "/" + name
            parts.append("### " + rel + "\n" + open(rel, encoding="utf-8").read().rstrip("\n"))
    return "\n\n".join(parts)

def ask(q):
    """QUESTION mode: one text line, cite the source, never JSON (R1/R2/R4)."""
    sys = (
        "You are the assistant over the user's second brain.\n"
        "RULES: R1 answer only from the materials below, no invention. R2 cite at the end: "
        "'SOURCE: <file or section>'. R4 contradiction -> say CONTRADICTION + the two sources.\n"
        "THIS INPUT IS A QUESTION -> reply ONE text line ending with 'SOURCE: ...'. "
        "NEVER output any JSON in this mode.\n"
        "PROJECTS (to-do):\n" + read_folder(PROJECTS) + "\n" +
        "AREAS (ongoing):\n" + read_folder(AREAS) + "\n" +
        "RESOURCES (brain notes):\n" + read_folder(RESOURCES)
    )
    return chat(sys, q, num_predict=150)

CMD = re.compile(r"^\s*(add|mark|done|move|delete)\b[^:]*:\s*(.+)$", re.I)
def command(text):
    """COMMAND mode: pure conversion to the typed contract (no brain, no drift)."""
    m = CMD.match(text)
    if not m:
        return ask(text)              # deterministic dispatch
    verb, item = m.group(1).lower(), m.group(2).strip()
    ACT = {"add": "ADD", "done": "DONE", "mark": "DONE", "move": "MOVE", "delete": "DELETE"}[verb]
    prompt = (
        'Convert this todo instruction to its contract. Reply ONLY the JSON '
        '{"action":"' + ACT + '","item":"<short,<=10 words>","cite":"SOURCE: ' + INBOX + '"} '
        '- no prose, no markdown, nothing else. Verb=' + ACT + '; item="' + item + '".'
    )
    out = chat(prompt, text, num_predict=90)
    try:
        j = json.loads(out)
        if j.get("action") != ACT:    # contract discipline: fix the verb locally (stays in the log)
            j["action"] = ACT
        j["item"] = str(j.get("item", item))[:80]
        j["cite"] = "SOURCE: " + INBOX
    except Exception:
        j = {"action": ACT, "item": item, "cite": "SOURCE: " + INBOX}   # deterministic fallback (logged)
    return json.dumps(j, ensure_ascii=False)

def archive_path():
    """Monthly archive file: 4 - Archive/Archive — <YYYY-MM>.md (created if needed)."""
    return ARCHIVE + "/Archive — " + str(date.today())[:7] + ".md"

def apply(contract, yes=False):
    """R (the runner HUMAN) applies the contract. DONE = PARA: the line leaves Inbox -> Archive, dated."""
    c = json.loads(contract)
    a = c.get("action")
    if a not in ("ADD", "DONE", "MOVE", "DELETE"):
        return "CONTRACT ERROR: unknown action " + repr(a) + " - logged, nothing written."
    if not yes and input("HUMAN GATE - " + a + " '" + c.get("item", "?") + "'? (y/N) ").strip().lower() not in ("y", "yes"):
        return "GATE: declined - logged, nothing written."
    inbox = read(INBOX) + "\n"
    item = c["item"]
    line = next((l for l in inbox.splitlines() if item[:12].lower() in l.lower()), None)
    if a == "ADD":
        if line:
            return "DUPLICATE? '" + item + "' already at: " + line + " - nothing written (logged)."
        inbox = inbox.rstrip("\n") + "\n- [ ] " + item + "\n"
        open(INBOX, "w", encoding="utf-8").write(inbox.rstrip("\n") + "\n")
    elif a == "DONE":
        if not line:
            return "NOT FOUND: no task matching '" + item + "' - nothing written (logged)."
        inbox = inbox.replace(line, "")
        ap = archive_path()
        ar = open(ap, encoding="utf-8").read() if os.path.exists(ap) else ""
        open(ap, "w", encoding="utf-8").write(
            (ar + "\n" if not ar.endswith("\n") else ar) + "- [x] " + item + " - done " + str(date.today()) + "\n")
    elif a == "DELETE" and line:
        inbox = inbox.replace(line, "")
    elif a == "MOVE" and line:
        inbox = inbox.replace(line, "- [ ] " + item + " (moved)")
    open(INBOX, "w", encoding="utf-8").write(inbox.rstrip("\n") + "\n")   # newline discipline
    return "APPLIED " + a + ": " + item + " -> " + INBOX + (" -> " + archive_path() if a == "DONE" else "")

if __name__ == "__main__":
    import os
    args = sys.argv[1:]
    if args and args[0] == "--apply":
        print(apply(args[1], "--yes" in args))
    elif args:
        print(command(" ".join(args)))
    else:
        print(__doc__)
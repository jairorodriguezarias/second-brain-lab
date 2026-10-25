#!/usr/bin/env python3
# brain_graph.py — C · GRAPH: TASK | FACT | NEW routing + the gated write into 3 - Resources/
# all-TASK drift fix: definitions + FEW-SHOT examples + the section catalog go INTO the routing prompt.
# usage:
#   python3 brain_graph.py "what's for dinner Friday?"
#   python3 brain_graph.py "what gift for a friend's birthday?" --gate     # NEW: draft -> gate -> write
import json, sys, argparse, urllib.request, os
OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "gemma4:e2b-it-qat"          # fallback: "gemma3:4b"
PROJECTS, RESOURCES = "1 - Projects", "3 - Resources"

def chat(system, user, num_predict=120):
    body = {"model": MODEL,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": num_predict},
            "think": False,           # gemma4 thinking ON ate the budget in run 1 -> empty content
            "keep_alive": "30m"}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.load(r)["message"]["content"].strip()
    except Exception as e:
        return json.dumps({"transport_error": str(e)[:100]})

def read(p):
    return open(p, encoding="utf-8").read().rstrip("\n")

def read_folder(folder):
    """Concatenate every .md file in a PARA folder, each prefixed with '### <path>'."""
    parts = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md"):
            rel = folder + "/" + name
            parts.append("### " + rel + "\n" + open(rel, encoding="utf-8").read().rstrip("\n"))
    return "\n\n".join(parts)

def topic_of(note_path):
    """First '§ ...' line of a note -> the topic name (without the §), or None."""
    try:
        for line in open(note_path, encoding="utf-8"):
            if line.startswith("§"):
                return line.lstrip("§ ").strip()
    except Exception:
        pass
    return None

def catalog():
    """List the § topics across all notes in 3 - Resources/ (one per note)."""
    out = []
    for name in sorted(os.listdir(RESOURCES)):
        if name.endswith(".md"):
            t = topic_of(RESOURCES + "/" + name)
            if t:
                out.append("§" + t)
    return out

def route(question):
    """TASK (Projects) | FACT (Resources note) | NEW (needs the gate)."""
    cat = catalog()
    sys = (
        "Classify the user's question into exactly ONE bucket. Reply ONLY the JSON "
        '{"bucket":"TASK|FACT|NEW","section":"the section name or none"}\n'
        "TASK = about my tasks/reminders/schedule (what's pending, add something, mark done).\n"
        "FACT = answerable from ONE of the BRAIN SECTIONS listed below.\n"
        "NEW = none of the sections matches (needs a new note at the human gate).\n"
        "EXAMPLES:\n"
        '"what\'s for dinner Friday?" -> {"bucket":"FACT","section":"§Recipes — Friday dinner"}\n'
        '"when is my Tuesday meeting?" -> {"bucket":"TASK","section":"none"}\n'
        '"how much is a visa for Japan?" -> {"bucket":"NEW","section":"none"}\n'
        "BRAIN SECTIONS:\n" + ("\n".join(cat) if cat else "(empty)")
    )
    out = chat(sys, question, num_predict=110)
    try:
        j = json.loads(out)
        b = j.get("bucket", "NEW")
        b = b if b in ("TASK", "FACT", "NEW") else "NEW"     # discipline: unknown bucket -> NEW (gate)
        return b, j.get("section", "none")
    except Exception:
        return "NEW", "none"      # unparsed -> safe: nothing guessed, the gate decides

def search_brain(section, question):
    """FACT path: find the note whose § topic matches, read it, answer with it (+ SOURCE)."""
    core = section.replace("§", "").strip().lower()
    match = None
    for name in sorted(os.listdir(RESOURCES)):
        if name.endswith(".md"):
            t = topic_of(RESOURCES + "/" + name)
            if t and t.lower() == core:
                match = RESOURCES + "/" + name
                break
    if not match:
        return "SECTION NOT FOUND: " + section + " (route said FACT but no note matched - treat as NEW)"
    block = read(match)
    ans = chat("Answer in ONE line using ONLY this section, ending with 'SOURCE: brain " + core +
               ".\n\n" + block, question)
    return ans + "\n(section: " + section + ")"

def task_answer(question):
    return chat("Answer TASK questions about this list in ONE line ending with 'SOURCE: 1 - Projects/Inbox.md'.\n\nTODO:\n"
                + read_folder(PROJECTS), question)

def note_filename(draft):
    """Derive a safe filename from a draft's '§ <short name>' first line."""
    for line in draft.splitlines():
        if line.startswith("§"):
            base = line.lstrip("§ ").strip()
            # filesystem-safe: drop punctuation, keep dashes
            safe = "".join(c if c.isalnum() or c in " -" else "" for c in base).strip()
            return (safe or "new-note") + ".md"
    return "new-note.md"

def gated_write(question, yes=False):
    """NEW path: draft a note -> HUMAN GATE -> only then it enters 3 - Resources/ as a new .md file."""
    draft = chat("Draft a brain-note section for this question: first line '§ <short name>' + 2 bullet facts, "
                 "mark unknown facts as 'open'. Only from the user's words + honest unknowns. "
                 "Reply the note text only.", question, num_predict=100)
    print("DRAFT (NOT written yet):\n---\n" + draft + "\n---")
    if not yes and input("HUMAN GATE - write this into " + RESOURCES + "/? (y/N) ").strip().lower() not in ("y", "yes"):
        return "GATE: declined - logged, " + RESOURCES + " untouched."
    fname = RESOURCES + "/" + note_filename(draft)
    open(fname, "w", encoding="utf-8").write(draft.rstrip("\n") + "\n")
    return "WRITTEN to " + fname + " (gated). Question was: " + question

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="+")
    ap.add_argument("--gate", action="store_true", help="allow the gated write on the NEW path")
    ap.add_argument("--yes", action="store_true", help="pre-approve the gate (tests only)")
    a = ap.parse_args()
    q = " ".join(a.question)
    bucket, section = route(q)
    print("ROUTE:", bucket, "| section:", section)
    if bucket == "TASK":
        print("TASK ->", task_answer(q))
    elif bucket == "FACT" and section not in (None, "", "none"):
        print("FACT ->", search_brain(section, q))
    else:
        print("NEW ->", gated_write(q, yes=a.yes) if a.gate else
              "NEW -> this becomes a draft at the gate (re-run with --gate). "
              "The graph forbids guessing: no note without a human.")
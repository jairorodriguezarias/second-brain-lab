#!/usr/bin/env python3
# new_project.py — minimal project scaffolder: create a new note in 1 - Projects/ from a template
# "arrancar": run this to mint a project, then grow it (areas, resources, the typed contract) in class
# usage:
#   python3 scripts/new_project.py "RAG Eval Harness"
import sys
from datetime import date
from pathlib import Path

PROJECTS = Path("1 - Projects")

TEMPLATE = """---
status: active
end: <define in class>
---
# Project — {name}

## Objective
<one line: what this project is for>

## Milestones
- [ ] <first milestone>
- [ ] <second milestone>

## Notes
- <a starting note for the team>

---
SOURCE: 1 - Projects/Project — {name}.md
"""

def create(name):
    slug = "".join(c if c.isalnum() or c in " -" else "" for c in name).strip() or "new-project"
    path = PROJECTS / f"Project — {slug}.md"
    if path.exists():
        print(f"✗ already exists: {path}  (pick another name)")
        return
    path.write_text(TEMPLATE.format(name=name), encoding="utf-8")
    print(f"✓ created {path}")
    print(f"  next: add a `- [ ] <task>` to its milestones, then `git add` it.")

if __name__ == "__main__":
    name = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Project name: ").strip()
    if name:
        create(name)
    else:
        print("✗ no name given")
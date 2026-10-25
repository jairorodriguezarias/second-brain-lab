#!/usr/bin/env python3
# slides.py — minimal slides starter: render a .deck.md → .html .pdf .pptx via Marp
# "arrancar": run this on any deck file, then grow it (themes, overflow scan, print kits) in class
# usage:
#   python3 scripts/slides.py "31 - Decks/My Deck.deck.md"
import sys, subprocess, shutil
from pathlib import Path

EDITORIAL = str(Path(__file__).resolve().parents[2] / "skills" / "slides" / "assets" / "theme-editorial.css")

def render(deck):
    """Render a Marp deck to HTML, PDF, and PPTX side by side."""
    base = str(Path(deck).with_suffix(""))        # drop .deck.md
    theme = str(EDITORIAL)
    for fmt, flag in [("html", "--html"), ("pdf", "--pdf"), ("pptx", "--pptx")]:
        out = f"{base}.deck.{fmt}"
        print(f"$ marp {flag} --theme {theme} {deck} -o {out}")
        subprocess.run(["marp", flag, "--theme", theme, deck, "-o", out], check=True)
    print(f"✓ {base}.deck.{{html,pdf,pptx}}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or not shutil.which("marp"):
        print("usage: python3 scripts/slides.py <deck.md>   (needs `marp` on PATH)")
        sys.exit(1)
    render(sys.argv[1])
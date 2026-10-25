#!/usr/bin/env bash
# new_lab_vault.sh — create a per-team lab vault + open it in Obsidian
#
# Usage:   bash new_lab_vault.sh <team-name>        (e.g.  bash new_lab_vault.sh alfa)
# Options: SKIP_OPEN=1 bash new_lab_vault.sh alfa   (create but don't launch Obsidian)
#
# What it does:
#   1) copies its own template folder to  ../lab-vault-<team>/
#   2) makes it an Obsidian vault (.obsidian/app.json) with .py/.txt VISIBLE
#      ("Detect all file extensions" pre-enabled — no settings tour needed)
#   3) warms the local model (gemma4:e2b-it-qat) if ollama is running
#   4) opens the new vault in Obsidian via the obsidian:// url scheme
set -euo pipefail

TEAM="${1:-}"
HERE="$(cd "$(dirname "$0")" && pwd)"

if [[ -z "$TEAM" ]]; then
  echo "usage: bash new_lab_vault.sh <team-name>   e.g.: bash new_lab_vault.sh alfa"
  exit 1
fi
TEAM="$(printf '%s' "$TEAM" | tr -c 'A-Za-z0-9_' '-')"

# where team vaults go: inside a git repo (gitclone flow), beside the template (zip flow)
REPO_ROOT="$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -n "$REPO_ROOT" ]]; then
  DEST="$REPO_ROOT/lab-vault-$TEAM"      # inside the repo — gitignored, tidy
else
  DEST="$(cd "$HERE/.." && pwd)/lab-vault-$TEAM"
fi

if [[ -e "$DEST" ]]; then
  echo "✗ already exists: $DEST  (pick another team name or delete it first)"
  exit 1
fi

# 1) copy the template (the script travels along — teams can mint a second vault)
cp -R "$HERE" "$DEST"

# 2) Obsidian vault config: show unsupported files (.py, .txt) from minute zero
mkdir -p "$DEST/.obsidian"
printf '{\n  "showUnsupportedFiles": true\n}\n' > "$DEST/.obsidian/app.json"

# 3) warm the model — non-fatal: the lab runs offline-first without it
if curl -s http://localhost:11434/api/chat \
     -d '{"model":"gemma4:e2b-it-qat","messages":[{"role":"user","content":"Reply OK"}],"stream":false}' \
     >/dev/null 2>&1; then
  echo "✓ model warm (gemma4:e2b-it-qat)"
else
  echo "⚠ ollama not answering — start it (open -a Ollama) and curl again; the lab still runs without wifi"
fi

# 4) open in Obsidian (obsidian://open?path=<url-encoded absolute path>)
echo "✓ vault ready: $DEST"
echo "  build it: we write the runner together in class (3 functions: agent · research · route)"
if [[ "${SKIP_OPEN:-0}" != "1" ]]; then
  ENC="$(python3 -c 'import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))' "$DEST")"
  if open "obsidian://open?path=$ENC" 2>/dev/null; then
    echo "✓ Obsidian launched with the team vault"
  else
    echo "⚠ open manually: Obsidian → 'Open folder as vault' → $DEST"
  fi
fi
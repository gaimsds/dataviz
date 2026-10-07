#!/usr/bin/env bash
# Sync DATS 6401 weekly materials into the book, leaving answer keys behind.
#
# Everything under dats6401/weekly/ ships to the public GitHub Pages site, so
# this script excludes the answer keys and then HARD-FAILS if any slipped
# through. Safe to re-run: it copies over the top and re-checks.
#
#   usage:  dats6401/tools/sync_weekly.sh [SOURCE_DIR]
#
# SOURCE_DIR is the PRIVATE staging folder holding the full materials set
# (demos, hands-on skeletons, starters AND the answer keys). It defaults to
# ~/projects/dats6401/weekly_materials and can also be set via WEEKLY_SRC.
# The destination is always weekly/ next to this script's parent.

set -euo pipefail

BOOK="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${1:-${WEEKLY_SRC:-$HOME/projects/dats6401/weekly_materials}}"
DEST="$BOOK/weekly"

[[ -d "$SRC" ]] || {
  echo "ERROR: source not found: $SRC" >&2
  echo "Pass the staging folder as an argument or set WEEKLY_SRC." >&2
  exit 1
}
mkdir -p "$DEST"

# Answer keys are withheld by default. Each path listed here is released ON
# PURPOSE -- the instructor decided students should have it -- and is exempt
# from both the rsync exclude below and the guard that follows. Everything not
# listed stays private, so adding a week here is a deliberate, visible edit.
# Paths are relative to SRC.
PUBLISHED_KEYS=(
  "week7/week07_SOLUTIONS.ipynb"
)

# rsync applies rules in order and the first match wins, so the exemptions have
# to precede the answer-key exclude.
includes=()
for key in "${PUBLISHED_KEYS[@]}"; do
  includes+=(--include="/$key")
done

# Exclusions are anchored on the underscore ("*_solution*", not "*solution*")
# so that legitimate files such as app_resolution_starter.py -- note the
# "re-SOLUTION" substring -- are not mistaken for answer keys and dropped.
#
# Note: --delete-excluded does NOT reach a key already sitting in DEST (tested
# 2026-10-07). The guard below is what catches that case; it fails the run and
# you remove the file by hand.
rsync -a --delete-excluded --itemize-changes \
  --exclude='.DS_Store' \
  --exclude='INTEGRATION.md' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='.ipynb_checkpoints/' \
  "${includes[@]}" \
  --exclude='*_[Ss][Oo][Ll][Uu][Tt][Ii][Oo][Nn]*' \
  "$SRC/" "$DEST/"

# Guard: no answer key may reach the published folder unless it was named above.
leaked=$(find "$DEST" \( -iname '*_solution*' -o -iname '*_answer*' -o -iname '*_key.*' \) -print)
for key in "${PUBLISHED_KEYS[@]}"; do
  leaked=$(printf '%s\n' "$leaked" | grep -vxF "$DEST/$key" || true)
done
leaked=$(printf '%s\n' "$leaked" | sed '/^$/d')
if [[ -n "$leaked" ]]; then
  echo "" >&2
  echo "ABORT: unreleased answer keys present in the published folder:" >&2
  echo "$leaked" >&2
  echo "Delete the file from weekly/, or add its path to PUBLISHED_KEYS if you" >&2
  echo "really do mean to release it to the public site." >&2
  exit 1
fi

echo ""
echo "OK - $(find "$DEST" -type f | wc -l | tr -d ' ') files in weekly/."
echo "Answer keys released on purpose: ${PUBLISHED_KEYS[*]:-(none)}"
echo "Reminder: chapter Materials: links are maintained by hand -- update them"
echo "if you added or renamed a file."

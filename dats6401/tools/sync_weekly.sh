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

# Exclusions are anchored on the underscore ("*_solution*", not "*solution*")
# so that legitimate files such as app_resolution_starter.py -- note the
# "re-SOLUTION" substring -- are not mistaken for answer keys and dropped.
# --delete-excluded also clears any key a previous, looser run left behind.
rsync -a --delete-excluded --itemize-changes \
  --exclude='.DS_Store' \
  --exclude='INTEGRATION.md' \
  --exclude='*_[Ss][Oo][Ll][Uu][Tt][Ii][Oo][Nn]*' \
  "$SRC/" "$DEST/"

# Guard: nothing resembling an answer key may exist under the published folder.
leaked=$(find "$DEST" \( -iname '*_solution*' -o -iname '*_answer*' -o -iname '*_key.*' \) -print)
if [[ -n "$leaked" ]]; then
  echo "" >&2
  echo "ABORT: answer keys present in the published folder:" >&2
  echo "$leaked" >&2
  exit 1
fi

echo ""
echo "OK - $(find "$DEST" -type f | wc -l | tr -d ' ') files in weekly/, no answer keys present."
echo "Reminder: chapter Materials: links are maintained by hand -- update them"
echo "if you added or renamed a file."

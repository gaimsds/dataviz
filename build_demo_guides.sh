#!/bin/bash
# build_demo_guides.sh — turn each week's DEMO_GUIDE.md into a readable web page.
#
#   ./build_demo_guides.sh
#
# Writes DEMO_GUIDE.html beside every dats6401/weekly/week*/DEMO_GUIDE.md. The
# chapters link to the .html, so run this again after editing a guide and
# commit both files. Uses the pandoc that ships with Quarto.
set -euo pipefail
cd "$(dirname "$0")/dats6401"

for md in weekly/week*/DEMO_GUIDE.md; do
  dir=$(dirname "$md")
  n=${dir#weekly/week}
  chapter=$(ls week_$(printf '%02d' "$n")_*.qmd | head -1)
  page="../../${chapter%.qmd}.html"
  tmp=$(mktemp -d)

  cat > "$tmp/head.html" <<'CSS'
<style>
  body { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.25rem 4rem;
         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
         font-size: 17px; line-height: 1.6; color: #1f2328; background: #fff; }
  h1 { color: #033C5A; font-size: 1.7rem; line-height: 1.25;
       padding-bottom: .5rem; border-bottom: 4px solid #D6BF91; }
  h2 { color: #033C5A; font-size: 1.25rem; margin-top: 2.2rem; }
  a { color: #0075C8; }
  code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
         font-size: .9em; background: #f3f5f6; padding: .1em .3em; border-radius: 3px; }
  pre { background: #f3f5f6; padding: .9rem 1rem; border-radius: 6px; overflow-x: auto; }
  pre code { background: none; padding: 0; }
  table { border-collapse: collapse; margin: 1rem 0; display: block; overflow-x: auto; }
  th, td { border: 1px solid #d0d7de; padding: .4rem .7rem; text-align: left; vertical-align: top; }
  th { background: #f3f5f6; }
  .back { font-size: .9rem; margin: 0 0 1.2rem; }
</style>
CSS
  echo "<p class=\"back\"><a href=\"$page\">&larr; Back to the Week $n page</a></p>" > "$tmp/before.html"

  quarto pandoc "$md" -f gfm -t html5 -s \
    --metadata pagetitle="Week $n — Block 2 demo guide" \
    -H "$tmp/head.html" -B "$tmp/before.html" -o "$dir/DEMO_GUIDE.html"
  rm -rf "$tmp"
  echo "wrote dats6401/$dir/DEMO_GUIDE.html  (back link: $page)"
done

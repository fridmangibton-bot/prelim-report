#!/usr/bin/env bash
# Build a LaTeX file into build/ without latexmk (no perl needed).
# Usage: bash scripts/build.sh [file.tex]   (default: main.tex)
# Runs lualatex, bibtex, lualatex, lualatex. Prints only error lines.
set -u
cd "$(dirname "$0")/.."
SRC="${1:-main.tex}"
JOB="$(basename "${SRC%.tex}")"
mkdir -p build
status=0

lua() {
  lualatex -interaction=nonstopmode -file-line-error -output-directory=build "$SRC" >"build/$JOB.build.out" 2>&1 || status=1
  grep -E '^(! |.*:[0-9]+: )' "build/$JOB.build.out" | sort -u
}

lua
if [ -f "build/$JOB.aux" ] && grep -q 'bibdata' "build/$JOB.aux"; then
  BIBINPUTS="build;.;${BIBINPUTS:-}" bibtex "build/$JOB" >"build/$JOB.bibtex.out" 2>&1 || status=1
  grep -E '^(I couldn.t|.*rror)' "build/$JOB.bibtex.out"
fi
lua
lua

if [ "$status" -ne 0 ]; then
  echo "BUILD FAILED"
else
  echo "BUILD OK: build/$JOB.pdf"
fi
exit "$status"

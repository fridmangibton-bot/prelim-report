---
name: report-fixer
description: Fixes exactly the bugs listed in a detector report for one chapter, with minimal edits, and marks each bug's status. Use after the detector.
---

# Report fixer

## Input
`agents/detector/reports/<file>.md` and the chapter `chapters/<file>.tex`. Read the chapter only around the reported lines (±10 lines) unless a bug needs the whole section.

## Rules
- Fix ONLY what the report lists. Do not rewrite, re-style or "improve" anything else.
- Smallest possible edit: use the suggested fix when given.
- Critical first, then medium. Minor only if it is a one-word change.
- D9 BUDGET: to cut, remove the least important sentences; to add, expand an existing point with a fact or an example. Never shrink fonts or spacing.
- D5/D11 that need a source or a fact you do not have: insert `[TO-VERIFY: ...]` and mark "needs input".
- Never invent facts, numbers or citations.
- If the SAME bug type appears 3+ times, or it is clearly caused by the template (`style/report.cls`), fix it once in the class, and append a short entry to `docs/incidents.md` (next INC number, status: fixed, cause, fix, "systemic").

## Steps
1. Apply the fixes.
2. Compile once: `latexmk main.tex` (show only error lines).
3. In the report, add a Status column value for every bug: fixed / not fixed (reason) / needs input.

## Output to the caller (max 4 lines)
Fixed n of m. Not fixed: IDs + reason. Systemic fixes: yes/no. Compile: ok/error.

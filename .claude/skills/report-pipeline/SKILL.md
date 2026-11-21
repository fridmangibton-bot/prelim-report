---
name: report-pipeline
description: Runs the full writer -> detector -> fixer loop for one or more chapters, unattended, with progress saved so it can resume after a token limit. Use when asked to "write chapters X, Y, Z".
---

# Report pipeline

For each chapter in the order given:
1. Run the `writer` subagent on it.
2. Run the `detector` subagent on it.
3. If the report has critical or medium bugs: run the `fixer` subagent, then the `detector` again.
4. Maximum 2 fixer rounds per chapter. Then move on even if minor bugs remain; list them.
5. After each chapter: append one line to `docs/progress.md` (chapter, rounds, remaining bugs) and commit with message "Write <chapter>" (do not push unless asked).

Resume rule: at the start, read `docs/progress.md`; skip chapters already marked done.
Do not ask the user questions during the run. If something blocks a chapter, log it in progress.md and continue with the next chapter.

Final reply (max 10 lines): one line per chapter (words, rounds, remaining bugs, TO-VERIFY count), then the list of figures still pending.

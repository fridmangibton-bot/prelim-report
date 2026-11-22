# Detector report – ch2-problem.tex – 2026-11-22
Summary: 0 critical, 1 medium, 2 minor. Words: 671/850. TO-VERIFY: 19.

Note: Words = whitespace tokens in prose (paragraphs, notebox, directornote), excluding tables. Table cells add about 109 tokens. Target range 850 ±15% is 723–978. Counted with `sed` and `grep -c` because `wc -w` mis-counts Hebrew on this machine.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch2-01 | D9 | 5–19, 35–50, 68–71 | medium | Prose is 671 words against a target of 850 (about 21% under the ±15% band of 723–978). | Add about 60–110 Hebrew words of prose, for example a sentence on how the baseline values will be measured in the section on the current state. Not a mechanical replacement. |
| BUG-ch2-02 | D10 | 39 | medium | English term \textenglish{SMART} appears with no Hebrew term before it. The parenthetical expansions do not gloss the acronym. | Replace `לפי מתודולוגיית \textenglish{SMART}` with `לפי מתודולוגיית ניסוח יעדים (\textenglish{SMART})`. |
| BUG-ch2-03 | D11 / budget | 21–32, 52–65 | minor | The chapter has two tables (the gap table and the requirements table). The budget in docs/agents-setup.md section 0 lists "850 + 1 table". | Decide whether the gap table stays. No mechanical fix. |

## Checks with no bugs
- D1 BIDI: no unwrapped Latin text. The only Latin residue is `[TO-VERIFY]` markers and the line-1 comment.
- D2 BIDI-JOIN: no hits.
- D3 REF: `tab:ch2-gap` (line 24) is referenced at line 19. `tab:ch2-req` (line 55) is referenced at line 48.
- D4 CAPTION: both captions (lines 23, 54) come before their tabular.
- D5 CITE: no `\cite` in the chapter.
- D6 VOICE: line 44 "שלנו" is inside directornote, which is allowed. Line 68 "נעשה" (three times) is an impersonal passive ("the check is done"), not first person. Dismissed as a false positive.
- D7 GENERIC: no hits.
- D11 REQ: CH2-01 (quantitative problem, lines 10–36), CH2-02 (no solution named; the current-state tools at line 8 are existing tools), CH2-03 (SMART goals at lines 39–41 and the hypothesis in the directornote at line 44), and CH2-04 (requirements table with ID, target and verification, lines 52–65) are all present. The five goals (lines 41) and the six requirements (table) are consistent with the functional and non-functional split at lines 68 and 71.
- D12 BUILD: `build/main.log` exists (modified 2026-11-22 21:29; chapter modified 2026-11-21 19:54, so the log is newer than the chapter). The ch2 segment of the log (from `(./chapters/ch2-problem.tex` to `ch3-literature.tex`) has no Overfull or Underfull hbox warnings and no `!` error lines. The Overfull warnings nearby belong to ch1, ch3, or the frontmatter. The build was not run.
- D13 BIDI-ORDER: no hits.

## Counts (info, not bugs)
- D8 TO-VERIFY: 19 markers, on lines 10, 12, 14, 16, 27 (×2), 28 (×2), 29 (×2), 30, 41 (×4), 58, 59, 61, 62. These are tracked target values and are not counted as bugs.
- D8 FIGURE PENDING: 0.

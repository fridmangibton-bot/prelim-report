# Detector report round 2 – ch6-workplan.tex – 2026-11-21
Summary: 0 critical, 0 medium, 1 minor open. Words: ~622/600 (round-1 estimate, not re-measured; within ±15%). TO-VERIFY: 2 (source lines 59 and 62, both wrapped in \textenglish). Known/accepted, not counted: BUG-ch6-05, BUG-ch6-06, intentional WBS placeholder (D8 pending = 1).

Inputs checked: chapters/ch6-workplan.tex (mtime 20:08:51), build/main.pdf and build/main.log (20:10:09, newer than the chapter), docs/agents-setup.md section 0, docs/requirements.md rows CH6-01..03, round-1 report agents/detector/reports/ch6-workplan.md.

## Round-1 status re-check
| Bug ID | Round-1 status | Round-2 result |
|---|---|---|
| BUG-ch6-01 | fixed | Verified. Line 59 reads `\textenglish{[TO-VERIFY]}`. Closed. |
| BUG-ch6-02 | fixed | Verified. Line 62 reads `\textenglish{[TO-VERIFY]}` inside directornote. Closed. |
| BUG-ch6-03 | fixed | Verified. build/main.log contains 0 "Overfull" lines. Closed. |
| BUG-ch6-04 | fixed | Verified. build/main.log contains 0 "Overfull" lines. Closed. |
| BUG-ch6-05 | accepted (Gantt dummy label) | Excluded per instruction. Label "נתוני דמה" still visible at top-left of the Gantt on PDF p. 16. |
| BUG-ch6-06 | accepted (RACI font, class-level) | Excluded per instruction. Latin R/C/A still in serif face on PDF p. 16. |

## Mechanical checks (round 2)
- D1 BIDI: every Latin run in Hebrew text is inside \textenglish{}, a command, a label/ref, or the includegraphics path. No hits.
- D2 BIDI-JOIN: no \textenglish{} run contains Hebrew letters. No hits.
- D3 REF: fig:ch6-wbs, tab:ch6-wbs, tab:ch6-raci, fig:ch6-gantt are all referenced in the text. No hits.
- D4 CAPTION: figure captions below content, table captions above tabular. No hits.
- D5 CITE: no \cite in this chapter. No hits.
- D6 VOICE: only "שלנו" on line 62, inside directornote (exempt). No hits.
- D7 GENERIC: no hits.
- D8 TODO: TO-VERIFY = 2; FIGURE PENDING = 1 (WBS placeholder, info only).
- D9 BUDGET: see summary line; not re-measured precisely (no detex or working python on this machine).
- D10 TERM: WBS, RACI and Gantt chart each have a Hebrew term with the English in parentheses on first use.
- D11 REQ: CH6-01 (5 WPs with tasks and deliverables, WBS table and placeholder figure), CH6-02 (one R per row, supervisor is A in all rows), CH6-03 (14 weeks, dependencies, critical path, two milestones at weeks 7 and 14, reserve weeks 6 and 13) are present. Text, table and Gantt bars agree.
- D12 BUILD: build/main.log has 0 errors ("^!" count 0) and 0 Overfull warnings. Underfull warnings exist but are not in the rule set (not counted).
- D13 BIDI-ORDER: grep patterns for maqaf-prefix adjacency and Hebrew between two \textenglish runs found no hits. Visual check of the RACI sentence (p. 16) and line 59 ("הוא [TO-VERIFY].", p. 17) shows correct order.
- D6/D7 in prose: no new hits.

## Visual check (300 dpi, build/main.pdf, PDF pages 15–17, chapter 6)
Rendered with pdftoppm -r 300 to scratchpad: p-15.png, p-16.png, p-17.png.
- Page 15: section 6.1, WBS placeholder (expected), caption, body text, WBS table. Table header and five rows render. Caption order correct.
- Page 16: section 6.2 RACI table renders with the known serif R/C/A font (BUG-ch6-06, accepted). Section 6.3 Gantt renders with the known "נתוני דמה" label (BUG-ch6-05, accepted). Milestones at weeks 7 and 14 and reserve bands at weeks 6 and 13 match the text.
- Page 17: section 6.3 continuation, the [TO-VERIFY] markers, directornote box, and section 6.4 render with correct order and no overflow.

## Open bugs
| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch6-07 | Read (visual) | 5 (WBS table, lines 24–28), 41–45 (RACI table) | minor | In both tables the item numbers ("1." to "5.") render at the left edge of the first column, after the Hebrew text of the same cell, which reads against the right-to-left flow of the rest of the cell. Visible on PDF p. 15 and p. 16. Cosmetic; Hebrew reads correctly. Confirm with the writer whether a different layout is wanted. | None mechanical. Option: drop the leading numbers, or move them after the Hebrew text. |

Open totals: critical 0, medium 0, minor 1.
Accepted and excluded from counts: BUG-ch6-05 (Gantt "נתוני דמה" label, in figures/python/make_figures.py), BUG-ch6-06 (RACI font, class-level), WBS placeholder (intentional).

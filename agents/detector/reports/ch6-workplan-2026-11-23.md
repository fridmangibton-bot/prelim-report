# Detector report – ch6-workplan.tex – 2026-11-23
Summary: 0 critical, 3 medium, 1 minor. Words: ~700/600 (prose incl. directornote; ~645 without it, inside ±15%). TO-VERIFY: 0.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-6-01 | D11 REQ (schedule consistency) | 75 | medium | Says WP3 has "שבוע גמישות אחד". The table has WP3 at weeks 3–4 and WP4 (which needs WP3) starting at week 8, so WP3 has weeks 5–7 of float (three weeks). Same claim in line 77 ("שבוע הגמישות שלה"). | "ולכן יש לה שלושה שבועות גמישות (שבועות 5 עד 7)"; line 77: "שלושת שבועות הגמישות שלה" |
| BUG-6-02 | D11 / cross-reference | 84 | medium | Promises that a scope reduction "מתועדת בטבלת הסיכונים בפרק הבא". Chapter 7 has no such log; its tables contain only risks and mitigations. | Either add a row/column for scope decisions in ch7, or reword to the source that actually records them (e.g. "מתועדת ביומן ההחלטות של הפרויקט"). |
| BUG-6-03 | D9 BUDGET | 1–84 | medium | Prose word count ~700 against a 600 target (range 510–690). Count includes the directornote box (~55 words). Marginal: about 645 without it. | Trim about 15 words from the prose, e.g. in line 84 the sentence starting "מדיניות הרזרבה קובעת". |
| BUG-6-04 | D11 consistency | 25 / 80 | minor | The 8-participant usability target appears only in the directornote (line 80), not in the body text describing the test in the table row (line 25). Ch2 also states 8. | Add "עם שמונה משתתפים (יעד תכנון)" to the body text of line 25 or to line 30, so the number is not only in the box. |

## Checks with no hits
- D1 BIDI: no Latin run outside `\textenglish{}`, math or commands.
- D2 BIDI-JOIN: no Hebrew inside `\textenglish{}`.
- D3 REF: all five labels (fig:ch6-wbs, tab:ch6-wbs, tab:ch6-raci, tab:ch6-schedule, fig:ch6-gantt) are referenced in the text.
- D4 CAPTION: figure captions below, table captions above. Correct.
- D5 CITE: no `\cite` in this chapter.
- D6 VOICE: no first person outside directornote.
- D7 GENERIC: none.
- D8 TODO: TO-VERIFY 0; FIGURE PENDING 0.
- D10 TERM: WBS, RACI, Gantt each carry a Hebrew term with the English in parentheses on first use.
- D11 REQ: CH6-01 (5 WPs with tasks and deliverables), CH6-02 (one R and one A per row, supervisor = A in all rows), CH6-03 (14 weeks, dependencies, critical path WP1-2-4-5, milestones at weeks 7 and 14, reserve weeks 6 and 13) present.
- D12 BUILD: build/main.log was being written by a build running at the time of the check (timestamp 22:01). The only Overfull \hbox in the log (lines 77–88) belongs to ch3. No hits point to ch6. Partial check only.
- D13 BIDI-ORDER: no hits.

## Notes
- No edits to chapters. Only this report was written.
- The weekly-hours statement (20 = 2 x 10, team assumption, line 75) and the RACI/schedule tables are consistent with each other.
- Earlier report of 2026-11-21 (agents/detector/reports/ch6-workplan.md) is kept untouched; it refers to a previous version of the chapter.

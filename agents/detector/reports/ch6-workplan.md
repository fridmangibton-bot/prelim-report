# Detector report – ch6-workplan.tex – 2026-11-21
Summary: 2 critical, 3 medium, 1 minor. Words: ~622/600 (within ±15%). TO-VERIFY: 2.

| Bug ID | Check | Line | Severity | Problem | Suggested fix | Status |
|---|---|---|---|---|---|---|
| BUG-ch6-01 | D1 | 59 | critical | Latin placeholder "[TO-VERIFY]" in Hebrew text, not wrapped in an LTR macro. Renders acceptably in the PDF (p. 17), but fails the D1 rule. | `\textenglish{[TO-VERIFY]}` | fixed |
| BUG-ch6-02 | D1 | 62 | critical | Same as BUG-ch6-01, inside the directornote box ("ייערך עם [TO-VERIFY] משתמשים חדשים"). | `\textenglish{[TO-VERIFY]}` | fixed |
| BUG-ch6-03 | D12 | 5–6 | medium | Build log: `Overfull \hbox (1.61626pt too wide) in paragraph at lines 5--6`. Paragraph contains the WBS English term. | Shorten or reword the sentence so it fits the line width (not mechanical). | fixed (shortened sentence) |
| BUG-ch6-04 | D12 | 16–17 | medium | Build log: `Overfull \hbox (2.54399pt too wide) in paragraph at lines 16--17`. Paragraph starting "האיור אמור להראות...". | Shorten or reword the sentence (not mechanical). | fixed (shortened and reworded) |
| BUG-ch6-05 | Read (figure) | 54 | medium | The Gantt figure (`figures/ch6_gantt.pdf`, generated at `figures/python/make_figures.py` near line 331) shows the red label "נתוני דמה" (dummy data) at its top-left. The text (line 59) presents the durations as planning estimates, so the figure contradicts the chapter. | Remove the "נתוני דמה" label in make_figures.py and regenerate the figure. Outside this chapter file; the detector does not edit it. | not fixed (skipped, out of scope: label is in figures/python/make_figures.py; figures used as is, pending real data) |
| BUG-ch6-06 | Read (visual) | 42–45 | minor | In the RACI table (p. 16 of build/main.pdf) the `\textenglish{R/C/A}` letters render in a Latin serif face that looks larger and differs from the Hebrew text in the same cells. Cosmetic only. | None mechanical. Check the `\textenglish` font in style/report.cls. | not fixed (skipped, needs a class-level font change, not trivial in the chapter) |

## Checks with no hits
- D2 BIDI-JOIN: none.
- D3 REF: all four labels (fig:ch6-wbs, tab:ch6-wbs, tab:ch6-raci, fig:ch6-gantt) are referenced in the text.
- D4 CAPTION: figure captions below their content, table captions above their tabular. Correct.
- D5 CITE: no `\cite` in this chapter.
- D6 VOICE: no first person outside directornote. The "שלנו" on line 62 is inside directornote and exempt.
- D7 GENERIC: none.
- D10 TERM: WBS, RACI and Gantt each have a Hebrew term with the English in parentheses on first use.
- D11 REQ: CH6-01 (5 WPs, task, deliverable), CH6-02 (one R per row, A = supervisor), CH6-03 (14 weeks, dependencies, critical path, two milestones, reserve week before each milestone) are all present. Rows and text agree.
- D13 BIDI-ORDER: grep found no hits. Visual check of the RACI sentence (p. 16) shows the correct RTL order.
- Content: Gantt bars match the text (WP1 1–2, WP2 3–5, WP3 3–4 with one week slack, WP4 8–10, WP5 11–12, milestones at weeks 7 and 14, reserves at weeks 6 and 13). Critical path listed in text matches the figure.

## Visual check (300 dpi, build/main.pdf, PDF pages 15–17)
- Page 15: WBS placeholder appears as expected (not counted as a bug). WBS table renders correctly; Hebrew numbered items and the English term in line 5 display in the correct order.
- Page 16: RACI table and Gantt figure both render. The Gantt figure is present with legend, axis and milestones (see BUG-ch6-05 for the dummy-data label).
- Page 17: Body text and directornote box render. [TO-VERIFY] markers display correctly.
- The PDF (19:03 timestamp at 20:03) is newer than the chapter (20:02), so the render reflects the current source.
- Build log also shows "Underfull \hbox" warnings at lines 2 (chapter and section headings). Not counted: they are headings and the rule covers only overfull boxes.

## Not bugs (per instructions)
- WBS figure is an intentional TikZ placeholder ("FIGURE PENDING: ch6-wbs"). Counted as info only: D8 pending count = 1.

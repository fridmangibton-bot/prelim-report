# Detector report – ch7-risks – 2026-11-21
Summary: 1 critical, 5 medium, 3 minor. Words: ~310 prose + ~110 table words (approx. Hebrew token count) / 350 target. TO-VERIFY: 2 (source count of `[TO-VERIFY]` in chapters/ch7-risks.tex, lines 5 and 57).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-7-01 | Unsourced numbers (CLAUDE.md "Any number without a source is marked [TO-VERIFY]") | 40, 48-51 (table 7.2 column "שיורי": 8, 10, 6, 6) | critical | Residual scores are the writer's own estimates, not in docs/sources.md, not in figures/python/data/risks.json (no residual field), and carry no [TO-VERIFY]. Line 40 calls them "ראשוניים" but does not mark them. The [TO-VERIFY] on line 5 covers the P/I/R estimates only, not the residual column. Verdict: this violates the rule. | Add `\textenglish{[TO-VERIFY]}` after the sentence on line 40, e.g. "הציונים השיוריים ראשוניים \textenglish{[TO-VERIFY]}, והם ייבדקו שוב באבן הדרך הראשונה." Also add a residual field to risks.json so the numbers have a single source. |
| BUG-7-02 | D13 BIDI-ORDER | 28 | medium | "ו־\textenglish{R7}" after "\textenglish{R3}" renders as "R3, R2R1 ... ו־R7" in the PDF (p.18, 300 dpi). Visual check confirmed the scramble. Not auto-fixable (RLM tested, no effect; see INC-001). | Not mechanical. Fixer must rework the sentence (e.g. put the run list in a different order or split into separate sentences) and re-check the crop at 300 dpi. |
| BUG-7-03 | D13 BIDI-ORDER | 57 | medium | "\textenglish{R4}, \textenglish{R5} ו־\textenglish{R6}" renders as "R5R4 , ו־R6" in the PDF (p.19, 300 dpi). | Not mechanical. Same as BUG-7-02; reorder or rephrase, then re-check visually. |
| BUG-7-04 | D12 BUILD (Overfull \hbox) | 47 | medium | Log `build/main.log` line 1862: "Overfull \hbox (1.65051pt too wide)" in the mitigation table header row (Arial bold "מזהה" / "פעולת מנע"). | `\begin{tabular}{p{0.9cm} p{3.9cm} p{3.9cm} p{1.4cm}}` -> `\begin{tabular}{p{1.0cm} p{3.8cm} p{3.9cm} p{1.4cm}}` (same total width, 10.1 cm). |
| BUG-7-05 | D9 BUDGET / STR-02 page budget | whole chapter (figure on line 34, table on line 42) | medium | Chapter spans 3 PDF pages (18-20) vs the 2-page budget in docs/agents-setup.md section 0 and STR-02 (risks = 2 pages). Table 7.2 sits alone on p.20 with about 2/3 of the page empty. | Shrink the figure (e.g. `width=0.85\textwidth`) and/or tighten text on p.18-19 so that table 7.2 fits on the same page as the figure, or reduce figure height. |
| BUG-7-06 | Figure bidi (same class as D13/INC-001, inside the figure) | 34 (figure `figures/ch7_risk.pdf`); source figures/python/make_figures.py `chart_risk()` and figures/python/data/risks.json id R6 | medium | In the key list, "מדיניות פלטפורמות לגבי תוכן AI" renders with the Latin "AI" misplaced ("AI  תוכן" reads reversed). | Change the label in risks.json R6 to "מדיניות פלטפורמות לגבי תוכן בינה מלאכותית" (matches the table text on line 18), or wrap "AI" in an LTR run inside make_figures.py. Regenerate ch7_risk.pdf. |
| BUG-7-07 | Figure content | 34 | minor | Figure carries the tag "נתוני דמה" (placeholder data) and the R5 label shows a stray space: "(דיפ-פייק )". The chapter text itself never says the figure is placeholder-based. Also the json uses "דיפ-פייק" with a hyphen, the text uses "דיפ־פייק" with maqaf. | Remove the stray space in the label. Harmonize the hyphen/maqaf between risks.json and line 18. Remove "נתוני דמה" from the figure once the real P/I values are confirmed. |
| BUG-7-08 | Table layout | 48-49 | minor | Justified cell text in table 7.2 produces wide word gaps ("מעבר לתמהיל מקומי", "מדיניות פלטפורמות לגבי תוכן בינה מלאכותית" in table 7.1, p.18). Cosmetic. | Use `\raggedleft` / `\raggedright` in those p{} columns, or shorten the cell text. |
| BUG-7-09 | D10 / unsupported claim about our own process | 23 | minor | "הסיכונים נבחרו לפי שלושה תחומים" is a methodology claim. docs/concept.md (section "סיכונים ראשונים", line 72) lists the seven risks without any selection criteria. | Reword to match the concept, e.g. "הסיכונים מקובצים לשלושה תחומים: ...", or add the selection basis to docs/concept.md before keeping the claim. |

## Checks with no hits (for the record)
- D1 BIDI: no Latin run outside \textenglish{} in prose; the only Latin hits are in \label, \ref and \textenglish{} runs.
- D2 BIDI-JOIN: no Hebrew inside \textenglish{}.
- D3 REF: tab:ch7-risks (line 5), fig:ch7-risk (line 28), tab:ch7-mitigation (line 40) each referenced. OK.
- D4 CAPTION: both table captions above tabular (lines 9, 44); figure caption below figure (line 35). OK.
- D5 CITE: no \cite in chapter. OK.
- D6 VOICE: no first person outside directornote. The "אנושית" hit is a false positive for "אנו". OK.
- D7 GENERIC: none.
- D8: TO-VERIFY = 2; FIGURE PENDING = 0 (info).
- D11 REQ: CH7-01 (P, I, R=P×I, R≥12 critical; table 7.1), CH7-02 (matrix figure), CH7-03 (mitigation, contingency, residual for R1, R2, R3, R7; table 7.2) all present. Must-contain items met, apart from the residual-marker issue in BUG-7-01.
- D12: only the Overfull in BUG-7-04 points to ch7. The Underfull hbox warnings in the log at lines 1868-1891 belong to the ch7 table rows (lines 48-51); they are not overfull and are not separately reported.

## Visual check (300 dpi, pdftoppm on build/main.pdf pages 18-20; figures/ch7_risk.pdf at 300 dpi)
- PDF build date (20:15) is newer than chapters/ch7-risks.tex (20:14), so the render reflects the current chapter.
- Mixed direction: Hebrew paragraphs render RTL correctly; the bugs are BUG-7-02 and BUG-7-03 (reordered R-runs).
- Tables: table 7.1 (p.18) and table 7.2 (p.20) render with the right column order and header row. Captions are right-aligned above the table. Only BUG-7-08 (word spacing) and BUG-7-05 (page placement) are visible.
- Risk matrix (p.19 and figures/ch7_risk.pdf): cells and IDs agree with figures/python/data/risks.json:
  - R2 P4 I5 R20; R1 P4 I4 R16; R7 P4 I3 R12 (cell (3,4)); R3 P3 I4 R12; R4 P2 I5 R10; R5 P2 I4 R8; R6 P3 I3 R9. All match.
  - Shaded critical zone is R>=12, which matches critical_threshold 12 and the four critical risks (R1, R2, R3, R7) in the text on line 28.
  - Key-list order (R2, R1, R3, R7, R4, R6, R5) matches sorting by R. Ties at R=12 (R3, R7) keep JSON order.
- Text vs data: the chapter's table 7.1 P, I, R values (lines 13-19) match risks.json exactly. The text on line 28 (critical = R1, R2, R3, R7), line 30 (R4 near threshold, R5 and R6 outside), and line 57 (highest residual is R2) are consistent with the data and with the residual column (8, 10, 6, 6).
- Residual values (8, 10, 6, 6) do not appear in risks.json. See BUG-7-01.

## Notes for the caller
- BUG-7-01 is the one judgment call. I classified it critical, because the rule is explicit ("any number without a source is marked [TO-VERIFY]") and the residual values are not sourced or in the data file. A medium rating would be defensible, but the rule is not optional under CLAUDE.md.
- BUG-7-02 and BUG-7-03 need a visual re-check at 300 dpi after the fix (per D13 and INC-001), not just a grep.
- Report path: /c/Users/User/Downloads/project2/agents/detector/reports/ch7-risks.md (Windows: C:\Users\User\Downloads\project2\agents\detector\reports\ch7-risks.md).
- Chapter file was not edited. Only the report file was written.

## Fixer status (2026-11-21)
| Bug ID | Status |
|---|---|
| BUG-7-01 | fixed: `\textenglish{[TO-VERIFY]}` added after the residual-scores sentence (line 40); numbers 8, 10, 6, 6 kept. Not added to the narrow 1.4 cm header cell (would overflow). risks.json residual field not added (out of scope). Needs input: the values themselves still need a source. |
| BUG-7-02 | fixed: Hebrew "הסיכון" before each ID, no maqaf. Verified at 300 dpi (p.18): R1, R2, R3, R7 in correct order. |
| BUG-7-03 | fixed: same rewording. Verified at 300 dpi (p.19): R4, R5, R6 in correct order. |
| BUG-7-04 | fixed: column widths 1.0/3.8/3.9/1.4 cm; no Overfull in log. |
| BUG-7-05 | fixed: chapter is now 2 pages (18-19). Figure width 0.6 text width; four least important sentences cut (lines 23, 25, 30, 55). |
| BUG-7-06 | not fixed (figures out of scope, used as is) |
| BUG-7-07 | not fixed (figures out of scope, used as is) |
| BUG-7-08 | not fixed (cosmetic, minor, not a one-word change) |
| BUG-7-09 | fixed: "נבחרו" changed to "מקובצים". |

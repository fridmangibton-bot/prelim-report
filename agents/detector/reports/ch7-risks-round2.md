# Detector report – ch7-risks – 2026-11-21 (round 2, after fixer round 1)
Summary: 0 critical, 1 medium, 1 minor open. Words: ~256/350 (below the -15% floor of 298; see BUG-7-R2-02). TO-VERIFY: 3 (lines 5, 37, 53). Pages: 2 (PDF pages 18-19).

Scope: re-check of chapters/ch7-risks.tex against build/main.pdf and build/main.log (log 20:28:49, chapter 20:27:32, so the build reflects the current chapter). Chapter not edited. Figures accepted as is (per caller): dummy-data tag, reversed "AI" label, stray space in R5 label. Minor table word gaps accepted.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-7-R2-01 | Unsourced numbers (CLAUDE.md) | 37 (residual column, table 7.2 lines 45-48) | minor | The residual values 8, 10, 6, 6 are covered by one `[TO-VERIFY]` in the sentence on line 37 ("הציונים השיוריים ראשוניים \textenglish{[TO-VERIFY]}"). Judgment: this is adequate as a minimum. The sentence names the residual scores as initial and points to them, and the marker is the only place the column is discussed. It is weaker than the rule's wording ("any number ... is marked"), because the four cells carry no marker of their own. Still open: the values are not in docs/sources.md or figures/python/data/risks.json. | Strengthen by putting the marker in the table caption (line 41), which sits directly above the column: `\caption{סיכונים קריטיים: מנע, מגירה וציון שיורי \textenglish{[TO-VERIFY]}}`. A marker inside the 1.4 cm header cell was already rejected by the fixer (overflow). Not blocking. |
| BUG-7-R2-02 | D9 BUDGET | whole chapter | medium | Mechanical count of the chapter text is about 256 words (wc on the .tex with commands stripped, tables included), against a target of 350 (+/-15% = 298-402). The round-1 cut of four sentences (lines 23, 25, 30, 55 in round 1) brought the chapter to 2 pages, which the page budget requires (STR-02). The word target is now missed. | Caller decision. Either accept the shortfall because the 2-page budget takes priority, or add about 40 words of prose elsewhere in the chapter without adding a line that pushes p.19 onto p.20. Re-run the build and confirm 2 pages after any change. |

## Round-1 bugs: status
| Bug ID | Round-1 severity | Round-2 status |
|---|---|---|
| BUG-7-01 residual numbers unmarked | critical | Closed as critical. Marker now present on line 37. Residual marker strength is open as BUG-7-R2-01 (minor). |
| BUG-7-02 bidi R1, R2, R3, R7 (line 26) | medium | Closed. Visually verified at 300 dpi (p.18): the sentence reads correctly RTL ("הסיכון R1, הסיכון R2, הסיכון R3 והסיכון R7"). The grep for D13 still hits line 26 (Hebrew word between two textenglish runs) and that hit is harmless here. |
| BUG-7-03 bidi R4, R5, R6 (line 53) | medium | Closed. Visually verified at 300 dpi (p.19): reads correctly RTL ("הסיכון R4, הסיכון R5 והסיכון R6 אינם קריטיים"). The grep hit on line 53 is the same harmless pattern. |
| BUG-7-04 Overfull hbox table 7.2 | medium | Closed. `build/main.log` contains 0 "Overfull" lines. Underfull warnings remain in the ch7 range of the log; they are not overfull and are not reported as bugs. |
| BUG-7-05 page budget | medium | Closed. Chapter spans PDF pages 18-19 (page 20 starts "SCENE 08"). Table 7.2 is on p.19 with the figure. |
| BUG-7-06 figure "AI" label | medium | Accepted by caller (figure out of scope). Not counted as open. |
| BUG-7-07 figure dummy tag, stray space, hyphen/maqaf | minor | Accepted by caller. Not counted as open. |
| BUG-7-08 table word gaps | minor | Accepted by caller. Not counted as open. |
| BUG-7-09 "נבחרו" methodology claim | minor | Closed. Line 23 now reads "מקובצים".

## Checks (round 2)
- D1 BIDI: no Latin letters outside textenglish, labels, refs or math in prose. The Latin hits in the file are \label, \ref, \textenglish runs, the math `R = P $\times$ I` (line 5), and `TO-VERIFY` inside textenglish. OK.
- D2 BIDI-JOIN: grep for Hebrew inside `\textenglish{...}` returns no matches. OK.
- D3 REF: tab:ch7-risks (line 5), fig:ch7-risk (line 26), tab:ch7-mitigation (line 37), each with a matching label. OK.
- D4 CAPTION: table captions above tabular (lines 9, 41); figure caption below the figure (line 32). OK.
- D5 CITE: no \cite in the chapter. OK.
- D6 VOICE: "אנושית" (line 48) is a false positive for "אנו". The directornote has no first person outside the box. OK.
- D7 GENERIC: none. OK.
- D8: TO-VERIFY = 3 (lines 5, 37, 53). FIGURE PENDING = 0.
- D10 TERM: the English terms P, I, R, and the ID tags are wrapped at first use. OK.
- D11 REQ: CH7-01 (P, I, R=P×I, R>=12 critical; table 7.1), CH7-02 (matrix figure), CH7-03 (mitigation, contingency, residual for R1, R2, R3, R7) present. The "four critical" count (line 5) matches the four rows in the table and the matrix text. OK.
- D12 BUILD: 0 Overfull in build/main.log. OK.
- D13 BIDI-ORDER: grep hits on lines 26 and 53 (Hebrew word between two textenglish runs). Visually verified correct at 300 dpi, so not a bug. The grep for the maqaf pattern (`־\textenglish`) returns no hits.

## Visual check (300 dpi, pdftoppm on build/main.pdf, pages 18-19)
- Page 18: section 7.1, table 7.1 (headers, P/I/R columns, row order R1-R7 correct), prose paragraphs, section 7.2 start. Renders RTL; caption above table, right-aligned. No overflow past margins.
- Page 19: matrix figure (accepted as is, with its dummy tag and "AI" label), caption below figure, section 7.3, table 7.2 with the four rows R1, R2, R3, R7 and the residual column (8, 10, 6, 6) present and aligned to the right edge. Paragraph lines 53-54 and the directornote render correctly.
- Only issues visible: the accepted word gaps in table 7.2 and the accepted figure issues.

## Notes for the caller
- BUG-7-R2-01 judgment: a single marker in the sentence is adequate for the four residual cells as a minimum, because the sentence explicitly calls them initial and the marker is the only mention. The rule's literal wording favours a marker per number, so the caption placement is the cheap strengthening.
- BUG-7-R2-02 is the only trade-off left: the 2-page budget forced the cut that dropped the word count below the target.
- Report path: C:\Users\User\Downloads\project2\agents\detector\reports\ch7-risks-round2.md (round-1 report at C:\Users\User\Downloads\project2\agents\detector\reports\ch7-risks.md is untouched).

## Fixer round 2 status
| Bug ID | Status |
|---|---|
| BUG-7-R2-01 | fixed: [TO-VERIFY] added to table 7.2 caption (line 41). |
| BUG-7-R2-02 | not fixed (reason: 2-page budget; any addition of 2+ sentences pushed the directornote onto page 3. Only one short sentence "המטריצה מתעדכנת בכל אבן דרך." was added; still below the 298 floor, accepted trade-off). |
Build: ok, 0 Overfull, chapter = 2 pages (PDF 18-19).

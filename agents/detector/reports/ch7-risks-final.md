# Detector report – ch7-risks.tex – 2026-11-22
Summary: 0 critical, 3 medium, 2 minor. Words: 297/350 (body text, tables and figure excluded; lower bound 298). TO-VERIFY: 1.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-7-01 | D13 | 26 | medium | Hebrew word "והסיכון" sits between two \textenglish runs (R3 and R7); order may render reversed. Needs a visual check of the PDF crop at 300 dpi. Not auto-fixed. | No auto-fix. Visual check of the crop around "R3 והסיכון R7". |
| BUG-7-02 | D13 | 52 | medium | Hebrew word "והסיכון" sits between two \textenglish runs (R5 and R6). Same risk as BUG-7-01. | No auto-fix. Visual check of the crop around "R5 והסיכון R6". |
| BUG-7-03 | D9 | 5-52 | medium | Body word count is 297, just below the lower bound of 298 (350 -15%). Borderline. Tables and figure are excluded from the count. | Add about 10-20 words of body text, e.g. one sentence on how the scores were reached. |
| BUG-7-04 | wording | 23 | minor | The text calls the legal and platform risks "low probability, high severity". R6 (platform policy) has P=3 and I=3 in the table, so it does not fit that description. | Replace with: "הסיכונים המשפטיים והפלטפורמיים הם בעלי הסתברות נמוכה עד בינונית, וחומרתם בינונית עד גבוהה." |
| BUG-7-05 | wording | 28 | minor | "R4 קרוב לסף, כי חומרתו מרבית": R4 scores R=10, two points under the threshold. The reason given (maximal severity) does not explain the closeness; the probability is what keeps R low. | Replace "כי חומרתו מרבית" with "כי חומרתו מרבית, והסתברותו נמוכה" or drop the clause. |

## Checks passed (no hits)
- D1 BIDI: no unwrapped Latin text. The regex hits on lines 2, 4, 9, 12-18, 25, 32, 36, 41, 44-47 are LaTeX command names, not text.
- D2 BIDI-JOIN: no Hebrew inside \textenglish.
- D3 REF: tab:ch7-risks (line 5), fig:ch7-risk (line 26) and tab:ch7-mitigation (line 37) are all referenced.
- D4 CAPTION: table captions are above the tabular, figure caption is below the figure. Consistent with the chapter convention.
- D5 CITE: no \cite in this chapter.
- D6 VOICE: no first person outside directornote. The hit on line 55 is inside directornote and is allowed.
- D7 GENERIC: no hits.
- D8 TODO: 1 [TO-VERIFY] (line 52, R1 cost target). No FIGURE PENDING.
- D10 TERM: P, I, R are given Hebrew names on first use. Deepfake is transliterated (דיפ־פייק).
- D11 REQ: CH7-01 (P, I, R=P×I, critical at R≥12), CH7-02 (risk matrix, fig:ch7-risk), CH7-03 (mitigation, contingency, residual, tab:ch7-mitigation) are all covered. The seven risks match docs/concept.md line 74.
- Arithmetic: all R=P×I values in tab:ch7-risks are correct. The four critical risks (R1, R2, R3, R7) match the text. Residual R2 = 10 is the highest, as the text says. risks.json agrees with the table.
- D12 BUILD: build/main.log exists but is being rewritten by a concurrent build (its size grew from 61440 to 73728 bytes during this run). In the current snapshot there are no Overfull or Underfull warnings inside the ch7 span (log lines 2268-2333). Result is provisional until the other build finishes.

## Notes
- Risk scores (P, I, residual) are the team's assessment by design and were not checked against an external source.
- Scratch scripts for the word count and bidi scan are in C:\Users\User\AppData\Local\Temp\claude\725de2467d3c0a1a\2748b183-463d-4f81-88b2-b272365f9b1f\scratchpad\det\ (not in the project).

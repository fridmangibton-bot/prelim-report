# Detector report – ch6-workplan.tex – 2026-11-22
Summary: 1 critical, 0 medium, 0 minor. Words: 606/600. TO-VERIFY: 2.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-6-01 | D12 | 9 (input of figures/tikz/ch6_wbs.tex, error at its line 18) | critical | build/main.log (21:29, newer than the chapter and the TikZ file) shows "Undefined control sequence" and "Package pgfkeys Error: The key '/tikz/out' requires a value" at ch6_wbs.tex:18, from the Hebrew node text after `}` with no line break: `\textbf{חבילה 1}\ספר הסדרה...` (the same pattern repeats for packages 1-5). The Hebrew word after the backslash is read as a control sequence. Fix belongs to the TikZ file, not this chapter. | In figures/tikz/ch6_wbs.tex line 18 (foreach list), replace `}\` with `}\\` before each package name, e.g. `{\textbf{חבילה 1}\\ספר הסדרה ומודל הנתונים}`. Rebuild and confirm no new pgfkeys errors. |

Notes (not bugs):
- D1, D2, D3, D4, D5, D6 (only hit is inside directornote, line 60), D7, D13: no hits. All four labels have matching refs. Captions: figures below, tables above.
- D8: 2 [TO-VERIFY] markers (line 57: weekly available hours; line 60: number of test users).
- D9: 606 words against a 600 target, within ±15%.
- D11: CH6-01, CH6-02, CH6-03 and the must-contain list (5 WPs, RACI with one R and one A per row and the supervisor as A, 14-week Gantt, two milestones at weeks 7 and 14, reserve weeks 6 and 13) are all present. The text agrees with figures/python/data/gantt.json.
- D12: no Overfull hbox points to this chapter in build/main.log (the Overfull entries are in earlier chapters).

# Review fixes from the human page-by-page check (Adi, 2026-11-24)

> 30 findings. Most come from a few root causes, so fix the ROOT CAUSE first (section A, mostly in style/report.cls and the LTR macro), then the single items (section B).
> After all fixes: rebuild, run `pdftotext -layout build/main.pdf build/check.txt` and run the rendered-text checks in section C on the OUTPUT, not on the .tex files.

## A. Systemic fixes (one fix repairs many pages)

| ID | Root cause | Symptoms (PDF pages) | Fix |
|---|---|---|---|
| A1 | Bibliography is typeset right-to-left | 35A–36A: periods at line start, URLs broken and mixed into text, quotes rendered as ``...'' | Typeset the whole bibliography in an English/LTR environment (e.g. wrap \printbibliography in the class's English environment); load csquotes so quotes render correctly; allow URL line breaks |
| A2 | Tables are built left-to-right | 4A, 6A, 11A, 17A, 20A, 22A, 28A, 29A, 31A, 32A: first column on the LEFT; 28A–29A: item numbers on the wrong side ("ספר הסדרה 1.") | Make tables right-to-left in the class (first column on the right). Check the \headrow / \hcell macros and the fix from INC-003, which forced LTR drawing – it must apply to TikZ only, not to tabular |
| A3 | "--" ranges are not converted to an en dash in the Hebrew font | 1A, 3A, 15A, 29A, 35A and more: "2026--2034", "1--2" | Enable TeX ligatures (Ligatures=TeX) for the Hebrew fonts, or replace every "--" range with a Unicode en dash inside an LTR run, e.g. \textenglish{2026–2034} |
| A4 | English words are hyphenated inside Hebrew text | 2A "LongSto-ries.ai", "StoryA-gent"; 12A "diffu-sion"; 14A "Dra-maAgent" | Disable hyphenation inside the LTR macro (e.g. \hyphenpenalty=10000 / \mbox-like behaviour for short runs) |
| A5 | Spaces are lost next to LTR runs | 7A "visualizationconsistent", "consistencyconsistent"; 9A "2024CVPR", "2025ICCV 2025ICLR", "2026AACL"; 11A "2025ICLR , במה"; 12A "ConsiStoryStoryDiffusion"; 20A "דרךAPI"; 34A "R2R1" | Find the cause (macro eating the following space, or two LTR runs written back to back). Put each English unit (a name, a venue + year, a query) in ONE LTR run, and make sure a real space or comma separates runs. Example: \textenglish{CVPR 2024}, not "2024" + \textenglish{CVPR} |
| A6 | Parentheses split from their LTR content | 8A "(LCTtext Tuning )" (should be "Long Context Tuning (LCT)"); 12A "(IStion )"; 13A "(FreeNoise ו , SEINEStreamingT2V)" | Rule: Hebrew parentheses stay OUTSIDE the LTR run, and an English expression with its own parentheses goes entirely inside one LTR run: \textenglish{Long Context Tuning (LCT)}. Rewrite lists of English names as separate runs joined by Hebrew commas/vav |
| A7 | Footer progress strip says "פרק 8/8" in the references | 35A–36A | In the references (and front matter) show "מקורות" instead of a chapter counter |

## B. Single fixes

| Page | Fix |
|---|---|
| vii | Remove the empty page in the front matter |
| viii | Abbreviations table runs over the footer (SOM over the film strip, TAM below it): let it break across pages (longtable or split) and keep it above the footer |
| 3A | Remove the file name from the report text: "(בדיקת הצוות, נובמבר 2026)" only – no "docs/market-data.md" |
| 4A | Table 2.2, target column: the "≥" sign shows on the wrong side. Write targets in words: "לפחות 90%", "עד 10%", "לכל היותר 5 דולר" |
| 6A | ".env" renders as "env." – wrap it in the LTR macro |
| 11A | Table 3.1 font is too small: no font below 9 pt – split the table into two or rotate it to a landscape page |
| 16A | The price paragraph is garbled. Rewrite it as one short sentence per product, each price inside one LTR run, e.g. "LTX Studio: \textenglish{Lite \$15, Standard \$35, Pro \$125}" – or move the prices into Table 4.1 and refer to it |
| 16A | Hebrew quotes rendered as ``...'': use Hebrew gershayim (״...״) |
| 17A | The date "21-22.11.2026" breaks across lines: make it unbreakable and LTR |
| 18A–19A | Chart legends: stray space inside parentheses "(יעד תכנון )", "( ידני)" – fix the label strings in make_figures.py |
| 26A, 33A | Near-empty pages at the end of ch5 and ch7: improve float placement (a box or figure is being pushed to its own page); a short page at the very end of a chapter is acceptable, a page with 2 lines plus a box is not |
| 28A | "'סטודנטית א" → use the Hebrew geresh: "סטודנטית א׳" (U+05F3), also anywhere else |
| 32A | Figure 7.1 (risk matrix): labels too small – enlarge fonts in make_figures.py to at least the body-text size when printed |
| 34A | "R3, R2R1 ו־R7" → "R1, R2, R3 ו־R7" |

## C. Rendered-text checks (new detector check D15 – add it to the detector SKILL.md)

The detector missed these because it checked the .tex source, not what the reader sees. After building, run checks on `build/check.txt` (pdftotext output):
- `--` anywhere → bug
- two Latin words glued together: a lowercase letter immediately followed by an uppercase letter in the middle of a word (e.g. "StoryDiffusion" is a real name, so list hits for a human decision rather than auto-fixing)
- a digit glued to a Latin word: `[0-9][A-Z]{2,}` or `[A-Z]{2,}[0-9]{4}` without a space (e.g. "2024CVPR")
- `` ` `` or `''` characters → bug
- a Latin word split by a hyphen at a line end
- "(" or ")" directly next to a space inside parentheses: `\( | \)`
- `TO-VERIFY` or `??` → bug

## D. Incident log

Add INC-008 to docs/incidents.md: "A human page-by-page review found 30 rendering bugs that the detector missed (bibliography direction, table direction, en dashes, hyphenated English, lost spaces, split parentheses). Root cause: the detector only read the .tex source, and most BiDi bugs appear only in the rendered PDF. Fix: systemic fixes A1–A7 in the class and the LTR macro, plus a new rendered-text check D15 on pdftotext output. Lesson: a human review of the real PDF is a required step, not an optional one."

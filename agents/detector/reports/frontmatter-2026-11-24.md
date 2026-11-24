# Detector report – frontmatter (titlepage, abstract, abbreviations) – 2026-11-24
Summary: 0 critical, 1 medium, 1 minor. Words: 327/250-350 (executive summary; 335 if maqaf-joined words are split). TO-VERIFY: 0.

Scope: checks D1, D2, D3, D12, D15 only. Inputs: `frontmatter/titlepage.tex`, `frontmatter/abstract.tex`, `frontmatter/abbreviations.tex`, `build/main.log`, `build/check.txt` (pdftotext -enc UTF-8 -layout, build of 2026-11-24 17:12).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-FM-01 | D12 (warning, not Overfull) | abbreviations.tex:24 (longtable, PDF pages 6-8) | medium | LaTeX warning "Infinite glue shrinkage found in box being split" at this table, plus loose alignment lines "Underfull \hbox (badness 10000) in alignment at lines 9--24" in the same table. Not an Overfull hbox, so it is not a D12 error by the skill definition, but it points to this front-matter file and the table rows may be stretched. Needs a visual check. | None mechanical. Render pages 6-8 at 300 dpi and check the table rows; if a row is stretched or split badly, shorten the definition text in the offending row or allow the column to break (`\raggedright` in `p{}` columns). |
| BUG-FM-02 | D15 (outside the four critical rules; not in the skill's rule list) | titlepage.tex:10,16,20; abstract.tex:5 and all pages | minor | pdftotext maps every Hebrew nun (נ) to U+F8FF (private-use glyph), e.g. "אויברסיטת" for "אוניברסיטת". The glyphs render correctly (checked visually on page 2: "נאמד", "לניהול"), so this is only a text-extraction defect: copy/paste, search and screen readers will see wrong text. It affects the whole document (about 1,000 occurrences), not only the front matter. | None in front matter. Check the font's ToUnicode mapping for the nun glyph (Hebrew font in `style/report.cls`). Not a visible bug; decide with the owner whether to fix. |

## Checks with no hits in the front matter
- D1 BIDI: no unwrapped Latin runs. The only flagged tokens were `toc` and `chapter` inside `\addcontentsline{toc}{chapter}` (command arguments, false positive).
- D2 BIDI-JOIN: no `\textenglish{}` run contains a Hebrew letter.
- D3 REF: no `\label`, `\ref` or `\cite` in the three files, so nothing is unmatched.
- D12 BUILD: no `^!` errors in `build/main.log`; zero Overfull hboxes in the whole log. Only the warning in BUG-FM-01 points to these files.
- D15 RENDERED-TEXT: `scripts/d15_check.py build/check.txt` reports 3 hits in the whole document, none on front-matter pages. Their locations: check.txt line 847 (PDF page 21, space inside parentheses, body chapter, out of scope for this report); check.txt lines 1793 and 1842 (PDF pages 43-44, digit glued to Latin in the references: report ID FBI110060 and DOI 10.1109/ICCV51701.2025.01605, which the skill says to ignore).

## Executive summary word count
- `frontmatter/abstract.tex` body between `\chapter*{תקציר מנהלים}` and `\section*{מילות מפתח}`: 327 whitespace-delimited words (after unwrapping `\textenglish{}`), 335 if maqaf-joined Hebrew words are counted as two. Both are inside 250-350.

## Notes for the caller
- Title page, abstract and abbreviations all fit on their pages in the build; no overfull boxes.
- The front matter contains no `[TO-VERIFY]` markers and no "FIGURE PENDING" text.
- Not checked (out of the requested scope): D13 on the title page (line 20 has `ו־\mbox{\textenglish{Vibe Coding}}`, which the D13 grep pattern does not match directly but is the same family of risk; a visual check of the title page would settle it).

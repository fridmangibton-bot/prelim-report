# Detector report – ch3-literature – 2026-11-21
Summary: 2 critical, 11 medium, 6 minor. Words: ~1,484/2,000 (prose only; target range 1,700–2,300). TO-VERIFY: 5.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch3-01 | D11 (CH3-04) | 86 | critical | Flagship model equations not presented: the two loss functions are only a [TO-VERIFY] placeholder. Requirement CH3-04 (equations) is not met. | Read zhao2025moviedreamer, write both loss functions in full (numbered, STY-03). Until then keep the marker. |
| BUG-ch3-02 | D11 (CH3-04) | 88 | critical | Experimental environment missing: datasets, metrics, hardware and numeric results are all a [TO-VERIFY] placeholder. CH3-04 requires the experimental setup. | Fill from the paper after full read; delete the "סביבת הניסוי" placeholder only when each item is sourced. |
| BUG-ch3-03 | D13 (BIDI-ORDER) | 4 | medium | "(\textenglish{StoryAgent} ו־\textenglish{VideoDirectorGPT})": Hebrew conjunction with maqaf between two LTR runs. The stale PDF (build/main.pdf, p.14) shows the pair out of order. | No auto-fix (INC-001). Visual check at 300 dpi after a clean build. If reversed, split the parenthesis into two sentences so no Hebrew word sits between the two runs. |
| BUG-ch3-04 | D13 (BIDI-ORDER) | 8 | medium | "בדף ה־\textenglish{arXiv}": maqaf-joined prefix directly before an LTR run. | Visual check at 300 dpi. No mechanical fix. |
| BUG-ch3-05 | D13 (BIDI-ORDER) | 8 | medium | "\textenglish{IEEE} ו־\textenglish{ACM}" inside the TO-VERIFY marker: Hebrew conjunction between two LTR runs. | Visual check at 300 dpi; the marker text can be reworded so the runs are not adjacent to a prefix. |
| BUG-ch3-06 | D13 (BIDI-ORDER) | 8 | medium | "\textenglish{arXiv} ביום \textenglish{21.11.2026}": single Hebrew word between two LTR runs. | Visual check at 300 dpi. |
| BUG-ch3-07 | D13 (BIDI-ORDER) | 55 | medium | "בכנס או ב־\textenglish{arXiv}": maqaf-joined prefix before an LTR run. | Visual check at 300 dpi. |
| BUG-ch3-08 | D13 (BIDI-ORDER, range) | 4 | medium | "\textenglish{2023}--\textenglish{2025}": the year range sits between Hebrew text and has no Hebrew word between runs, but the stale PDF (p.14) shows it rendered as "20252023--". | Write the range as one run: \textenglish{2023--2025} and check the 300 dpi crop. |
| BUG-ch3-09 | D9 BUDGET | 1–107 | medium | Prose is about 1,484 words, 26% under the 2,000 target (±15% = 1,700–2,300). Count excludes figure, matrix table and TO-VERIFY markers. Method: detex-like strip of commands, then whitespace/hyphen split. | Add roughly 220–300 words of substance (e.g. the experiment-setup and equations once read, and a fuller comparison paragraph in 3.1.5). |
| BUG-ch3-10 | FIG (legibility) | 20 | medium | Figure node "סיפור מרובה סוכנים": \textenglish{VideoDirectorGPT} is hyphenated mid-word ("VideoDi-" / "rectorGPT") in the 2.9 cm text width. Visible in build/main.pdf p.14. Other figure text is legible and arrows run right-to-left. | Use \mbox{\textenglish{VideoDirectorGPT}} inside the node and set text width=3.3cm for the box style (line 15). Centres are 4.2 cm apart, so widths up to about 3.5 cm do not overlap. |
| BUG-ch3-11 | READ-FACT | 49 | medium | Uncited claim about the third family: "התכנון נוצר מחדש בכל הרצה, ואין מבנה נתונים שנשאר בין הרצות" (VideoDirectorGPT, StoryAgent). No source and no [TO-VERIFY]. Also "ולכן היא זולה להפעלה" (ConsiStory) is an unsourced inference. | Add a citation to the specific paper that supports it, or mark [TO-VERIFY] and soften to "לפי תיאור המאמר". |
| BUG-ch3-12 | READ-FACT | 88 | medium | "המאמר מדווח על השוואה למערכות קיימות במדדי עקביות וקוהרנטיות": a claim about zhao2025moviedreamer with no citation and no [TO-VERIFY] flag on this sentence. | Add \cite{zhao2025moviedreamer} and confirm after reading the paper, or mark [TO-VERIFY]. |
| BUG-ch3-13 | READ-FACT / consistency | 90 | medium | "המאמר גם אינו מתמודד עם קלט, קול וכתוביות בעברית. אלה בדיוק שלושת הממדים שהפרויקט מוסיף": claim about the paper's scope is uncited, and the "three dimensions" do not match the three gap components used in lines 93 and 106 (זיכרון עלילה, זיהוי סתירות, עברית). concept.md line 38 lists input, voice and subtitles as the Hebrew-first dimension. | Rephrase so the three dimensions match the gap list (episodes/memory, contradiction detection, Hebrew); add a citation or [TO-VERIFY] for the scope claim. |
| BUG-ch3-14 | Gap sentence (verbatim) | 102 | minor | Not verbatim with docs/sources.md line 18: the chapter uses maqaf U+05BE in "קצה־לקצה", the source uses ASCII hyphen "קצה-לקצה". Words and punctuation are otherwise identical (251 characters each). | Pick one authority. Recommended: change docs/sources.md line 18 to the maqaf form (correct Hebrew typography). Alternatively change ch3 line 102 to "קצה-לקצה". Caller decides. |
| BUG-ch3-15 | D13-adjacent (typography) | 41 | minor | "\textenglish{StoryAgent}" breaks as "Sto-/ryAgent" across lines in the stale PDF (p.15). English term broken mid-word. | Wrap as \mbox{\textenglish{StoryAgent}}. |
| BUG-ch3-16 | STY-06 / quotes | 41 | minor | Straight ASCII quotes in "כ\"במאי\"": not the Hebrew gershayim and not the LaTeX `` '' convention used on line 55. | Replace with ״במאי״ (or ``במאי''). |
| BUG-ch3-17 | D10 | 19, 36 | minor | "LCT" appears in the figure (line 19) before any text introduces it. "Long Context Tuning" (line 36) is given no Hebrew gloss or short form on first use. | In line 36 write "\textenglish{Long Context Tuning} (\textenglish{LCT})" on first mention; the figure label is acceptable after that. |
| BUG-ch3-18 | READ-FACT (rhetoric) | 104 | minor | "יוצר שמפיק סדרה ארוכה נתקל בסתירות עלילתיות הרבה לפני שהוא נתקל בדמות שמשנה את פניה" is an unsourced generalisation presented as fact. | Soften ("לעיתים קרובות") or mark [TO-VERIFY] / cite a practitioner source if one is added to docs/sources.md. |
| BUG-ch3-19 | READ-FACT (sourcing) | 46 | minor | "LongStories.ai שומר על צוות הדמויות, על הקולות ועל העולם בין פרקים": docs/market-data.md confirms series and consistent characters, but not voices or world. Only the note in docs/sources.md supports "קולות". | Confirm "קולות" and "עולם" on the public page (sources.md line 4 verification date), then keep; otherwise trim to "צוות הדמויות". |

## Verification results (no bug unless listed above)
- Cites (D5): all 15 cite keys present in bib/references.bib and in docs/sources.md, including longstories (listed in the competitor section of the whitelist). No cite outside the whitelist.
- Knowledge-gap sentence: present at line 102, one sentence, matches sources.md except the dash (BUG-ch3-14). The "no product keeps characters" claim is not made: line 46 only says the report will not claim it, and line 102 says "לעיתים גם בין פרקים" for existing products. Pass.
- D1 BIDI: no Latin letter outside \textenglish in Hebrew prose. The only Latin hits are inside [TO-VERIFY] markers and TikZ syntax. Pass.
- D2: no Hebrew inside \textenglish. Pass.
- D3: fig:ch3-families, tab:ch3-matrix, sec:ch3-flagship, sec:ch3-gap all referenced. sec:ch3-matrix (line 54) is not referenced in this chapter (not a D3 bug; only a label). Pass.
- D4: figure caption below the TikZ picture (line 26); table caption above the tabular (line 59). Pass.
- D6, D7: no first-person voice outside directornote (line 97 "שלנו" is inside directornote, allowed); no generic openings. Pass.
- D8: 5 [TO-VERIFY] markers (lines 8, 55, 81, 86, 88). No "FIGURE PENDING".
- D10: "StoryDiffusion", "Intelligent Grimm", "preprints", "observer", "LLM" have Hebrew or parenthetical glosses where needed. Only BUG-ch3-17 remains.
- D11 (other CH3 rows): CH3-01 thematic structure, CH3-02 matrix with empty gap columns (lines 62–71), CH3-03 four criteria (line 79), CH3-05 one-sentence gap (line 102) met. CH3-04 partly unmet (BUG-ch3-01/02). CH3-06: verification date stated (line 8); each source is in sources.md as verified. The REQ IDs used (REQ-CHR-01, REQ-NAR-01, REQ-LNG-01) exist in docs/concept.md and chapters/ch2-problem.tex; they are not in docs/requirements.md, which only holds CH2/CH3/STY rows.
- Figure (inline TikZ, lines 12–28): present. Right-to-left flow (family 1 on the right, gap on the left, arrows point left). Text in nodes is RTL via the class fix (style/report.cls line 84). Legibility problem only at the VideoDirectorGPT hyphenation (BUG-ch3-10).
- Stale PDF (build/main.pdf, pages 14–15) was viewed as the only available render. It reflects an earlier build and may not match the current .tex.

## Build status (D12)
- build/main.log is truncated: it ends mid-line in the front matter ("Underfull \hbox ... in paragraph a"), build/main.aux is 0 bytes and build/main.toc is 0 bytes. There is no "Output written" line and no final error summary. The log cannot be used to confirm or clear chapter 3.
- The captured part of the log has no "^!" errors and no Overfull hbox for ch3. Warnings present are in abstract/TOC (Underfull) and biblatex "Language 'hebrew' not supported" (not chapter-specific).
- Recommended action for the caller (not run by this detector): a clean `bash scripts/build.sh` by the lead, then re-check D12 and the 300 dpi crops for BUG-ch3-03 to 08.

## Notes for caller
- Detector did not edit chapters/ch3-literature.tex and did not run scripts/build.sh.
- D13 bugs follow the skill rule (medium, visual check, no auto-fix). INC-001 says the source order renders correctly in RTL; the stale PDF crop on p.14 still reads "StoryAgent ר־VideoDirectorGPT", so the 300 dpi check is needed.

## Fixer status (2026-11-21)
| Bug ID | Status |
|---|---|
| BUG-ch3-01 | needs input (paper not in docs/; [TO-VERIFY] kept, safe prose added) |
| BUG-ch3-02 | needs input (paper not in docs/; [TO-VERIFY] kept; unsourced "comparison" claim replaced by a cited focus statement) |
| BUG-ch3-03 | fixed (sentence split, no Hebrew word between LTR runs; 300 dpi check OK) |
| BUG-ch3-04 | fixed (reworded to "במאגר arXiv"; 300 dpi check OK) |
| BUG-ch3-05 | fixed (marker reworded, IEEE/ACM removed; 300 dpi check OK) |
| BUG-ch3-06 | fixed (date clause reworded; 300 dpi check OK) |
| BUG-ch3-07 | fixed (reworded; no maqaf prefix) |
| BUG-ch3-08 | fixed (\textenglish{2023--2025}; renders 2023-2025 correctly) |
| BUG-ch3-09 | fixed in part (about 300 words added from sources.md facts; word count not re-measured, may still be near the 1,700 floor) |
| BUG-ch3-10 | fixed (\mbox + text width 3.3cm; renders on one line) |
| BUG-ch3-11 | fixed (cited + [TO-VERIFY], "זולה" removed) |
| BUG-ch3-12 | fixed (cited, softened) |
| BUG-ch3-13 | fixed (three dimensions match gap list; cite + [TO-VERIFY]) |
| BUG-ch3-14 | fixed (chapter now uses the ASCII hyphen exactly as docs/sources.md) |
| BUG-ch3-15 | fixed (\mbox) |
| BUG-ch3-16 | fixed (gershayim) |
| BUG-ch3-17 | fixed (LCT introduced in text) |
| BUG-ch3-18 | fixed (softened) |
| BUG-ch3-19 | fixed (trimmed to cast only) |

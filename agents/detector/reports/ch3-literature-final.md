# Detector report – ch3-literature – 2026-11-22
Summary: 2 critical, 5 medium, 2 minor. Words: 1,697/2,000 (target range 1,700–2,300). TO-VERIFY: 7.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch3-01 | D11 (CH3-04) | 88 | critical | Flagship model equations not presented. Both loss functions are only a [TO-VERIFY] placeholder; CH3-04 requires the equations. | Read zhao2025moviedreamer, write both loss functions in full (numbered). Keep the marker until then. Input needed: paper not in docs/. |
| BUG-ch3-02 | D11 (CH3-04, CH3-03) | 90 | critical | Experimental environment missing: datasets, metrics, hardware and numeric results are all [TO-VERIFY]. CH3-03 (quantitative metrics, repeatability) and CH3-04 (experimental setup) are therefore unmet. | Fill from the paper after full read; each item must carry its source. Input needed. |
| BUG-ch3-03 | D13 (BIDI-ORDER) | 51 | medium | "ו־\textenglish{CVPR}" in "ו־\textenglish{CVPR}": Hebrew prefix joined by maqaf directly before an LTR run. | Split line 51 into one sentence per venue, and write the conjunction with a space, not a maqaf: "ו \textenglish{CVPR}". Visual check at 300 dpi (no mechanical guarantee, INC-001). |
| BUG-ch3-04 | D13 (BIDI-ORDER) | 51 | medium | "ו־\textenglish{ICLR}": Hebrew prefix joined by maqaf directly before an LTR run. | As BUG-ch3-03: separate sentence, conjunction with a space. Visual check at 300 dpi. |
| BUG-ch3-05 | D13 (BIDI-ORDER, between runs) | 51 | medium | A Hebrew word between two LTR runs, three times: "\textenglish{2024} עבור \textenglish{StoryDiffusion}", "\textenglish{2024} עבור \textenglish{ConsiStory}", "\textenglish{2024} עבור \textenglish{Intelligent Grimm}". The order can render reversed. | Rewrite the venue list without a Hebrew word between runs, e.g. one sentence per paper ("\textenglish{StoryDiffusion} פורסם ב\textenglish{NeurIPS} 2024"), or a parenthetical list. Visual check at 300 dpi. |
| BUG-ch3-06 | D9 BUDGET | 1–107 | medium | Prose is 1,697 words by scripts/wordcount.py (1,632 Hebrew), 3 words below the 1,700 floor of the ±15% range for the 2,000 target. | Add at least 100 words of substance (for example, the setup and equations once read, or a fuller comparison in 3.5). Re-count with scripts/wordcount.py. |
| BUG-ch3-07 | D12 (BUILD) | 17–26, 41–42, 51–52, 57–58, 90–91, 96–97 | medium | build/main.log (read during the run, while another process was rewriting it; it was 0 lines at one check and 2,212 lines at the next) lists 8 Overfull \hbox entries inside the ch3 span (log lines 1851–1932): 18.18pt (lines 17–26), 12.89pt (41–42), 2.14pt, 1.42pt, 0.35pt, 4.46pt (57–58), 5.04pt (90–91), 2.69pt (96–97). No "!" errors in ch3. The log may predate the current text, so line numbers are unverified. | Re-check after the other build finishes. Fix the 12.89pt and 18.18pt boxes first (long unbreakable LTR runs; check the figure text at lines 17–26). |
| BUG-ch3-08 | D10 | 19 (figure) | minor | "LCT" appears in the figure (line 19) before the text introduces it (line 36: "Long Context Tuning (LCT)"). | Acceptable as is, but the first textual mention (line 36) is the place to gloss it; no change needed unless the figure is moved. |
| BUG-ch3-09 | READ-FACT | 106 | minor | "יוצר שמפיק סדרה ארוכה עלול להיתקל בסתירות עלילתיות לא פחות מאשר בדמות שמשנה את פניה" is an unsourced generalisation about practitioners. | Soften ("לעיתים קרובות") or mark [TO-VERIFY], or cite a source once one is added to docs/sources.md. |

## Verification results (no bug unless listed above)
- D1 BIDI: no Latin letter outside \textenglish in Hebrew prose. Pass.
- D2: no Hebrew inside \textenglish. Pass.
- D3: fig:ch3-families, tab:ch3-matrix, sec:ch3-flagship, sec:ch3-gap are referenced. sec:ch3-matrix is a section label, not a fig/tab label, so D3 does not apply. Pass.
- D4: figure caption below the tikzpicture (line 26); table caption above the tabular (line 61). Pass.
- D5: all 8 cite keys (zhou2024storydiffusion, tewel2024consistory, liu2024grimm, guo2025lct, zhao2025moviedreamer, lin2023videodirectorgpt, hu2024storyagent, longstories) are in bib/references.bib and docs/sources.md. Pass.
- D6: first person only inside directornote (line 99). Pass.
- D7: no generic openings. Pass.
- D8: 7 [TO-VERIFY] markers (lines 8, 49, 57, 83, 88, 90, 92). 0 "FIGURE PENDING". Info only.
- D10: other English terms are glossed on first use (preprints, LLM, observer, Consistent Self-Attention). Only BUG-ch3-08 remains.
- D11 other rows: CH3-01 thematic (sections 3.1–3.5), CH3-02 matrix with empty gap columns (lines 65–74, 76), CH3-03 venue and proximity (line 83), CH3-05 one-sentence gap (line 104), CH3-06 verification date and sources (line 8, sources.md). Figure present (lines 12–28). The four REQ IDs used (REQ-CHR-01, REQ-NAR-01, REQ-LNG-01) exist in docs/concept.md.
- Knowledge-gap sentence (line 104): verbatim match with docs/sources.md line 18 (ASCII hyphen in "קצה-לקצה" in both). Pass.
- Sources: no claim about a paper that contradicts its sources.md row (venues: NeurIPS 2024, SIGGRAPH 2024, CVPR 2024, ICCV 2025, ICLR 2025; preprints StoryAgent and VideoDirectorGPT disclosed in line 4). Pass.

## Notes for caller
- Detector did not edit chapters/ch3-literature.tex and did not run scripts/build.sh.
- Fixer status from the previous round (ch3-literature.md) is not re-checked here; this report is a fresh pass over the current text.

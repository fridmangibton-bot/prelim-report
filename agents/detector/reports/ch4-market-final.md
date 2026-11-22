# Detector report – ch4-market.tex – 2026-11-22
Summary: 0 critical, 3 medium, 0 minor. Words: 837/1100 (range 935–1265). TO-VERIFY: 5.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-4-01 | D9 | 5–70 | medium | Word count is 837, below the 1100 ±15% target range (935–1265), about 24% under target. Method: LaTeX commands stripped, table cells and captions included; detex not run. | Add about 100–130 words of content to the sections, not mechanical. Candidate: a short paragraph in 4.3 or 4.5 on what the radar and scatter scores do not show. |
| BUG-4-02 | D10/read (count consistency) | 25 | medium | "המתחרה הרביעי" conflicts with the chapter's own count. Line 19 has four AI tools plus one manual process, and line 22 lists five products. In that order the manual process is the fifth competitor, not the fourth. | \textenglish{...} not applicable: replace "הוא המתחרה הרביעי" with "הוא המתחרה החמישי" (confirm the intended count first). |
| BUG-4-03 | read (fact vs. source) | 46 (table row "וידאו מקצה לקצה", flagship column) | medium | The flagship column is marked "לא" for end-to-end video, but sources.md describes MovieDreamer as multimodal script input with diffusion rendering, which produces video. The cell may be wrong or the definition of "end-to-end" in the table needs a note. | Verify against the paper. If it renders video from script, change the cell to "כן" and keep the "סדרה ופרקים" cell as is. Otherwise add a table note. |

## Checks with no bug found
- D1 BIDI: no Latin run outside \textenglish{} in Hebrew lines (scripted check, TO-VERIFY and command arguments excluded).
- D2 BIDI-JOIN: no Hebrew letter inside \textenglish{}.
- D3 REF: labels tab:ch4-compare, fig:ch4-radar, fig:ch4-scatter are each referenced (lines 28, 50, 60).
- D4 CAPTION: table caption (line 32) is above the tabular (line 35). Figure captions are below the figures, the standard position; no rule violated.
- D5 CITE: all 8 keys used (atlabs, capcut, fbi2026aivideo, longstories, ltxstudio, mnm2023t2v, openart, zhao2025moviedreamer) exist in bib/references.bib and docs/sources.md.
- D6 VOICE: 2 grep hits, both not first person: line 25 "נעשה ביד" and line 42 "נבנה" are passive or third-person. Line 73 is inside directornote, which allows "שלנו". No bug.
- D7 GENERIC: no hits.
- D8 TODO: 5 [TO-VERIFY] markers (line 25: 1; line 37: 2; line 70: 2). 0 "FIGURE PENDING". The SAM/SOM "team assumption" labels were not flagged, per instruction.
- D11 REQ: CH4-01 (TAM/SAM/SOM with CAGR and sources; SAM/SOM labelled as team estimate), CH4-02 (4 AI competitors plus manual process), CH4-03 (comparison table, lines 35–44), CH4-04 (radar with 6 axes at line 50, scatter at line 60). All present. Arithmetic checked: 100,000 × 25 × 12 = 30M, which is about 3.5% of 847M; 0.5% × 100,000 = 500 users; 500 × 300 = 150,000. All correct.
- D12 BUILD: build/main.log exists (modified 2026-11-22 21:28) but has no entries for ch4-market.tex. Its file opens stop at ch3 and the tail shows errors in figures/tikz/ch6_wbs.tex (undefined Hebrew control sequences). The log looks incomplete or from a build in progress, so ch4 could not be checked. No ch4 error or overfull hbox found in it. Not a build run, per instructions.
- D13 BIDI-ORDER: no maqaf or prefix pattern adjacent to \textenglish{} runs.
- Table structure: all 7 rows have 8 cells, matching the 8 columns. The macros \headrow, \hcell, \rowrule and directornote are defined in style/report.cls.
- Facts checked against docs/market-data.md and docs/sources.md: prices (LTX 35, OpenArt 14, LongStories 59, Atlabs 19 flagged, CapCut 19.99 flagged), Hebrew support (Atlabs paid only), OpenArt starter has no commercial license, and the market figures (716.8M, 847M, 3,350M, 18.8%, 41%, 0.9B 2027, 37.1%). All consistent.

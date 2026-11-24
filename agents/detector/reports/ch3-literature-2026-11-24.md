# Detector report – ch3-literature – 2026-11-24
Summary: 2 critical, 5 medium, 3 minor. Words: ~2,650/2,000. TO-VERIFY: 0.

Scope: chapters/ch3-literature.tex (168 lines). Rendered-text check on build/check.txt (fresh build). LTR runs wrapped in \mbox and RTL tables were not reported, as instructed.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-3-01 | D11 (content) | 155 (also 39) | critical | Line 155 says MovieDreamer is the only candidate that combines peer review, closeness to the problem and plot planning. The chapter itself contradicts this: line 48 calls DramaAgent "the most recent and closest work", line 56 places it at AACL 2026 (peer reviewed), and the matrix (line 87) gives it plot-state tracking. Line 39 ("the closest to the problem") has the same conflict. | Writer decision. Rewrite line 155 and line 39 around the real differentiator (MovieDreamer's planning/rendering split), or change the flagship. |
| BUG-3-02 | D11 (content) | 116, 118 | critical | Replicability is one of the four selection criteria (line 116). Line 118 states that MovieDreamer fails it (code not public). It is still chosen as the flagship, and the three reasons given in line 118 do not include the criterion. DramaAgent and StoryDiffusion pass it. | Writer decision. Either state explicitly that the flagship is chosen despite failing criterion four and justify it, or revisit the selection. |
| BUG-3-03 | consistency (figure) | 21-27 (fig:ch3-families) | medium | The figure has 7 nodes. DramaAgent, which line 48 calls the closest work and line 56 places in the third family, is missing from the "סיפור מרובה סוכנים" node. The matrix has 8 rows. | Line 23: replace `\mbox{\textenglish{VideoDirectorGPT}}, \textenglish{StoryAgent}` with `\textenglish{VideoDirectorGPT}, \textenglish{StoryAgent}, \textenglish{DramaAgent}` and check that the box still fits. |
| BUG-3-04 | consistency (matrix) | 70 vs 83 | medium | Line 70 says the partial mark for VideoDirectorGPT reflects consistency groups. In the matrix row (line 83) the partial mark sits in the "מעקב מצב עלילה" column, and the consistency column is "כן". | Reword line 70 to match the column, e.g. replace "ב־\textenglish{VideoDirectorGPT} הוא משקף קבוצות עקביות" with "ב־\textenglish{VideoDirectorGPT} הוא משקף מצב עלילה שנבנה מחדש בכל הרצה" (consistent with line 63). |
| BUG-3-05 | consistency (cross-chapter) | 163 vs ch4 lines 22, 27 | medium | Line 163 says "ואף אחד אינו נגיש ליוצרים בעברית" (no solution is accessible to Hebrew creators). Chapter 4 reports Atlabs with Hebrew on paid plans (line 22) and CapCut with a Hebrew UI (line 27). The sentence reads as a contradiction. The same wording is in docs/sources.md line 19. | Replace "ואף אחד אינו נגיש ליוצרים בעברית" with "ואין פתרון שמנהל זיכרון עלילתי בעברית" in line 163, and update docs/sources.md line 19 to match. |
| BUG-3-06 | D9 BUDGET | whole chapter | medium | About 2,650 words (prose, tables, figure, equations and captions excluded; English runs counted; headings included). Target 2,000 +/-15% (1,700-2,300), so about 15% over the upper bound. | Trim about 350 words, mainly from the comparison section (lines 53-58) and the per-paper list (lines 61-63), which repeat the family summaries. |
| BUG-3-07 | D10 TERM | 121, 133 | medium | First use without a Hebrew description or parenthetical: "מפענח מבוסס על SDXL" (121), "מודל תמונה־לוידאו (SVD)" (121), "ציון CLIP" and "מרחק FID" (133). | Line 121: `\textenglish{SDXL} (\textenglish{Stable Diffusion XL})`; `(\textenglish{Stable Video Diffusion})` in place of `(\textenglish{SVD})`. Line 133: `ציון \textenglish{CLIP} (\textenglish{Contrastive Language-Image Pretraining})` and `מרחק \textenglish{FID} (\textenglish{Fréchet Inception Distance})`. |
| BUG-3-08 | wording | 91 | minor | Says the last two matrix columns are "ריקות בכל השורות" (empty in every row). Their cells contain "לא". | Replace "ריקות בכל השורות" with "לא מסומנות באף שורה". |
| BUG-3-09 | citation (tab:ch3-code) | 108, 109 | minor | Row "LCT" gives "שלושה מיליארד פרמטרים" with no \cite. Row "StoryAgent" states the release plan with no \cite. CLAUDE.md requires a source or [TO-VERIFY] for numbers. The 3B figure is not in docs/sources.md. | Add \cite{guo2025lct} to the LCT note and \cite{hu2024storyagent} to the StoryAgent note, after confirming the 3B figure in the source; otherwise mark it [TO-VERIFY]. |
| BUG-3-10 | D3 (info) | 69 | minor | Label sec:ch3-matrix has no \ref. D3 covers fig/tab labels only, so this is informational. | Add a reference to the section, or remove the label. |

Checks with no hits in chapter 3:
- D1: no unwrapped Latin runs in Hebrew lines (tikz and tabular bodies excluded).
- D2: no Hebrew inside \textenglish{}.
- D3: all fig/tab labels are referenced (fig:ch3-families, tab:ch3-matrix, tab:ch3-code, tab:ch3-moviedreamer).
- D4: figure caption below the figure (line 29); table captions above the tabulars (lines 74, 97, 137).
- D5: all 9 cite keys are present in bib/references.bib and docs/sources.md.
- D6: no first-person voice. The line 127 match is a false positive ("אני" inside "גאוסיאנית"). The line 158 "בפרויקט שלנו" is inside directornote, which is allowed.
- D7: none.
- D8: TO-VERIFY 0, FIGURE PENDING 0.
- D12: no Overfull hbox in the chapter 3 part of build/main.log (lines 1952-2022). Underfull hbox warnings (badness 10000 at paragraph lines 2, 8-9, 39-40, 44-45, 56-57) are not in the skill's severity table; not counted.
- D13: none (LTR runs excluded per instruction).
- D15: 0 hits in chapter 3. The two hits in build/check.txt (lines 1793 and 1842) are a report ID and a DOI in the references, excluded by the rule.
- D11 (requirement IDs): REQ-CHR-01, REQ-NAR-01 and REQ-LNG-01 appear in ch2 and docs/concept.md, not in docs/requirements.md. Not a bug in this chapter.

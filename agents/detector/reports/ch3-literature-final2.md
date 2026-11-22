# Detector report – ch3-literature.tex – 2026-11-22
Summary: 1 critical, 10 medium, 4 minor. Words: ~2430/n.a. (no word target in agents-setup section 0; page budget 9). TO-VERIFY: 5.

Scope: chapters/ch3-literature.tex only. No build was run. build/main.log was read only. Checks: D1–D13 plus CH3-01..06, STY-04/05, REQ IDs in concept.md. The MovieDreamer code-availability TO-VERIFY (line 94) is intentional and is not a bug.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch3-01 | D5 / unsourced number | 124 | critical | Numbers 19.520 (CLIP) and 0.704 (CLIP similarity), the claim "tens of minutes and even hours", and the baselines StreamingT2V, SEINE, FreeNoise have no \cite and no [TO-VERIFY] | Add \cite{zhao2025moviedreamer} only if that paper reports these values, otherwise append [TO-VERIFY: ערכי ההשוואה לוידאו ארוך] to the sentence |
| BUG-ch3-02 | D13 BIDI-ORDER | 54 | medium | Maqaf prefix "ו־" directly before \textenglish{CVPR} and \textenglish{ICLR}; Hebrew word "עבור" between several runs | Do not auto-fix. Visual check of PDF crop at 300 dpi |
| BUG-ch3-03 | D13 BIDI-ORDER | 64 | medium | "ל־" before \textenglish{MovieDreamer}; "ול־" before \textenglish{VideoDirectorGPT}; "ל־" before \textenglish{StoryAgent} | Do not auto-fix. Visual check of PDF crop at 300 dpi |
| BUG-ch3-04 | D13 BIDI-ORDER | 109 | medium | "ביחס ל־" before \textenglish{StoryDiffusion}; "ו־" before \textenglish{FID} | Do not auto-fix. Visual check of PDF crop at 300 dpi |
| BUG-ch3-05 | D13 BIDI-ORDER | 113 | medium | Table caption: "ו־" before \textenglish{StoryGen} | Do not auto-fix. Visual check of PDF crop at 300 dpi |
| BUG-ch3-06 | D13 BIDI-ORDER | 124 | medium | "ו־" before \textenglish{FreeNoise} | Do not auto-fix. Visual check of PDF crop at 300 dpi |
| BUG-ch3-07 | D11 CH3-01 | 4, 8, 130 | medium | CH3-01 requires peer-reviewed papers. Two arXiv preprints (StoryAgent, VideoDirectorGPT) are kept. Disclosed in the text, but the must-contain conflict is not resolved | No mechanical fix. Team decision needed: keep with disclosure, or replace |
| BUG-ch3-08 | D5 / STY-07 provenance | 94, 109 | medium | MovieDreamer equations, dataset and metrics were taken from arXiv 2407.16655 (per the previous writer). The bib entry (zhao2025moviedreamer) and docs/sources.md list only the ICLR 2025 proceedings URL. Line 94 says the numbers were checked in the full text, but the version used is not recorded | Record arXiv 2407.16655 in docs/sources.md with the version used. Or verify the table values against the ICLR 2025 version and state which one was used |
| BUG-ch3-09 | D11 cross-reference | 56, 128, 142 | medium | REQ-NAR-01, REQ-CHR-01 and REQ-LNG-01 are defined only in docs/concept.md (lines 45–47). docs/requirements.md has no such IDs, so the chapter cites requirements that are not in the requirements list | Add the three IDs to docs/requirements.md (chapter 2 rows), or change the references to match the list |
| BUG-ch3-10 | Internal consistency | 8 (also 4, 44) | medium | Criterion "פרסום בשלוש השנים האחרונות" (the date is 2026). VideoDirectorGPT is a 2023 arXiv preprint (line 4 gives range 2023–2025). The text does not list it as an exception to the criterion | Name the exception in line 8, or change the window to match the cited years |
| BUG-ch3-11 | D7-type overgeneralization | 138 | medium | "המחקרים והמוצרים הקיימים ... אף אחד מהם" and "ואף אחד אינו נגיש ... ליוצרים בעברית" make universal claims beyond the seven reviewed sources. Line 8 admits the search is not systematic [TO-VERIFY] | Replace "המחקרים והמוצרים הקיימים" with "המקורות שנסקרו בפרק זה" and qualify the Hebrew-access claim to the same scope |
| BUG-ch3-12 | D10 first use | 109 | minor | "FID" and "CLIP" metrics are not expanded on first use | Use \textenglish{FID} (\textenglish{Fréchet Inception Distance}) and \textenglish{CLIP} (\textenglish{Contrastive Language-Image Pretraining}) at first mention |
| BUG-ch3-13 | Wording / equation count | 99–107 | minor | Text says "שלוש פונקציות מטרה" but only two equations are displayed. The rendering loss is described only as "באותה צורה" | Display the third equation, or write "שתי פונקציות מטרה ושלישית באותה צורה" |
| BUG-ch3-14 | Wording overclaim | 61 | minor | "VideoDirectorGPT מוכיחה" overstates what a single method shows | Replace "מוכיחה" with "מדגימה" |
| BUG-ch3-15 | Unused label | 67 | minor | \label{sec:ch3-matrix} is never referenced. This is not a fig/tab label, so D3 does not apply | Remove the label, or reference it from the matrix sentence |

## Checks with no bug
- D1 BIDI: no unwrapped Latin text outside math, commands, cites, TO-VERIFY markers. Equation and tabular text is excluded.
- D2 BIDI-JOIN: no Hebrew inside \textenglish{}.
- D3 REF: tab:ch3-matrix (line 68), tab:ch3-moviedreamer (line 109), fig:ch3-families (line 12) are all referenced.
- D4 CAPTION: figure caption is below (line 29). Both table captions are above their tabular (lines 72, 113). Correct.
- D5 CITE: all 8 cite keys exist in bib/references.bib and docs/sources.md. The uncited numbers are handled in BUG-ch3-01.
- D6 VOICE: "גאוסיאנית" (line 103) is a substring match, not first person. Line 133 is inside directornote, which is allowed.
- D7 GENERIC: no hits.
- D8 TO-VERIFY: 5 markers, at lines 8, 52, 61, 68, 94. Line 94 is intentional per the caller.
- D9 BUDGET: about 2,430 body words. No word target in agents-setup section 0 and the file header states a 9-page budget. The ±15% test cannot be applied as written.
- D10 TERM: other terms (LCT, LLM, SVD, GMM, observer, tokens, diffusion autoencoder, preprints, AS, IS, ST, LT) are expanded on first use.
- D11 REQ (CH3-02, 03, 04, 05): matrix, flagship choice, equations, environment, metrics, limitations and gap sentence are present. CH3-01 is the exception (BUG-ch3-07).
- D12 BUILD: build/main.log has no error or Overfull line pointing to ch3. The log was not regenerated and may be stale.
- Facts checked against docs/sources.md: venues (ICLR 2025, NeurIPS 2024, SIGGRAPH 2024, CVPR 2024, ICCV 2025), the team affiliation for ConsiStory, and the StorySalon dataset. All consistent.
- Table arithmetic (line 109 vs table at lines 117–121): the StoryDiffusion vs MovieDreamer values match.

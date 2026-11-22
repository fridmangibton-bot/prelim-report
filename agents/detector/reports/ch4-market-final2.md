# Detector report – chapters/ch4-market.tex – 2026-11-22
Summary: 1 critical, 8 medium, 2 minor. Words: 1116/1100 (within ±15%). TO-VERIFY: 5.

Scope note: SAM and SOM figures (100,000 creators, 25 USD, 0.5% penetration, 500 users, 150 thousand USD) are labelled as team assumptions without [TO-VERIFY], as instructed, and are not reported. Mechanical checks D1, D2, D3, D4, D5, D7 and D12 found no ch4 hits (details below).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch4-01 | read (sources.md) | 43 | critical | Flagship paper MovieDreamer is marked "לא" for end-to-end video, but docs/sources.md describes it as autoregressive planning plus diffusion rendering (video generation). The "לא" is unsupported by the whitelist. | Verify against the paper; until then mark the cell as unverified: `\textenglish{[TO-VERIFY]}` in place of "לא". |
| BUG-ch4-02 | D13 BIDI-ORDER | 24 | medium | Maqaf prefix directly before wrapped runs: ב־\textenglish{LTX Studio}, ב־\textenglish{OpenArt}, ב־\textenglish{LongStories.ai}, ב־\textenglish{Atlabs}, מ־\textenglish{Standard} (INC-001 risk). | Not auto-fixed (RLM tested, no effect). Check the PDF crop at 300 dpi. |
| BUG-ch4-03 | D13 BIDI-ORDER | 27 | medium | ל־\textenglish{Pro} with maqaf directly before the wrapped run. | Not auto-fixed. Check the PDF crop at 300 dpi. |
| BUG-ch4-04 | D13 BIDI-ORDER | 52 | medium | ב־\textenglish{LongStories.ai} with maqaf directly before the wrapped run. | Not auto-fixed. Check the PDF crop at 300 dpi. |
| BUG-ch4-05 | D13 BIDI-ORDER | 54 | medium | ו־\textenglish{CapCut} appears three times, each with maqaf directly before the wrapped run. | Not auto-fixed. Check the PDF crop at 300 dpi. |
| BUG-ch4-06 | D13 BIDI-ORDER | 74 | medium | ו־\textenglish{CapCut} with maqaf directly before the wrapped run. | Not auto-fixed. Check the PDF crop at 300 dpi. |
| BUG-ch4-07 | D13 BIDI-ORDER | 77 | medium | ו־\textenglish{CapCut} with maqaf directly before the wrapped run. | Not auto-fixed. Check the PDF crop at 300 dpi. |
| BUG-ch4-08 | read (consistency) | 27 | medium | "CapCut ... הוא המתחרה הרביעי" contradicts line 19 (four AI tools plus one manual process) and line 22 (five products). CapCut is the fifth product. | Replace "המתחרה הרביעי" with "המתחרה החמישי". |
| BUG-ch4-09 | read (consistency with docs/market-data.md) | 54 | medium | "זהו הציון הגבוה היחיד (5) שניתן ליעד התכנון" is false as written. The team's target scores 5 on Hebrew and on ease of use too (docs/market-data.md, section 3). | Replace "הגבוה היחיד (5) שניתן ליעד התכנון" with "הגבוה (5) שניתן ליעד התכנון בציר זה". |
| BUG-ch4-10 | D10 TERM | 24 | minor | Tier names "Starter" and "Wonder" are used without a Hebrew gloss on first use (the other tiers are glossed or are plain names). | Optional: add a short Hebrew gloss on first use, for example "מסלול \textenglish{Starter} (מסלול הכניסה)". |
| BUG-ch4-11 | read (rationale) | 54 | minor | Target scores have no stated rationale for consistency (4), Hebrew (5) or ease of use (5). The text explains only the cost and continuity scores. | Add one sentence per axis explaining the target score. Not mechanical. |

Checks with no bug:
- D1 BIDI: every Latin run in Hebrew lines is inside \textenglish{}, \cite{}, \ref{} or a command. No hit.
- D2 BIDI-JOIN: no \textenglish{} run contains Hebrew letters.
- D3 REF: labels tab:ch4-compare, fig:ch4-radar and fig:ch4-scatter are each referenced (lines 30, 52, 64).
- D4 CAPTION: table caption (line 34) is above the tabular; figure captions (lines 59, 69) follow the includegraphics, which is correct.
- D5 CITE: all cited keys (fbi2026aivideo, mnm2023t2v, ltxstudio, openart, longstories, atlabs, capcut, zhao2025moviedreamer) exist in bib/references.bib and docs/sources.md.
- D6 VOICE: grep hits at lines 27 ("נעשה") and 44 ("נבנה") are third-person passive or impersonal forms, not first person. Line 80 ("שלנו") is inside directornote, which is allowed. No bug.
- D7 GENERIC: no hit.
- D8 TODO: 5 [TO-VERIFY] markers (line 27 x1, line 39 x2, line 77 x2). 0 "FIGURE PENDING". Info only.
- D9 BUDGET: 1116 words against target 1100, within ±15% (935 to 1265).
- D11 REQ: CH4-02 to CH4-04 present (five products plus the manual process, comparison table with flagship and proposed solution, radar with 6 axes and scatter). CH4-01 covered by the TAM section (source cited); SAM/SOM are team assumptions, as instructed.
- D12 BUILD: build/main.log has no Overfull or error lines for ch4. The overfull at log line 1701 belongs to an earlier chapter. The log may predate the current text, so this check is not conclusive.
- Competitor facts (prices, tiers, character counts, Hebrew support) match docs/market-data.md.

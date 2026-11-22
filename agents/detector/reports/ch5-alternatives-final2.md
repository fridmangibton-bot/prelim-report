# Detector report – ch5-alternatives.tex – 2026-11-22
Summary: 1 critical, 11 medium, 0 minor. Words: ~2050/1500 (prose + directornote; tables add ~150 more; ±15% = 1275–1725). TO-VERIFY: 0.

Method: mechanical checks D1–D13 run on chapters/ch5-alternatives.tex (node scripts in the scratchpad, python is unavailable). No build was run, as requested. Build log (build/main.log) has one Overfull \vbox at line 1701, before the ch5 pages, so it is not attributed to this chapter (D12: none).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch5-01 | Wrong fact about own result (D10/accuracy) | 78 | critical | Text says ב׳ is most sensitive to the quality and cost weights. The sensitivity table (sensitivity.md) shows dev_time moves ב׳ the most (2.82 to 3.28, ±0.23). Quality and cost move it only ±0.13 (2.92 to 3.18). A's range (2.61 to 3.09, 0.48) is also wider than ב׳'s (2.82 to 3.28, 0.46). | Replace the first sentence of the paragraph with: "חלופה ב׳ רגישה ביותר למשקל זמן הפיתוח, שבו ציונה נע בין \textenglish{2.82} לבין \textenglish{3.28}, ואחריה למשקלי האיכות והעלות, שבהם ציונה נע בין \textenglish{2.92} לבין \textenglish{3.18}." |
| BUG-ch5-02 | D9 BUDGET | body | medium | About 2050 words (prose + directornote), target 1500 ±15%. Over the upper bound (1725) by about 325 words. | Cut about 325 words of prose. Candidates: the paragraph after the decision matrix (line 37) and the paragraph on the StoryAgent/VideoDirectorGPT contrast (line 117). Not mechanical. |
| BUG-ch5-03 | D10 TERM | 18 | medium | "API" is first used in the table with no Hebrew term and parentheses. The first use is in the table, not in prose. | In line 18 replace `דרך \textenglish{API}` with `דרך ממשק תכנות יישומים (\textenglish{API})`. |
| BUG-ch5-04 | Unsourced claim (writing rule: every claim needs a number or citation) | 64 | medium | "מודלים מסחריים מספקים את האיכות הטובה ביותר הזמינה כיום" has no source. Not in docs/sources.md. | Append `[TO-VERIFY: source for commercial video model quality ranking]`, or cite a source listed in docs/sources.md. |
| BUG-ch5-05 | Unsourced claim | 31, 64 | medium | The existence and availability of open Hebrew speech models ("מודלי דיבור פתוחים בעברית נבחרים מקומית", line 31; "אפשר לבחור מקומית מודלי דיבור פתוחים בעברית", line 64) is the basis of the score 4 for ג׳ in Hebrew support. No source. | Append `[TO-VERIFY: source for open Hebrew speech models]` on both lines, or cite a whitelisted source. |
| BUG-ch5-06 | Claim about cited works (unverified) | 117 | medium | Says StoryAgent and VideoDirectorGPT do not have a script-memory or continuity-checking agent as a goal. docs/sources.md lists an "observer" agent in StoryAgent, whose role is not described there. The claim is not supported by the whitelist. | Verify against the StoryAgent paper's observer role, then narrow the wording (for example "אינם מופיעים בתיאור של המאמר"), or append `[TO-VERIFY: check observer role in StoryAgent]`. |
| BUG-ch5-07 | D13 BIDI-ORDER | 19 | medium | `ו־\textenglish{API}`: ו־ joined by maqaf directly before a `\textenglish` run. | Visual check at 300 dpi (INC-001 says a similar case renders correctly). No auto-fix. |
| BUG-ch5-08 | D13 BIDI-ORDER | 40 | medium | `בין \textenglish{1} ל־\textenglish{5}`: ל־ joined by maqaf directly before a `\textenglish` run. | Visual check at 300 dpi. No auto-fix. |
| BUG-ch5-09 | D13 BIDI-ORDER | 66 | medium | `מ־\textenglish{3}`: מ־ joined by maqaf directly before a `\textenglish` run. | Visual check at 300 dpi. No auto-fix. |
| BUG-ch5-10 | D13 BIDI-ORDER | 76 | medium | Six maqaf-prefix runs (`ב־`, `ל־` before `\textenglish`), plus `\textenglish{3.44} מול \textenglish{3.28}` (Hebrew word between two runs). | Visual check at 300 dpi. No auto-fix. |
| BUG-ch5-11 | D13 BIDI-ORDER | 78 | medium | Six maqaf-prefix runs (`ל־`, `ול־` before `\textenglish`). | Visual check at 300 dpi. No auto-fix. |
| BUG-ch5-12 | D13 BIDI-ORDER | 162 | medium | `ו־\textenglish{StoryAgent}`: ו־ joined by maqaf directly before a `\textenglish` run. | Visual check at 300 dpi. No auto-fix. |

Notes (not bugs, no row):
- D1 and D2: no Latin run outside \textenglish in Hebrew prose, no Hebrew inside \textenglish. Hits in TikZ node labels (lines 96–148) and the `\begin{tabular}` spec are commands and labels, not prose.
- D3: all fig:/tab: labels are referenced. `sec:ch5-alternatives` (line 7) and `sec:ch5-innovation` (line 159) are not referenced in any chapter (outside the D3 scope; info only).
- D4: table captions are above, figure captions are below. OK.
- D5: all five cited keys (hu2024storyagent, lin2023videodirectorgpt, longstories, ltxstudio, zhao2025moviedreamer) exist in bib/references.bib and docs/sources.md. `\ref{sec:ch3-gap}` exists in ch3.
- D6: line 120 "נעשה" is impersonal/passive, not first person. No violation.
- D7: none. D8: TO-VERIFY 0, FIGURE PENDING 0.
- D11: CH5-01 to CH5-05 covered. Must-contain items present: 3 alternatives, Sj = Σ wi·cij, sensitivity, architecture, data flow, innovation. 2 tables, 3 figures. Weights sum to 1.0. Base scores (2.85, 3.05, 3.50) recomputed from the weights and scores: correct.
- Numbers checked against sensitivity.md: 12 scenarios, C wins in all, C range 3.43–3.57, minimum C-B gap 0.16 at dev_time +0.1, A beats B in 4 scenarios, two scenarios set a weight to 0. All match the text. The only error is BUG-ch5-01.
- REQ-NAR-01 at line 168 refers to the ch2 table, per the caller's note. Not a bug.

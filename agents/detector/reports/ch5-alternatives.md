# Detector report – ch5-alternatives.tex – 2026-11-22
Summary: 1 critical, 11 medium, 0 minor. Words: waived by owner (about 860 incl. tables; target 1500, not flagged). TO-VERIFY: 0.

Scope notes: D9 not flagged (owner waiver). Weights and scores treated as the team's approved assessment. D12: `build/main.log` exists but contains no chapter-5 entries (its chapter listing ends at ch3), so the log does not cover this chapter; no D12 hits. D1, D2, D6, D7, D4, D5, D8 checks: no hits. D3: all `fig:`/`tab:` labels (ch5-decision, ch5-architecture, ch5-dataflow, ch5-matrix, ch5-alternatives) have matching refs. Sensitivity claims (range 3.43–3.57, gap 0.16 at dev_time 0.25, 4 scenarios where A beats B, 2 scenarios with weight 0) checked against `figures/python/data/sensitivity.md` and match. Weighted sums S_j (2.85, 3.05, 3.50) recomputed and match.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch5-01 | D11 | 154 | critical | Cites requirement ID "REQ-NAR-01", which is absent from `docs/requirements.md` (present only in `docs/concept.md:46` and used in ch2). Dangling cross-reference to the requirements register. Verify the ID, then add it to requirements.md or cite the ID that exists there. | No mechanical fix; verify against requirements.md |
| BUG-ch5-02 | D13 | 19 | medium | Maqaf joins prefix "ו" directly before `\textenglish{API}` ("ו־\textenglish{API}"); order may render reversed (INC-001). | Do not auto-fix; visual check of PDF crop at 300 dpi |
| BUG-ch5-03 | D13 | 32 | medium | "ל־" joined by maqaf directly before `\textenglish{5}` ("בין \textenglish{1} ל־\textenglish{5}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-04 | D13 | 58 | medium | "מ־" joined by maqaf directly before `\textenglish{3}` ("נמוך מ־\textenglish{3}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-05 | D13 | 68 | medium | "ב־" joined by maqaf directly before `\textenglish{0.1}` ("הוזז בנפרד ב־\textenglish{0.1}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-06 | D13 | 68 | medium | "ל־" joined by maqaf directly before `\textenglish{3.57}` ("ל־\textenglish{3.57}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-07 | D13 | 68 | medium | Hebrew word "מול" between two `\textenglish{}` runs ("\textenglish{3.44} מול \textenglish{3.28}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-08 | D13 | 68 | medium | "ל־" joined by maqaf directly before `\textenglish{0.25}` ("עלה ל־\textenglish{0.25}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-09 | D13 | 68 | medium | "ל־" joined by maqaf directly before `\textenglish{0}` ("הופחת ל־\textenglish{0}"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-10 | D13 | 150 | medium | "ו־" joined by maqaf directly before `\textenglish{StoryAgent}` ("ו־\textenglish{StoryAgent} מארגן"). | Do not auto-fix; visual check at 300 dpi |
| BUG-ch5-11 | D10 | 19 | medium | "GPU" first used in the report here without a Hebrew term and parentheses. "API" is defined in ch2 (line 71), so it is not flagged. GPU is also absent from `frontmatter/abbreviations.tex`. | `נדרש מעבד גרפי (\textenglish{GPU})` in place of `נדרש \textenglish{GPU}` |
| BUG-ch5-12 | read (claim) | 142 | medium | Asserts as fact that "רק מיעוט מהשוטים יוצא מהמערכת", while the same paragraph states the share of hard shots is unknown ("אינו ידוע כעת"). Unsupported quantitative claim. | `בדרך זו אמור להישלח לספק רק מיעוט מהשוטים, וזה הבסיס לציונים בעלות ובפרטיות בטבלה~\ref{tab:ch5-matrix}. שיעור השוטים הקשים טרם נמדד` |

Note on the count of medium rows: BUG-ch5-02 to BUG-ch5-10 are nine D13 rows (line 68 has four maqaf hits and one between-run hit); BUG-ch5-11 and BUG-ch5-12 are the other two medium rows, giving 11 in total.

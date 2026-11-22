# Detector report – ch2-problem.tex – 2026-11-22
Summary: 0 critical, 1 medium, 1 minor. Words: 949/850 (prose; tables excluded; band 723-978, in range). TO-VERIFY: 19 (tracked, not counted as bugs).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch2-01 | D6 | 74 (x2) | medium | "נעשה" matched the first-person list, but in "האימות נעשה" it is an impersonal passive, not first person. Likely false positive. | None required. If the rule is applied literally, reword "האימות נעשה" to "האימות מתבצע". |
| BUG-ch2-02 | D10 | 41 | minor | "SMART" first appears as an English acronym with no Hebrew term. The parenthetical gives only the English letter words, not the Hebrew expansion. | Writer decision. Example: "מתודולוגיית \textenglish{SMART} (יעד ספציפי, מדיד, בר־השגה, רלוונטי ומוגבל בזמן)". |

Checks with no hits:
- D1 BIDI: no unwrapped Latin runs found on manual review of all non-comment lines. Latin terms are wrapped in \textenglish, and the remaining Latin is inside \label, \ref, TO-VERIFY, or math.
- D2 BIDI-JOIN: no Hebrew letters inside \textenglish.
- D3 REF: tab:ch2-gap and tab:ch2-req are each referenced (lines 21 and 52).
- D4 CAPTION: both captions (lines 25, 60) sit above their tabular.
- D5 CITE: no \cite in this chapter.
- D7 GENERIC: no hits.
- D8 TO-VERIFY: 19 markers (info only). No "FIGURE PENDING".
- D9 BUDGET: prose 949 words, inside 850 ±15%. Tables add about 187 tokens, which the budget text does not count.
- D11 REQ: CH2-01 to CH2-04 are met. Must-contain items are present: quantitative current vs. target table, SMART goals, requirements table with ID, target, and verification. Values match docs/concept.md (REQ-CHR-01, REQ-NAR-01, REQ-LNG-01, REQ-UX-01, REQ-CST-01, REQ-SEC-01).
- D12 BUILD: build/main.log has 0 "!" errors and 0 Overfull \hbox. One "Overfull \vbox (124.86pt)" exists at log line 1701 with no chapter attribution. The log predates the 2026-11-22 expansion noted in docs/progress.md, so D12 is stale and should be re-checked after the next build.
- D13 BIDI-ORDER: no maqaf-prefix or Hebrew-between-runs patterns.
- D9 note: the chapter has been expanded since the last progress entry (834 words). The current prose count is in band.

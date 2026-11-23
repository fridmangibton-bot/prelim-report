# Detector report – ch2-problem.tex – 2026-11-23
Summary: 3 critical, 4 medium, 1 minor. Words: 908 prose (1102 incl. tables)/850 (prose within ±15%: 722–978). TO-VERIFY: 0. FIGURE PENDING: 0.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-2-01 | D5/CLAUDE.md (unsourced numbers) | 29–31, 43, 64–68 | critical | The targets 20 min, 90%, 80%, 10% false alarms, $5/min, 8 participants and 20 test chapters are stated as numbers. `docs/concept.md` lists every one of them as `[לאמת]`, and none is in `docs/market-data.md` or `docs/sources.md`. The TO-VERIFY markers were removed, but CLAUDE.md requires `[TO-VERIFY]` on any unsourced number before submission. The label "יעד תכנון" marks them as design targets but does not source them. | Either restore `[TO-VERIFY]` after each target number, or add a sourced rationale for each value to `docs/sources.md`. Decision for the writer or the user. |
| BUG-2-02 | Invented facts | 43 | critical | "מחיר היעד הוא 25 דולר לחודש", "ארבעה פרקים בני דקה בחודש", "כ־6.25 דולר לדקה" and "שולי רווח של לפחות 20%" have no source. `docs/concept.md` has no price, no episode rate and no margin, and `docs/market-data.md` has no $25 price. The sentence attributes the figures to "חישוב הצוות", but no such calculation is recorded in the docs. | Mark "25 דולר" and "ארבעה פרקים בחודש" as `[TO-VERIFY]` (or cite a file in `docs/sources.md` that records them), and keep the derivation only if the inputs are verified. |
| BUG-2-03 | Logic / wrong comparison | 10, 18, 29, 43–44 | critical | The baseline row "זמן הפקה לדקת וידאו" is measured in hours of work per video minute (line 18), but its target "עד 20 דקות לפרק ראשון בן דקה" is a different metric: REQ-UX-01 is the time for a new user to get a first episode, in minutes. The gap table therefore compares incomparable quantities, and the "gap" the chapter claims cannot be read from it. | Align the metrics. Either change the target row to hours per video minute, or change the baseline row to time-to-first-episode for a new user, and use the same unit in both columns and in REQ-UX-01. |
| BUG-2-04 | D12 BUILD | 77–88 | medium | `build/main.log` (22:00) reports "Overfull \hbox (186.02821pt too wide) in paragraph at lines 77--88" for `ch2-problem.tex`. The current file has 78 lines, so the log either predates the last edit or refers to different content. The overfull box is therefore not confirmed against the current text. | Re-run the chapter build (`bash scripts/build.sh`) after the current edit and check the log again. Do not edit the chapter for this item. |
| BUG-2-05 | Unsourced claim | 14 | medium | "בסקירת דפי המוצר ... לא נמצא מוצר שמציג זיהוי סתירות עלילתיות" is stated as a team finding, but `docs/market-data.md` has no column or note on contradiction detection. Only `docs/concept.md` line 31 repeats it, and that line is not a source. | Add a contradiction-detection column to `docs/market-data.md` with the check date, or mark the sentence `[TO-VERIFY]`. |
| BUG-2-06 | Source whitelist (CLAUDE.md) | 16 | medium | The claim that "רק Atlabs מצהיר על תמיכה בעברית, בתוכניות בתשלום, לפי צוות התמיכה שלו" rests on a private chat with Atlabs support. That chat is not an entry in `docs/sources.md`, and the paragraph cites the repo path `docs/market-data.md` as the source. | Cite the Atlabs pricing page (listed in `docs/sources.md`, if it is) and remove the internal-file reference from the body text, or add the support chat to `docs/sources.md` as a dated entry. |
| BUG-2-07 | Wrong fact (own logic) | 56 | medium | "דרישת האבטחה ... היא היחידה שאינה תלויה בשיפוט אנושי." This is false as written. REQ-CST-01 is a calculation from price lists and also needs no human judgment. REQ-CHR-01 and REQ-NAR-01 are automated checks too. | Replace with a claim the table supports, for example "דרישת האבטחה ודרישת העלות נבדקות בחישוב או בסריקה אוטומטית, בלי שיפוט אנושי". |
| BUG-2-08 | D13/D1 display | 16 | minor | `\textenglish{docs/market-data.md}` puts a repository path inside Hebrew body text. A reader of the report will not find this file. | Replace with the source name from `docs/sources.md`, or drop the path. |

Checks with no hit (for the record):
- D1 BIDI: no Latin letter outside `\textenglish{}` in prose; the only Latin hits are LaTeX option tokens (`[h]`, `p{...}`).
- D2 BIDI-JOIN: no `\textenglish{}` run contains Hebrew.
- D3 REF: labels `tab:ch2-gap` and `tab:ch2-req` are each referenced once in the text.
- D4 CAPTION: both tables have the caption above the tabular.
- D5 CITE: no `\cite` in the chapter.
- D6 VOICE: no first person outside `directornote`. Line 48 "בפרויקט שלנו" is inside the directornote box, which is allowed.
- D7 GENERIC: no hits.
- D8 TODO: TO-VERIFY 0, FIGURE PENDING 0.
- D9 BUDGET: prose 908 words, inside the 722–978 window. With tables, 1102 words.
- D10 TERM: English terms (SMART, API, RTL, face verification, character drift) are glossed in Hebrew with the English in parentheses on first use.
- D11 REQ: the chapter covers CH2-01 (quantitative problem, line 10–18 and table), CH2-02 (problem does not name a solution), CH2-03 (SMART goals and directornote hypothesis, lines 41–48), and CH2-04 (requirements table with ID, target, verification, lines 58–71).
- D13 BIDI-ORDER: no hits for the maqaf or between-run patterns.
- Numbers cross-checked: 90% and ten scenes match REQ-CHR-01 in `docs/concept.md`; 80%, 10% FP and 20 test chapters match REQ-NAR-01; 100% matches REQ-LNG-01; 20 minutes and eight participants match REQ-UX-01; the 20% margin matches 6.25 minus 5 over 6.25.

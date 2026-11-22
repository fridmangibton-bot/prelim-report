# Detector report – ch1-intro.tex – 2026-11-22
Summary: 2 critical, 5 medium, 2 minor. Words: ~690/750 (approx., within ±15%). TO-VERIFY: 6.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch1-01 | D11 / CH1-02 | 19 | critical | "לפי בדיקת הצוות, הכלים שומרים על מראה הדמות ועל עולמה" is a factual claim about competitors with no citation, no [TO-VERIFY], and no matching entry in docs/sources.md | Add `[TO-VERIFY: source for character and world retention claim]` or cite a listed source |
| BUG-ch1-02 | D11 / CH1-02 | 21 | critical | "ואין מערכת קצה־לקצה הנגישה ליוצרים בעברית בלי תשלום" is a market-gap claim with no source and no [TO-VERIFY] (every claim needs a number or source) | Append `[TO-VERIFY: source for absence of free Hebrew end-to-end tool]` |
| BUG-ch1-03 | D13 BIDI-ORDER | 16 | medium | Maqaf prefix `ו־` directly before `\textenglish{LongStories.ai}` (INC-001 risk, rendered order may be reversed) | No mechanical fix (RLM tested, no effect). Visual check of PDF crop at 300 dpi |
| BUG-ch1-04 | D13 BIDI-ORDER | 21 | medium | Maqaf prefix `ו־` directly before `\textenglish{StoryDiffusion}` | No mechanical fix. Visual check of PDF crop at 300 dpi |
| BUG-ch1-05 | D13 BIDI-ORDER | 21 | medium | Maqaf prefix `ו־` directly before `\textenglish{StoryAgent}` | No mechanical fix. Visual check of PDF crop at 300 dpi |
| BUG-ch1-06 | D12 BUILD | 7 | medium | Overfull \hbox (15.5pt too wide), paragraph at lines 7--8 in build/main.log (Markets-and-Markets sentence) | Reword the sentence so the line breaks (no exact mechanical fix) |
| BUG-ch1-07 | D12 BUILD | 21 | medium | Overfull \hbox (23.4pt too wide), paragraph at lines 21--22 in build/main.log (MovieDreamer sentence) | Reword the sentence so the line breaks (no exact mechanical fix) |
| BUG-ch1-08 | wording (duplicate) | 9 | minor | The sentence "לכן השאלה המעשית אינה אם אפשר ליצור וידאו באמצעות בינה מלאכותית, אלא אם אפשר ליצור באמצעותה סדרה שלמה שנשארת עקבית לאורך זמן." appears twice in a row at the end of the paragraph | Delete the second occurrence |
| BUG-ch1-09 | wording (duplicate) | 12 | minor | The sentence "כשדמות משנה את מראיה, או כשעובדה שנקבעה בפרק אחד נסתרת בפרק מאוחר יותר, נשבר הקשר בין הצופה לסדרה, והיוצר נאלץ לתקן את הפרק או להסביר את הסתירה." appears twice in a row | Delete the second occurrence |

## Checks with no hit
- D1 BIDI: no unwrapped Latin runs found on reading of the chapter (all AI, CAGR, RTL, product, model and Showrunner terms wrapped).
- D2 BIDI-JOIN: no Hebrew inside `\textenglish{}`; no hits.
- D3 REF: chapter has no labels or refs.
- D4 CAPTION: no figures or tables in the chapter.
- D5 CITE: all 14 cite keys (fbi2026aivideo, mnm2023t2v, goldman2023creator, ltxstudio, openart, longstories, capcut, zhao2025moviedreamer, zhou2024storydiffusion, hu2024storyagent) exist in bib/references.bib and docs/sources.md.
- D6 VOICE: no first-person forms outside directornote.
- D7 GENERIC: no listed generic openings.
- D10 TERM: English terms (AI, CAGR, Creator Economy, Text-to-Video, RTL, Showrunner) all have Hebrew term plus parentheses on first use.
- D11 REQ: CH1-01 funnel present (trends, applied context, motivation, report map). CH1-02 is covered by BUG-ch1-01 and BUG-ch1-02.
- Figures from docs/sources.md match the chapter: 18.8% CAGR 2026–2034, 41% North America, Markets-and-Markets 0.1B/0.9B and 37.1%, Goldman 250B/480B and ~4% professionals.

## Notes
- D8 TO-VERIFY: 6 markers (lines 5, 14, and four on line 19). No "FIGURE PENDING".
- D12: build/main.log exists (mtime 2026-11-22 21:28, same minute as this check, so another build may be writing it). Used as-is. No "!" errors in the log. The Overfull \vbox at log line 1707 is printed just before the "(./chapters/ch1-intro.tex" marker and is not tied to a line of this chapter, so it is not listed as a bug. Underfull \hbox entries are info only (line 24–25 directornote, title lines).
- Word count is approximate. The shell's detex/sed substitutes did not run cleanly, so the count is from an awk pass that leaves a few LaTeX command tokens in. Expected range is 638–863 words.

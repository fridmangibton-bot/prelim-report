# Detector report – ch1-intro.tex – 2026-11-23
Summary: 0 critical, 6 medium, 1 minor. Words: ~685/750 (approx., Perl strip count, incl. directornote; range 638–862). TO-VERIFY: 0.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-1-01 | D11 CH1-02 / CLAUDE.md numbers rule | 14 | medium | "כ־100,000 יוצרים דוברי עברית" has no source and no [TO-VERIFY] marker. It is labelled "הנחת צוות" and ch4 line 13 labels it "אומדן צוות, לא נתון ממקור", so it is disclosed, not invented. CLAUDE.md says any unsourced number is marked [TO-VERIFY] before submission, and the marker was removed in this edit. Caller to decide: keep the label as the marker, or re-mark. | Either add `[TO-VERIFY]` after "(כ־100,000 יוצרים דוברי עברית, הנחת צוות)", or cite a source. Not auto-fixed. |
| BUG-1-02 | D13 BIDI-ORDER | 16 | medium | Prefix maqaf directly before an English run: `ו־\textenglish{LongStories.ai}`. Per the skill this needs a visual check. INC-001 (closed, false alarm) found the logical RTL order renders correctly. | No auto-fix. Check a 300 dpi crop of the PDF. |
| BUG-1-03 | D13 BIDI-ORDER | 19 | medium | Prefix maqaf directly before an English run: `ל־\textenglish{CapCut}`. Same as above. | No auto-fix. Check a 300 dpi crop of the PDF. |
| BUG-1-04 | D13 BIDI-ORDER | 21 | medium | Prefix maqaf directly before an English run: `ו־\textenglish{StoryDiffusion}`. Same as above. | No auto-fix. Check a 300 dpi crop of the PDF. |
| BUG-1-05 | D13 BIDI-ORDER | 21 | medium | Prefix maqaf directly before an English run: `ו־\textenglish{StoryAgent}`. Same as above. | No auto-fix. Check a 300 dpi crop of the PDF. |
| BUG-1-06 | D11 CH1-02 / overgeneralised claim | 19 | medium | "אף מוצר אינו מציג תיעוד של אירועי העלילה או התראה כשפרק חדש סותר פרק קודם" is stated for all products. docs/market-data.md shows LTX Studio and OpenArt were not tested ("Cannot be tried without paying", "Loaded for a long time and produced no result") and their series feature is "Not found". The claim covers products the team could not test. | Replace "אף מוצר אינו מציג" with "באף אחד מהמוצרים שנבדקו לא נמצא", which matches the "Not found" wording in market-data.md. |
| BUG-1-07 | D5 CITE (uncited product) | 19 | minor | "ורק \textenglish{Atlabs} מצהיר על תמיכה בעברית" has no citation. The key `atlabs` exists in bib/references.bib (line 99) and docs/sources.md. | `ורק \textenglish{Atlabs}~\cite{atlabs} מצהיר` |

## Checks with no hits
- D1 BIDI: scan of all Hebrew lines with Latin letters, after stripping \textenglish, cite, ref, label, commands and math: no unwrapped Latin run.
- D2 BIDI-JOIN: no \textenglish containing Hebrew letters. Multi-word runs (lines 5, 9, 16) are English-only.
- D3 REF / D4 CAPTION: no labels, refs, figures or tables in ch1.
- D5 CITE: all 11 cite keys (fbi2026aivideo, mnm2023t2v, goldman2023creator, ltxstudio, openart, longstories, capcut, huang2026dramaagent, zhao2025moviedreamer, zhou2024storydiffusion, hu2024storyagent) exist in bib/references.bib and docs/sources.md. huang2026dramaagent is present in both. Gap sentence (line 21) matches the authorised sentence in docs/sources.md, including the "not persistent plot memory across separately produced episodes" scope.
- D6 VOICE: no first person outside directornote.
- D7 GENERIC: no listed empty openings.
- D8 TO-VERIFY: 0 markers, 0 "FIGURE PENDING".
- D9 BUDGET: ~685 words vs 750 target, within ±15%.
- D10 TERM: "בינה מלאכותית (AI)", "קצב צמיחה שנתי מצטבר (CAGR)", "כלכלת היוצרים (Creator Economy)", "מנהל סדרה (Showrunner)" and the Text-to-Video term all carry Hebrew term plus parentheses on first use.
- D12 BUILD: build/main.log (22:01) is newer than references.bib (21:54) and ch1 (21:56). No "Citation ... undefined" warnings. No overfull hbox or error is attributable to ch1. Log errors seen are in ch3-literature.tex (l.86 DramaAgent table row "You have given more & marks", l.124/126 "Undefined control sequence", and the overfull hbox at lines 77–88). These are out of scope for this chapter but should go to the ch3 detector.
- Market figures vs docs/sources.md: FBI 716.8M (2025), 847M (2026), 3,350M (2034), CAGR 18.8% for 2026–2034, North America 41% (2025). MnM 0.1B (2022), 0.9B (2027), CAGR 37.1%. Goldman ≈250B (2023), ≈480B (2027), ~4% professionals above USD 100K/year. All match.
- CH1-01 funnel (trends, application context, motivation, report map): present in order.
- Structure paragraph (line 28): chapter numbers and descriptions match ch2–ch8 in docs/requirements.md.
- directornote (line 24) matches docs/concept.md (מנהל סדרה, ספר סדרה, סתירות, עברית).

## Previous report
The earlier ch1-intro.md (2026-11-21) was for an older text and is replaced by this report. Its critical items (undefined citations, the "אף אחד מוצע כמערכת קצה־לקצה" claim, and the overfull hbox rows) no longer apply to the current text: the citations resolve, the wording is changed, and no ch1 overfull hbox is in the current log.

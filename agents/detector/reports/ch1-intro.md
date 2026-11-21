# Detector report – ch1-intro.tex – 2026-11-21
Summary: 2 critical, 8 medium, 1 minor. Words: 578/750 (approx., regex count incl. directornote; target range 638–862). TO-VERIFY: 4 (lines 14, 19 ×3).

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-1-01 | D12 BUILD | 5, 7, 16, 21 | critical | build/main.log (21:41) reports "Citation ... undefined" for ch1 keys fbi2026aivideo, mnm2023t2v, goldman2023creator, ltxstudio, openart, longstories, capcut, zhao2025moviedreamer, zhou2024storydiffusion, hu2024storyagent. build/main.bbl (15:50) contains 0 hits for fbi2026aivideo and is older than bib/references.bib (21:17). Likely stale bibliography; PDF would show [?] for these cites. Keys themselves are present in bib and sources.md. | No source edit. Re-run `bash scripts/build.sh` and confirm no ch1 citation warnings. |
| BUG-1-02 | Factual vs docs/market-data.md | 21 | critical | "ואף אחד אינו מוצע כמערכת קצה־לקצה ליוצרים בעברית" is contradicted by docs/market-data.md: Atlabs is listed as end-to-end AI video (Yes) with Hebrew on paid plans. The team's own finding is narrower: no Hebrew end-to-end tool is accessible on a free tier. docs/concept.md line 33 uses the broader wording, so the fix belongs in the concept wording too. | "ואף אחד אינו מוצע כמערכת קצה־לקצה ליוצרים בעברית" → "ואין מערכת קצה־לקצה הנגישה ליוצרים בעברית בלי תשלום" |
| BUG-1-03 | D10 TERM | 5 | medium | First English use "AI" (\textenglish{AI}, second sentence of para 1) has no Hebrew term and parentheses. The Hebrew "בינה מלאכותית" appears earlier in the same paragraph without the English gloss. | In first clause: "מבוססי בינה מלאכותית" → "מבוססי בינה מלאכותית (\textenglish{AI})". Keep later "מבוססי \textenglish{AI}" as is. |
| BUG-1-04 | D11 CH1-02 | 5 | medium | First sentence "...גדל בקצב דו־ספרתי, והיצירה האוטומטית של וידאו הופכת מניסוי טכנולוגי למוצר מסחרי" has no citation. The second clause is an unsupported claim. CH1-02 requires every claim to carry a number or source. | "בקצב דו־ספרתי" → "בקצב דו־ספרתי~\cite{fbi2026aivideo}". Second clause: add \cite or mark [TO-VERIFY]. |
| BUG-1-05 | D12 overfull hbox | 5 (log: paragraph lines 5–6) | medium | Overfull \hbox 73.1pt; text "ולצמוח ל־3,350 ... 2026--2034" segment. | Not mechanical. Rewrap the sentence or split the list of figures; re-check PDF. |
| BUG-1-06 | D12 overfull hbox | 7 (log: lines 7–8) | medium | Overfull \hbox 28.6pt and 15.5pt. Unbreakable English run \textenglish{MarketsandMarkets}. | Optional: \textenglish{Markets\-and\-Markets} (visible text unchanged). Otherwise rewrap. |
| BUG-1-07 | D12 overfull hbox | 9 (log: lines 9–10) | medium | Overfull \hbox 48.7pt and 25.7pt in the Goldman paragraph. | Not mechanical. Rewrap or split the sentence with "250" / "480" figures; re-check PDF. |
| BUG-1-08 | D12 overfull hbox | 21 (log: lines 21–22) | medium | Overfull \hbox 132.0pt in the academic-research paragraph. | Not mechanical. Rewrap; likely a long English run among \textenglish{...} items. |
| BUG-1-09 | D11 CH1-02 / factual | 19 | medium | "הכלים שומרים על מראה הדמות ועל עולמה, אך אינם מתעדים את אירועי העלילה ואינם מתריעים כשפרק חדש סותר פרק קודם" is a general claim about the commercial tools with no source. docs/market-data.md says LTX Studio and OpenArt could not be tried, and LongStories has a series feature. Only the team's internal assessment (market-data line 52) supports the "no contradiction checks" part. | Scope the claim to the team's test and mark it: "...ואינם מתריעים כשפרק חדש סותר פרק קודם [TO-VERIFY]" with "לפי בדיקת הצוות" before the claim. |
| BUG-1-10 | D9 BUDGET | whole chapter | medium | 578 words against a 750 target (±15% = 638–862). About 60 words under the lower bound. Count is an approximation (regex strip, no detex). | Add about 60–100 Hebrew words, e.g. to the funnel transition or the report-map paragraph. |
| BUG-1-11 | D11 CH1-02 wording | 9 | minor | "הנתונים מצביעים על קהל גדול של יוצרים עצמאיים" is an interpretation with no source for "קהל גדול". | Soften, e.g. "הנתונים מרמזים על קהל לא מבוטל של יוצרים עצמאיים" or drop. |

## Fix status
- BUG-1-01: not fixed (needs rebuild; build blocked by ch3 pgf/undefined-control-sequence errors, no source edit needed; re-verify after ch3 compiles)
- BUG-1-02: fixed (docs/concept.md untouched, per instruction)
- BUG-1-03: fixed
- BUG-1-04: fixed (cite added; second clause marked [TO-VERIFY], needs input)
- BUG-1-05: not fixed (needs PDF check after build; not mechanical)
- BUG-1-06: fixed (Markets\-and\-Markets hyphenation points; verify after build)
- BUG-1-07: not fixed (needs PDF check after build; not mechanical)
- BUG-1-08: not fixed (needs PDF check after build; not mechanical)
- BUG-1-09: fixed (scoped to team test, [TO-VERIFY] added, needs input; LongStories series feature noted with cite)
- BUG-1-10: fixed (about 55-65 words added from sourced material, est. ~640, unverified count)
- BUG-1-11: fixed

## Checks with no hits
- D1 BIDI: no Latin run outside \textenglish, cite, or command. (The two lines flagged by the scan, 14 and 19, contain only the [TO-VERIFY] marker.)
- D2 BIDI-JOIN: no \textenglish with Hebrew letters.
- D3 REF / D4 CAPTION: no figures, tables, or labels in ch1.
- D5 CITE: all 10 keys used (fbi2026aivideo, mnm2023t2v, goldman2023creator, ltxstudio, openart, longstories, capcut, zhao2025moviedreamer, zhou2024storydiffusion, hu2024storyagent) exist in bib/references.bib and docs/sources.md. atlabs is in both files but not cited in ch1.
- D6 VOICE: no first person outside directornote.
- D7 GENERIC: no listed empty openings.
- D13 BIDI-ORDER: no maqaf-prefix or two-run pattern hits.
- Market figures vs docs/sources.md: match. FBI: 716.8M (2025), 847M (2026), 3,350M (2034), CAGR 18.8% for 2026–2034, North America 41% (2025). MarketsandMarkets: 0.1B (2022), 0.9B (2027), CAGR 37.1%. Goldman Sachs: ≈250B (2023), ≈480B (2027), ~4% professionals earning over 100K USD/year.
- Structure paragraph: chapter numbers and descriptions match ch2–ch8 in the requirements (ch6 = 14 weeks, ch8 = three immediate actions).
- CH1-01 funnel (trends → application context → motivation → report map): present.
- directornote concept wording matches docs/concept.md line 37 (מנהל סדרה / ספר סדרה / סתירות).
- Build log stale-check: main.log (21:41) is newer than ch1 (21:35), so the overfull and citation warnings apply to the current text.

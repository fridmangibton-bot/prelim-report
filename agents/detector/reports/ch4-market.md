# Detector report – ch4-market.tex – 2026-11-23
Summary: 3 critical, 9 medium, 2 minor. Words: 1069/1100 (prose; 1114 with directornote; target +-15% = 935-1265). TO-VERIFY: 0 in chapter (market-data.md expects 1 for CapCut).

Scope: chapters/ch4-market.tex, checked against docs/market-data.md (sections 1-3 and verification log), figures/python/data/scatter.json, docs/sources.md, bib/references.bib, docs/requirements.md (CH4-01..04), docs/agents-setup.md section 0, build/main.log.

Mechanical checks with no hits: D1 (all Latin runs wrapped), D2, D3 (3 labels, 3 refs, no orphans), D4 (table caption above tabular, figure captions below), D5 (all 8 cite keys present in bib and sources.md), D7, D12 (build/main.log has no Overfull/undefined lines; log may predate the 2026-11-22 edit, not rebuilt as instructed).
D6 raw grep hits at lines 27 (נעשה) and 44 (נבנה) are impersonal passives, not first person; line 82 (שלנו) is inside directornote. Not bugs.

Consistency with docs/market-data.md: table cells (prices, consistency, series, Hebrew, e2e, weakness), Atlabs tiers and "consistency from Pro 39", LongStories 59/99/199, OpenArt 14/~13/~353, LTX 15/35/125, radar scores except BUG-ch4-03, scatter points, criteria list (4 items), and captions all match. Scatter.json and chapter agree on X/Y values.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-ch4-01 | D11 (CH4-01, CLAUDE.md [TO-VERIFY] rule) | 13 | critical | Numbers without a source and without [TO-VERIFY]: 100,000 creators, 25 USD/month. CH4-01 requires a source for each number; the paragraph only says "הנחת צוות". | Append " [TO-VERIFY]" after "100,000" and after "25 דולר" (both in this line). |
| BUG-ch4-02 | D11 (CH4-01), D8 | 16 | critical | Numbers without a source and without [TO-VERIFY]: 0.5\% penetration, 500 paying users, 150 אלף דולר. Same rule as above. | Append " [TO-VERIFY]" after "0.5\%" and after "150 אלף דולר". |
| BUG-ch4-03 | D11 / D5 (CapCut price source) | 27 (and table cell line 39, footnote line 47) | critical | CapCut 19.99 USD and 69.9 ILS are attributed to "מקור משני", which is not named and not in docs/sources.md. \cite{capcut} points to the homepage, whose pricing page was never opened. market-data.md marks this as [TO-VERIFY: CapCut footnote]; the chapter has 0 markers. | Add [TO-VERIFY] after "19.99 דולר" in line 27 and after "19.99*" in the table cell; or name the secondary source, list it in docs/sources.md, and cite it. Do not cite the homepage for the price. |
| BUG-ch4-04 | Logic vs market-data §3 | 56 | medium | Stated rule "ציר העלות נגזר ממחיר הכניסה ... וככל שהמחיר נמוך הציון גבוה" contradicts the scores: Atlabs (entry 39) gets 4 and LTX Studio (entry 35) gets 3. | Decide: set Atlabs cost to 3 in market-data §3 and the radar figure, or restate the rule as a team judgment. Do not change only the text. |
| BUG-ch4-05 | Definition vs data | 66 | medium | The scatter X axis is defined (market-data §2) as the price of the cheapest plan that includes consistent characters, but CapCut (19.99, Y=1) has no consistent characters. The text describes the axis generically and does not say CapCut is plotted at its only price. | Add: "לגבי CapCut מוצג מחיר המנוי היחיד שלו, שאינו כולל דמויות עקביות." |
| BUG-ch4-06 | Date consistency | 22 (also table caption line 34, figure captions lines 61 and 71, line 79) | medium | Chapter states prices "נכון ל־21.11.2026", but Atlabs prices were verified 22.11.2026 (line 24 and market-data §1). | Change the reference date to "21.11.2026; Atlabs 22.11.2026" in line 22 and line 79, and note the same in the table caption; or re-check all prices on one date and update every date. |
| BUG-ch4-07 | D13 BIDI-ORDER | 24 | medium | Maqaf-joined prefix before \textenglish runs: "ב־\textenglish{LTX Studio}", "ב־\textenglish{OpenArt}", "ב־\textenglish{LongStories.ai}", "ב־\textenglish{Atlabs}"; plus Hebrew word between runs: "\textenglish{OpenArt} מסלול \textenglish{Starter}". Per INC-001 the construct renders correctly; visual check only. | No auto-fix. Visual check at 300 dpi of the crop (pdftoppm -r 300). |
| BUG-ch4-08 | D13 BIDI-ORDER | 27 | medium | "ל־\textenglish{Pro}" (maqaf before run). | No auto-fix. Visual check at 300 dpi. |
| BUG-ch4-09 | D13 BIDI-ORDER | 54 | medium | "ב־\textenglish{LongStories.ai}" (maqaf before run). | No auto-fix. Visual check at 300 dpi. |
| BUG-ch4-10 | D13 BIDI-ORDER | 56 | medium | "ו־\textenglish{CapCut}" appears three times, maqaf before run (ל/ו prefix). | No auto-fix. Visual check at 300 dpi. |
| BUG-ch4-11 | D13 BIDI-ORDER | 76 | medium | "ו־\textenglish{CapCut}" (maqaf before run). | No auto-fix. Visual check at 300 dpi. |
| BUG-ch4-12 | D13 BIDI-ORDER | 79 | medium | "ו־\textenglish{LTX Studio}" (maqaf before run). | No auto-fix. Visual check at 300 dpi. |
| BUG-ch4-13 | Wording (agreement) | 24 | minor | "שמירת דמויות עקבית" – "דמויות" is feminine plural. | "שמירת דמויות עקביות" |
| BUG-ch4-14 | Wording | 56 | minor | "זהו אחד הציונים הגבוהים (5) שניתנו ליעד התכנון" is vague when 5 is the maximum score. | "זהו הציון הגבוה ביותר (5) שניתן ליעד התכנון" (or keep and say which other scores are 5). |

Notes for the caller:
- Counts: 3 critical, 9 medium, 2 minor. D13 rows are the same construct INC-001 closed as correct rendering; they are kept per the skill for a visual check.
- No edits made to the chapter. No build run.

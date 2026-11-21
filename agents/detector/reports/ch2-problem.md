# Detector report – ch2-problem – 2026-11-21
Summary: 0 critical, 7 medium, 2 minor. Words: ~645/850 (band 723–978). TO-VERIFY: 19.

| Bug ID | Check | Line | Severity | Problem | Suggested fix | Status |
|---|---|---|---|---|---|---|
| BUG-ch2-01 | D13 | 66 | medium | Maqaf joins the Hebrew prefix "ו" to a \textenglish run: "ו־\textenglish{REQ-LNG-01}", with a Hebrew word between two runs (INC-001 pattern). Not auto-fixable (RLM tested, no effect). | No mechanical fix. Visual check of the PDF crop at 300 dpi around "REQ-NAR-01 ו־REQ-LNG-01". | not fixed (no mechanical fix; needs visual PDF check) |
| BUG-ch2-02 | D13 | 69 | medium | Same pattern: "\textenglish{REQ-CST-01} ו־\textenglish{REQ-SEC-01}". | No mechanical fix. Visual check at 300 dpi. | not fixed (no mechanical fix; needs visual PDF check) |
| BUG-ch2-03 | D10 | 39 | medium | "SMART" first use is not given an English/Hebrew parenthetical. The Hebrew expansion follows a colon instead. | "מתודולוגיית \textenglish{SMART} (\textenglish{Specific, Measurable, Achievable, Relevant, Time-bound})" | fixed |
| BUG-ch2-04 | D10 | 69 | medium | "API" first use without a Hebrew term. The only occurrence in the chapter. | "שמפתחות ממשק תכנות יישומים (\textenglish{API}) יישמרו בקובץ \textenglish{.env}" | fixed |
| BUG-ch2-05 | D9 | 1–69 | medium | Body is about 645 words (method below). The target is 850 ±15%, so the band is 723–978 and the chapter is about 80 words under the floor. progress.md logs 834 words, which does not match this count. | Add about 80–200 words of substance (for example the consequences of each failure, or the baseline measurement plan). No mechanical fix. | fixed (real count by token split was 720 before, 768 now; band 723-978) |
| BUG-ch2-06 | D12 | 48–49 | medium | Overfull \hbox (10.26pt too wide) in paragraph at lines 48–49 of build/main.log (line 1676). Build log is newer than the chapter, so the warning is current. | Shorten or split the sentence "המפרט מתרגם ... לאחר מדידת קו הבסיס" (for example split after "לדרישות"). Recompile to confirm. | fixed (sentence split; no Overfull in log after rebuild) |
| BUG-ch2-07 | D11 (CH2-02) | 8 | medium | Judgment call. "אין שכבה משותפת ששומרת מידע על הדמויות ועל העולם" frames the problem as the absence of a solution component (a shared memory layer). This is the "אין לנו כלי X" trap that CH2-02 forbids. | "המידע על הדמויות ועל העולם מפוזר בין הכלים ואינו נשמר במקום אחד" | fixed |
| BUG-ch2-08 | wording | 48 | minor | "הטבלה מחלקה" uses a non-existent feminine verb form. "טבלה" is feminine, so the verb is "מחלקת". | "הטבלה מחלקת את הדרישות לתפקודיות" | fixed |
| BUG-ch2-09 | wording (unsourced claim) | 12, 14 | minor | Causal/trend claims with no number and no source: "הסחיפה נובעת מכך שכל שוט נוצר ללא זיכרון מלא" (12) and "ולכן הסתירות מתרבות ככל שהסדרה מתארכת" (14). Not numbers, so no TO-VERIFY marker is required, but they are unsupported. | Rephrase as a hypothesis ("צפוי ש...") or add a source from docs/sources.md first. | fixed (rephrased as hypotheses "צפוי ש..."; no source added) |

## Checks with zero hits
- D1 BIDI: no unwrapped Latin text. All Latin runs are inside \textenglish{} or math (REQ IDs, .env, API, RTL, SMART, face embedding, character drift).
- D2 BIDI-JOIN: no Hebrew letter inside \textenglish{}.
- D3 REF: tab:ch2-gap is referenced at line 19 and tab:ch2-req at line 48. No figure labels.
- D4 CAPTION: both tables have the caption above the tabular (lines 23 and 52). Correct for tables.
- D5 CITE: no \cite in the chapter.
- D7 GENERIC: none found.
- D8 TO-VERIFY: 19 occurrences on 13 lines (info only). FIGURE PENDING: 0.
- D11 CH2-01 (quantitative problem, table at lines 21–32), CH2-03 (SMART goals plus the hypothesis in the directornote, line 44), CH2-04 (requirements table with ID, target and verification, lines 50–63). Requirement IDs match docs/concept.md (REQ-CHR-01, REQ-NAR-01, REQ-LNG-01, REQ-UX-01, REQ-CST-01, REQ-SEC-01).
- D12 errors: none. The only chapter-pointing warning is the overfull hbox (BUG-ch2-06). Underfull hboxes are cosmetic and not counted.
- Facts vs docs/concept.md: no contradictions found. Concept SMART and REQ values match the chapter, and the placeholders are consistent.

## Notes (not counted as bugs)
- D6 VOICE: line 66 contains "נעשה" in "והאימות נעשה" ("the verification is done"). This is passive, not first person, so it is a grep false positive. Line 44 contains "שלנו", which is inside directornote and exempt.
- Page budget (agents-setup section 0) lists "850 + 1 table" for ch2. The chapter has 2 tables (tab:ch2-gap and tab:ch2-req). Writer should confirm this is intended.
- Word count method: LaTeX commands and comments stripped, \textenglish content kept, whitespace tokens with Hebrew or Latin characters counted. Prose about 531, tables about 101, captions and boxes about 13. This is an estimate; detex + wc on the compiled text may differ by a few percent.
- Build log (build/main.log, 19:45) is newer than the chapter (19:44), so D12 results are current.

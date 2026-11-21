# Detector report (round 2) – ch2-problem – 2026-11-21
Summary: 0 critical, 4 medium (open), 0 minor (open). Words: 776/850 incl. tables (band 723–978); 651 prose-only. TO-VERIFY: 19.
Round-1 report kept unchanged: agents/detector/reports/ch2-problem.md
Build checked: build/main.pdf and build/main.log at 19:50, chapter at 19:49 (build is current).

| Bug ID | Check | Line | Severity | Problem | Suggested fix | Status |
|---|---|---|---|---|---|---|
| BUG-ch2-01 | D13 | 68 | medium | Maqaf joins "ו" to \textenglish{REQ-LNG-01}, with a Hebrew word between two runs. Visual check at 300 dpi (build/main.pdf page 10, section 2.3.1) confirms the INC-001 reversal: the rendered line reads "REQ-NAR-01REQ-CHR-01 , ו־REQ-LNG-01", so the runs are out of order and the prefix sits away from its run. | Rewrite without maqaf-prefix adjacency, for example: "הדרישות התפקודיות הן \textenglish{REQ-CHR-01}, \textenglish{REQ-NAR-01} ו\textenglish{REQ-LNG-01}" is NOT verified; a safer option is a reworded sentence ("והדרישה השלישית היא \textenglish{REQ-LNG-01}"). Recompile and re-check page 10 at 300 dpi. | fixed (round 2): Hebrew words now separate the IDs; verified at 300 dpi |
| BUG-ch2-02 | D13 | 71 | medium | Same pattern: "\textenglish{REQ-CST-01} ו־\textenglish{REQ-SEC-01}". Visual check at 300 dpi (page 11, section 2.3.2) confirms the reversal: the rendered line reads "REQ-UX-01REQ-CST-01 , ו־REQ-SEC-01" with the runs out of order, and the ו־ sits at the line end. | As BUG-ch2-01: reword so that no Hebrew prefix touches a \textenglish run. Recompile and re-check page 11. | fixed (round 2): Hebrew words now separate the IDs; verified at 300 dpi |
| BUG-ch2-10 | D13 (visual, new) | 39 | medium | In the SMART parenthetical, the English list breaks inside a token on page 10 ("Specific, Measur-" / "SMART" on the next line, "able, Achievable..." on the following line). The parenthetical is also rendered out of order, so the reader cannot follow it. | Not mechanical. Options: keep the English list in one \mbox, or move the list out of the parenthetical into a separate sentence. Recompile and re-check page 10. | fixed (round 2): list split into per-term parentheticals; verified at 300 dpi |
| BUG-ch2-05 | D9 | 1–71 | medium | Word count: 776 with tables and captions, inside the band 723–978. Prose only (tables excluded) is 651, below the 723 floor. agents-setup section 0 says "850 + 1 table" and the chapter now has 2 tables, so the budget is ambiguous. | Owner decision needed: either accept the total-with-tables count, or add about 70–100 words of prose. | accepted (owner decision: total with tables 776 within band 723-978); no action |

## Resolved since round 1 (verified in current chapter)
- BUG-ch2-03 (D10, SMART first use): line 39 now has \textenglish{SMART} with the English expansion in parentheses. Resolved in the source. Note the rendering problem above (BUG-ch2-10).
- BUG-ch2-04 (D10, API first use): line 71 "(\textenglish{API})" with Hebrew term. Resolved.
- BUG-ch2-06 (D12, overfull hbox): build/main.log has no "Overfull" lines. Resolved.
- BUG-ch2-07 (D11 CH2-02, solution-in-problem framing): line 8 now reads "המידע על הדמויות ועל העולם מפוזר בין הכלים ואינו נשמר במקום אחד". Resolved.
- BUG-ch2-08 (wording, "הטבלה מחלקה"): line 66 now reads "הטבלה מחלקת". Resolved.
- BUG-ch2-09 (unsourced causal claims): lines 12 and 14 rephrased as "צפוי ש...". Resolved.

## Mechanical checks (round 2)
- D1 BIDI: no unwrapped Latin text. Only hits are the [TO-VERIFY] markers, which are exempt. 0.
- D2 BIDI-JOIN: no Hebrew letter inside any \textenglish{} run. 0.
- D3 REF: tab:ch2-gap referenced (line 19), tab:ch2-req referenced (line 48). 0.
- D4 CAPTION: both captions above their tables. 0.
- D5 CITE: no \cite in the chapter. 0.
- D6 VOICE: no first person outside directornote (line 44 "שלנו" is exempt). "נעשה" in lines 68 and 71 is passive, not a hit. 0.
- D7 GENERIC: 0.
- D8 TO-VERIFY: 19 (info only). FIGURE PENDING: 0.
- D10/D11: requirement IDs match docs/requirements.md CH2-01 to CH2-04 and docs/concept.md. Must-contain items present: quantitative problem with table (CH2-01), SMART goals plus hypothesis in directornote (CH2-03), requirements table with ID, target and verification (CH2-04), problem does not name a solution (CH2-02). 0 open.
- D12 BUILD: no errors ("^!") in build/main.log; no Overfull hbox. 0.

## Visual check (300 dpi, pdftoppm, scratchpad)
- Rendered pages 10–11 of build/main.pdf at 300 dpi. Both maqaf bugs are visible (see BUG-ch2-01 and -02). The fixer did not fix them, and the sentences need rewording rather than a character change, since the earlier RLM test had no effect.
- Page 10 also shows the SMART line-break problem (BUG-ch2-10).

## Notes
- Counts: critical 0, medium 4 open (BUG-ch2-01, -02, -05, -10), minor 0 open.
- Writer's round-1 line numbers (66, 69) are stale; the current lines are 68 and 71.

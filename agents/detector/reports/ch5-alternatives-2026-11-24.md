# Detector report – ch5-alternatives.tex – 2026-11-24
Summary: 1 critical, 2 medium, 1 minor. Words: ~2050/1500 (regex count of prose and directornote; tables, TikZ and equations excluded; ±15% = 1275–1725). TO-VERIFY: 0.

Scope: checks D1–D12 and D15 on chapters/ch5-alternatives.tex. D13 was not evaluated, per the caller's note (LTR runs now in \mbox). D15 used the fresh build/check.txt (`py scripts/d15_check.py build/check.txt`): 2 hits, both in the references section (report ID FBI110060 and a DOI), none in chapter 5 text.

| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-5-01 | D11 / wrong fact (contradicts docs/sources.md and ch3) | 160 | critical | "אף אחד מהם אינו מנהל זיכרון של העלילה עצמה" is contradicted by the source list: DramaAgent (huang2026dramaagent) "maintains persistent character and story states" within one story, and ch3 line 163 says so explicitly. The sentence must keep the ch3 limitation (persistence across separately produced episodes). | Replace "אך אף אחד מהם אינו מנהל זיכרון של העלילה עצמה ואינו מזהה סתירות עלילתיות" with "אך אף אחד מהם אינו מנהל זיכרון עלילתי מתמשך לסדרה שפרקיה מופקים בנפרד, ואינו מזהה סתירות עלילתיות בין פרקים" |
| BUG-5-02 | D9 BUDGET | 1–168 | medium | Prose is about 2050 words against a target of 1500 (+37%, outside ±15%). Table 1.1 of the booklet sets 1500 words plus 2 tables and 3 figures for this chapter. | Cut about 350–500 words (candidates: the paragraphs at lines 25, 31 and 113–117 repeat points already made in the tables and figures). No mechanical fix. |
| BUG-5-03 | Internal consistency (ch2 REQ-NAR-01) | 168 | medium | "אם הבודק אינו מגיע לסף שייקבע" says the threshold is still open, but ch2 line 65 already sets it: at least 80% of planted contradictions detected and up to 10% false alerts (design target). | Replace "אם הבודק אינו מגיע לסף שייקבע" with "אם הבודק אינו מגיע ליעד התכנון של \textenglish{REQ-NAR-01} (לפחות 80\% מהסתירות ועד 10\% התראות שווא, ראו פרק~2)" |
| BUG-5-04 | D10 TERM | 18 | minor | \textenglish{API} is first used in the chapter without a Hebrew term or expansion. It is defined in frontmatter/abbreviations.tex, so this is informational. | No change needed if the front-matter list counts as the first-use definition. Otherwise add the Hebrew term in parentheses at first use. |

Checks with no hits in this chapter:
- D1 BIDI: every Latin run in Hebrew text is inside \textenglish{} or \mbox{\textenglish{}}. Math runs (\mathdir TLT) are excluded by the caller's note.
- D2 BIDI-JOIN: none.
- D3 REF: all five fig/tab labels are referenced (tab:ch5-alternatives, tab:ch5-matrix, fig:ch5-decision, fig:ch5-architecture, fig:ch5-dataflow). eq:ch5-score is referenced once.
- D4 CAPTION: both tables have the caption above the tabular; the three figures have the caption below the figure or tikzpicture.
- D5 CITE: keys hu2024storyagent, lin2023videodirectorgpt, longstories, ltxstudio, zhao2025moviedreamer are in bib/references.bib and docs/sources.md. The cross-reference sec:ch3-gap exists in ch3.
- D6 VOICE: none.
- D7 GENERIC: none.
- D8 TODO: TO-VERIFY 0, FIGURE PENDING 0.
- D11 REQ: CH5-01 to CH5-05 are covered (alternatives with pro and con, weighted matrix with weights set before scores, sensitivity analysis, architecture and data-flow figures, innovation section with the "not a copy of an existing product" argument). REQ-NAR-01 is referenced at line 168.
- D12 BUILD: no Overfull \hbox in build/main.log that points to chapter 5.
- D15 (chapter 5 text): no hits.

Numbers checked (recomputed, all match the text):
- Base scores: A 2.85, B 3.05, C 3.50. Weights sum to 1.0.
- Twelve sensitivity scenarios: C wins all. C ranges 3.43–3.57. A beats B in four scenarios. The smallest C–B gap is 0.16 (3.44 vs 3.28, development weight 0.25), as stated.
- B at development weight 0.05 gives 2.82; B at quality 0.15 or cost 0.30 gives 2.92; A at dependence or privacy 0.20 gives 3.09; C at those points gives 3.44 and 3.56.
- Criterion contributions in the text (line 67) match the table.

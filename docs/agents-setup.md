# Agents setup – skills and subagents for the preliminary report

> How to use: save this file as `docs/agents-setup.md` in the project, then tell Claude Code:
> `Read docs/agents-setup.md and create every file it defines, exactly as written. Before writing, open style/report.cls and replace the LaTeX macro names in section 0 with the real ones from the class. Then run the self-test in section 6.`

---

## 0. Project facts the skills rely on (verify against style/report.cls)

| Thing | Macro / path (adjust to the real class) |
|---|---|
| Wrap an English run inside Hebrew text | `\textenglish{...}` (real class macro; `\en` does not exist and is not used) |
| Table header row | `\headrow` + `\hcell{...}` ; rows separated by `\rowrule` |
| "In our project" box | `\begin{directornote} ... \end{directornote}` |
| Note box | `\begin{notebox} ... \end{notebox}` |
| Missing number marker | `[TO-VERIFY]` |
| Chapters | `chapters/ch1-intro.tex` ... `chapters/ch8-summary.tex` |
| Sources whitelist | `docs/sources.md` + `bib/references.bib` |
| Requirements | `docs/requirements.md` (IDs like CH2-04, STY-05) |
| Detector reports | `agents/detector/reports/<chapter>.md` |
| Progress log | `docs/progress.md` |
| Incident log | `docs/incidents.md` |

### Page budget per chapter (from booklet table 1.1)

Rule of thumb for this class: about 280 Hebrew words per full text page. A full-width figure or table ≈ 1/3 page.

| Chapter | Pages | Target words (±15%) | Must contain |
|---|---|---|---|
| ch1-intro | 3 | 750 | Funnel: trends → context → motivation → report map |
| ch2-problem | 4 | 850 + 1 table | Quantitative problem, SMART goals, requirements table (ID, target, verification) |
| ch3-literature | 9 | 2000 + 1 matrix table + 1 figure | Thematic review, literature matrix, flagship paper analysis, one-sentence gap |
| ch4-market | 6 | 1100 + 1 table + 2 figures | TAM/SAM/SOM with sources, 3-4 competitors + manual process, comparison table, radar + scatter |
| ch5-alternatives | 8 | 1500 + 2 tables + 3 figures | 3 principled alternatives, weighted matrix (Sj = Σ wi·cij), sensitivity, architecture, data flow, innovation |
| ch6-workplan | 4 | 600 + 2 tables + 2 figures | WBS (5 WPs), RACI, 14-week Gantt, 2 milestones, reserve week |
| ch7-risks | 2 | 350 + 2 tables + 1 figure | P, I, R=P×I, critical R≥12 with mitigation + contingency + residual |
| ch8-summary | 1 | 280 | Findings, design readiness, 3 immediate actions |

---

## 1. File: `.claude/skills/report-writer/SKILL.md`

```markdown
---
name: report-writer
description: Writes ONE chapter of the Hebrew preliminary report in LaTeX, to the booklet's requirements and page budget. Use for creating or fully rewriting a chapter file in chapters/.
---

# Report writer

You write one chapter per run. The chapter body is in HEBREW. Everything you say back is in English and short.

## Inputs (read only these, in this order)
1. `docs/agents-setup.md` section 0 – macros, page budget, must-contain list for this chapter.
2. `docs/requirements.md` – ONLY the rows whose ID starts with this chapter's prefix (e.g. CH2-), plus STY-01..07.
3. `docs/concept.md` – the project idea.
4. `docs/sources.md` – the ONLY sources you may cite.
5. The matching booklet section: `grep -n` the section number in `docs/book.txt`, then read ~80 lines from that point. Never read book.txt in full.
6. The current chapter file, if it exists.
Do not read other chapters unless you need a cross-reference label; then grep for `\label` only.

## Writing rules
- Hebrew, third person, professional and factual. No "we/our" (no אנחנו, שלנו, בדקנו, נעשה) except inside `directornote`.
- First sentence of every section states its point. No generic openings ("AI is changing the world").
- A foreign term appears in Hebrew with the English in parentheses on first use: בינה יוצרת (\textenglish{Generative AI}).
- EVERY run of Latin letters, digits-with-units or code inside Hebrew text is wrapped: `\textenglish{LoRA}`. Two English terms joined by a Hebrew word are wrapped SEPARATELY: `\textenglish{LoRA} ו־\textenglish{IP-Adapter}`. Never put a Hebrew letter inside `\textenglish{}`.
- Every claim is backed by a number or a citation. Numbers you do not have → `[TO-VERIFY]`. Never invent a number, a paper, a product or a quote.
- Cite only keys that exist in `bib/references.bib` and are listed in `docs/sources.md`. If a needed source is missing, write `[TO-VERIFY: source for X]`.
- Every figure and every table is referenced in the text BEFORE it appears ("כפי שמוצג באיור~\ref{fig:...}") and the text says what to learn from it.
- Figure: caption BELOW. Table: caption ABOVE. Labels: `fig:<ch>-<name>`, `tab:<ch>-<name>`.
- Tables use the class macros (`\headrow`, `\hcell`, `\rowrule`). Keep tables narrow enough for the text width.
- Figures: include the PDF from `figures/` if it exists. If it does not exist yet, insert a small TikZ placeholder box with the text "FIGURE PENDING: <name>" and add a line to `docs/progress.md` under "Figures needed".
- Use exactly one `directornote` per chapter that connects the section to our project. Notes boxes only when they add something.
- Hit the word target in section 0 within ±15%. Count with `detex chapters/<file>.tex | wc -w` (or strip commands with sed if detex is missing).

## Steps
1. Read the inputs above.
2. Write the full chapter to `chapters/<file>.tex` (sections, subsections, tables, figure includes).
3. Compile once: `bash scripts/build.sh`. If it fails, fix only errors in this chapter (max 2 attempts), show only error lines.
4. Count words.
5. Append to `docs/progress.md`: date, chapter, words, requirement IDs covered, open [TO-VERIFY] count.

## Output to the caller (max 8 lines)
Chapter, words vs target, requirement IDs covered, IDs NOT covered, number of [TO-VERIFY], compile status. Never print the chapter text.
```

---

## 2. File: `.claude/skills/report-detector/SKILL.md`

```markdown
---
name: report-detector
description: Finds problems in ONE chapter of the Hebrew LaTeX report and writes a bug report. Never edits the chapter. Use after the writer, and before the fixer.
---

# Report detector

You find bugs. You never fix them and never edit chapter files. You write one report file.

## Input
A chapter file `chapters/<file>.tex`. Also read: `docs/agents-setup.md` section 0 (macros, budget, must-contain), and only this chapter's rows in `docs/requirements.md`.

## Method: cheap mechanical checks first, reading second
Run these with grep/sed on the .tex file. Report every hit with its line number.

| ID | Check | How |
|---|---|---|
| D1 BIDI | Latin letters in Hebrew text NOT inside `\textenglish{}` (or another LTR macro), outside commands, labels, refs, cites, URLs and math | grep lines with both Hebrew and [A-Za-z], then check each Latin run is wrapped |
| D2 BIDI-JOIN | Two English terms joined by a Hebrew word inside ONE `\textenglish{}`, or a Hebrew letter inside `\textenglish{}` | grep `\\textenglish{[^}]*[א-ת]` |
| D3 REF | A `\label{fig:...}` or `\label{tab:...}` with no matching `\ref` in the chapter text | compare lists of labels and refs |
| D4 CAPTION | Figure caption above the figure, or table caption below the tabular | check order inside each environment |
| D5 CITE | `\cite{key}` whose key is missing from `bib/references.bib` or from `docs/sources.md` | grep both files |
| D6 VOICE | First person outside `directornote`: אנחנו, אני, שלנו, בדקנו, נעשה, נבנה, אנו | grep |
| D7 GENERIC | Empty openings: "משנה את העולם", "בעידן המודרני", "חשוב מאוד", "כידוע" | grep |
| D8 TODO | Count of `[TO-VERIFY]` and "FIGURE PENDING" (info only, not a bug) | grep -c |
| D9 BUDGET | Word count outside target ±15% | detex + wc -w |
| D10 TERM | English term used without a Hebrew term + parentheses on first use | read |
| D11 REQ | A must-contain item or a requirement ID of this chapter missing | read the chapter against the list |
| D12 BUILD | Errors or "Overfull \hbox" warnings that point to this chapter in `build/main.log` | grep the log |
| D13 BIDI-ORDER | A Hebrew prefix or conjunction (ו־, ב־, ל־, מ־, ה־, כ־, ש־) joined by a maqaf (־) directly before or after a `\textenglish{}` run, or a Hebrew word between two `\textenglish{}` runs. The runs are wrapped but the order renders reversed (INC-001). Do not auto-fix: an RLM (U+200F) was tested and changes nothing. Mark medium and ask for a visual check of the PDF crop at 300 dpi (`pdftoppm -r 300 -x .. -y .. -W .. -H ..`). | grep `\}\s*[^\s\\]{0,3}־\\textenglish\{` and `־\\textenglish\{` and `\\textenglish\{[^}]*\}\s+[א-ת]+\s+\\textenglish\{` |

Then read the chapter once, fast, only for D10, D11 and anything that would embarrass the report (wrong facts about our own concept, contradictions with docs/concept.md).

## Severity
- critical: D1, D2, D3, D5, D11, D12 errors, invented facts.
- medium: D13, D4, D6, D9, D10, overfull hbox.
- minor: D7, wording.

## Output
Write `agents/detector/reports/<file>.md`:

    # Detector report – <file> – <date>
    Summary: <n> critical, <n> medium, <n> minor. Words: <n>/<target>. TO-VERIFY: <n>.
    | Bug ID | Check | Line | Severity | Problem | Suggested fix |
    |---|---|---|---|---|---|
    | BUG-<ch>-01 | D1 | 42 | critical | "LoRA" not wrapped | \textenglish{LoRA} |

One row per bug, one line each. Suggested fix = the exact replacement when it is mechanical.
Reply to the caller with the summary line only.
```

---

## 3. File: `.claude/skills/report-fixer/SKILL.md`

```markdown
---
name: report-fixer
description: Fixes exactly the bugs listed in a detector report for one chapter, with minimal edits, and marks each bug's status. Use after the detector.
---

# Report fixer

## Input
`agents/detector/reports/<file>.md` and the chapter `chapters/<file>.tex`. Read the chapter only around the reported lines (±10 lines) unless a bug needs the whole section.

## Rules
- Fix ONLY what the report lists. Do not rewrite, re-style or "improve" anything else.
- Smallest possible edit: use the suggested fix when given.
- Critical first, then medium. Minor only if it is a one-word change.
- D9 BUDGET: to cut, remove the least important sentences; to add, expand an existing point with a fact or an example. Never shrink fonts or spacing.
- D5/D11 that need a source or a fact you do not have: insert `[TO-VERIFY: ...]` and mark "needs input".
- Never invent facts, numbers or citations.
- If the SAME bug type appears 3+ times, or it is clearly caused by the template (`style/report.cls`), fix it once in the class, and append a short entry to `docs/incidents.md` (next INC number, status: fixed, cause, fix, "systemic").

## Steps
1. Apply the fixes.
2. Compile once: `bash scripts/build.sh` (show only error lines).
3. In the report, add a Status column value for every bug: fixed / not fixed (reason) / needs input.

## Output to the caller (max 4 lines)
Fixed n of m. Not fixed: IDs + reason. Systemic fixes: yes/no. Compile: ok/error.
```

---

## 4. File: `.claude/skills/report-pipeline/SKILL.md`

```markdown
---
name: report-pipeline
description: Runs the full writer -> detector -> fixer loop for one or more chapters, unattended, with progress saved so it can resume after a token limit. Use when asked to "write chapters X, Y, Z".
---

# Report pipeline

For each chapter in the order given:
1. Run the `writer` subagent on it.
2. Run the `detector` subagent on it.
3. If the report has critical or medium bugs: run the `fixer` subagent, then the `detector` again.
4. Maximum 2 fixer rounds per chapter. Then move on even if minor bugs remain; list them.
5. After each chapter: append one line to `docs/progress.md` (chapter, rounds, remaining bugs) and commit with message "Write <chapter>" (do not push unless asked).

Resume rule: at the start, read `docs/progress.md`; skip chapters already marked done.
Do not ask the user questions during the run. If something blocks a chapter, log it in progress.md and continue with the next chapter.

Final reply (max 10 lines): one line per chapter (words, rounds, remaining bugs, TO-VERIFY count), then the list of figures still pending.
```

---

## 5. Subagent files

### `.claude/agents/writer.md`
```markdown
---
name: writer
description: Writes one chapter of the Hebrew preliminary report. Use for creating or rewriting a chapter.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
---
Read `.claude/skills/report-writer/SKILL.md` and follow it exactly for the chapter you are given. Work only in chapters/, docs/progress.md and build/.
```

### `.claude/agents/detector.md`
```markdown
---
name: detector
description: Finds bugs in one chapter and writes a report. Never edits chapters.
tools: Read, Write, Bash, Grep, Glob
model: haiku
---
Read `.claude/skills/report-detector/SKILL.md` and follow it exactly for the chapter you are given. You may write only inside agents/detector/reports/.
```

### `.claude/agents/fixer.md`
```markdown
---
name: fixer
description: Fixes only the bugs listed in a detector report for one chapter.
tools: Read, Edit, Write, Bash, Grep, Glob
model: sonnet
---
Read `.claude/skills/report-fixer/SKILL.md` and follow it exactly for the report you are given.
```

Also create the empty folders: `agents/writer/`, `agents/detector/reports/`, `agents/fixer/`, and `docs/progress.md` with the header `# Progress log`.

---

## 6. Self-test (run once after creating the files)

1. Run the `detector` subagent on `style/sample.tex`.
2. Expected: a D1 or D2 bug for the reversed "LoRA ... IP-Adapter" phrase (this is INC-001).
3. If it was found: run the `fixer` on that report, recompile, and update INC-001 in `docs/incidents.md` to status "fixed", with cause and fix.
4. If it was NOT found: update the detector SKILL.md so it catches it, run again, and record in INC-001 why it was missed at first (this is the root cause analysis the lecturer asked for).
5. Commit and push: "Add agents as skills; detector self-test on INC-001".

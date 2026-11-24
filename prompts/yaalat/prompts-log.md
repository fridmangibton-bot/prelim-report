# Prompts log (yaalat) - Claude Code

Tool: Claude Code, working in this repository. Dates are the day the prompt was sent (2026).
Prompts are word for word; the line below each date says what it was for.
Left out: autosuggestions, approvals such as "continue", duplicates, and shell commands typed with `!`.
Personal details were checked; none appear in the prompts below.

---

### 001
2026-11-19. Purpose: Convert the booklet PDF to text and set up docs/ for the project.

> 1. Convert docs/preparation-report-book.pdf to a text file docs/book.txt using a tool already installed on my machine.
> 2. Run git init.
> 3. Create .gitignore containing: .env, *.aux, *.log, *.toc, *.out, *.fls, *.fdb_latexmk, *.synctex.gz

### 002
2026-11-19. Purpose: Rewrite CLAUDE.md as a short instruction file.

> <pasted_content id="f9f5">
> Rewrite CLAUDE.md to be short (max 40 lines), in English, with only these standing rules:
> - Project: a ~40-page preliminary report (Hebrew "doch mechin") written in LaTeX with LuaLaTeX. Concept: docs/concept.md. Requirements: docs/requirements.md.
> - Institution for the title page: University of Haifa, Department of Data Science.
> - The report body text is written in HEBREW. Everything else (code, comments, file names, skills, agent instructions, logs) is in English.
> - Never read docs/book.txt in full. When a booklet chapter is needed, grep for its section number and read only that part.
> - One chapter per file in chapters/. Main file: main.tex. Template: style/.
> - Charts only from Python code in figures/python. Diagrams only from TikZ in figures/tikz. No images from the internet.
> - Hebrew text: third person, professional tone. A foreign term appears in parentheses on first use.
> - Never invent sources. A source enters the report only if listed in docs/sources.md.
> - Any number without a source is marked [TO-VERIFY]. All [TO-VERIFY] markers must be resolved before submission.
> - Secrets and API keys only in .env or environment variables, never in code.
> - Compile: latexmk -lualatex main.tex. On errors, show only the error lines from the log, not the full log.
> </pasted_content id="f9f5">

### 003
2026-11-19. Purpose: First commit: CLAUDE.md, requirements and docs.

> commit all files with the message "Setup: CLAUDE.md, requirements and concept docs"

### 004
2026-11-19. Purpose: Create the project structure and LaTeX skeleton from booklet chapter 13.

> Set up the project structure according to chapter 13 of the booklet (grep "13.1" in docs/book.txt and read only that section):
> - main.tex, style/, chapters/, figures/python/, figures/tikz/, bib/references.bib, docs/sources.md (empty), docs/incidents.md (empty)
> - One chapter file per chapter, following table 1.1 in docs/requirements.md: ch1-intro, ch2-problem, ch3-literature, ch4-market, ch5-alternatives, ch6-workplan, ch7-risks, ch8-summary
> - Front matter files: titlepage, abstract (executive summary + keywords), abbreviations
> - Each chapter file contains only Hebrew headings and subheadings, plus an English comment with its page budget
> - Use a temporary, plain template only. Design comes in the next step.
> Then compile and show me the PDF was created with a table of contents.

### 005
2026-11-19. Purpose: Commit the project structure.

> commit all files with the message "Project structure and LaTeX skeleton"

### 006
2026-11-19. Purpose: Untrack main.pdf and the bib helper files; add them to .gitignore.

> untrack main.pdf and *-blx.bib, add them to .gitignore, and commit

### 007
2026-11-20. Purpose: Clean up the build (latexmkrc, output to build/).

> <pasted_content id="d9dc">
> Clean up the build:
> 1. Create a .latexmkrc so all LaTeX auxiliary files and the PDF are written to a build/ folder.
> 2. Delete the existing auxiliary files (main.aux, main.log, main.toc, etc.) and main-blx.bib from the project root.
> 3. Untrack main.pdf and main-blx.bib from git, and make sure build/ is in .gitignore.
> 4. Update the compile instructions in CLAUDE.md accordingly.
> 5. Recompile once to confirm build/main.pdf is created, then commit with the message "Move build output to build/".
> </pasted_content id="d9dc">

### 008
2026-11-20. Purpose: Read booklet chapter 15 and propose the report design directions.

> <pasted_content id="558c">
> Read chapter 15 of the booklet (grep "15.2" and "15.3" in docs/book.txt) and prepare to build style/report.cls.
> Project topic: AI-generated narrative video series with persistent characters. I want a design that feels like a "production studio", not a standard academic template.
> Before writing any code, propose 3 different design directions. For each give:
> - A color palette (3-4 colors with HEX codes)
> - Chapter heading style (e.g. a film-strip, clapperboard or storyboard motif drawn in TikZ)
> - Page background or frame, headers and footers
> - Box styles (note / warning / "in our project")
> Also note: the current template adds a blank page before each chapter. The new design must not do that (chapters start on the next page, no blank pages).
> Do not build yet. Wait for my choice.
> </pasted_content id="558c">

### 009
2026-11-20. Purpose: Build the core design in style/report.cls (Creator's Pre-Production Journal).

> Build the core design in style/report.cls (replace direction C). Keep it simple and robust - extras come later.
> Concept: "Creator's Pre-Production Journal" - a handmade film-journal look that expresses authentic human creation. A preliminary report is the "pre-production" stage of a project. Everything is drawn in TikZ - no image files.
>
> Palette (named colors): paper #F8F3E8, ink #1E1B2E, brandMain #D6336C, brandAccent #F2C12E, brandHighlight #D9C8F5. Never use brandAccent for text. No purple.
>
> Rule 80/20: body pages stay calm and readable. Decoration only on chapter openers, boxes and the footer.
>
> Core elements only:
> 1. Page: cream paper background (paper color) on all pages. Body text in ink.
> 2. Chapter opener: a solid ink panel with a scalloped bottom edge (a row of small half-circles in TikZ). Chapter number and title in cream (paper color) Hebrew sans, and a brandMain pill tag "SCENE 0X" with white text. The panel takes at most 1/3 of the page, and the text starts on the same page. The table of contents shows the normal chapter titles.
> 3. Section headings: Hebrew sans in ink, with a short brandMain underline.
> 4. Tables: header row in ink with cream text, thin light rule between rows, caption above the table.
> 5. Boxes: the "in our project" box is a post-it note titled "הערת במאי" (brandAccent background, ink text). The note box has a brandHighlight background with ink text.
> 6. Footer: a thin ink film strip across the page width with a frame-style page number (like "12A") and progress "chapter X/8" shown as small brandMain segments.
>
> Fonts: headings in a Hebrew sans font (Arial or Segoe UI). Body text in David.
>
> Mandatory rules from table 11.1 in the booklet: Hebrew font size 11-12pt, 1.5 line spacing, justified text, 2.5 cm margins plus 0.5 cm binding gutter on the RIGHT (Hebrew book), figure captions below figures, table captions above tables, numbering per chapter, front matter numbered separately.
>
> No blank pages before chapters. Verify this in the compiled PDF.
>
> Also:
> - Save the palette to style/palette.json so the Python charts use the same colors.
> - Write docs/design-decisions.md (short, in English): the concept, each element and why we chose it, and what we deliberately left out (photos, cut-outs, stickers) and why.
>
> Compile one sample chapter opener page with a section heading, a paragraph mixing Hebrew and English, a table and a post-it box. If anything fails, report it instead of retrying more than twice.

### 010
2026-11-20. Purpose: Commit the core design.

> commit all files with the message "Core design: Creator's Pre-Production Journal class"

### 011
2026-11-20. Purpose: Log the first BiDi problem as INC-001.

> Log this in docs/incidents.md as INC-001 (status: open): in build/sample.pdf, the phrase "LoRA [Hebrew vav + maqaf] IP-Adapter" renders in reversed order (IP-Adapter appears first when read right-to-left) and the vav is attached to LoRA - a BiDi issue (booklet ch.14). Also log the 4 issues you fixed while building the class (class name clash, TikZ shifted in RTL, mirrored margins, underline position) as INC-002 to INC-005 (status: fixed), each with cause and fix. Then commit.

### 012
2026-11-20. Purpose: Create the English README and check for secrets before the first push.

> <pasted_content id="7c19">
> 1. Create a README.md in English with these sections:
>    - Project title and a 3-line description (preliminary report for a Hebrew-first AI showrunner platform; University of Haifa, Department of Data Science)
>    - Concept: "Creator's Pre-Production Journal" design, linking to docs/design-decisions.md
>    - Folder structure: a tree with one line explaining each folder
>    - How to build: requirements (MiKTeX, LuaLaTeX, Python), the command latexmk main.tex, output in build/main.pdf
>    - Agents workflow: writer -> detector -> fixer loop, built as skills in .claude/skills (to be added)
>    - Quality process: docs/requirements.md checklist and docs/incidents.md root cause log
>    - Status: a checklist of chapters 1-8 (all unchecked for now)
>    - Team: placeholders [NAME 1], [NAME 2] - no ID numbers or emails
> 2. Check that no secrets, ID numbers or personal emails are in any tracked file.
> 3. Commit the README, then add the remote origin https://github.com/fridmangibton-bot/prelim-report.git and push the master branch.
> </pasted_content id="7c19">

### 013
2026-11-20. Purpose: Untrack docs/book.txt and remove it from earlier commits.

> Untrack it and also remove docs/book.txt from all previous commits (you are rewriting history anyway for the email). Add it to .gitignore and keep the local file so agents can still grep it.

### 014
2026-11-20. Purpose: Confirm that docs/book.txt is in no pushed commit.

> Confirm that docs/book.txt does not appear in any commit that was pushed to GitHub.

### 015
2026-11-21. Purpose: Create the writer, detector and fixer agents and skills from docs/agents-setup.md.

> <pasted_content id="32a1">
> Read docs/agents-setup.md and create every file it defines.
> Before writing: open style/report.cls and check the real names of the LaTeX macros listed in section 0. Use the real names consistently in docs/agents-setup.md AND in every skill file. If the class has no macro for wrapping English inside Hebrew, add \newcommand{\en}[1]{\LR{#1}} to the class (or the correct equivalent for this class) and note it in docs/design-decisions.md.
> Then run the self-test in section 6, including the commit and push.
> Keep your final reply short: files created, macro names used, and the self-test result for INC-001.
> </pasted_content id="32a1">

### 016
2026-11-21. Purpose: Close INC-001 as a false alarm and tidy the incident log.

> 1. Close INC-001 in docs/incidents.md as "not a bug (false alarm)": the source order renders correctly; the human reviewer misread a low-resolution screenshot. Lesson: mixed Hebrew/English must be checked at high resolution; D13 stays a visual-confirmation check.
> 2. latexmk fails because perl is missing. Create scripts/build.sh that compiles main.tex into build/ with lualatex, runs bibtex, then lualatex twice more, and prints only error lines. Replace every "latexmk" instruction in CLAUDE.md, README.md, docs/agents-setup.md and all skill files with "bash scripts/build.sh".
> 3. Confirm the self-test commit exists, then commit these changes and push.

### 017
2026-11-21. Purpose: Create figures/python/make_figures.py with the five charts.

> <pasted_content id="d9b8">
> Create figures/python/make_figures.py that generates all report charts as PDF files in figures/.
> - Read colors from style/palette.json (paper, ink, brandMain, brandAccent, brandHighlight). Chart background = paper.
> - Hebrew labels must render right-to-left correctly in matplotlib (use python-bidi or reverse the strings; install what is missing with pip). Use a Hebrew-capable font (Arial).
> - Data lives in JSON files in figures/python/data/, never hard-coded. Mark every placeholder value with "placeholder": true, and print a warning listing placeholder charts.
> - Charts:
>   1. ch4 radar (6 axes: consistency, cost, Hebrew support, narrative continuity, ease of use, creator control) for 4 competitors + our solution. Placeholder data for now.
>   2. ch4 scatter: cost per finished minute (USD) vs character consistency. Placeholder data for now.
>   3. ch5 weighted decision matrix for alternatives A (own fine-tuned model), B (agent layer over commercial APIs), C (hybrid open-source + API). Weights, fixed BEFORE scoring: quality/consistency 0.25, cost per minute 0.20, Hebrew support 0.20, development time 0.15, vendor dependency 0.10, privacy/IP control 0.10. Scores 1-5 with a one-line rationale each in weights.json. Assert weights sum to 1.0. Output: stacked bar chart of each criterion's contribution, plus a sensitivity check (does the winner change if any weight moves by +/-0.1?) saved as a small table in figures/python/data/sensitivity.md.
>   4. ch6 Gantt: 14 weeks, 5 work packages from docs/concept.md, critical path in brandMain, 2 milestones, a reserve week before each milestone.
>   5. ch7 risk matrix P vs I (1-5), critical zone R>=12 shaded, risks from docs/concept.md.
> - Run the script with python and confirm all 5 PDFs exist. Then commit and push.
> </pasted_content id="d9b8">

### 018
2026-11-21. Purpose: Commit and push pending work.

> commit and push if anything is not pushed yet

### 019
2026-11-21. Purpose: Log INC-006 (mixed Hebrew/English chart labels).

> <pasted_content id="d9b8">
> Log INC-006 in docs/incidents.md: Hebrew labels that mix English terms (API, AI, IP, WP1) render in the wrong order in the matplotlib charts, and some labels are clipped. Cause: matplotlib's built-in bidi does not handle mixed-direction labels with punctuation.
> Fix in figures/python/make_figures.py:
> 1. Avoid mixed labels where possible: "WP1:" becomes "חבילה 1:"; put English terms at the END of a Hebrew label, never in the middle or start.
> 2. For labels that must stay mixed, force the right order (e.g. wrap the English run with Unicode LRI/PDI isolates, or process with python-bidi using base_dir 'R'), and verify each mixed label renders correctly by rendering it and checking the order.
> 3. Fix clipping: wrap long tick labels onto two lines, use tight bbox, keep milestone labels inside the plot without overlap, and keep the placeholder watermark fully visible.
> Regenerate all 5 charts, mark INC-006 fixed with cause and fix, then commit and push.
> </pasted_content id="d9b8">

### 020
2026-11-21. Purpose: List the available subagents.

> List the subagents available in this project.

### 021
2026-11-21. Purpose: Run the report-pipeline skill on the first chapters.

> Use the report-pipeline skill to write these chapters, in this order: ch2-problem, ch6-workplan, ch7-risks.
> Use the existing figures in figures/ (the Gantt chart in ch6, the risk matrix in ch7). Numbers that need an external source get [TO-VERIFY].
> Do not ask me questions during the run. At the end, build the full PDF, then commit and push.

### 022
2026-11-21. Purpose: Update the chapter 4 charts from the verified market data.

> <pasted_content id="d6a1">
> Update the chapter 4 charts from docs/market-data.md:
> 1. Radar: use the 4 competitors + our design target with the scores in section 3. Move axis labels further outside the circle so no label overlaps a data line at value 5.
> 2. Replace the scatter with section 2: X = monthly price of the cheapest plan with consistent characters (USD), Y = capability coverage 0-4. Draw our solution as a "design target" marker. Prices marked [TO-VERIFY] (Atlabs, CapCut) are plotted with an asterisk and a footnote "price to be confirmed".
> 3. Remove the placeholder flag and watermark from these two charts only. Add the caption basis from section 3.
> Regenerate, check the Hebrew renders correctly, then commit and push.
> </pasted_content id="d6a1">

### 023
2026-11-21. Purpose: Run the report-pipeline skill on the next chapters.

> <pasted_content id="333e">
> Use the report-pipeline skill to write these chapters, in this order: ch3-literature, ch4-market, ch1-intro.
> Cite only sources from docs/sources.md and bib/references.bib.
> ch3: MovieDreamer (zhao2025moviedreamer) is the flagship paper. Use the exact knowledge-gap sentence from docs/sources.md and follow its "careful wording note": never claim that no product keeps characters across episodes; the gap is plot memory, contradiction detection and Hebrew. The chapter figure is a TikZ diagram drawn inline (e.g. the families of approaches: single-image consistency -> multi-shot video -> multi-agent storytelling -> our gap), not a pending placeholder.
> ch4: use docs/market-data.md for the competitor table (all 5 products, monthly prices as of 21.11.2026), and add a column for the flagship paper, as in booklet table 6.1. Use the updated charts. Market size as three layers: TAM = the Fortune Business Insights figure, presented as a range together with MarketsandMarkets (note the CAGR period 2026-2034); SAM and SOM = transparent team estimates, each with its assumptions written out in the text and marked as team estimates. Never present an estimate as sourced. State the limitations openly: some tools could not be tested without paying, so ease-of-use scores are partly estimated, and Atlabs Hebrew support is based on correspondence with its support team.
> ch1: use the market figures from docs/sources.md.
> Do not ask me questions during the run. At the end, build the full PDF, then commit and push.
> </pasted_content id="333e">

### 024
2026-11-21. Purpose: Stop background shells and commit the bibliography.

> Stop any background shell that is still running. Then commit bib/references.bib, docs/sources.md and the regenerated figure PDFs with the message "Verified sources and market data", and push.

### 025
2026-11-22. Purpose: Fix docs/team.md, which was created as a folder by mistake.

> docs/team.md is a folder created by mistake. Find the text file inside it, then replace the folder with a single UTF-8 file docs/team.md that has the same content. Confirm it has 3 lines (student names, advisor, course name).

### 026
2026-11-22. Purpose: Finish the whole report in one run (chapters, front matter, charts, final PDF).

> <pasted_content id="5b78">
> Finish the report in one run. Do not ask me questions; log anything blocking in docs/progress.md and continue. If the session limit stops you, the next session continues from docs/progress.md.
>
> 1. Charts: the team approves the current weights and scores in the decision-matrix data as the team's assessment. Remove the placeholder flag and the "dummy data" watermark from the decision matrix, Gantt and risk matrix charts (team assessments, not sourced facts). Regenerate the charts.
> 2. Use the report-pipeline skill to write ch5-alternatives, then ch8-summary.
> 3. Front matter: title page with University of Haifa, Department of Data Science, the Hebrew and English titles from docs/concept.md, the Hebrew words for "preliminary report", student names, advisor and course name from docs/team.md, date November 2026. No ID numbers or emails. Abbreviations list built from the terms used in the report.
> 4. Cleanup across all chapters:
>  - CH3-06 is done: all sources in docs/sources.md were verified on 2026-11-21. Mark it in docs/requirements.md.
>  - MarketsandMarkets: state the period 2022-2027 and that the source rounds its figures.
>  - SAM/SOM inputs (100,000 Hebrew-speaking creators, $25/month, 0.5% penetration) stay, labelled as team assumptions, not [TO-VERIFY].
>  - Decision scores, schedule and risk scores are labelled as team assessments, not [TO-VERIFY].
>  - Replace the ch6 WBS placeholder with a TikZ WBS diagram of the 5 work packages.
>  - Fix overfull-box warnings and bring ch1 into its word range.
>  - Any [TO-VERIFY] that remains: list it in docs/progress.md with page and reason. Never invent numbers.
> 5. Run the detector once more on every chapter; fix critical bugs only.
> 6. Write the executive summary now, from the final chapters: one paragraph of 250-350 Hebrew words plus 5-7 keywords.
> 7. Build the full PDF. Report the page count (target: 40 body pages plus front matter); adjust only if it is off by more than 3 pages.
> 8. Copy build/main.pdf to report/main.pdf, update the README status checklist, commit (including docs/team.md) and push.
> Final reply, max 12 lines: page count, chapters done, remaining [TO-VERIFY] list, open bugs.
> </pasted_content id="5b78">

### 027
2026-11-23. Purpose: Fix report/main.pdf missing on GitHub (INC-007) and apply the 2026-11-23 fixes.

> <pasted_content id="d215">
> 1. report/main.pdf is missing on GitHub: the "main.pdf" rule in .gitignore also ignores report/main.pdf. Add the exception "!report/main.pdf" to .gitignore so that only build output stays ignored. Log this as INC-007 in docs/incidents.md: the agent reported a file as pushed but git had ignored it; root cause = an overly broad .gitignore pattern; prevention = after every push, verify with "git ls-tree -r origin/master --name-only" that the expected files are on the remote.
> 2. Apply every item in docs/fixes-2026-11-23.md: update bib/references.bib, docs/sources.md, docs/market-data.md, docs/concept.md (new knowledge-gap sentence), the affected chapters and the scatter chart. Make sure the executive summary, ch1 and ch8 match the new knowledge-gap wording; keep the summary at 250-350 words.
> 3. Run the detector on the changed chapters and fix critical bugs. List any [TO-VERIFY] still left (should be zero except the CapCut footnote).
> 4. Run "git status --ignored" and check that nothing except build output, the booklet text and .env is ignored. Fix anything else that should be tracked, and report it.
> 5. Add a permanent rule to CLAUDE.md: after every push, verify with git ls-tree that the expected files are on the remote before reporting success.
> 6. Build the PDF, copy it to report/main.pdf, commit and push. Then run "git ls-tree -r origin/master --name-only | grep report" and show me the output, to prove report/main.pdf is on GitHub.
> Final reply, max 12 lines: markers left, page count, open bugs, ignored files found, and the ls-tree output.
> </pasted_content id="d215">

### 028
2026-11-23. Purpose: Make the ch4 radar cost axis follow the verified prices.

> Fix the ch4 radar "low cost" axis so it follows the prices (cheaper = higher): CapCut 4, our design target 4, LTX Studio 3, Atlabs 3, LongStories 2. Update docs/market-data.md, the radar chart and the ch4 text. Change the data date in ch4 to "21-22.11.2026". Build, copy to report/main.pdf, commit, push and verify with git ls-tree.

### 029
2026-11-24. Purpose: Apply the human PDF review fixes, detector check D15, INC-008 and the final requirements check.

> <pasted_content id="9503">
> First run git pull to get any changes my partner pushed.
> 1. Apply every item in docs/review-fixes-2026-11-24.md: the systemic fixes in section A first, then the single fixes in section B.
> 2. Fix the remaining medium bugs listed in agents/detector/reports/ for ch1 and ch4.
> 3. Add check D15 from section C to the detector SKILL.md. Rebuild, then run the detector (including D15 on the rendered PDF) on ALL chapters and the front matter, because the class changes affect every page. Fix critical and medium bugs. Log INC-008 from section D.
> 4. Final check: go through docs/requirements.md item by item, including the signature checklist in section ו, against the compiled PDF. Mark [x] what is covered and list anything missing. Confirm: no [TO-VERIFY], no "??", executive summary 250-350 words, every figure and table referenced in the text, page count close to 40 body pages.
> 5. Update the README status to final.
> 6. Build, copy to report/main.pdf, commit and push, and verify with git ls-tree that report/main.pdf is on the remote.
> Final reply, max 15 lines: findings fixed / not fixed and why, D15 results, requirements checklist result, page count.
> </pasted_content id="9503">

### 030
2026-11-24. Purpose: Ch3 flagship justification and comparison, ch4 audience segmentation, writer/detector/fixer pass.

> <pasted_content id="9503">
> Keep MovieDreamer as the flagship paper. In ch3, add an explicit justification: it addresses narrative coherence and character identity over a full film, it is peer-reviewed (ICLR 2025), and it reports quantitative metrics; its missing public code is stated openly as a reproducibility limitation. DramaAgent (AACL, November 2026) was published after the flagship selection and is presented as the closest recent work, in a short comparison with MovieDreamer.
> The body is about 36 of 40 pages. Add about 3 pages of substantive content, using only existing sources and team decisions, never invented facts: ch3 (the justification, the MovieDreamer vs DramaAgent comparison, and a short subsection on threats to validity of the literature review), and ch4 (target-audience segmentation: YouTube storytellers, TikTok character creators, ad agencies as a future extension, each with needs and pain points).
> Run the writer, detector (including D15) and fixer on ch3 and ch4. Build, check the page count, copy to report/main.pdf, commit and push, and verify with git ls-tree.
> Final reply, max 8 lines: page count, D15 result, open bugs.
> </pasted_content id="9503">

### 031
2026-11-24. Purpose: Review the docs edits against the report and fix the remaining first-use glosses.

> Run git diff HEAD~1 -- docs/concept.md docs/sources.md. Keep a change only if it matches what the report now says; revert anything else. Also fix the first-use glosses BUG-3-11, BUG-3-13 and BUG-ch4-09 (skip the unreferenced labels). Rebuild, copy to report/main.pdf, commit, push, verify with git ls-tree. Reply in max 4 lines.

### 032
2026-11-24. Purpose: Create prompts/yaalat/ with this prompts log.

> First run git pull (Adi pushed changes). Then create prompts/yaalat/ in the same style as Adi's prompts folder. Extract every prompt I typed in this project, verbatim and in chronological order, from the Claude Code session transcripts in ~/.claude/projects/ for this folder. Save them as prompts/yaalat/prompts-log.md with a date and a one-line purpose for each prompt. Skip autosuggestions, "yes"/"continue" approvals and duplicates. Also copy docs/prompts-en.md there as prompts/yaalat/step-prompts.md. Before committing, scan for secrets (tokens, API keys, emails, ID numbers) and redact any. Add a short README.md in prompts/yaalat/. Commit, push, verify with git ls-tree. Reply in max 4 lines.

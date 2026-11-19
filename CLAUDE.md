# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project
- A ~40-page preliminary report (Hebrew "doch mechin") written in LaTeX, compiled with LuaLaTeX.
- Concept: `docs/concept.md`. Requirements: `docs/requirements.md`.
- Title page institution: University of Haifa, Department of Data Science.

## Language
- The report body text is in HEBREW. Everything else is in English: code, comments, file names, skills, agent instructions, logs.

## Reading the booklet
- Never read `docs/book.txt` in full. When a booklet chapter is needed, grep for its section number and read only that part.

## Structure
- One chapter per file in `chapters/`. Main file: `main.tex`. Template: `style/`.
- Charts only from Python code in `figures/python`. Diagrams only from TikZ in `figures/tikz`. No images from the internet.

## Writing rules
- Hebrew text: third person, professional tone. A foreign term appears in parentheses on first use.
- Never invent sources. A source enters the report only if it is listed in `docs/sources.md`.
- Any number without a source is marked [TO-VERIFY]. All [TO-VERIFY] markers must be resolved before submission.

## Secrets
- Secrets and API keys only in `.env` or environment variables, never in code.

## Build
- Compile: `latexmk -lualatex main.tex`.
- On errors, show only the error lines from the log, not the full log.

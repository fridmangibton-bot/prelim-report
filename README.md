# A Hebrew-First Multi-Agent "Showrunner" Platform for Narrative-Consistent AI Video Series

Preliminary report (Hebrew "doch mechin", ~40 pages) for a Hebrew-first AI showrunner platform.
The platform helps creators produce video series with recurring characters while keeping the story consistent across episodes.
University of Haifa, Department of Data Science.

## Concept

The report uses the **"Creator's Pre-Production Journal"** design: a handmade film-journal look that expresses authentic human creation. The preliminary report is treated as the "pre-production" stage of the project. All graphics are drawn in TikZ, and the report uses no image files. Body pages stay calm, and decoration appears only on chapter openers, boxes and the footer.

The elements, the palette and what was deliberately left out are explained in [docs/design-decisions.md](docs/design-decisions.md).

## Folder structure

```
.
├── main.tex            # Main file: front matter, chapters, bibliography
├── .latexmkrc          # Build config: LuaLaTeX, all output to build/
├── chapters/           # One chapter per file (ch1-intro ... ch8-summary), Hebrew body text
├── frontmatter/        # Title page, executive summary, abbreviations
├── bib/                # references.bib (only sources listed in docs/sources.md)
├── style/              # report.cls (the design), palette.json (shared colors), sample.tex (design sample)
├── figures/
│   ├── python/         # Python scripts that generate all charts
│   └── tikz/           # TikZ sources for all diagrams
├── docs/               # Concept, requirements checklist, sources, design decisions, incidents log
└── build/              # Compiled output (git-ignored)
```

## How to build

Requirements:

- [MiKTeX](https://miktex.org/) (or TeX Live) with **LuaLaTeX** and `latexmk`
- Fonts: David and Arial (included with Windows)
- Python 3, for generating charts in `figures/python`

Build:

```
latexmk main.tex
```

The output is `build/main.pdf`. To build the one-page design sample, run `latexmk style/sample.tex`, which writes `build/sample.pdf`.

## Agents workflow

The report is written with an agent loop:

```
writer -> detector -> fixer -> (back to detector until clean)
```

- **writer** drafts a chapter according to `docs/requirements.md` and the booklet.
- **detector** checks the draft and the compiled PDF against the rules, for example sources, `[TO-VERIFY]` markers, captions and BiDi.
- **fixer** resolves what the detector found and records root causes.

The agents will be built as skills in `.claude/skills/`. They have not been added yet.

## Quality process

- [docs/requirements.md](docs/requirements.md) is the checklist of mandatory requirements (structure, style, figures, sources). Each item is checked off when it is met.
- [docs/incidents.md](docs/incidents.md) is the root cause log. Every build or rendering problem gets an ID, a status, its cause and its fix.

## Status

- [ ] Chapter 1: Introduction
- [ ] Chapter 2: Problem definition
- [ ] Chapter 3: Literature review
- [ ] Chapter 4: Market research
- [ ] Chapter 5: Design alternatives
- [ ] Chapter 6: Work plan
- [ ] Chapter 7: Risks
- [ ] Chapter 8: Summary

## Team

- [NAME 1]
- [NAME 2]

"""Build prompts/yaalat/prompts-log.md from build/prompts.json (output of extract_prompts.py)."""
import json
from pathlib import Path

d = json.load(open("build/prompts.json", encoding="utf-8"))
skip = {0, 4, 5, 29}  # "model" (picker), a "!" shell command with a personal email, an empty bash echo, "continue"
purpose = {
    1: "Convert the booklet PDF to text and set up docs/ for the project.",
    2: "Rewrite CLAUDE.md as a short instruction file.",
    3: "First commit: CLAUDE.md, requirements and docs.",
    6: "Create the project structure and LaTeX skeleton from booklet chapter 13.",
    7: "Commit the project structure.",
    8: "Untrack main.pdf and the bib helper files; add them to .gitignore.",
    9: "Clean up the build (latexmkrc, output to build/).",
    10: "Read booklet chapter 15 and propose the report design directions.",
    11: "Build the core design in style/report.cls (Creator's Pre-Production Journal).",
    12: "Commit the core design.",
    13: "Log the first BiDi problem as INC-001.",
    14: "Create the English README and check for secrets before the first push.",
    15: "Untrack docs/book.txt and remove it from earlier commits.",
    16: "Confirm that docs/book.txt is in no pushed commit.",
    17: "Create the writer, detector and fixer agents and skills from docs/agents-setup.md.",
    18: "Close INC-001 as a false alarm and tidy the incident log.",
    19: "Create figures/python/make_figures.py with the five charts.",
    20: "Commit and push pending work.",
    21: "Log INC-006 (mixed Hebrew/English chart labels).",
    22: "List the available subagents.",
    23: "Run the report-pipeline skill on the first chapters.",
    24: "Update the chapter 4 charts from the verified market data.",
    25: "Run the report-pipeline skill on the next chapters.",
    26: "Stop background shells and commit the bibliography.",
    27: "Fix docs/team.md, which was created as a folder by mistake.",
    28: "Finish the whole report in one run (chapters, front matter, charts, final PDF).",
    30: "Fix report/main.pdf missing on GitHub (INC-007) and apply the 2026-11-23 fixes.",
    31: "Make the ch4 radar cost axis follow the verified prices.",
    32: "Apply the human PDF review fixes, detector check D15, INC-008 and the final requirements check.",
    33: "Ch3 flagship justification and comparison, ch4 audience segmentation, writer/detector/fixer pass.",
    34: "Review the docs edits against the report and fix the remaining first-use glosses.",
    35: "Create prompts/yaalat/ with this prompts log.",
}
lines = [
    "# Prompts log (yaalat) - Claude Code",
    "",
    "Tool: Claude Code, working in this repository. Dates are the day the prompt was sent (2026).",
    "Prompts are word for word; the line below each date says what it was for.",
    "Left out: autosuggestions, approvals such as \"continue\", duplicates, and shell commands typed with `!`.",
    "Personal details were checked; none appear in the prompts below.",
    "",
    "---",
    "",
]
n = 0
for i, x in enumerate(d):
    if i in skip:
        continue
    n += 1
    ts = x["ts"][:10]
    lines.append(f"### {n:03d}")
    lines.append(f"{ts}. Purpose: {purpose[i]}")
    lines.append("")
    for ln in x["text"].split("\n"):
        lines.append("> " + ln if ln.strip() else ">")
    lines.append("")
Path("prompts/yaalat").mkdir(parents=True, exist_ok=True)
Path("prompts/yaalat/prompts-log.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(n, "prompts")

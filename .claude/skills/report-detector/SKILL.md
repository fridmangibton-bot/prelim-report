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
| D15 RENDERED-TEXT | Bugs that exist only in the compiled PDF (BiDi order, lost spaces, split parentheses). Run on the pdftotext OUTPUT, never on the .tex. Rules: `--`; a backtick or `''`; `TO-VERIFY` or `??`; a digit glued to a Latin word (`[0-9][A-Z]{2,}` or `[A-Z]{2,}[0-9]{4}`, ignore report IDs and DOIs in the references); a space inside parentheses (`\( ` or ` \)`); two Latin words glued by a lowercase-to-uppercase step (list hits for a human decision, many are real names such as StoryDiffusion); a Latin word split by a hyphen at a line end. Critical for the first four rules, medium for the rest. | `pdftotext -enc UTF-8 -layout build/main.pdf build/check.txt && py scripts/d15_check.py build/check.txt` (needs a fresh build; `-enc UTF-8` is required or Hebrew becomes U+FFFD) |

Then read the chapter once, fast, only for D10, D11 and anything that would embarrass the report (wrong facts about our own concept, contradictions with docs/concept.md).

## Severity
- critical: D1, D2, D3, D5, D11, D12 errors, D15 (first four rules), invented facts.
- medium: D13, D4, D6, D9, D10, D15 (other rules), overfull hbox.
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

# Design decisions

Implementation: `style/report.cls`. Palette: `style/palette.json` (used by the Python charts). Sample page: `style/sample.tex`, which builds to `build/sample.pdf` via `latexmk style/sample.tex`.

## Concept: "Creator's Pre-Production Journal"

A preliminary report is the pre-production stage of the project. The design looks like a handmade film journal and expresses authentic human creation. That fits a project about AI video for human creators. All graphics are drawn in TikZ, and there are no image files.

**80/20 rule:** body pages stay calm and readable. Decoration appears only on chapter openers, boxes and the footer.

## Palette

| Name | Hex | Use |
|---|---|---|
| paper | `#F8F3E8` | Page background (cream journal paper) |
| ink | `#1E1B2E` | Body text, headings, opener panel, table header, footer strip |
| brandMain | `#D6336C` | SCENE pill, heading underline, progress segments |
| brandAccent | `#F2C12E` | Post-it fill only. **Never text** (fails contrast on cream) |
| brandHighlight | `#D9C8F5` | Note box fill |

No other hues are used. In particular there is no purple beyond the light brandHighlight fill.

## Elements

1. **Paper page.** A cream background on every page, with body text in ink rather than pure black. This gives a softer, "printed journal" contrast that is still easy to read.
2. **Chapter opener.** A solid ink panel with a scalloped bottom edge (a row of TikZ half-circles), like a torn-off journal header. It shows "פרק X" and the title in cream Arial, and a brandMain "SCENE 0X" pill. The panel uses about 7.3 cm, which is under 1/3 of the page, and the text starts on the same page. That way the panel costs no page budget and adds no blank pages. Starred chapters (front matter) get the same panel without the number or pill. The TOC shows the plain titles.
3. **Section headings.** Arial in ink with a short brandMain underline at the start of the line (the right side). This gives one small brand mark per section without colouring the text.
4. **Tables.** An ink header row with cream text, thin light rules between rows, no vertical rules, and the caption above. The tables stay clean and match the film strip. Macros: `\headrow`, `\hcell{}`, `\rowrule`.
5. **Boxes.**
   - `directornote` is the "in our project" box. It is a yellow post-it titled "הערת במאי" with a strip of tape and a soft shadow, and it is the one playful, handmade touch in the body.
   - `notebox` is for general notes, with a lavender (brandHighlight) fill.

   Both use ink text.
6. **Footer.** A thin ink film strip with sprocket holes spans the page width. It shows a frame-style page number ("12A", like film edge codes) and chapter progress "פרק X/8" as 8 small segments, with the done ones in brandMain. The front matter shows only the roman page number.

## Mandatory rules (booklet table 11.1) and how they are met

- 12pt David body text, `\onehalfspacing`, justified.
- 2.5 cm margins, plus a 0.5 cm gutter on the **right**. In LuaTeX with Hebrew as the main language, the page is laid out right-to-left, so geometry's `left` is the physical right edge. The class sets `left=3.0cm,right=2.5cm`, and the result was measured in the PDF.
- Figure captions go below and table captions above. In a table, write `\caption` before the `tabular`.
- Figures, tables and equations are numbered per chapter (report class default). The front matter uses roman numbering (`main.tex`).
- The class uses `oneside,openany`, so a chapter never adds a blank page. This was verified on the full `build/main.pdf`.

## Technical notes

- **RTL fix:** in a right-to-left paragraph, LuaTeX draws every pgf picture mirrored or shifted. This affects TikZ and also tcolorbox frames. The class builds each picture in a left-to-right box (`\hbox dir TLT`) and sets node text back to right-to-left.
- The class file is `style/report.cls`, but LaTeX registers it under the basename `report`. The class clears that marker so that `\LoadClass{report}` still loads the standard class.

## Deliberately left out

- **Photos and images from the internet.** The project rules ban them. They also bring licensing questions and print poorly, and they would compete with the content.
- **Paper cut-outs and collage edges.** They are hard to draw cleanly in TikZ, and they add visual noise on every page, which breaks the 80/20 rule.
- **Stickers and doodles.** They are fun on a cover but look unprofessional in an academic report. The post-it and the film strip already carry the "handmade" feel.
- **Rotated boxes and handwritten fonts.** They hurt readability, and a script font has no reliable Hebrew support.
- **Colour in body text.** Text is always ink, so the report stays readable in grayscale print.

## Macro for English inside Hebrew

- The class already provides English wrapping through polyglossia: `\textenglish{...}`. It is used in `style/sample.tex` and inside `style/report.cls`. No `\en` alias was added, so the agent skills and `docs/agents-setup.md` use `\textenglish` everywhere.


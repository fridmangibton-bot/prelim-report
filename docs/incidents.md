# Incidents

Log of build and rendering problems. One entry per incident: ID, status, where it appears, cause, fix.

## INC-001: Reversed order of a mixed Hebrew/English phrase

- **Status:** closed - not a bug (false alarm)
- **Date:** 2026-11-20
- **Where:** `build/sample.pdf`, from `style/sample.tex`, body paragraph. Source: `\textenglish{IP-Adapter} ו־\textenglish{LoRA}`
- **Symptom:** The phrase "LoRA [vav + maqaf] IP-Adapter" renders in reversed order. Read right-to-left, IP-Adapter appears first, and the vav is attached to LoRA.
- **Category:** BiDi (booklet ch. 14: Hebrew and English on the same page, RTL, LTR and BiDi).
- **Cause:** not confirmed as a defect. On 2026-11-21 the source was rendered at 300 dpi next to variants (plain hyphen, `\textenglish{-}`, `\texthebrew{־}`, U+200F marks before/after). All eight render identically: from the right, `IP-Adapter`, then `ו`, then the maqaf, then `LoRA`. That is the correct logical RTL order, and it only looks reversed when scanned left to right. An RLM mark has no effect.
- **Detector self-test:** the first run missed it (BUG list had D1/D10 only). Root cause of the miss: every Latin run was already wrapped, so D1/D2 had nothing to flag, and no check covered a Hebrew prefix between two `\textenglish{}` runs. Fix: D13 BIDI-ORDER added to the detector skill (medium, requests a visual check, no auto-fix). The second run flagged it as BUG-sample-02.
- **Fix:** none needed. The source order renders correctly; the human reviewer misread a low-resolution screenshot. Only `\textenglish{David}` in `sample.tex` was wrapped (D1).
- **Lesson:** mixed Hebrew/English must be checked at high resolution (300 dpi crop), never on a full-page screenshot. D13 stays a visual-confirmation check.

## INC-002: `\LoadClass{report}` skipped the standard class

- **Status:** fixed
- **Date:** 2026-11-20
- **Where:** `style/report.cls`
- **Symptom:** The first compile failed with "The font size command \normalsize is not defined", and the log showed that only `./style/report.cls` was loaded.
- **Cause:** `\documentclass{style/report}` is registered under the basename `report`, so `\ver@report.cls` was already defined. `\LoadClass{report}` treated the standard class as loaded and silently skipped it.
- **Fix:** Clear the marker before loading: `\expandafter\let\csname ver@report.cls\endcsname\relax`, then `\LoadClass{report}`.
- **Note:** The failed run left a broken `build/sample.out`, which caused "Missing \endcsname" errors on the next run. Deleting `build/sample.*` cleared them.

## INC-003: TikZ pictures and tcolorbox frames shifted in RTL

- **Status:** fixed
- **Date:** 2026-11-20
- **Where:** `style/report.cls`: the chapter panel, footer strip and boxes
- **Symptoms:**
  - Text in the chapter panel ran off the right edge of the page.
  - The SCENE pill and the footer page number were invisible.
  - The box backgrounds were drawn shifted to the right of their text.
- **Cause:** With Hebrew as the main language, every pgf picture is built inside a right-to-left (`TRT`) box in LuaTeX. pgf's internal horizontal offsets then run in the wrong direction, so the drawing and node text are displaced. tcolorbox frames are drawn with pgf, so they were affected too.
- **Fix:** In the class, wrap every pgf picture in a left-to-right box:
  - `\def\pgfpicture{\leavevmode\hbox dir TLT\bgroup...}`, with a matching `\egroup` in `\endpgfpicture`
  - Set node text back to RTL with `\tikzset{every node/.append style={execute at begin node={\textdir TRT}}}`

  This was verified in a scratch test with inline pictures, overlay pictures and both tcolorbox skins.

## INC-004: Mirrored page margins (gutter on the wrong side)

- **Status:** fixed
- **Date:** 2026-11-20
- **Where:** `style/report.cls`, geometry options
- **Symptom:** The 0.5 cm binding gutter was meant to be on the right, but it appeared on the left. Measured in the rendered PDF, the physical left margin was 3.0 cm and the right margin was 2.5 cm.
- **Cause:** With Hebrew as the main language, LuaTeX lays the page out right-to-left, so geometry's `left` margin is the physical right edge.
- **Fix:** Swap the values to `left=3.0cm,right=2.5cm`, with a comment in the class. Re-measured: right margin 3.0 cm, left margin 2.5 cm.

## INC-005: Section heading underline placed a full line below the heading

- **Status:** fixed
- **Date:** 2026-11-20
- **Where:** `style/report.cls`, `\section` format
- **Symptom:** The short brandMain underline appeared about one line below the heading text. It was detached from the heading.
- **Cause:** The underline was typeset as a separate line, in the titlesec after-code and then in a block shape. That line got its own baseline skip under 1.5 line spacing, and `\nointerlineskip` did not remove the gap.
- **Fix:** Draw the underline as a zero-size TikZ overlay at the start (right side) of the heading line, 6–7.6 pt below the baseline (`\journal@underline`). It now hugs the heading and does not affect the spacing.

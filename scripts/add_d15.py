from pathlib import Path
p = Path(".claude/skills/report-detector/SKILL.md"); s = p.read_text(encoding="utf-8")
row = ("| D15 RENDERED-TEXT | Bugs that exist only in the compiled PDF (BiDi order, lost spaces, split parentheses). Run on the pdftotext OUTPUT, never on the .tex. "
       "Rules: `--`; a backtick or `''`; `TO-VERIFY` or `??`; a digit glued to a Latin word (`[0-9][A-Z]{2,}` or `[A-Z]{2,}[0-9]{4}`, ignore report IDs and DOIs in the references); "
       "a space inside parentheses (`\( ` or ` \)`); two Latin words glued by a lowercase-to-uppercase step (list hits for a human decision, many are real names such as StoryDiffusion); "
       "a Latin word split by a hyphen at a line end. Critical for the first four rules, medium for the rest. | `pdftotext -enc UTF-8 -layout build/main.pdf build/check.txt && py scripts/d15_check.py build/check.txt` (needs a fresh build; `-enc UTF-8` is required or Hebrew becomes U+FFFD) |")
i = s.index("| D13 BIDI-ORDER")
j = s.index("\n", i)
s = s[:j+1] + row + "\n" + s[j+1:]
s = s.replace("- critical: D1, D2, D3, D5, D11, D12 errors, invented facts.", "- critical: D1, D2, D3, D5, D11, D12 errors, D15 (first four rules), invented facts.")
s = s.replace("- medium: D13, D4, D6, D9, D10, overfull hbox.", "- medium: D13, D4, D6, D9, D10, D15 (other rules), overfull hbox.")
p.write_text(s, encoding="utf-8", newline="")

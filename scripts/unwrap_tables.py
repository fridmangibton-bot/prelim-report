"""Undo the unbreakable box in table rows (narrow p-columns must be able to wrap)."""
import re
from pathlib import Path
R = Path(__file__).resolve().parent.parent
BS = chr(92)
pat = re.compile(re.escape(BS + "mbox{") + "(" + re.escape(BS + "textenglish") + r"\{[^{}]*\})\}")
for f in sorted(R.glob("chapters/*.tex")) + sorted(R.glob("frontmatter/*.tex")):
    out = []
    for line in f.read_text(encoding="utf-8").split("\n"):
        if "&" in line:
            line = pat.sub(lambda m: m.group(1), line)
        out.append(line)
    f.write_text("\n".join(out), encoding="utf-8", newline="")

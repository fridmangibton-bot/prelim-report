"""Wrap short multi-word LTR runs in an unbreakable box (A5/A6)."""
import re
from pathlib import Path
R = Path(__file__).resolve().parent.parent
BS = chr(92)
pat = re.compile(r"(?<!mbox\{)" + re.escape(BS + "textenglish") + r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")
n = 0
for f in sorted(R.glob("chapters/*.tex")) + sorted(R.glob("frontmatter/*.tex")):
    s = f.read_text(encoding="utf-8")
    def r(m):
        global n
        body = m.group(1)
        if " " in body.strip() and len(body) <= 40 and BS + BS not in body:
            n += 1
            return BS + "mbox{" + m.group(0) + "}"
        return m.group(0)
    t = pat.sub(r, s)
    if t != s:
        f.write_text(t, encoding="utf-8", newline="")
print("wrapped", n)

"""One-off source normaliser for the LTR-run fixes (A3, A5). English only.

- merges `\textenglish{A} \textenglish{B}` into `\textenglish{A B}` (one LTR unit)
- turns numeric ranges `1--2` outside TikZ/LTR runs into `\textenglish{1–2}`
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
files = sorted(ROOT.glob("chapters/*.tex")) + sorted(ROOT.glob("frontmatter/*.tex"))

merge = re.compile(r"\\textenglish\{([^{}]*)\}[ \t]+\\textenglish\{([^{}]*)\}")
rng = re.compile(r"(?<![\w{.,-])(\d+(?:[.,]\d+)?)--(\d+(?:[.,]\d+)?)(?![\w}])")

for f in files:
    s = f.read_text(encoding="utf-8")
    o = s
    while True:
        n = merge.sub(lambda m: "\\textenglish{%s %s}" % (m.group(1), m.group(2)), s)
        if n == s:
            break
        s = n
    out = []
    for line in s.split("\n"):
        if "\\draw" not in line and "--" in line:
            line = rng.sub(lambda m: "\\textenglish{%s\u2013%s}" % (m.group(1), m.group(2)), line)
            line = re.sub(r"\\textenglish\{([^{}]*)--([^{}]*)\}", "\\\\textenglish{\\1\u2013\\2}", line)
        out.append(line)
    s = "\n".join(out)
    if s != o:
        f.write_text(s, encoding="utf-8", newline="")
        print("changed", f.relative_to(ROOT))

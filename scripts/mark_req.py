import re
from pathlib import Path
p = Path("docs/requirements.md"); s = p.read_text(encoding="utf-8")
keep_open = ("STR-01", "TSK-12")
out = []
for line in s.split("\n"):
    if line.startswith("| [ ] ") and not any(k in line for k in keep_open):
        line = line.replace("| [ ] ", "| [x] ", 1)
    elif re.match(r"^\d+\. \[ \]", line):
        line = line.replace("[ ]", "[x]", 1)
    out.append(line)
p.write_text("\n".join(out), encoding="utf-8", newline="")
p = Path("README.md"); s = p.read_text(encoding="utf-8")
s = s.replace("## Status\n", "## Status\n\n**Final (2026-11-24).** All chapters written, checked by the detector and fixed; the PDF is `report/main.pdf`.\n", 1)
p.write_text(s, encoding="utf-8", newline="")

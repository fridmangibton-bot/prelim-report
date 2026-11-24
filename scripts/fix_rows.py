from pathlib import Path

p = Path("chapters/ch4-market.tex")
lines = p.read_text(encoding="utf-8").split("\n")
for i in range(28, 33):
    t = lines[i].rstrip()
    if t.endswith(" \\ \\rowrule"):
        t = t[: -len(" \\ \\rowrule")] + " \\\\ \\rowrule"
    elif t.endswith(" \\") and not t.endswith("\\\\"):
        t = t + "\\"
    lines[i] = t
p.write_text("\n".join(lines), encoding="utf-8", newline="")

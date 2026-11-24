from pathlib import Path
p = Path("chapters/ch4-market.tex"); s = p.read_text(encoding="utf-8")
a = " (כ־69.9 שקלים בישראל)*"
assert a in s
s = s.replace(a, "*")
p.write_text(s, encoding="utf-8", newline="")

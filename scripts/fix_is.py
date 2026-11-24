from pathlib import Path
p = Path(__file__).resolve().parent.parent/"chapters/ch3-literature.tex"; s = p.read_text(encoding="utf-8")
B = chr(92)
a = B+"textenglish{Inception} ("+B+"textenglish{IS})"
assert a in s
s = s.replace(a, B+"mbox{"+B+"textenglish{Inception Score (IS)}}")
p.write_text(s, encoding="utf-8", newline="")

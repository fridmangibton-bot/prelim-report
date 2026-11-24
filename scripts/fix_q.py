from pathlib import Path
p = Path(__file__).resolve().parent.parent/"chapters/ch3-literature.tex"; s = p.read_text(encoding="utf-8")
B="\\"
for q in ["consistent character video generation","story visualization consistent characters","multi-shot video generation character consistency","long video generation story consistency"]:
    a = B+"textenglish{"+q+"}"
    assert a in s, q
    s = s.replace(a, B+"mbox{"+a+"}")
p.write_text(s, encoding="utf-8", newline="")
p = Path(__file__).resolve().parent.parent/"chapters/ch2-problem.tex"; s = p.read_text(encoding="utf-8")
a = B+"begin{tabular}{p{1.9cm} p{4.2cm} p{3.0cm} p{3.0cm}}"
assert a in s
s = s.replace(a, B+"begin{tabular}{p{2.7cm} p{3.6cm} p{3.2cm} p{2.8cm}}")
p.write_text(s, encoding="utf-8", newline="")

from pathlib import Path
R = Path(__file__).resolve().parent.parent
BS = chr(92)
def sub(rel, pairs):
    p = R/rel; s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in s, a
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8", newline="")
cs = BS + "setlength" + BS + "tabcolsep{3pt}"
sub("chapters/ch4-market.tex", [(BS+"begin{tabular}{p{1.7cm} *{7}{p{1.95cm}}}", cs+"\n  "+BS+"begin{tabular}{p{1.7cm} *{7}{p{1.7cm}}}")])
t = BS+"begin{tabular}{p{2.9cm} *{6}{>{"+BS+"centering"+BS+"arraybackslash}p{2.0cm}}}"
n = BS+"begin{tabular}{p{2.7cm} *{6}{>{"+BS+"centering"+BS+"arraybackslash}p{1.8cm}}}"
sub("chapters/ch3-literature.tex", [(t, cs+"\n  "+n)])

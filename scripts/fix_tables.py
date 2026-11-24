from pathlib import Path
R = Path(__file__).resolve().parent.parent
def sub(rel, pairs):
    p = R / rel; s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        if a not in s: print("MISSING", rel, a[:50]); continue
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8", newline="")
C = r"\raggedleft"
sub("chapters/ch3-literature.tex", [
 (r"  \scriptsize" + "\n" + r"  \begin{tabular}{p{2.5cm} c c c c c c}",
  r"  \footnotesize" + "\n" + r"  \begin{tabular}{p{2.9cm} *{6}{>{\centering\arraybackslash}p{2.0cm}}}"),
 (r"\begin{tabular}{p{2.8cm} c c c c c c}", r"\begin{tabular}{p{2.9cm} *{6}{>{\centering\arraybackslash}p{2.0cm}}}"),
])
sub("chapters/ch4-market.tex", [
 (r"  \scriptsize" + "\n" + r"  \begin{tabular}{p{1.5cm} p{1.4cm} p{1.4cm} p{1.4cm} p{1.4cm} p{1.4cm} p{1.4cm} p{1.4cm}}",
  r"  \footnotesize" + "\n" + r"  \begin{tabular}{p{1.7cm} *{7}{p{1.95cm}}}"),
])

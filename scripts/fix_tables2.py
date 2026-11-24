from pathlib import Path
R = Path(__file__).resolve().parent.parent
p = R/"chapters/ch5-alternatives.tex"; s = p.read_text(encoding="utf-8")
s = s.replace("{\mathdir TLT $w_i$}", "$w_i$").replace("$w_i$", "{\mathdir TLT $w_i$}").replace("$S_j$", "{\mathdir TLT $S_j$}")
s = s.replace(r"\begin{tabular}{p{4.6cm} c c c c}", r"\begin{tabular}{p{4.6cm} *{4}{>{\centering\arraybackslash}p{2.2cm}}}")
p.write_text(s, encoding="utf-8", newline="")
p = R/"frontmatter/abbreviations.tex"; s = p.read_text(encoding="utf-8")
s = s.replace(r"\noindent\begin{tabular}{@{}p{3.4cm} p{3.6cm} p{6.6cm}@{}}", "\begingroup\textdir TRT\setlength\LTleft{0pt}\setlength\LTright{0pt}\n\begin{longtable}{@{}p{3.4cm} p{3.6cm} p{6.6cm}@{}}")
s = s.replace(r"\headrow \hcell{קיצור או מונח} & \hcell{שם מלא} & \hcell{הגדרה} \\", r"\headrow \hcell{קיצור או מונח} & \hcell{שם מלא} & \hcell{הגדרה} \\" + "\n  \endhead")
s = s.replace(r"\end{tabular}", "\end{longtable}\n\endgroup")
p.write_text(s, encoding="utf-8", newline="")

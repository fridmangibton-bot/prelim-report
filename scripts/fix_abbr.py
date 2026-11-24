from pathlib import Path
R = Path(__file__).resolve().parent.parent
p = R/"frontmatter/abbreviations.tex"; s = p.read_text(encoding="utf-8")
BS = "\\"
s = s.replace(BS+"noindent"+BS+"begin{tabular}{@{}p{3.4cm} p{3.6cm} p{6.6cm}@{}}",
  BS+"begingroup"+BS+"textdir TRT"+BS+"setlength"+BS+"LTleft{0pt}"+BS+"setlength"+BS+"LTright{0pt}\n"+BS+"begin{longtable}{@{}p{3.4cm} p{3.6cm} p{6.6cm}@{}}")
s = s.replace("\hcell{הגדרה} \\\\", "\hcell{הגדרה} \\\n  "+BS+"endhead")
s = s.replace(BS+"end{tabular}", BS+"end{longtable}\n"+BS+"endgroup")
p.write_text(s, encoding="utf-8", newline="")

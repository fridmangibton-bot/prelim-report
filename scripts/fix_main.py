from pathlib import Path
p = Path(__file__).resolve().parent.parent/"main.tex"; s = p.read_text(encoding="utf-8")
BS="\\"
s = s.replace(BS+"journal@inrefstrue\n","")
s = s.replace(BS+"addcontentsline{toc}{chapter}{מקורות}\n", BS+"addcontentsline{toc}{chapter}{מקורות}\n"+BS+"makeatletter"+BS+"journal@inrefstrue"+BS+"makeatother\n")
p.write_text(s, encoding="utf-8", newline="")

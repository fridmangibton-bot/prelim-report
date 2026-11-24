from pathlib import Path
p = Path(__file__).resolve().parent.parent/"main.tex"; s = p.read_text(encoding="utf-8")
BS = chr(92)
i = s.index(BS+"AtBeginDocument{")
j = s.index("\n", i)
q = "{"+BS+"fontspec{Times New Roman}"+BS+"char\""
new = BS+"DeclareFieldFormat[article,inproceedings,online,misc,report,techreport,book,unpublished,inbook,incollection]{title}{"+q+"201C}#1"+q+"201D}}"
s = s[:i] + new + s[j:]
p.write_text(s, encoding="utf-8", newline="")

"""Final checks: labels vs refs, cites vs bib, figure/table counts, abstract word count."""
import re
from pathlib import Path

R = Path(".")
src = "\n".join(p.read_text(encoding="utf-8") for p in sorted(R.glob("chapters/*.tex")) + sorted(R.glob("frontmatter/*.tex")))
labels = re.findall(r"\\label\{([^}]+)\}", src)
refs = set(re.findall(r"\\(?:ref|autoref|pageref)\{([^}]+)\}", src))
print("labels", len(labels), "unreferenced:", [l for l in labels if l not in refs])
print("undefined refs:", [r for r in refs if r not in labels])
cites = set(k.strip() for m in re.findall(r"\\cite\{([^}]+)\}", src) for k in m.split(","))
bib = set(re.findall(r"@\w+\{([^,]+),", (R / "bib/references.bib").read_text(encoding="utf-8")))
print("cited not in bib:", cites - bib, "| in bib not cited:", bib - cites)
print("figures:", len(re.findall(r"\\begin\{figure", src)), "tables:", len(re.findall(r"\\begin\{(?:table|longtable)", src)))
a = (R / "frontmatter/abstract.tex").read_text(encoding="utf-8")
body = re.split(r"\\section\*\{", a)[0]
body = re.sub(r"^%.*$", " ", body.replace("\\%", "PCT"), flags=re.M)
body = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", body)
body = re.sub(r"[{}~\\]", " ", body)
words = [w for w in body.split() if re.search(r"\w", w)]
print("abstract words (minus heading 2):", len(words) - 2)

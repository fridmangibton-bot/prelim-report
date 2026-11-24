from pathlib import Path
p = Path(__file__).resolve().parent.parent/"chapters/ch1-intro.tex"; s = p.read_text(encoding="utf-8")
a = " הרחבה עתידית אפשרית היא משרדי פרסום, שבהם דמויות מותג וקמפיינים מתמשכים דורשים את אותה רציפות."
assert a in s
s = s.replace(a, "")
p.write_text(s, encoding="utf-8", newline="")

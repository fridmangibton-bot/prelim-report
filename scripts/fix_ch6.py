from pathlib import Path

p = Path("chapters/ch6-workplan.tex")
s = p.read_text(encoding="utf-8")
a = "חבילה~3 תלויה רק בהגדרת הממשקים של חבילה~2, ולכן אפשר לבצע אותן במקביל."
assert a in s
s = s.replace(a, "חבילה~3 תלויה רק בספר הסדרה של חבילה~1, ולכן אפשר לבצע אותה במקביל לחבילה~2.")
p.write_text(s, encoding="utf-8", newline="")

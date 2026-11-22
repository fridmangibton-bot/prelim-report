"""Rough word count of a chapter .tex file (strips comments, commands, math, figure/table bodies).
Usage: py scripts/wordcount.py chapters/ch1-intro.tex"""
import re
import sys

for f in sys.argv[1:]:
    t = open(f, encoding="utf-8").read()
    t = re.sub(r"%.*", "", t)
    t = re.sub(r"\\(label|ref|cite|includegraphics|input)\{[^}]*\}", " ", t)
    t = re.sub(r"\\begin\{(tikzpicture|figure|table)\}.*?\\end\{\1\}", " ", t, flags=re.S)
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    t = re.sub(r"[{}$&~\\\[\]]|--|\u05be|־", " ", t)
    words = [w for w in t.split() if re.search(r"[\u0590-\u05ff A-Za-z0-9]", w)]
    heb = [w for w in words if re.search(r"[\u0590-\u05ff]", w)]
    print(f, "all:", len(words), "hebrew:", len(heb))

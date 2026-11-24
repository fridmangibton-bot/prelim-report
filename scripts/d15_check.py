"""D15 RENDERED-TEXT: checks pdftotext output of the compiled PDF (not the .tex).
Usage: pdftotext -layout build/main.pdf build/check.txt && py scripts/d15_check.py build/check.txt
Prints every hit as  <rule>  <line>: <text>. Exit code 1 if any hard rule hits.
"""
import re
import sys

rules = [
    ("double-hyphen", re.compile(r"--"), True),
    ("backtick-or-double-apostrophe", re.compile(r"`|''"), True),
    ("TO-VERIFY-or-??", re.compile(r"TO-VERIFY|\?\?"), True),
    ("digit-glued-to-Latin", re.compile(r"[0-9][A-Z]{2,}|[A-Z]{2,}[0-9]{4}"), True),
    ("space-inside-parentheses", re.compile(r"\( | \)"), False),
    ("glued-latin-words (human decision)", re.compile(r"\b[a-z]+[A-Z][a-z]+[A-Z][a-z]+"), False),
    ("latin-hyphen-at-line-end", re.compile(r"[A-Za-z]{2,}-\s*$"), False),
]
hard = 0
for n, line in enumerate(open(sys.argv[1], encoding="utf-8", errors="replace"), 1):
    if re.search(r"\.{4,}", line):  # TOC/LOF/LOT dot leaders: layout artefacts
        continue
    for name, rx, is_hard in rules:
        if rx.search(line):
            sys.stdout.buffer.write((f"{name:40s} {n}: {line.strip()[:110]}" + chr(10)).encode("utf-8"))
            hard += is_hard
sys.exit(1 if hard else 0)

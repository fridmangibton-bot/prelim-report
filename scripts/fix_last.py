from pathlib import Path


def sub(rel, pairs):
    p = Path(rel)
    s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in s, (rel, a)
        s = s.replace(a, b, 1)
    p.write_text(s, encoding="utf-8", newline="")


new_gap = "ותמיכה בעברית בכלים הקיימים מוגבלת, ואין כלי שמשלב אותה עם כל השאר."
sub("chapters/ch1-intro.tex", [("ובבדיקת הצוות אף אחד אינו נגיש ליוצרים בעברית.", new_gap)])
sub("chapters/ch8-summary.tex", [("ואף אחד אינו נגיש ליוצרים בעברית.", new_gap)])
sub("chapters/ch3-literature.tex", [
    ("לאימון המודל האוטורגרסיבי.", "לאימון המודל האוטורגרסיבי~\\cite{zhao2025moviedreamer}."),
    ("שמונה מקורות אקדמיים", "שמונה מקורות אקדמיים ומוצר מסחרי אחד שנבדק לצורך ההשוואה"),
    (" שצוטט רבות", " שזכה לתשומת לב בתחום"),
])
sub("chapters/ch4-market.tex", [("\\section{היקף השוק}", "\\section{היקף השוק וקהל היעד}")])

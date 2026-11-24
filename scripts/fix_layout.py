from pathlib import Path


def sub(rel, pairs):
    p = Path(rel)
    s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in s, a
        s = s.replace(a, b, 1)
    p.write_text(s, encoding="utf-8", newline="")


sub("chapters/ch1-intro.tex", [
    (": מהמספרים המעוגלים עצמם נגזר שיעור צמיחה של כ־55\\%, ולא 37.1\\%.", "."),
    (" ההפרש בין הדוחות נובע מהגדרות שונות של השוק, ולכן הדוח הנוכחי מתייחס לנתונים אלה כאל טווח ולא כאל מספר יחיד.",
     " ההפרש בין הדוחות נובע מהגדרות שונות של השוק, ולכן הנתונים מוצגים כטווח."),
])
sub("chapters/ch7-risks.tex", [("width=\\textwidth]{figures/ch7_risk.pdf}", "width=0.82\\textwidth]{figures/ch7_risk.pdf}")])

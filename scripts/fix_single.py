"""One-off single fixes from docs/review-fixes-2026-11-24.md section B (and A5/A6)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sub(rel, pairs):
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        if a not in s:
            print("MISSING in", rel, ":", a[:60])
            continue
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8", newline="")


sub("chapters/ch2-problem.tex", [
    (r"(נובמבר 2026, \textenglish{docs/market-data.md})", r"(בדיקת הצוות, נובמבר 2026)"),
    (r"בבדיקת הצוות (בדיקת הצוות, נובמבר 2026)", r"בבדיקת הצוות (נובמבר 2026)"),
    (r"$\ge$ 90\% מזוגות", r"לפחות 90\% מזוגות"),
    (r"$\ge$ 80\% מהסתירות", r"לפחות 80\% מהסתירות"),
    (r"קובץ \textenglish{.env} או", r"קובץ \textenglish{.env} או"),
])
sub("chapters/ch4-market.tex", [
    (r"\textenglish{21-22.11.2026}", r"\mbox{\textenglish{21--22.11.2026}}"),
    (r"הערך ``לא נמצא''", r"הערך ״לא נמצא״"),
])
sub("chapters/ch6-workplan.tex", [
    (r"סטודנטית א'", r"סטודנטית א׳"),
    (r"סטודנטית ב'", r"סטודנטית ב׳"),
])
sub("chapters/ch8-summary.tex", [
    (r"\textenglish{R1}, \textenglish{R2}, \textenglish{R3} ו־\textenglish{R7}", r"\textenglish{R1, R2, R3} ו־\textenglish{R7}"),
])
sub("chapters/ch7-risks.tex", [
    (r"\textenglish{R1}, הסיכון \textenglish{R2}, הסיכון \textenglish{R3} והסיכון", r"\textenglish{R1}, הסיכון \textenglish{R2}, הסיכון \textenglish{R3} והסיכון"),
])
sub("chapters/ch3-literature.tex", [
    (r"\textenglish{Long Context Tuning} (\textenglish{LCT})", r"\textenglish{Long Context Tuning (LCT)}"),
    (r"\textenglish{Consistent Self-Attention}", r"\textenglish{Consistent Self-Attention}"),
])

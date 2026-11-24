import re
from pathlib import Path
R = Path(__file__).resolve().parent.parent
for rel in ["figures/python/data/scatter.json", "figures/python/data/radar.json"]:
    p = R/rel; s = p.read_text(encoding="utf-8")
    s = re.sub(r'נבדק ב-[^"]*"', 'נבדק ב־21 וב־22 בנובמבר 2026"', s)
    s = s.replace("עקביות (דולר)", "עקביות, בדולרים").replace("כיסוי יכולות (0–4)", "כיסוי יכולות, סולם 0 עד 4")
    p.write_text(s, encoding="utf-8", newline="")
p = R/"figures/python/make_figures.py"; s = p.read_text(encoding="utf-8")
s = s.replace("{c['label_he']} ({c['weight']:.2f})", "{c['label_he']}, {c['weight']:.2f}")
s = s.replace('heb("ציון משוקלל (מתוך 5)")', 'heb("ציון משוקלל, סולם 1 עד 5")')
s = s.replace('heb("קריטריון (משקל)")', 'heb("קריטריון ומשקלו")')
p.write_text(s, encoding="utf-8", newline="")

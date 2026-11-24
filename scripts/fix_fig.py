from pathlib import Path
R = Path(__file__).resolve().parent.parent
p = R/"figures/python/make_figures.py"; s = p.read_text(encoding="utf-8")
def rep(a, b):
    global s
    assert a in s, a
    s = s.replace(a, b)
rep("fig = plt.figure(figsize=(6.8, 4.4))\n    ax = fig.add_axes([0.09, 0.14, 0.46, 0.80])", "fig = plt.figure(figsize=(6.1, 4.3))\n    ax = fig.add_axes([0.10, 0.17, 0.42, 0.78])")
rep('ha="right", va="bottom", fontsize=7, color=INK, alpha=0.5)', 'ha="right", va="bottom", fontsize=9, color=INK, alpha=0.5)')
rep("s=330, color=MAIN if crit else INK", "s=520, color=MAIN if crit else INK")
rep('ha="center", va="center", fontsize=8,\n                    fontweight="bold", color=PAPER, zorder=4)', 'ha="center", va="center", fontsize=10,\n                    fontweight="bold", color=PAPER, zorder=4)')
rep('ax.set_xlabel(heb("השפעה – I"))', 'ax.set_xlabel(heb("השפעה – I"), fontsize=11)')
rep('ax.set_ylabel(heb("הסתברות – P"))', 'ax.set_ylabel(heb("הסתברות – P"), fontsize=11)\n    ax.tick_params(labelsize=11)')
rep("lx = fig.add_axes([0.58, 0.14, 0.40, 0.80])", "lx = fig.add_axes([0.55, 0.17, 0.44, 0.78])")
rep('ha="right", va="top", fontsize=9.5, fontweight="bold")', 'ha="right", va="top", fontsize=11, fontweight="bold")')
rep('y = 0.90 - k * 0.115', 'y = 0.88 - k * 0.135')
rep('lx.text(1, y, r["id"], ha="right", va="center", fontsize=8.5, fontweight=w)', 'lx.text(1, y, r["id"], ha="right", va="center", fontsize=11, fontweight=w)')
rep('lx.text(0.88, y, heb(r["name_he"], wrap=34), ha="right", va="center", fontsize=8.5, fontweight=w)', 'lx.text(0.86, y, heb(r["name_he"], wrap=22), ha="right", va="center", fontsize=11, fontweight=w)')
rep('lx.text(0.0, y, f"R={R}", ha="left", va="center", fontsize=8.5, fontweight=w)', 'lx.text(0.0, y, f"R={R}", ha="left", va="center", fontsize=11, fontweight=w)')
rep('fig.text(0.58, 0.04, heb(f"האזור הקריטי מוצלל: R ≥ {thr}"), ha="left", fontsize=8.5)', 'fig.text(0.55, 0.04, heb(f"האזור הקריטי מוצלל: R ≥ {thr}"), ha="left", fontsize=11)')
p.write_text(s, encoding="utf-8", newline="")
for rel, pairs in {"figures/python/data/radar.json": [("CapCut (ידני)", "CapCut, ידני"), ("הפתרון המוצע (יעד תכנון)", "הפתרון המוצע, יעד תכנון")],
                   "figures/python/data/scatter.json": [("הפתרון המוצע (יעד תכנון)", "הפתרון המוצע, יעד תכנון")]}.items():
    q = R/rel; t = q.read_text(encoding="utf-8")
    for a, b in pairs:
        t = t.replace(a, b)
    q.write_text(t, encoding="utf-8", newline="")
c = R/"chapters/ch7-risks.tex"; t = c.read_text(encoding="utf-8")
t = t.replace("width=0.6" + chr(92) + "textwidth]{figures/ch7_risk.pdf}", "width=" + chr(92) + "textwidth]{figures/ch7_risk.pdf}")
c.write_text(t, encoding="utf-8", newline="")

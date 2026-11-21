"""Generate all report charts as PDF files in figures/.

Usage: py figures/python/make_figures.py

Colors come from style/palette.json, data from figures/python/data/*.json.
Hebrew labels go through python-bidi so they render right-to-left in matplotlib.
"""
import json
import re
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from bidi import get_display
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(__file__).resolve().parent / "data"
OUT = ROOT / "figures"

PAL = json.loads((ROOT / "style" / "palette.json").read_text(encoding="utf-8"))
PAPER, INK = PAL["paper"], PAL["ink"]
MAIN, ACCENT, HIGHLIGHT = PAL["brandMain"], PAL["brandAccent"], PAL["brandHighlight"]

matplotlib.rcParams.update({
    "font.family": "Arial",
    "font.size": 10,
    "pdf.fonttype": 42,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "text.color": INK,
    "axes.labelcolor": INK,
    "axes.edgecolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "legend.facecolor": PAPER,
    "legend.edgecolor": INK,
    "axes.unicode_minus": False,
})

NATIVE_BIDI = tuple(int(x) for x in matplotlib.__version__.split(".")[:2]) >= (3, 11)
HEB = re.compile(r"[֐-׿]")
placeholder_charts = []


# ---------- helpers ----------
RLI, PDI = "⁧", "⁩"  # Unicode right-to-left isolate / pop directional isolate


def heb(text, wrap=None):
    """Prepare a label for matplotlib (see INC-006).

    A label that contains Hebrew is wrapped in an RLI..PDI isolate so the base
    direction is right-to-left even when it starts or ends with English or digits.
    Each line is isolated separately, so wrapping (`wrap` = max characters per
    line) never splits an isolate. Labels without Hebrew are returned unchanged.
    On matplotlib < 3.11 (no libraqm) python-bidi converts to visual order instead.
    """
    text = str(text)
    if wrap:
        text = "\n".join(textwrap.wrap(text, wrap, break_on_hyphens=False)) if "\n" not in text else text
    out = []
    for line in text.split("\n"):
        if not HEB.search(line):
            out.append(line)
        elif NATIVE_BIDI:
            out.append(RLI + line + PDI)
        else:
            out.append(get_display(line, base_dir="R"))
    return "\n".join(out)


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def has_placeholder(node):
    if isinstance(node, dict):
        return node.get("placeholder") is True or any(has_placeholder(v) for v in node.values())
    if isinstance(node, list):
        return any(has_placeholder(v) for v in node)
    return False


def blend(c1, c2, t):
    """Mix hex color c1 with c2; t = share of c2."""
    a = np.array(matplotlib.colors.to_rgb(c1))
    b = np.array(matplotlib.colors.to_rgb(c2))
    return matplotlib.colors.to_hex(a * (1 - t) + b * t)


def text_on(color):
    r, g, b = matplotlib.colors.to_rgb(color)
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return INK if lum > 0.55 else PAPER


def finish(fig, name, data):
    """Mark placeholder charts, save PDF."""
    if has_placeholder(data):
        placeholder_charts.append(name)
        fig.text(0.01, 0.99, heb("נתוני דמה"), fontsize=8, color=MAIN, ha="left", va="top")
    fig.savefig(OUT / name, format="pdf", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


# ---------- ch4: radar ----------
def chart_radar():
    d = load("radar.json")
    labels = [heb(a["label_he"]) for a in d["axes"]]
    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    fig = plt.figure(figsize=(6.3, 5.9))
    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    lo, hi = d["scale"]
    ax.set_ylim(lo - 1, hi)
    ax.set_yticks(range(lo, hi + 1))
    ax.set_yticklabels([str(v) for v in range(lo, hi + 1)], fontsize=8)
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=10)
    ax.tick_params(axis="x", pad=24)
    ax.grid(color=INK, alpha=0.2)
    ax.spines["polar"].set_color(INK)
    ax.spines["polar"].set_alpha(0.4)
    styles = [("-", "o"), ("--", "s"), ("-.", "^"), (":", "D")]
    handles, k = [], 0
    for s in d["series"]:
        vals = s["values"] + s["values"][:1]
        ang = list(angles) + [angles[0]]
        if s["ours"]:
            ax.fill(ang, vals, color=HIGHLIGHT, alpha=0.6, zorder=2)
            ax.plot(ang, vals, color=MAIN, lw=2.6, marker="o", ms=6, zorder=5)
            handles.append(Line2D([0], [0], color=MAIN, lw=2.6, marker="o", label=heb(s["name"])))
        else:
            ls, mk = styles[k % len(styles)]
            k += 1
            ax.plot(ang, vals, color=INK, lw=1.4, ls=ls, marker=mk, ms=4.5, alpha=0.85, zorder=3)
            handles.append(Line2D([0], [0], color=INK, lw=1.4, ls=ls, marker=mk, ms=4.5, label=heb(s["name"])))
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.06), ncol=2, fontsize=9, frameon=False)
    fig.text(0.5, 0.01, heb(d["basis_he"]), ha="center", va="bottom", fontsize=8.5)
    fig.subplots_adjust(top=0.92, bottom=0.30, left=0.20, right=0.80)
    finish(fig, "ch4_radar.pdf", d)


# ---------- ch4: scatter ----------
def chart_scatter():
    d = load("scatter.json")
    fig, ax = plt.subplots(figsize=(6.3, 4.6))
    markers = ["o", "s", "^", "D"]
    k = 0
    offsets = {"OpenArt": (8, -4), "Atlabs": (-8, 8)}
    for p in d["points"]:
        if p["ours"]:
            xm = (p["price_min"] + p["price_max"]) / 2
            ax.errorbar(xm, p["capabilities"], xerr=(p["price_max"] - p["price_min"]) / 2,
                        fmt="none", ecolor=MAIN, elinewidth=2, capsize=5, zorder=4)
            ax.scatter(xm, p["capabilities"], s=230, marker="*", facecolor=PAPER,
                       edgecolor=MAIN, lw=1.8, zorder=5)
            ax.annotate(heb(p["name"]), (xm, p["capabilities"]), xytext=(0, -20),
                        textcoords="offset points", fontsize=10, fontweight="bold",
                        color=INK, ha="center")
        else:
            mk = markers[k % 4]
            k += 1
            star = "*" if p["to_verify"] else ""
            ax.scatter(p["price_usd"], p["capabilities"], s=60, marker=mk,
                       color=HIGHLIGHT, edgecolor=INK, lw=1.0, zorder=4)
            dx, dy = offsets.get(p["name"], (8, -4))
            label = p["name"] + star + (chr(10) + p["note_he"] if p.get("note_he") else "")
            ax.annotate(heb(label), (p["price_usd"], p["capabilities"]), xytext=(dx, dy),
                        textcoords="offset points", fontsize=9, color=INK,
                        ha="right" if dx < 0 else "left")
    ax.set_xlabel(heb(d["x_label_he"]))
    ax.set_ylabel(heb(d["y_label_he"]))
    ax.set_xlim(0, 70)
    ax.set_ylim(-0.3, 4.6)
    ax.set_yticks(range(0, 5))
    ax.grid(color=INK, alpha=0.15)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    fig.text(0.98, 0.055, heb(d["footnote_he"]), ha="right", va="bottom", fontsize=8.5)
    fig.text(0.5, 0.01, heb(d["basis_he"]), ha="center", va="bottom", fontsize=8.5)
    finish(fig, "ch4_scatter.pdf", d)


# ---------- ch5: weighted decision matrix ----------
def decision_totals(weights, alts, crit_keys):
    return {a["key"]: sum(weights[c] * a["scores"][c]["score"] for c in crit_keys) for a in alts}


def sensitivity_md(d):
    crit = d["criteria"]
    keys = [c["key"] for c in crit]
    base_w = {c["key"]: c["weight"] for c in crit}
    alts = d["alternatives"]
    ak = [a["key"] for a in alts]

    def winners(tot):
        m = max(tot.values())
        return [k for k in ak if abs(tot[k] - m) < 1e-9]

    base = decision_totals(base_w, alts, keys)
    base_win = winners(base)
    rows = [("base", "-", base_w, base, base_win)]
    for c in crit:
        for delta in (-0.1, 0.1):
            wk = round(base_w[c["key"]] + delta, 10)
            if wk < 0 or wk > 1:
                continue
            scale = (1 - wk) / (1 - base_w[c["key"]])
            w = {k: (wk if k == c["key"] else base_w[k] * scale) for k in keys}
            assert abs(sum(w.values()) - 1.0) < 1e-9
            tot = decision_totals(w, alts, keys)
            rows.append((c["key"], f"{delta:+.1f}", w, tot, winners(tot)))
    changed = [r for r in rows[1:] if r[4] != base_win]
    lines = [
        "# Sensitivity check (weighted decision matrix)",
        "",
        "Each weight is moved by +/-0.1; the other weights are rescaled proportionally so the sum stays 1.0.",
        "",
        "| Criterion | Change | New weight | " + " | ".join(ak) + " | Winner | Winner changed? |",
        "|---|---|---|" + "---|" * len(ak) + "---|---|",
    ]
    for key, delta, w, tot, win in rows:
        nw = "-" if key == "base" else f"{w[key]:.2f}"
        lines.append(
            f"| {key} | {delta} | {nw} | " + " | ".join(f"{tot[k]:.2f}" for k in ak)
            + f" | {'/'.join(win)} | {'yes' if win != base_win else 'no'} |"
        )
    lines += ["", f"Base winner: {'/'.join(base_win)}. "
              + (f"The winner changes in {len(changed)} of {len(rows) - 1} scenarios."
                 if changed else f"The winner does not change in any of {len(rows) - 1} scenarios."),
              "", "Scores are placeholders (see weights.json), so this result is provisional.", ""]
    (DATA / "sensitivity.md").write_text("\n".join(lines), encoding="utf-8")
    return changed


def chart_decision():
    d = load("weights.json")
    crit, alts = d["criteria"], d["alternatives"]
    assert abs(sum(c["weight"] for c in crit) - 1.0) < 1e-9, "weights must sum to 1.0"
    sensitivity_md(d)

    colors = [MAIN, ACCENT, HIGHLIGHT, INK, blend(MAIN, PAPER, 0.5), blend(INK, PAPER, 0.55)]
    hatches = [None, None, None, None, "///", ".."]
    fig, ax = plt.subplots(figsize=(6.3, 4.6))
    x = np.arange(len(alts))
    bottom = np.zeros(len(alts))
    for i, c in enumerate(crit):
        vals = np.array([c["weight"] * a["scores"][c["key"]]["score"] for a in alts])
        ax.bar(x, vals, 0.55, bottom=bottom, color=colors[i], edgecolor=INK, lw=0.7,
               hatch=hatches[i], label=heb(f"{c['label_he']} ({c['weight']:.2f})"))
        for xi, v, b in zip(x, vals, bottom):
            if v >= 0.14:
                ax.text(xi, b + v / 2, f"{v:.2f}", ha="center", va="center", fontsize=8,
                        color=text_on(colors[i]) if hatches[i] is None else INK,
                        bbox=None if hatches[i] is None else dict(fc=PAPER, ec="none", pad=1, alpha=0.8))
        bottom += vals
    for xi, t in zip(x, bottom):
        ax.text(xi, t + 0.05, f"{t:.2f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([heb(a["label_he"], wrap=16) for a in alts], fontsize=9)
    ax.set_ylim(0, 5)
    ax.set_ylabel(heb("ציון משוקלל (מתוך 5)"))
    ax.grid(axis="y", color=INK, alpha=0.15)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc="center left", bbox_to_anchor=(1.02, 0.5),
              fontsize=8.5, frameon=False, title=heb("קריטריון (משקל)"), title_fontsize=9)
    fig.tight_layout()
    finish(fig, "ch5_decision.pdf", d)


# ---------- ch6: Gantt ----------
def chart_gantt():
    d = load("gantt.json")
    weeks, wps, mss = d["weeks"], d["work_packages"], d["milestones"]
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    rows = {wp["id"]: i for i, wp in enumerate(wps)}
    ms_y = len(wps) + 0.2
    # reserve weeks as hatched vertical bands
    for m in mss:
        w = m["reserve_week"]
        ax.add_patch(Rectangle((w - 1, -0.6), 1, ms_y + 1.2, facecolor=ACCENT, alpha=0.45,
                               edgecolor=INK, lw=0.6, hatch="///", zorder=1))
    # bars
    for wp in wps:
        y = rows[wp["id"]]
        x0, x1 = wp["start"] - 1, wp["end"]
        col = MAIN if wp["critical"] else HIGHLIGHT
        ax.barh(y, x1 - x0, left=x0, height=0.5, color=col, edgecolor=INK, lw=0.9, zorder=3)
        ax.text((x0 + x1) / 2, y, f"{wp['start']}–{wp['end']}", ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=text_on(col), zorder=4)
    # dependencies
    for wp in wps:
        for dep in wp["depends"]:
            p = next(w for w in wps if w["id"] == dep)
            crit = p["critical"] and wp["critical"]
            ax.annotate("", xy=(wp["start"] - 1, rows[wp["id"]]), xytext=(p["end"], rows[dep]),
                        arrowprops=dict(arrowstyle="-|>", color=MAIN if crit else INK,
                                        lw=1.4 if crit else 0.9, shrinkA=1, shrinkB=1,
                                        connectionstyle="angle,angleA=0,angleB=90,rad=0"), zorder=2)
    # milestones
    for m in mss:
        xc = m["week"] - 0.5  # middle of the milestone week
        ax.plot([xc], [ms_y], marker="D", ms=10, color=INK, zorder=5)
        ax.axvline(xc, color=INK, lw=0.8, ls="--", alpha=0.6, zorder=1)
        last = m["week"] >= weeks - 1
        ax.text(weeks if last else xc + 0.3, ms_y + 0.95, heb(m["name_he"], wrap=22),
                ha="right" if last else "left", va="center", fontsize=8.5, zorder=6,
                bbox=dict(fc=PAPER, ec="none", pad=1))
    ax.set_xlim(0, weeks)
    ax.set_ylim(ms_y + 1.5, -0.7)
    ax.set_xticks(np.arange(weeks) + 0.5)
    ax.set_xticklabels([str(i) for i in range(1, weeks + 1)], fontsize=9)
    ax.set_xticks(np.arange(weeks + 1), minor=True)
    ax.grid(axis="x", which="minor", color=INK, alpha=0.12)
    ax.tick_params(axis="x", which="both", length=0)
    ax.set_yticks(list(rows.values()) + [ms_y])
    ax.set_yticklabels([heb(f"חבילה {wp['id'][2:]}: {wp['name_he']}", wrap=26) for wp in wps] + [heb("אבני דרך")], fontsize=9)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel(heb("שבוע"))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    handles = [
        Patch(facecolor=MAIN, edgecolor=INK, label=heb("נתיב קריטי")),
        Patch(facecolor=HIGHLIGHT, edgecolor=INK, label=heb("מחוץ לנתיב הקריטי")),
        Patch(facecolor=ACCENT, edgecolor=INK, alpha=0.6, hatch="///", label=heb("שבוע רזרבה")),
        Line2D([0], [0], marker="D", color="none", markerfacecolor=INK, markeredgecolor=INK,
               ms=8, label=heb("אבן דרך")),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, fontsize=9, frameon=False)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    finish(fig, "ch6_gantt.pdf", d)


# ---------- ch7: risk matrix ----------
def chart_risk():
    d = load("risks.json")
    thr = d["critical_threshold"]
    risks = d["risks"]
    fig = plt.figure(figsize=(6.8, 4.4))
    ax = fig.add_axes([0.09, 0.14, 0.46, 0.80])
    for p in range(1, 6):
        for i in range(1, 6):
            crit = p * i >= thr
            ax.add_patch(Rectangle((i - 0.5, p - 0.5), 1, 1,
                                   facecolor=MAIN if crit else PAPER, alpha=0.28 if crit else 1,
                                   edgecolor=INK, lw=0.6, zorder=1))
            ax.text(i + 0.4, p - 0.4, str(p * i), ha="right", va="bottom", fontsize=7, color=INK, alpha=0.5)
    # spread risks that share a cell
    cells = {}
    for r in risks:
        cells.setdefault((r["I"], r["P"]), []).append(r)
    offs = {1: [(0, 0)], 2: [(-0.2, 0), (0.2, 0)], 3: [(-0.22, -0.12), (0.22, -0.12), (0, 0.18)],
            4: [(-0.2, -0.17), (0.2, -0.17), (-0.2, 0.17), (0.2, 0.17)]}
    for (i, p), grp in cells.items():
        for r, (dx, dy) in zip(grp, offs[min(len(grp), 4)]):
            crit = r["P"] * r["I"] >= thr
            ax.scatter(i + dx, p + dy, s=330, color=MAIN if crit else INK, edgecolor=INK, lw=0.8, zorder=3)
            ax.text(i + dx, p + dy, r["id"], ha="center", va="center", fontsize=8,
                    fontweight="bold", color=PAPER, zorder=4)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel(heb("השפעה – I"))
    ax.set_ylabel(heb("הסתברות – P"))
    ax.set_aspect("equal")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    # key list
    lx = fig.add_axes([0.58, 0.14, 0.40, 0.80])
    lx.axis("off")
    lx.set_xlim(0, 1)
    lx.set_ylim(0, 1)
    ordered = sorted(risks, key=lambda r: -r["P"] * r["I"])
    lx.text(1, 1, heb("סיכון"), ha="right", va="top", fontsize=9.5, fontweight="bold")
    for k, r in enumerate(ordered):
        y = 0.90 - k * 0.115
        R = r["P"] * r["I"]
        crit = R >= thr
        w = "bold" if crit else "normal"
        lx.text(1, y, r["id"], ha="right", va="center", fontsize=8.5, fontweight=w)
        lx.text(0.88, y, heb(r["name_he"], wrap=34), ha="right", va="center", fontsize=8.5, fontweight=w)
        lx.text(0.0, y, f"R={R}", ha="left", va="center", fontsize=8.5, fontweight=w)
    fig.text(0.58, 0.04, heb(f"האזור הקריטי מוצלל: R ≥ {thr}"), ha="left", fontsize=8.5)
    finish(fig, "ch7_risk.pdf", d)


def main():
    OUT.mkdir(exist_ok=True)
    chart_radar()
    chart_scatter()
    chart_decision()
    chart_gantt()
    chart_risk()
    if placeholder_charts:
        print("WARNING: charts built from PLACEHOLDER data (resolve before submission):")
        for n in placeholder_charts:
            print("  -", n)
    print("Wrote:", ", ".join(sorted(p.name for p in OUT.glob("*.pdf"))))


if __name__ == "__main__":
    main()

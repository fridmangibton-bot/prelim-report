"""Build contact sheets of rendered pages: py scripts/contact_sheet.py first last out.png [cols]"""
import sys
from pathlib import Path
from PIL import Image
a, b, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 4
d = Path("build/png")
ims = [Image.open(d / f"p-{i:02d}.png") for i in range(a, b + 1)]
w, h = ims[0].size
rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (w * cols, h * rows), "white")
for k, im in enumerate(ims):
    sheet.paste(im, ((k % cols) * w, (k // cols) * h))
sheet.save(out)

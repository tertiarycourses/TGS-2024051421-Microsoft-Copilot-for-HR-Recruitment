#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from PIL import Image, ImageDraw

source = Path(sys.argv[1])
out = Path(sys.argv[2])
per = int(sys.argv[3]) if len(sys.argv) > 3 else 24
out.mkdir(parents=True, exist_ok=True)
files = sorted(source.glob("*.png"), key=lambda p: int(re.search(r"(\d+)$", p.stem).group(1)))
thumb_w, thumb_h = 320, 180
cols = 4
rows = (per + cols - 1) // cols
for sheet_no, start in enumerate(range(0, len(files), per), 1):
    subset = files[start:start+per]
    canvas = Image.new("RGB", (cols*thumb_w, rows*(thumb_h+24)), "#dfe6ee")
    draw = ImageDraw.Draw(canvas)
    for i, path in enumerate(subset):
        im = Image.open(path).convert("RGB")
        im.thumbnail((thumb_w-8, thumb_h-8))
        x = (i % cols)*thumb_w + (thumb_w-im.width)//2
        y = (i // cols)*(thumb_h+24) + 4
        canvas.paste(im, (x, y))
        draw.text(((i % cols)*thumb_w+8, (i//cols)*(thumb_h+24)+thumb_h+2), path.stem, fill="#161b26")
    canvas.save(out/f"sheet-{sheet_no:02d}.jpg", quality=88)
print(f"files={len(files)} sheets={len(list(out.glob('*.jpg')))}")

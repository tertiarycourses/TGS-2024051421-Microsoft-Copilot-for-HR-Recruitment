#!/usr/bin/env python3
"""Rewrite PDF page objects to ensure stable rendering across Poppler and Preview."""

import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


for name in sys.argv[1:]:
    path = Path(name)
    reader = PdfReader(str(path))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    tmp = path.with_suffix(".normalized.pdf")
    with tmp.open("wb") as handle:
        writer.write(handle)
    tmp.replace(path)
    print(f"normalized pages={len(reader.pages)} file={path}")

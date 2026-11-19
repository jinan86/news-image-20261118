#!/usr/bin/env python3
"""News-image entry (Python 3.13, standard library only).

Writes the one picture of Wednesday 18 November 2026's world news to
/output/entry.png. The image is the entry.png beside this file, drawn
with PIL as a newspaper front page; this program copies it byte for byte,
so two runs always write the same bytes and no network is needed.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")

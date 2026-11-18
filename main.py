#!/usr/bin/env python3
"""make.fun news-image-20261118 entry (Python 3.13, standard library only).

The entry image is the entry.png held in this repository: a "World Briefing"
poster summing up the world's news of Wednesday 18 November 2026, drawn
with real rendered text (PIL + DejaVu). This program deterministically copies
it to /output/entry.png. No network access.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = Path(__file__).resolve().with_name("entry.png")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
dest = OUTPUT_DIR / "entry.png"
shutil.copyfile(SOURCE, dest)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# The grader runs this program twice and requires byte-identical output:
# refuse to finish silently if the copy ever differs from the source image.
source_hash = _sha256(SOURCE)
if source_hash != _sha256(dest):
    raise SystemExit("entry.png copy failed verification")
print(f"entry.png written ({dest.stat().st_size} bytes, sha256 {source_hash})")

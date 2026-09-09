#!/usr/bin/env python3
"""Extract one image per page from a scanned PDF that has no text layer.

The BFRE whitepaper is a scan: every page is a single embedded JPEG, so
pdftotext yields nothing and any transcription has to go through the images.

    pip install pypdf pillow
    python tools/extract_pages.py BFRE_paper.pdf out/img
"""
import os
import sys

from pypdf import PdfReader


def main(pdf_path: str, out_dir: str) -> int:
    reader = PdfReader(pdf_path)
    os.makedirs(out_dir, exist_ok=True)
    written = 0
    for index, page in enumerate(reader.pages, start=1):
        images = list(page.images)
        if not images:
            print(f"page {index}: no embedded image (text-layer page?)")
            continue
        image = images[0]
        ext = os.path.splitext(image.name)[1] or ".jpg"
        path = os.path.join(out_dir, f"p{index:03d}{ext}")
        with open(path, "wb") as handle:
            handle.write(image.data)
        written += 1
    print(f"wrote {written} page images to {out_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))

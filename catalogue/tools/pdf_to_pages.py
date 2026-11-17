#!/usr/bin/env python3
"""
Converts the real catalogue PDF into the page images + pages.json manifest
the viewer expects, replacing the dummy placeholder data.

Usage:
    python3 tools/pdf_to_pages.py --pdf /path/to/catalogue.pdf

Optional:
    --dpi 150            Render resolution (150 is plenty for screen viewing;
                          go higher only if people will zoom in a lot)
    --max-width 1100      Downscale render to this width in px (keeps file
                          size sane even if --dpi is high)
    --quality 80          JPEG quality (70-85 is a good range for catalogues)
    --out-dir .           Project root (where images/ and data/ live)
    --title "..."         Catalogue title stored in the manifest
    --poppler-path ...    Folder containing pdftoppm.exe / pdfinfo.exe
                          (Windows only, if poppler isn't on your PATH —
                          point this at poppler's "Library\\bin" or "bin"
                          folder instead of editing PATH)

This REPLACES images/pages/*, images/thumbs/* and data/pages.json.
If you have per-page captions / product links / SKUs, see
--captions-csv below to merge them in.

    --captions-csv captions.csv
        CSV with columns: page,caption,product_url
        (page is the 1-based page number; captions.csv is optional —
        without it, pages just get "Page N" captions, which you can
        fill in by hand in data/pages.json afterwards)
"""
import argparse
import csv
import json
import os
import shutil

from pdf2image import convert_from_path
from PIL import Image


def load_captions(path):
    if not path or not os.path.exists(path):
        return {}
    out = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            out[int(row["page"])] = {
                "caption": row.get("caption", "").strip(),
                "product_url": row.get("product_url", "").strip() or None,
            }
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True, help="Path to the catalogue PDF")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--max-width", type=int, default=1100)
    ap.add_argument("--quality", type=int, default=80)
    ap.add_argument("--out-dir", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--title", default="Product Catalogue")
    ap.add_argument("--captions-csv", default=None)
    ap.add_argument("--poppler-path", default=None, help="Windows: folder with pdftoppm.exe, if not on PATH")
    args = ap.parse_args()

    pages_dir = os.path.join(args.out_dir, "images", "pages")
    thumbs_dir = os.path.join(args.out_dir, "images", "thumbs")
    data_path = os.path.join(args.out_dir, "data", "pages.json")

    for d in (pages_dir, thumbs_dir, os.path.dirname(data_path)):
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)

    captions = load_captions(args.captions_csv)

    print(f"Rendering {args.pdf} at {args.dpi} DPI ...")
    images = convert_from_path(args.pdf, dpi=args.dpi, poppler_path=args.poppler_path)
    total = len(images)
    print(f"{total} pages found.")

    manifest_pages = []
    page_w = page_h = None

    for i, im in enumerate(images, start=1):
        im = im.convert("RGB")
        if im.width > args.max_width:
            ratio = args.max_width / im.width
            im = im.resize((args.max_width, int(im.height * ratio)), Image.LANCZOS)

        if page_w is None:
            page_w, page_h = im.width, im.height

        fname = f"page-{i:03d}.jpg"
        page_path = os.path.join(pages_dir, fname)
        im.save(page_path, "JPEG", quality=args.quality, optimize=True)

        thumb = im.copy()
        thumb.thumbnail((200, 280))
        thumb.save(os.path.join(thumbs_dir, fname), "JPEG", quality=70, optimize=True)

        meta = captions.get(i, {})
        page_type = "cover" if i in (1, total) else "product"
        manifest_pages.append({
            "page": i,
            "type": page_type,
            "img": f"images/pages/{fname}",
            "thumb": f"images/thumbs/{fname}",
            "caption": meta.get("caption") or (None if page_type == "cover" else f"Page {i}"),
            "product_url": meta.get("product_url"),
        })

        if i % 25 == 0 or i == total:
            print(f"  {i}/{total} pages done")

    manifest = {
        "title": args.title,
        "page_width": page_w,
        "page_height": page_h,
        "total_pages": total,
        "pages": manifest_pages,
    }
    with open(data_path, "w") as f:
        json.dump(manifest, f, indent=2)

    total_bytes = sum(os.path.getsize(os.path.join(args.out_dir, p["img"])) for p in manifest_pages)
    print(f"\nDone. {total} pages written to {pages_dir}")
    print(f"Avg page size: {total_bytes/total/1024:.0f} KB  (total {total_bytes/1024/1024:.1f} MB)")
    print(f"Manifest: {data_path}")
    if not args.captions_csv:
        print("\nNo --captions-csv given — captions/product links are blank except on product pages' default 'Page N'.")
        print("Edit data/pages.json directly, or re-run with --captions-csv to merge them in bulk.")


if __name__ == "__main__":
    main()

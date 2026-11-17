#!/usr/bin/env python3
"""
Generates a placeholder 150-page catalogue (images + pages.json) so the
flipbook viewer can be tested at full scale before the real catalogue
artwork is ready.

Run: python3 tools/generate_dummy_pages.py
Output: images/pages/page-XXX.jpg, images/thumbs/page-XXX.jpg, data/pages.json
"""
import json
import os
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(ROOT, "images", "pages")
THUMBS_DIR = os.path.join(ROOT, "images", "thumbs")
DATA_PATH = os.path.join(ROOT, "data", "pages.json")

PAGE_W, PAGE_H = 900, 1260  # ~A4-ish portrait, catalogue-sized
THUMB_W, THUMB_H = 180, 252

NUM_PRODUCT_PAGES = 148  # + 1 front cover + 1 back cover = 150

CATEGORIES = [
    "Downlights", "Panel Lights", "Street Lights", "Flood Lights",
    "High Bay Lights", "Strip Lights", "Track Lights", "Bulkheads",
    "Linear Lights", "Garden Spikes", "Wall Washers", "Emergency Exit",
]

BRAND_BG = (16, 20, 28)
ACCENT = (241, 196, 15)  # matches sample style.css yellow accent
WHITE = (240, 240, 240)
MUTED = (150, 158, 170)


def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def draw_cover(path, title, subtitle):
    img = Image.new("RGB", (PAGE_W, PAGE_H), BRAND_BG)
    d = ImageDraw.Draw(img)
    for i in range(0, PAGE_H, 4):
        shade = int(16 + 10 * (i / PAGE_H))
        d.line([(0, i), (PAGE_W, i)], fill=(shade, shade + 2, shade + 6))
    d.rectangle([60, PAGE_H - 420, PAGE_W - 60, PAGE_H - 60], outline=ACCENT, width=3)
    title_font = _font(64, bold=True)
    sub_font = _font(28)
    d.text((PAGE_W / 2, PAGE_H / 2 - 60), title, font=title_font, fill=WHITE, anchor="mm")
    d.text((PAGE_W / 2, PAGE_H / 2 + 20), subtitle, font=sub_font, fill=ACCENT, anchor="mm")
    img.save(path, quality=82, optimize=True)


def draw_product_page(path, page_no, category, sku):
    img = Image.new("RGB", (PAGE_W, PAGE_H), (250, 250, 250))
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, PAGE_W, 90], fill=BRAND_BG)
    d.text((40, 45), category, font=_font(26, bold=True), fill=ACCENT, anchor="lm")
    d.text((PAGE_W - 40, 45), "LumaCore LED", font=_font(22), fill=WHITE, anchor="rm")

    cx, cy = PAGE_W / 2, 480
    rng = random.Random(page_no)
    shape = rng.choice(["circle", "panel", "tube", "bay"])
    fixture_color = (60, 64, 70)
    if shape == "circle":
        r = 180
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fixture_color, outline=(30, 30, 30), width=4)
        d.ellipse([cx - r + 25, cy - r + 25, cx + r - 25, cy + r - 25], fill=(255, 250, 225))
    elif shape == "panel":
        d.rectangle([cx - 220, cy - 150, cx + 220, cy + 150], fill=fixture_color, outline=(30, 30, 30), width=4)
        d.rectangle([cx - 190, cy - 120, cx + 190, cy + 120], fill=(255, 250, 225))
    elif shape == "tube":
        d.rounded_rectangle([cx - 260, cy - 50, cx + 260, cy + 50], radius=25, fill=fixture_color, outline=(30, 30, 30), width=4)
        d.rounded_rectangle([cx - 230, cy - 25, cx + 230, cy + 25], radius=15, fill=(255, 250, 225))
    else:
        pts = [(cx, cy - 190), (cx - 190, cy + 140), (cx + 190, cy + 140)]
        d.polygon(pts, fill=fixture_color, outline=(30, 30, 30), width=4)
        d.ellipse([cx - 60, cy + 40, cx + 60, cy + 160], fill=(255, 250, 225))

    name_font = _font(34, bold=True)
    label_font = _font(20)
    val_font = _font(20, bold=True)
    d.text((60, 740), f"{category} — Model LC-{900 + page_no}", font=name_font, fill=(20, 20, 20))

    specs = [
        ("SKU", sku),
        ("Wattage", f"{rng.choice([9, 12, 18, 24, 36, 50, 100])} W"),
        ("Lumens", f"{rng.choice([900, 1200, 1800, 2400, 3600, 5000])} lm"),
        ("CCT", f"{rng.choice(['3000K Warm','4000K Natural','6500K Cool'])}"),
        ("Body Material", rng.choice(["Die-cast Aluminium", "Aluminium + PC", "Extruded Aluminium"])),
        ("IP Rating", rng.choice(["IP20", "IP44", "IP65", "IP66"])),
        ("Warranty", f"{rng.choice([1,2,3,5])} Years"),
    ]
    y = 800
    for label, val in specs:
        d.text((60, y), label, font=label_font, fill=MUTED)
        d.text((320, y), str(val), font=val_font, fill=(20, 20, 20))
        y += 42

    d.rectangle([0, PAGE_H - 70, PAGE_W, PAGE_H], fill=BRAND_BG)
    d.text((40, PAGE_H - 35), f"www.yourledbrand.com", font=_font(18), fill=MUTED, anchor="lm")
    d.text((PAGE_W - 40, PAGE_H - 35), f"Page {page_no}", font=_font(18), fill=WHITE, anchor="rm")

    img.save(path, quality=80, optimize=True)


def main():
    os.makedirs(PAGES_DIR, exist_ok=True)
    os.makedirs(THUMBS_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    pages = []

    cover_path = os.path.join(PAGES_DIR, "page-001.jpg")
    draw_cover(cover_path, "LED LIGHTING", "2026 Product Catalogue")
    pages.append({"page": 1, "type": "cover", "img": "images/pages/page-001.jpg",
                  "caption": "2026 Product Catalogue"})

    page_no = 2
    sku_counter = 1000
    for _ in range(NUM_PRODUCT_PAGES):
        category = random.choice(CATEGORIES)
        sku = f"LED-{sku_counter}"
        sku_counter += 1
        fname = f"page-{page_no:03d}.jpg"
        draw_product_page(os.path.join(PAGES_DIR, fname), page_no, category, sku)
        pages.append({
            "page": page_no, "type": "product", "img": f"images/pages/{fname}",
            "caption": f"{category} · {sku}",
            "product_url": f"/products/{sku.lower()}"
        })
        page_no += 1

    back_fname = f"page-{page_no:03d}.jpg"
    draw_cover(os.path.join(PAGES_DIR, back_fname), "THANK YOU", "Scan or call for a custom quote")
    pages.append({"page": page_no, "type": "cover", "img": f"images/pages/{back_fname}",
                  "caption": "Thank you"})

    # thumbnails
    for p in pages:
        src = os.path.join(ROOT, p["img"])
        im = Image.open(src)
        im.thumbnail((THUMB_W, THUMB_H))
        thumb_rel = p["img"].replace("images/pages/", "images/thumbs/")
        im.save(os.path.join(ROOT, thumb_rel), quality=70, optimize=True)
        p["thumb"] = thumb_rel

    manifest = {
        "title": "LED Lighting Catalogue",
        "page_width": PAGE_W,
        "page_height": PAGE_H,
        "total_pages": len(pages),
        "pages": pages,
    }
    with open(DATA_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    total_bytes = sum(os.path.getsize(os.path.join(ROOT, p["img"])) for p in pages)
    print(f"Generated {len(pages)} pages.")
    print(f"Total images size: {total_bytes/1024/1024:.1f} MB (avg {total_bytes/len(pages)/1024:.0f} KB/page)")
    print(f"Manifest: {DATA_PATH}")


if __name__ == "__main__":
    main()

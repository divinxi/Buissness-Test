"""Generates 'look inside' preview images (real content, not a branded mockup).

Gumroad supports 4-6 additional listing images beyond the cover; research
(products/MARKET-NOTES.md, 2026-08-02 entry) found none of our listings use
this, even though showing real page/spreadsheet content is a documented
conversion lever for zero-review listings. These images pull directly from
content.py so they can never drift out of sync with the actual PDF.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import content

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "dist")

W, H = 1600, 1000
BG = (28, 28, 30)
ACCENT = (122, 200, 174)
MUTED = (170, 170, 176)
PAGE_BG = (250, 250, 249)
INK = (40, 40, 42)
INK_MUTED = (110, 110, 116)

FONT_DIRS = [
    "C:/Windows/Fonts",
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]
FONT_ALIASES = {
    "arialbd.ttf": ["arialbd.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"],
    "arial.ttf": ["arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf"],
}


def load_font(name, size):
    for fname in FONT_ALIASES.get(name, [name]):
        for d in FONT_DIRS:
            c = os.path.join(d, fname)
            if os.path.exists(c):
                return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textbbox((0, 0), trial, font=font)[2] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def frame(label):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=ACCENT)
    tag_font = load_font("arialbd.ttf", 26)
    d.text((44, 36), label, font=tag_font, fill=ACCENT)
    d.text((44, H - 56), "Ledger & Loop Digital — AI Prompt Playbook Vol. 2: Systems & Automation",
           font=load_font("arial.ttf", 24), fill=MUTED)
    return img, d


def build_inside_page():
    img, d = frame("LOOK INSIDE — A REAL PAGE FROM THE GUIDE")
    cat = content.CATEGORIES[0]  # Build Your AI Systems
    px, py, pw, ph = 300, 110, 1000, 800
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=18, fill=PAGE_BG)

    head_font = load_font("arialbd.ttf", 38)
    body_font = load_font("arial.ttf", 24)
    small_font = load_font("arial.ttf", 21)
    label_font = load_font("arialbd.ttf", 21)

    x = px + 60
    y = py + 50
    d.rounded_rectangle([x, y, x + 16, y + 44], radius=4, fill=ACCENT)
    d.text((x + 32, y), cat["name"], font=head_font, fill=INK)
    y += 80
    d.text((x, y), f"{len(cat['prompts'])} prompts in this category — showing 2 of them below",
           font=small_font, fill=INK_MUTED)
    y += 50

    for p in cat["prompts"][:2]:
        d.text((x, y), p["title"], font=load_font("arialbd.ttf", 28), fill=(30, 110, 90))
        y += 40
        snippet = p["prompt"][:220].rsplit(" ", 1)[0] + "..."
        for line in wrap(d, snippet, body_font, pw - 120)[:3]:
            d.text((x, y), line, font=body_font, fill=INK)
            y += 32
        y += 6
        d.text((x, y), "WHEN: ", font=label_font, fill=(150, 150, 155))
        w0 = d.textbbox((0, 0), "WHEN: ", font=label_font)[2]
        for line in wrap(d, p["when"], small_font, pw - 120 - w0)[:1]:
            d.text((x + w0, y), line, font=small_font, fill=INK_MUTED)
        y += 46

    d.line([x, y, px + pw - 60, y], fill=(220, 220, 222), width=2)
    y += 24
    remaining = sum(len(c["prompts"]) for c in content.CATEGORIES) - 2
    tail = (f"...plus {remaining} more prompts across {len(content.CATEGORIES)} categories: "
            + ", ".join(c["name"] for c in content.CATEGORIES[1:]))
    for line in wrap(d, tail, small_font, pw - 120):
        d.text((x, y), line, font=small_font, fill=INK_MUTED)
        y += 30
    img.save(os.path.join(OUT_DIR, "preview-1-inside-guide.png"))
    print("Wrote preview-1-inside-guide.png")


def build_inside_tracker():
    img, d = frame("LOOK INSIDE — THE COMPANION AUTOMATION ROI TRACKER (.xlsx)")
    headers = ["Date Set Up", "Workflow Name", "Frequency", "Monthly Min. Saved", "Notes"]
    sample_rows = [
        ["2026-08-03", "Weekly Ops Review Generator", "Weekly", "130", "Now runs itself every Monday"],
        ["2026-08-10", "Knowledge Base Q&A Builder", "One-time", "0", "Built once, still referenced daily"],
        ["2026-08-17", "Customer Win-Back Sequence", "Monthly", "45", "3 replies from 12 sent"],
    ]
    gx, gy, gw = 200, 300, 1200
    col_w = [160, 320, 170, 230, 320]
    header_h = 76
    row_h = 64
    header_font = load_font("arialbd.ttf", 19)
    cell_font = load_font("arial.ttf", 20)

    d.rounded_rectangle([gx - 20, gy - 40, gx + gw + 20, gy + header_h + row_h * len(sample_rows) + 40],
                         radius=16, fill=PAGE_BG)
    x = gx
    for h, w in zip(headers, col_w):
        d.rectangle([x, gy, x + w, gy + header_h], fill=ACCENT)
        lines = wrap(d, h, header_font, w - 20)[:2]
        ty = gy + header_h / 2 - (len(lines) * 24) / 2
        for line in lines:
            d.text((x + 12, ty), line, font=header_font, fill=(20, 20, 22))
            ty += 24
        x += w
    for ri, row in enumerate(sample_rows):
        ry = gy + header_h + row_h * ri
        x = gx
        fill = (255, 255, 255) if ri % 2 == 0 else (240, 240, 238)
        d.rectangle([gx, ry, gx + gw, ry + row_h], fill=fill)
        for val, w in zip(row, col_w):
            for li, line in enumerate(wrap(d, val, cell_font, w - 20)[:2]):
                d.text((x + 12, ry + 10 + li * 24), line, font=cell_font, fill=INK)
            x += w
    for c in range(len(headers) + 1):
        xx = gx + sum(col_w[:c])
        d.line([xx, gy, xx, gy + header_h + row_h * len(sample_rows)], fill=(210, 210, 212), width=1)

    note_font = load_font("arial.ttf", 22)
    note_y = gy + header_h + row_h * len(sample_rows) + 60
    d.text((gx - 20, note_y),
           "Also tracks Category and Time Saved per Run — Monthly Minutes Saved auto-calculates",
           font=note_font, fill=MUTED)
    d.text((gx - 20, note_y + 32),
           "from frequency, so a Weekly habit compounds correctly against a Monthly one.",
           font=note_font, fill=MUTED)
    img.save(os.path.join(OUT_DIR, "preview-2-inside-tracker.png"))
    print("Wrote preview-2-inside-tracker.png")


if __name__ == "__main__":
    build_inside_page()
    build_inside_tracker()

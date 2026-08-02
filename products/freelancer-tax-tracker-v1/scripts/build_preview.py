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
    d.text((44, H - 56), "Ledger & Loop Digital — Freelancer Quarterly Tax & Expense Tracker (2026)",
           font=load_font("arial.ttf", 24), fill=MUTED)
    return img, d


def build_inside_page():
    """A real page from the guide: the actual 2026 quarterly deadlines + Schedule C excerpt."""
    img, d = frame("LOOK INSIDE — REAL 2026 FIGURES, NOT PLACEHOLDERS")
    px, py, pw, ph = 220, 110, 1160, 800
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=18, fill=PAGE_BG)

    head_font = load_font("arialbd.ttf", 36)
    small_font = load_font("arial.ttf", 21)
    label_font = load_font("arialbd.ttf", 21)
    cell_font = load_font("arial.ttf", 22)

    x = px + 50
    y = py + 40
    d.rounded_rectangle([x, y, x + 16, y + 40], radius=4, fill=ACCENT)
    d.text((x + 32, y - 4), f"{content.TAX_YEAR} Quarterly Estimated Tax Deadlines", font=head_font, fill=INK)
    y += 70

    col_w = [180, 340, 220]
    gx = x
    header_h = 44
    row_h = 46
    for h, w in zip(["Quarter", "Covers", "Due"], col_w):
        d.rectangle([gx, y, gx + w, y + header_h], fill=ACCENT)
        d.text((gx + 12, y + 10), h, font=label_font, fill=(20, 20, 22))
        gx += w
    for i, row in enumerate(content.QUARTERLY_DEADLINES):
        ry = y + header_h + row_h * i
        gx = x
        fill = (255, 255, 255) if i % 2 == 0 else (240, 240, 238)
        d.rectangle([gx, ry, gx + sum(col_w), ry + row_h], fill=fill)
        for val, w in zip([row["quarter"], row["covers"], row["due"]], col_w):
            d.text((gx + 12, ry + 11), val, font=cell_font, fill=INK)
            gx += w
    y += header_h + row_h * len(content.QUARTERLY_DEADLINES) + 40

    se_line = (f"Self-employment tax rate: {content.SE_TAX_FACTS['rate_total']*100:.1f}% "
               f"(on {content.SE_TAX_FACTS['net_earnings_factor']*100:.2f}% of net profit) — "
               f"the guide shows this worked with your own numbers.")
    for line in wrap(d, se_line, small_font, pw - 100):
        d.text((x, y), line, font=small_font, fill=INK_MUTED)
        y += 30
    y += 16

    d.line([x, y, px + pw - 50, y], fill=(220, 220, 222), width=2)
    y += 26
    d.text((x, y), "3 of 17 real IRS Schedule C categories decoded in the guide:", font=label_font, fill=INK)
    y += 40
    for cat in content.SCHEDULE_C_CATEGORIES[:3]:
        d.text((x, y), f"{cat['line']} — {cat['name']}", font=load_font("arialbd.ttf", 23), fill=(30, 110, 90))
        y += 32
        for line in wrap(d, cat["what_counts"], small_font, pw - 100)[:2]:
            d.text((x, y), line, font=small_font, fill=INK_MUTED)
            y += 28
        y += 10

    img.save(os.path.join(OUT_DIR, "preview-1-inside-guide.png"))
    print("Wrote preview-1-inside-guide.png")


def build_inside_tracker():
    """A mockup of the real Expense Log, showing the auto-50%-meals-rule in action."""
    img, d = frame("LOOK INSIDE — THE EXPENSE LOG (.xlsx), AUTO-FILLS THE 50% MEALS RULE")
    headers = ["Date", "Category", "Vendor", "Amount", "Ded. %", "Ded. Amount"]
    sample_rows = [
        ["2026-08-03", "Office Expense", "Adobe Creative Cloud", "$54.99", "100%", "$54.99"],
        ["2026-08-05", "Meals", "Lunch w/ Acme Co (scope review)", "$62.40", "50%", "$31.20"],
        ["2026-08-12", "Contract Labor", "J. Rivera (subcontractor)", "$400.00", "100%", "$400.00"],
    ]
    gx, gy, gw = 200, 300, 1200
    col_w = [150, 220, 340, 150, 130, 210]
    header_h = 56
    row_h = 64
    header_font = load_font("arialbd.ttf", 19)
    cell_font = load_font("arial.ttf", 20)

    d.rounded_rectangle([gx - 20, gy - 40, gx + gw + 20, gy + header_h + row_h * len(sample_rows) + 40],
                         radius=16, fill=PAGE_BG)
    x = gx
    for h, w in zip(headers, col_w):
        d.rectangle([x, gy, x + w, gy + header_h], fill=ACCENT)
        d.text((x + 12, gy + header_h / 2 - 12), h, font=header_font, fill=(20, 20, 22))
        x += w
    for ri, row in enumerate(sample_rows):
        ry = gy + header_h + row_h * ri
        x = gx
        fill = (255, 255, 255) if ri % 2 == 0 else (240, 240, 238)
        d.rectangle([gx, ry, gx + gw, ry + row_h], fill=fill)
        for ci, (val, w) in enumerate(zip(row, col_w)):
            hl = fill if ci != 4 else (200, 232, 220)  # highlight the auto-filled Ded.% cell
            if ci == 4:
                d.rectangle([x, ry, x + w, ry + row_h], fill=hl)
            for li, line in enumerate(wrap(d, val, cell_font, w - 20)[:2]):
                d.text((x + 12, ry + 10 + li * 24), line, font=cell_font, fill=INK)
            x += w
    for c in range(len(headers) + 1):
        xx = gx + sum(col_w[:c])
        d.line([xx, gy, xx, gy + header_h + row_h * len(sample_rows)], fill=(210, 210, 212), width=1)

    note_font = load_font("arial.ttf", 22)
    note_y = gy + header_h + row_h * len(sample_rows) + 60
    d.text((gx - 20, note_y),
           "The Ded. % column (highlighted) auto-fills to 50% for Meals and 100% for everything",
           font=note_font, fill=MUTED)
    d.text((gx - 20, note_y + 32),
           "else — Ded. Amount then calculates itself. Sample rows shown — yours starts blank.",
           font=note_font, fill=MUTED)
    img.save(os.path.join(OUT_DIR, "preview-2-inside-tracker.png"))
    print("Wrote preview-2-inside-tracker.png")


if __name__ == "__main__":
    build_inside_page()
    build_inside_tracker()

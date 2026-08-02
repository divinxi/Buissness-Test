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
    d.text((44, H - 56), "Ledger & Loop Digital — Freelancer Invoice & Late-Payment Toolkit",
           font=load_font("arial.ttf", 24), fill=MUTED)
    return img, d


def build_inside_page():
    """A real page from the guide: the actual payment-terms decision table."""
    img, d = frame("LOOK INSIDE — CHOOSE PAYMENT TERMS BY CLIENT RISK, NOT GUESSWORK")
    px, py, pw, ph = 130, 110, 1360, 800
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=18, fill=PAGE_BG)

    head_font = load_font("arialbd.ttf", 34)
    small_font = load_font("arial.ttf", 20)
    label_font = load_font("arialbd.ttf", 20)
    cell_font = load_font("arial.ttf", 19)

    x = px + 46
    y = py + 40
    d.rounded_rectangle([x, y, x + 16, y + 40], radius=4, fill=ACCENT)
    d.text((x + 32, y - 6), "Payment Terms, Ranked by Risk", font=head_font, fill=INK)
    y += 66

    col_w = [230, 430, 470, 130]
    header_h = 40
    row_h_min = 58
    gx = x
    for h, w in zip(["Term", "Meaning", "Best For", "Risk"], col_w):
        d.rectangle([gx, y, gx + w, y + header_h], fill=ACCENT)
        d.text((gx + 12, y + 8), h, font=label_font, fill=(20, 20, 22))
        gx += w
    ty = y + header_h
    term_font = load_font("arialbd.ttf", 19)
    for i, row in enumerate(content.PAYMENT_TERMS):
        term_lines = wrap(d, row["term"], term_font, col_w[0] - 24)
        meaning_lines = wrap(d, row["meaning"], cell_font, col_w[1] - 24)
        best_lines = wrap(d, row["best_for"], cell_font, col_w[2] - 24)
        risk_lines = wrap(d, row["risk"], cell_font, col_w[3] - 20)
        rh = max(len(term_lines), len(meaning_lines), len(best_lines), len(risk_lines), 1) * 24 + 18
        rh = max(rh, row_h_min)
        gx = x
        fill = (255, 255, 255) if i % 2 == 0 else (240, 240, 238)
        d.rectangle([gx, ty, gx + sum(col_w), ty + rh], fill=fill)
        for li, line in enumerate(term_lines):
            d.text((gx + 12, ty + 10 + li * 24), line, font=term_font, fill=(30, 110, 90))
        gx += col_w[0]
        for li, line in enumerate(meaning_lines):
            d.text((gx + 12, ty + 10 + li * 24), line, font=cell_font, fill=INK)
        gx += col_w[1]
        for li, line in enumerate(best_lines):
            d.text((gx + 12, ty + 10 + li * 24), line, font=cell_font, fill=INK_MUTED)
        gx += col_w[2]
        for li, line in enumerate(risk_lines):
            d.text((gx + 10, ty + 10 + li * 24), line, font=cell_font, fill=INK)
        ty += rh
    for c in range(5):
        xx = x + sum(col_w[:c])
        d.line([xx, y, xx, ty], fill=(210, 210, 212), width=1)

    y = ty + 30
    d.line([x, y, px + pw - 46, y], fill=(220, 220, 222), width=2)
    y += 24
    d.text((x, y), content.DEPOSIT_STRATEGY["headline"], font=load_font("arialbd.ttf", 22), fill=INK)
    img.save(os.path.join(OUT_DIR, "preview-1-inside-guide.png"))
    print("Wrote preview-1-inside-guide.png")


def build_inside_tracker():
    """A mockup of the real Invoice Log, showing the auto Paid/Overdue/Upcoming flag."""
    img, d = frame("LOOK INSIDE — THE INVOICE LOG (.xlsx), AUTO-FLAGS WHAT'S OVERDUE")
    headers = ["Client", "Invoice #", "Amount", "Due Date", "Status", "Days Late"]
    sample_rows = [
        ["Acme Co", "INV-014", "$1,200.00", "2026-07-20", "Overdue", "13"],
        ["Rivera Design", "INV-015", "$450.00", "2026-08-10", "Upcoming", ""],
        ["Blue Fern LLC", "INV-013", "$800.00", "2026-07-05", "Paid", ""],
    ]
    status_colors = {"Overdue": (240, 200, 200), "Upcoming": (255, 236, 196), "Paid": (200, 232, 220)}
    col_w = [230, 150, 170, 180, 190, 150]
    gx, gy, gw = 200, 300, sum(col_w)
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
        base_fill = (255, 255, 255) if ri % 2 == 0 else (240, 240, 238)
        d.rectangle([gx, ry, gx + gw, ry + row_h], fill=base_fill)
        for ci, (val, w) in enumerate(zip(row, col_w)):
            if ci == 4:
                d.rectangle([x, ry, x + w, ry + row_h], fill=status_colors[val])
            for li, line in enumerate(wrap(d, val, cell_font, w - 20)[:2]):
                d.text((x + 12, ry + 10 + li * 24), line, font=cell_font, fill=INK)
            x += w
    for c in range(len(headers) + 1):
        xx = gx + sum(col_w[:c])
        d.line([xx, gy, xx, gy + header_h + row_h * len(sample_rows)], fill=(210, 210, 212), width=1)

    note_font = load_font("arial.ttf", 22)
    note_y = gy + header_h + row_h * len(sample_rows) + 60
    d.text((gx - 20, note_y),
           "Status (highlighted) and Days Late calculate themselves from Due Date and Date",
           font=note_font, fill=MUTED)
    d.text((gx - 20, note_y + 32),
           "Paid — no formulas to write. Sample rows shown — yours starts blank.",
           font=note_font, fill=MUTED)
    img.save(os.path.join(OUT_DIR, "preview-2-inside-tracker.png"))
    print("Wrote preview-2-inside-tracker.png")


if __name__ == "__main__":
    build_inside_page()
    build_inside_tracker()

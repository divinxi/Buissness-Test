import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "cover.png")

W, H = 1600, 1000  # Gumroad recommends ~1280x720+ landscape cover
BG = (28, 28, 30)
ACCENT = (122, 200, 174)
MUTED = (170, 170, 176)
WHITE = (245, 245, 244)

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


# Gumroad auto-generates a 600x600 thumbnail by center-cropping the cover
# (confirmed via 2026-08-20 research + a rendered simulation — see
# products/MARKET-NOTES.md). For a 1600x1000 cover that crop keeps only
# x:300-1300, so anything meant to be recognizable in that thumbnail
# (product title, brand name) must be centered inside this safe zone
# rather than left-margin aligned.
SAFE_L, SAFE_W = 320, 960


def safe_center(d, y, text, font, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = SAFE_L + max(0, (SAFE_W - tw) // 2)
    d.text((x, y), text, font=font, fill=fill)


def draw_doc_mockup(d, ox, oy, accent):
    """Small PDF-page + spreadsheet-grid mockup so the cover isn't text-only."""
    pdf_w, pdf_h = 250, 320
    page_bg = (245, 245, 244)
    line_col = (205, 205, 208)
    d.rounded_rectangle([ox, oy, ox + pdf_w, oy + pdf_h], radius=14, fill=page_bg)
    d.rounded_rectangle([ox + 22, oy + 26, ox + pdf_w - 22, oy + 46], radius=6, fill=accent)
    for i in range(6):
        ly = oy + 78 + i * 28
        lw = pdf_w - 44 if i % 3 != 2 else pdf_w - 100
        d.rectangle([ox + 22, ly, ox + 22 + lw, ly + 8], fill=line_col)

    xl_w, xl_h = 250, 200
    xox, xoy = ox + 60, oy + pdf_h - 80
    d.rounded_rectangle([xox + 8, xoy + 8, xox + xl_w + 8, xoy + xl_h + 8], radius=14, fill=(18, 18, 20))
    d.rounded_rectangle([xox, xoy, xox + xl_w, xoy + xl_h], radius=14, fill=(255, 255, 255))
    rows, cols = 4, 5
    gx0, gy0 = xox + 16, xoy + 16
    gw, gh = xl_w - 32, xl_h - 32
    cw, ch = gw / cols, gh / rows
    grid_col = (222, 222, 224)
    for r in range(rows + 1):
        yy = gy0 + r * ch
        d.line([gx0, yy, gx0 + gw, yy], fill=grid_col, width=2)
    for c in range(cols + 1):
        xx = gx0 + c * cw
        d.line([xx, gy0, xx, gy0 + gh], fill=grid_col, width=2)
    hr, hc = 1, 2
    d.rectangle([gx0 + hc * cw, gy0 + hr * ch, gx0 + (hc + 1) * cw, gy0 + (hr + 1) * ch], fill=accent)


def draw_badge(d, ox, oy, text, font):
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 20, 12
    d.rounded_rectangle([ox, oy, ox + tw + pad_x * 2, oy + th + pad_y * 2 + 6], radius=10, fill=ACCENT)
    d.text((ox + pad_x, oy + pad_y - 2), text, font=font, fill=(18, 18, 20))


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # subtle accent bar
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    draw_doc_mockup(d, 1220, 300, ACCENT)

    title_font = load_font("arialbd.ttf", 60)
    sub_font = load_font("arial.ttf", 38)
    tag_font = load_font("arialbd.ttf", 22)
    badge_font = load_font("arialbd.ttf", 30)

    margin = 110
    draw_badge(d, margin, 165, "VOL. 2", badge_font)

    safe_center(d, 240, "AI Prompt Playbook", title_font, WHITE)
    safe_center(d, 340, "Systems & Automation", title_font, ACCENT)

    d.text((margin, 470), "25 prompts for turning AI into repeatable systems —", font=sub_font, fill=MUTED)
    d.text((margin, 516), "not just one-off tasks.", font=sub_font, fill=MUTED)

    # bottom tag chips (two rows so long labels never collide with the mockup or run off-canvas)
    chip_rows = [
        ["AI SYSTEMS", "CUSTOMER LIFECYCLE", "COMPETITIVE INTEL"],
        ["OPS REPORTING", "DELEGATION"],
    ]
    y = 640
    for row in chip_rows:
        x = margin
        for chip in row:
            bbox = d.textbbox((0, 0), chip, font=tag_font)
            tw = bbox[2] - bbox[0]
            pad = 18
            d.rounded_rectangle([x, y, x + tw + pad * 2, y + 46], radius=23, outline=ACCENT, width=2)
            d.text((x + pad, y + 9), chip, font=tag_font, fill=ACCENT)
            x += tw + pad * 2 + 12
        y += 60

    safe_center(d, H - 90, "Ledger & Loop Digital", sub_font, MUTED)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

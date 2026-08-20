import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "cover.png")

W, H = 1600, 1000
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
    """Single PDF-page mockup — this is a PDF-only giveaway, no companion xlsx."""
    pdf_w, pdf_h = 300, 380
    page_bg = (245, 245, 244)
    line_col = (205, 205, 208)
    shadow = (18, 18, 20)
    d.rounded_rectangle([ox + 10, oy + 10, ox + pdf_w + 10, oy + pdf_h + 10], radius=16, fill=shadow)
    d.rounded_rectangle([ox, oy, ox + pdf_w, oy + pdf_h], radius=16, fill=page_bg)
    d.rounded_rectangle([ox + 26, oy + 32, ox + pdf_w - 26, oy + 56], radius=7, fill=accent)
    for i in range(8):
        ly = oy + 92 + i * 32
        lw = pdf_w - 52 if i % 3 != 2 else pdf_w - 120
        d.rectangle([ox + 26, ly, ox + 26 + lw, ly + 9], fill=line_col)


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, 14, H], fill=ACCENT)

    draw_doc_mockup(d, 1180, 290, ACCENT)

    title_font = load_font("arialbd.ttf", 56)
    sub_font = load_font("arial.ttf", 34)
    tag_font = load_font("arialbd.ttf", 26)
    eyebrow_font = load_font("arialbd.ttf", 28)
    price_font = load_font("arialbd.ttf", 42)

    margin = 110
    d.text((margin, 120), "FREE — 3-PAGE QUICK-START", font=eyebrow_font, fill=ACCENT)
    safe_center(d, 190, "The Freelancer Money", title_font, WHITE)
    safe_center(d, 258, "Admin Quick-Start", title_font, ACCENT)

    d.text((margin, 380), "Quarterly tax deadlines, the savings rule of thumb,", font=sub_font, fill=MUTED)
    d.text((margin, 422), "the #1 invoice habit, and a 5-question self-audit.", font=sub_font, fill=MUTED)

    chips = ["TAX DEADLINES", "INVOICE HABIT", "SELF-AUDIT"]
    x = margin
    y = 520
    for chip in chips:
        bbox = d.textbbox((0, 0), chip, font=tag_font)
        tw = bbox[2] - bbox[0]
        pad = 22
        d.rounded_rectangle([x, y, x + tw + pad * 2, y + 52], radius=26, outline=ACCENT, width=2)
        d.text((x + pad, y + 10), chip, font=tag_font, fill=ACCENT)
        x += tw + pad * 2 + 16

    d.text((margin, 640), "Free download", font=price_font, fill=WHITE)

    safe_center(d, H - 90, "Ledger & Loop Digital", sub_font, MUTED)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

import os
from PIL import Image, ImageDraw, ImageFont

DIST = os.path.join(os.path.dirname(__file__), "..", "dist")

# Pinterest's own 2026 spec (see products/OUTREACH-KIT.md section 5):
# vertical pins, 2:3 ratio, PNG. 1000x1500 is the standard size used there.
W, H = 1000, 1500
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


def centered(d, y, text, font, fill, w=W):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    d.text(((w - tw) // 2, y), text, font=font, fill=fill)


def draw_doc_mockup(d, cx, oy, accent, scale=1.0):
    """Same PDF-page + spreadsheet-grid mockup used on the Gumroad covers,
    centered horizontally, so the pin reads as the same product family at a
    glance rather than a one-off design."""
    pdf_w, pdf_h = int(220 * scale), int(280 * scale)
    ox = cx - pdf_w // 2 - int(40 * scale)
    page_bg = (245, 245, 244)
    line_col = (205, 205, 208)
    d.rounded_rectangle([ox, oy, ox + pdf_w, oy + pdf_h], radius=14, fill=page_bg)
    d.rounded_rectangle(
        [ox + 20, oy + 24, ox + pdf_w - 20, oy + 42], radius=6, fill=accent
    )
    for i in range(5):
        ly = oy + 68 + i * int(24 * scale)
        lw = pdf_w - 40 if i % 3 != 2 else pdf_w - 90
        d.rectangle([ox + 20, ly, ox + 20 + lw, ly + 7], fill=line_col)

    xl_w, xl_h = int(220 * scale), int(170 * scale)
    xox, xoy = ox + int(70 * scale), oy + pdf_h - int(60 * scale)
    d.rounded_rectangle(
        [xox + 8, xoy + 8, xox + xl_w + 8, xoy + xl_h + 8], radius=14, fill=(18, 18, 20)
    )
    d.rounded_rectangle([xox, xoy, xox + xl_w, xoy + xl_h], radius=14, fill=(255, 255, 255))
    rows, cols = 4, 5
    gx0, gy0 = xox + 14, xoy + 14
    gw, gh = xl_w - 28, xl_h - 28
    cw, ch = gw / cols, gh / rows
    grid_col = (222, 222, 224)
    for r in range(rows + 1):
        yy = gy0 + r * ch
        d.line([gx0, yy, gx0 + gw, yy], fill=grid_col, width=2)
    for c in range(cols + 1):
        xx = gx0 + c * cw
        d.line([xx, gy0, xx, gy0 + gh], fill=grid_col, width=2)
    d.rectangle([gx0 + 2 * cw, gy0 + ch, gx0 + 3 * cw, gy0 + 2 * ch], fill=accent)


def price_badge(d, y, text, font):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    pad_x, pad_y = 34, 18
    bw = tw + pad_x * 2
    x = (W - bw) // 2
    d.rounded_rectangle([x, y, x + bw, y + (bbox[3] - bbox[1]) + pad_y * 2], radius=999, fill=ACCENT)
    d.text((x + pad_x, y + pad_y - bbox[1]), text, font=font, fill=(18, 18, 20))


def build_pin(filename, eyebrow, headline_lines, subhead_lines, price_text):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 10], fill=ACCENT)

    eyebrow_font = load_font("arialbd.ttf", 30)
    title_font = load_font("arialbd.ttf", 74)
    sub_font = load_font("arial.ttf", 34)
    price_font = load_font("arialbd.ttf", 38)
    brand_font = load_font("arial.ttf", 28)

    y = 110
    centered(d, y, eyebrow, eyebrow_font, ACCENT)
    y += 70

    for line in headline_lines:
        centered(d, y, line, title_font, WHITE)
        y += 92

    y += 20
    for line in subhead_lines:
        centered(d, y, line, sub_font, MUTED)
        y += 46

    draw_doc_mockup(d, W // 2, y + 40, ACCENT, scale=1.15)

    price_badge(d, 1060, price_text, price_font)

    centered(d, H - 90, "Ledger & Loop Digital", brand_font, MUTED)

    out = os.path.join(DIST, filename)
    img.save(out)
    print(f"Wrote {out}")


def build():
    os.makedirs(DIST, exist_ok=True)

    build_pin(
        "pin-freelancer-bundle.png",
        "FOR FREELANCERS",
        ["Freelancer", "Money Bundle"],
        ["Know what you owe the IRS —", "and get paid on time."],
        "$29 · tax + invoice toolkit",
    )

    build_pin(
        "pin-tax-tracker.png",
        "2026 QUARTERLY TAXES",
        ["Self-Employment", "Tax Tracker"],
        ["Real deadlines, real Schedule C", "categories, your exact tax owed."],
        "$19 · guide + spreadsheet",
    )

    build_pin(
        "pin-ai-prompt-playbook.png",
        "FOR SMALL BUSINESS",
        ["25 AI Prompts", "That Actually Help"],
        ["Marketing, support, finance,", "hiring & sales — not generic filler."],
        "$19 · guide + ROI tracker",
    )


if __name__ == "__main__":
    build()

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


def draw_doc_mockup(d, ox, oy, accent):
    """Two overlapping PDF-page mockups (Vol. 1 + Vol. 2) so the cover reads as a 2-guide bundle."""
    pdf_w, pdf_h = 220, 290
    page_bg = (245, 245, 244)
    line_col = (205, 205, 208)

    # back page (Vol. 1), offset behind
    bx, by = ox - 40, oy + 30
    d.rounded_rectangle([bx, by, bx + pdf_w, by + pdf_h], radius=14, fill=(210, 210, 212))

    # front page (Vol. 2), on top
    d.rounded_rectangle([ox, oy, ox + pdf_w, oy + pdf_h], radius=14, fill=page_bg)
    d.rounded_rectangle([ox + 20, oy + 24, ox + pdf_w - 20, oy + 42], radius=6, fill=accent)
    for i in range(6):
        ly = oy + 70 + i * 26
        lw = pdf_w - 40 if i % 3 != 2 else pdf_w - 90
        d.rectangle([ox + 20, ly, ox + 20 + lw, ly + 7], fill=line_col)


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, 14, H], fill=ACCENT)

    draw_doc_mockup(d, 1260, 260, ACCENT)

    title_font = load_font("arialbd.ttf", 60)
    sub_font = load_font("arial.ttf", 34)
    tag_font = load_font("arialbd.ttf", 24)
    eyebrow_font = load_font("arialbd.ttf", 28)
    price_font = load_font("arialbd.ttf", 40)

    margin = 110
    d.text((margin, 110), "50 PROMPTS — VOL. 1 + VOL. 2, TOGETHER", font=eyebrow_font, fill=ACCENT)
    d.text((margin, 178), "The AI Prompt", font=title_font, fill=WHITE)
    d.text((margin, 250), "Playbook Bundle", font=title_font, fill=ACCENT)

    d.text((margin, 380), "One-off tasks and repeatable systems —", font=sub_font, fill=MUTED)
    d.text((margin, 422), "both playbooks, both trackers, one price.", font=sub_font, fill=MUTED)

    chips = ["2 PDF GUIDES", "2 XLSX TRACKERS", "50 PROMPTS TOTAL"]
    x = margin
    y = 520
    for chip in chips:
        bbox = d.textbbox((0, 0), chip, font=tag_font)
        tw = bbox[2] - bbox[0]
        pad = 20
        d.rounded_rectangle([x, y, x + tw + pad * 2, y + 48], radius=24, outline=ACCENT, width=2)
        d.text((x + pad, y + 9), chip, font=tag_font, fill=ACCENT)
        x += tw + pad * 2 + 14

    d.text((margin, 630), "$29 bundle  ·  $38 if bought separately", font=price_font, fill=WHITE)

    d.text((margin, H - 90), "Ledger & Loop Digital", font=sub_font, fill=MUTED)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

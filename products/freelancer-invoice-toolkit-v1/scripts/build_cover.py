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


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, 14, H], fill=ACCENT)

    title_font = load_font("arialbd.ttf", 70)
    sub_font = load_font("arial.ttf", 36)
    tag_font = load_font("arialbd.ttf", 28)
    eyebrow_font = load_font("arialbd.ttf", 28)

    margin = 110
    d.text((margin, 130), "FOR FREELANCERS", font=eyebrow_font, fill=ACCENT)
    d.text((margin, 200), "The Freelancer", font=title_font, fill=WHITE)
    d.text((margin, 285), "Invoice &", font=title_font, fill=WHITE)
    d.text((margin, 370), "Late-Payment Toolkit", font=title_font, fill=ACCENT)

    d.text((margin, 510), "Ready-to-send reminder scripts, payment terms that", font=sub_font, fill=MUTED)
    d.text((margin, 555), "cut risk, and a clear plan for clients who go quiet.", font=sub_font, fill=MUTED)

    chips = ["PDF GUIDE", "XLSX TRACKER", "EMAIL SCRIPTS", "INVOICE TEMPLATE"]
    x = margin
    y = 660
    for chip in chips:
        bbox = d.textbbox((0, 0), chip, font=tag_font)
        tw = bbox[2] - bbox[0]
        pad = 22
        d.rounded_rectangle([x, y, x + tw + pad * 2, y + 54], radius=27, outline=ACCENT, width=2)
        d.text((x + pad, y + 11), chip, font=tag_font, fill=ACCENT)
        x += tw + pad * 2 + 16

    d.text((margin, H - 90), "Ledger & Loop Digital", font=sub_font, fill=MUTED)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

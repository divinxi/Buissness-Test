import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "cover.png")

W, H = 1600, 1000  # Gumroad recommends ~1280x720+ landscape cover
BG = (28, 28, 30)
ACCENT = (122, 200, 174)
MUTED = (170, 170, 176)
WHITE = (245, 245, 244)

def load_font(name, size):
    candidates = [
        f"C:/Windows/Fonts/{name}",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # subtle accent bar
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    title_font = load_font("arialbd.ttf", 92)
    sub_font = load_font("arial.ttf", 40)
    tag_font = load_font("arialbd.ttf", 30)

    margin = 110
    d.text((margin, 220), "The Small Business", font=title_font, fill=WHITE)
    d.text((margin, 330), "AI Prompt Playbook", font=title_font, fill=ACCENT)

    d.text((margin, 470), "25 ready-to-use prompts for marketing, support,", font=sub_font, fill=MUTED)
    d.text((margin, 520), "finance, hiring & sales — plus an ROI tracker.", font=sub_font, fill=MUTED)

    # bottom tag chips
    chips = ["MARKETING", "SUPPORT", "FINANCE", "HIRING", "SALES"]
    x = margin
    y = 640
    for chip in chips:
        bbox = d.textbbox((0, 0), chip, font=tag_font)
        tw = bbox[2] - bbox[0]
        pad = 24
        d.rounded_rectangle([x, y, x + tw + pad * 2, y + 56], radius=28, outline=ACCENT, width=2)
        d.text((x + pad, y + 12), chip, font=tag_font, fill=ACCENT)
        x += tw + pad * 2 + 18

    d.text((margin, H - 90), "Ledger & Loop Digital", font=sub_font, fill=MUTED)

    img.save(OUT)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()

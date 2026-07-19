import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import CATEGORIES

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "Small-Business-AI-Prompt-Playbook.pdf")

INK = HexColor("#1c1c1e")
MUTED = HexColor("#5a5a60")
ACCENT = HexColor("#2f5d50")
BOX_BG = HexColor("#f2f1ec")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=28, leading=34,
                           textColor=INK, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle("CoverSub", fontName="Helvetica", fontSize=13, leading=18,
                           textColor=MUTED, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle("CatHeader", fontName="Helvetica-Bold", fontSize=19, leading=23,
                           textColor=ACCENT, spaceBefore=6, spaceAfter=14))
styles.add(ParagraphStyle("PromptTitle", fontName="Helvetica-Bold", fontSize=13, leading=16,
                           textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle("PromptBody", fontName="Helvetica", fontSize=10, leading=14,
                           textColor=INK))
styles.add(ParagraphStyle("MetaLabel", fontName="Helvetica-Bold", fontSize=9, leading=12,
                           textColor=ACCENT))
styles.add(ParagraphStyle("MetaBody", fontName="Helvetica-Oblique", fontSize=9.5, leading=13,
                           textColor=MUTED))
styles.add(ParagraphStyle("TOCEntry", fontName="Helvetica", fontSize=11.5, leading=20,
                           textColor=INK))
styles.add(ParagraphStyle("FootNote", fontName="Helvetica", fontSize=8.5, leading=12,
                           textColor=MUTED))

def prompt_block(idx, item):
    title = Paragraph(f"{idx}. {item['title']}", styles["PromptTitle"])
    box_table = Table(
        [[Paragraph(item["prompt"], styles["PromptBody"])]],
        colWidths=[6.3 * inch],
    )
    box_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#d8d6cc")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    when = Paragraph(f'<font color="#2f5d50"><b>When to use it:</b></font> {item["when"]}', styles["MetaBody"])
    tip = Paragraph(f'<font color="#2f5d50"><b>Pro tip:</b></font> {item["tip"]}', styles["MetaBody"])
    return KeepTogether([title, Spacer(1, 4), box_table, Spacer(1, 6), when, Spacer(1, 3), tip, Spacer(1, 18)])

def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=1.0 * inch, rightMargin=1.0 * inch,
        title="Small Business AI Prompt Playbook",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover page
    story.append(Spacer(1, 1.8 * inch))
    story.append(Paragraph("The Small Business<br/>AI Prompt Playbook", styles["CoverTitle"]))
    story.append(Paragraph("25 ready-to-use prompts for marketing, support, finance, hiring &amp; sales", styles["CoverSub"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Copy. Paste. Fill in the brackets. Done.", styles["CoverSub"]))
    story.append(Spacer(1, 2.2 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital", styles["FootNote"]))
    story.append(PageBreak())

    # How to use this
    story.append(Paragraph("How to use this playbook", styles["CatHeader"]))
    story.append(Paragraph(
        "Every prompt below works with any modern AI chat assistant (Claude, ChatGPT, Gemini, "
        "or similar). Replace anything in [BRACKETS] with your own details, then paste the whole "
        "prompt in. Each one includes a note on when it's actually worth using and a tip on how "
        "to adapt it to your business specifically — templates only work if you customize them.",
        styles["PromptBody"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "A companion spreadsheet (AI-Ops-Tracker.xlsx) is included in your download — use it to "
        "log which prompts you use, how much time each one saves, and see a running ROI estimate.",
        styles["PromptBody"]))
    story.append(Spacer(1, 24))

    # TOC
    story.append(Paragraph("What's inside", styles["CatHeader"]))
    for cat in CATEGORIES:
        story.append(Paragraph(f"&bull; {cat['name']} — {len(cat['prompts'])} prompts", styles["TOCEntry"]))
    story.append(PageBreak())

    for cat in CATEGORIES:
        story.append(Paragraph(cat["name"], styles["CatHeader"]))
        for i, item in enumerate(cat["prompts"], start=1):
            story.append(prompt_block(i, item))
        story.append(PageBreak())

    # Closing page
    story.append(Paragraph("Want this tailored to your business?", styles["CatHeader"]))
    story.append(Paragraph(
        "These prompts are deliberately generic templates so they work across industries. If you "
        "want a custom set built specifically around your business, your voice, and your actual "
        "recurring tasks, reach out — contact details are on the product page you downloaded this from.",
        styles["PromptBody"]))

    doc.build(story)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()

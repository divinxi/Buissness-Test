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

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "AI-Prompt-Playbook-Vol2-Systems-Automation.pdf")

INK = HexColor("#1c1c1e")
MUTED = HexColor("#5a5a60")
ACCENT = HexColor("#2f5d50")
BOX_BG = HexColor("#f2f1ec")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=27, leading=33,
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
        title="AI Prompt Playbook Vol. 2: Systems & Automation",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover page
    story.append(Spacer(1, 1.7 * inch))
    story.append(Paragraph("AI Prompt Playbook<br/>Vol. 2: Systems &amp; Automation", styles["CoverTitle"]))
    story.append(Paragraph("25 prompts for turning AI into repeatable systems — not just one-off tasks", styles["CoverSub"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Set it up once. Reuse it every week.", styles["CoverSub"]))
    story.append(Spacer(1, 2.1 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital", styles["FootNote"]))
    story.append(PageBreak())

    # How to use this + relationship to Vol 1
    story.append(Paragraph("How this is different from Vol. 1", styles["CatHeader"]))
    story.append(Paragraph(
        "Vol. 1 (The Small Business AI Prompt Playbook) covers one-off tasks — draft this email, "
        "write that job post. Vol. 2 is about the next level: prompts that become <i>systems</i> you "
        "set up once and reuse on a schedule — a weekly ops review, a customer win-back sequence, a "
        "recurring competitive scan. You don't need Vol. 1 to use this book; the two are companions, "
        "not a strict sequence.",
        styles["PromptBody"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Every prompt works with any modern AI chat assistant (Claude, ChatGPT, Gemini, or similar). "
        "Replace anything in [BRACKETS] with your own details. A companion spreadsheet "
        "(Automation-ROI-Tracker.xlsx) is included — use it to log which of these you've turned into "
        "a recurring habit, how often they run, and the compounding time saved.",
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
        "recurring systems, reach out — contact details are on the product page you downloaded this "
        "from.",
        styles["PromptBody"]))
    story.append(PageBreak())

    # Cross-sell
    story.append(Paragraph("More From Ledger &amp; Loop Digital", styles["CatHeader"]))
    story.append(Paragraph(
        "Look for these on the same store page you downloaded this from.",
        styles["PromptBody"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("The Small Business AI Prompt Playbook (Vol. 1) — $19", styles["MetaLabel"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "25 ready-to-use, one-off prompts for marketing, support, finance, hiring &amp; sales, plus "
        "an ROI tracker.",
        styles["PromptBody"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("The Freelancer Quarterly Tax &amp; Expense Tracker (2026 Edition) — $19", styles["MetaLabel"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "2026 quarterly deadlines, a self-employment tax calculator with a worked example, all 17 "
        "Schedule C expense categories, and a live tax-estimator spreadsheet.",
        styles["PromptBody"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("The Freelancer Invoice &amp; Late-Payment Toolkit — $19", styles["MetaLabel"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "A ready-to-copy 4-stage reminder email sequence, how to choose payment terms and set an "
        "enforceable late fee, and a spreadsheet that auto-flags overdue invoices.",
        styles["PromptBody"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("The Freelancer Money Bundle (Tax Tracker + Invoice Toolkit) — $29", styles["MetaLabel"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Both freelancer toolkits above together, for less than buying them separately.",
        styles["PromptBody"]))

    doc.build(story)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import PROMPTS, CHECKLIST, CTA_TEXT

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "Small-Business-AI-Prompt-Quick-Start.pdf")

INK = HexColor("#1c1c1e")
MUTED = HexColor("#5a5a60")
ACCENT = HexColor("#2f5d50")
BOX_BG = HexColor("#f2f1ec")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=25, leading=31,
                           textColor=INK, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle("CoverSub", fontName="Helvetica", fontSize=12.5, leading=17,
                           textColor=MUTED, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle("CatHeader", fontName="Helvetica-Bold", fontSize=17, leading=21,
                           textColor=ACCENT, spaceBefore=6, spaceAfter=10))
styles.add(ParagraphStyle("PromptTitle", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                           textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle("PromptCat", fontName="Helvetica-Oblique", fontSize=9, leading=12,
                           textColor=ACCENT, spaceAfter=4))
styles.add(ParagraphStyle("PromptBody", fontName="Helvetica", fontSize=9.8, leading=13.5,
                           textColor=INK))
styles.add(ParagraphStyle("MetaBody", fontName="Helvetica-Oblique", fontSize=9.3, leading=12.5,
                           textColor=MUTED))
styles.add(ParagraphStyle("CheckItem", fontName="Helvetica", fontSize=10.5, leading=17,
                           textColor=INK, leftIndent=4))
styles.add(ParagraphStyle("FootNote", fontName="Helvetica", fontSize=8.5, leading=12,
                           textColor=MUTED))
styles.add(ParagraphStyle("CTABody", fontName="Helvetica", fontSize=10.3, leading=15,
                           textColor=INK))


def prompt_block(idx, item):
    header = Paragraph(f"{idx}. {item['title']}", styles["PromptTitle"])
    cat = Paragraph(item["category"].upper(), styles["PromptCat"])
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
    tip = Paragraph(f'<font color="#2f5d50"><b>Adapt it:</b></font> {item["tip"]}', styles["MetaBody"])
    return KeepTogether([cat, header, Spacer(1, 4), box_table, Spacer(1, 6), when, Spacer(1, 3), tip, Spacer(1, 16)])


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=1.0 * inch, rightMargin=1.0 * inch,
        title="The Small Business AI Prompt Quick-Start",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover
    story.append(Spacer(1, 1.4 * inch))
    story.append(Paragraph("The Small Business<br/>AI Prompt Quick-Start", styles["CoverTitle"]))
    story.append(Paragraph(
        "5 ready-to-use prompts — one each for Marketing, Support, Finance, Hiring, "
        "and Sales — plus a 5-question self-audit.",
        styles["CoverSub"]))
    story.append(Spacer(1, 1.9 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital &mdash; free excerpt, share freely", styles["FootNote"]))
    story.append(PageBreak())

    # How to use
    story.append(Paragraph("How to use this", styles["CatHeader"]))
    story.append(Paragraph(
        "Each prompt below works with any modern AI chat assistant (Claude, ChatGPT, Gemini, or "
        "similar). Replace anything in [BRACKETS] with your own details, then paste the whole "
        "prompt in. These are one real prompt from each of the 5 categories in the full playbook "
        "&mdash; not a cut-down teaser, each one is complete and usable on its own.",
        styles["PromptBody"]))
    story.append(Spacer(1, 20))

    for i, item in enumerate(PROMPTS, start=1):
        story.append(prompt_block(i, item))
    story.append(PageBreak())

    # Self-audit
    story.append(Paragraph("Your 60-Second AI-Readiness Self-Audit", styles["CatHeader"]))
    for item in CHECKLIST:
        story.append(Paragraph(f"[&nbsp;&nbsp;]&nbsp;&nbsp;{item}", styles["CheckItem"]))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 16))

    # CTA
    box = Paragraph(CTA_TEXT, styles["CTABody"])
    bt = Table([[box]], colWidths=[6.3 * inch])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#d8d6cc")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(bt)
    story.append(Spacer(1, 14))
    story.append(Paragraph(
        "The Small Business AI Prompt Playbook &mdash; $19 &bull; AI Prompt Playbook Vol. 2: "
        "Systems &amp; Automation &mdash; $19 &bull; both together as The AI Prompt Playbook Bundle "
        "&mdash; $29.",
        styles["PromptBody"]))

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

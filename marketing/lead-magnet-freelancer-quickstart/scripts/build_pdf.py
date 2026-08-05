import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import TAX_YEAR, DEADLINES, SAVE_RULE, INVOICE_TIPS, CHECKLIST, CTA_TEXT

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "Freelancer-Money-Admin-Quick-Start.pdf")

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
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=10.2, leading=14.5,
                           textColor=INK))
styles.add(ParagraphStyle("BulletItem", fontName="Helvetica", fontSize=10, leading=15,
                           textColor=INK, leftIndent=12))
styles.add(ParagraphStyle("CheckItem", fontName="Helvetica", fontSize=10.5, leading=17,
                           textColor=INK, leftIndent=4))
styles.add(ParagraphStyle("FootNote", fontName="Helvetica", fontSize=8.5, leading=12,
                           textColor=MUTED))
styles.add(ParagraphStyle("CTABody", fontName="Helvetica", fontSize=10.3, leading=15,
                           textColor=INK))


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=1.0 * inch, rightMargin=1.0 * inch,
        title="The Freelancer Money Admin Quick-Start",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph("The Freelancer<br/>Money Admin Quick-Start", styles["CoverTitle"]))
    story.append(Paragraph(
        f"The {TAX_YEAR} tax deadlines you can't miss, the one invoice habit that "
        "gets you paid faster, and a 60-second self-audit.",
        styles["CoverSub"]))
    story.append(Spacer(1, 2.2 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital &mdash; free excerpt, share freely", styles["FootNote"]))
    story.append(PageBreak())

    # Deadlines
    story.append(Paragraph(f"{TAX_YEAR} Quarterly Tax Deadlines", styles["CatHeader"]))
    story.append(Paragraph(
        "If you expect to owe $1,000+ in federal tax for the year after withholding/credits, "
        "the IRS expects estimated tax paid quarterly, not once at filing time. Miss one and "
        "you can owe a penalty even if you pay in full by April.",
        styles["Body"]))
    story.append(Spacer(1, 10))
    rows = [["Quarter", "Due Date", "Covers"]]
    for d in DEADLINES:
        rows.append([d["quarter"], d["due"], d["covers"]])
    t = Table(rows, colWidths=[1.0 * inch, 2.0 * inch, 3.3 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), BOX_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d8d6cc")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"How much to set aside: {SAVE_RULE}", styles["Body"]))
    story.append(Spacer(1, 20))

    # Invoice tip
    story.append(Paragraph("The Invoice Habit That Gets You Paid Faster", styles["CatHeader"]))
    for tip in INVOICE_TIPS:
        story.append(Paragraph(f"&bull; {tip}", styles["BulletItem"]))
        story.append(Spacer(1, 4))
    story.append(PageBreak())

    # Checklist
    story.append(Paragraph("Your 60-Second Money Admin Self-Audit", styles["CatHeader"]))
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
        "The Freelancer Quarterly Tax &amp; Expense Tracker (2026 Edition) &mdash; $19 &bull; "
        "The Freelancer Invoice &amp; Late-Payment Toolkit &mdash; $19 &bull; both together as "
        "The Freelancer Money Bundle &mdash; $29.",
        styles["Body"]))

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

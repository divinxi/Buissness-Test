import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import (
    INVOICE_ELEMENTS, PAYMENT_TERMS, DEPOSIT_STRATEGY, REMINDER_SEQUENCE,
    LATE_FEES, ESCALATION_STEPS, SCOPE_CREEP,
)

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "Freelancer-Invoice-Late-Payment-Toolkit-Guide.pdf")

INK = HexColor("#1c1c1e")
MUTED = HexColor("#5a5a60")
ACCENT = HexColor("#2f5d50")
WARN = HexColor("#9a5b12")
BOX_BG = HexColor("#f2f1ec")
WARN_BG = HexColor("#f7ecdb")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=27, leading=33,
                           textColor=INK, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle("CoverSub", fontName="Helvetica", fontSize=13, leading=18,
                           textColor=MUTED, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle("CatHeader", fontName="Helvetica-Bold", fontSize=18, leading=22,
                           textColor=ACCENT, spaceBefore=6, spaceAfter=12))
styles.add(ParagraphStyle("SubHeader", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                           textColor=INK, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=10.2, leading=14.5,
                           textColor=INK))
styles.add(ParagraphStyle("CatName", fontName="Helvetica-Bold", fontSize=12, leading=15,
                           textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle("CatBody", fontName="Helvetica", fontSize=9.7, leading=13.5,
                           textColor=INK))
styles.add(ParagraphStyle("CatNote", fontName="Helvetica-Oblique", fontSize=9.3, leading=13,
                           textColor=MUTED))
styles.add(ParagraphStyle("FootNote", fontName="Helvetica", fontSize=8.5, leading=12,
                           textColor=MUTED))
styles.add(ParagraphStyle("WarnBody", fontName="Helvetica", fontSize=9.7, leading=14,
                           textColor=INK))
styles.add(ParagraphStyle("BulletItem", fontName="Helvetica", fontSize=10, leading=15,
                           textColor=INK, leftIndent=12))
styles.add(ParagraphStyle("EmailLabel", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
                           textColor=ACCENT, spaceAfter=2))
styles.add(ParagraphStyle("EmailBody", fontName="Courier", fontSize=8.7, leading=13,
                           textColor=INK, leftIndent=8))


def warn_box(text, label="Watch out"):
    p = Paragraph(f'<font color="#9a5b12"><b>{label}:</b></font> {text}', styles["WarnBody"])
    t = Table([[p]], colWidths=[6.3 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARN_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#e0c48f")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def element_block(item):
    header = Paragraph(item["name"], styles["CatName"])
    why = Paragraph(item["why"], styles["CatBody"])
    return KeepTogether([header, Spacer(1, 2), why, Spacer(1, 10)])


def email_block(item):
    label = Paragraph(f'{item["stage"]} <font color="#5a5a60" size=8.5>— {item["tone"]}</font>', styles["EmailLabel"])
    subj = Paragraph(f'<b>Subject:</b> {item["subject"]}', styles["CatBody"])
    body_lines = item["body"].replace("\n", "<br/>")
    body = Paragraph(body_lines, styles["EmailBody"])
    box = Table([[body]], colWidths=[6.3 * inch])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#d8d6cc")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([label, Spacer(1, 2), subj, Spacer(1, 5), box, Spacer(1, 14)])


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=1.0 * inch, rightMargin=1.0 * inch,
        title="Freelancer Invoice & Late-Payment Toolkit — Guide",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover
    story.append(Spacer(1, 1.6 * inch))
    story.append(Paragraph("The Freelancer Invoice &<br/>Late-Payment Toolkit", styles["CoverTitle"]))
    story.append(Paragraph("Get paid faster, chase less, and know exactly what to do<br/>when a client goes quiet.", styles["CoverSub"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Ready-to-send reminder scripts, payment terms that reduce risk,<br/>and a clear escalation path for non-payment.", styles["CoverSub"]))
    story.append(Spacer(1, 1.8 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital", styles["FootNote"]))
    story.append(PageBreak())

    # How to use
    story.append(Paragraph("How to use this guide", styles["CatHeader"]))
    story.append(Paragraph(
        "This guide is the reference companion to Invoice-Payment-Tracker.xlsx. Use the guide for "
        "the reminder scripts and the decision-making (payment terms, deposits, escalation); use "
        "the spreadsheet to track real invoices and see at a glance what's overdue.",
        styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "This is practical freelance business guidance built from common, field-tested practice — "
        "it is not legal advice. Collections law, interest-rate caps, and small claims limits vary "
        "by state and country; where that matters, this guide says so explicitly instead of "
        "guessing at your jurisdiction.",
        styles["Body"]))
    story.append(Spacer(1, 20))

    # Invoice elements
    story.append(Paragraph("8 Things Every Invoice Needs", styles["CatHeader"]))
    story.append(Paragraph(
        "Invoices that are missing basic information get disputed, delayed, or simply forgotten. "
        "Every one of these is a real reason an invoice sat unpaid longer than it should have.",
        styles["Body"]))
    story.append(Spacer(1, 12))
    for item in INVOICE_ELEMENTS:
        story.append(element_block(item))
    story.append(PageBreak())

    # Payment terms
    story.append(Paragraph("Choosing Payment Terms", styles["CatHeader"]))
    story.append(Paragraph(
        "The terms you set upfront do more to prevent late payment than any reminder email ever "
        "will. Match the term to the client relationship, not just habit.",
        styles["Body"]))
    story.append(Spacer(1, 10))
    rows = [["Term", "Meaning", "Best For", "Risk"]]
    for t in PAYMENT_TERMS:
        rows.append([t["term"], t["meaning"], t["best_for"], t["risk"]])
    t = Table(rows, colWidths=[1.15 * inch, 2.05 * inch, 2.15 * inch, 0.95 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.3),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), BOX_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d8d6cc")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 16))

    story.append(Paragraph(DEPOSIT_STRATEGY["headline"], styles["SubHeader"]))
    story.append(Paragraph(DEPOSIT_STRATEGY["note"], styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(warn_box(DEPOSIT_STRATEGY["new_client_rule"], label="New clients"))
    story.append(PageBreak())

    # Reminder sequence
    story.append(Paragraph("The 4-Stage Reminder Sequence", styles["CatHeader"]))
    story.append(Paragraph(
        "Copy, paste, and fill in the brackets. Sending these on a schedule — not waiting until "
        "you're frustrated — keeps the tone professional and keeps the paper trail clean if you "
        "ever need to escalate.",
        styles["Body"]))
    story.append(Spacer(1, 12))
    for item in REMINDER_SEQUENCE:
        story.append(email_block(item))
    story.append(PageBreak())

    # Late fees
    story.append(Paragraph("Late Fees, Done Correctly", styles["CatHeader"]))
    story.append(Paragraph(LATE_FEES["headline"], styles["SubHeader"]))
    story.append(Paragraph(LATE_FEES["common_range"], styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(LATE_FEES["how_to_set_up"], styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(warn_box(LATE_FEES["caveat"]))
    story.append(Spacer(1, 20))

    # Scope creep
    story.append(Paragraph(SCOPE_CREEP["headline"], styles["CatHeader"]))
    story.append(Paragraph(SCOPE_CREEP["note"], styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(SCOPE_CREEP["change_order_rule"], styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f'<font color="#2f5d50"><b>Script:</b></font> {SCOPE_CREEP["script"]}', styles["CatNote"]))
    story.append(PageBreak())

    # Escalation
    story.append(Paragraph("When a Client Won't Pay", styles["CatHeader"]))
    story.append(Paragraph(
        "If the reminder sequence runs out and the balance is still unpaid, work through these "
        "steps in order. Most non-payment situations resolve at step 1 or 2 — few freelancers ever "
        "need step 4.",
        styles["Body"]))
    story.append(Spacer(1, 12))
    for item in ESCALATION_STEPS:
        story.append(Paragraph(item["step"], styles["SubHeader"]))
        story.append(Paragraph(item["detail"], styles["Body"]))
        story.append(Spacer(1, 8))
    story.append(Spacer(1, 12))

    # Closing
    story.append(Paragraph("Using the Companion Spreadsheet", styles["CatHeader"]))
    story.append(Paragraph(
        "Invoice-Payment-Tracker.xlsx has four tabs: Start Here, Invoice Log, Reminder Dashboard, "
        "and Invoice Template. Log every invoice the day you send it. The Reminder Dashboard tab "
        "flags exactly which invoices are overdue and which reminder stage they're due for — no "
        "mental math, no missed follow-ups.",
        styles["Body"]))

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

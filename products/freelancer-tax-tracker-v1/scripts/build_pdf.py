import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import (
    TAX_YEAR, QUARTERLY_DEADLINES, SE_TAX_FACTS, SCHEDULE_C_CATEGORIES,
    HOME_OFFICE, SAVINGS_RULE_OF_THUMB, AUDIT_RISK_NOTES,
)

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)

OUT = os.path.join(os.path.dirname(__file__), "..", "dist", "Freelancer-Tax-Expense-Tracker-Guide.pdf")

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
styles.add(ParagraphStyle("CatLine", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
                           textColor=ACCENT))
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


def category_block(item):
    header = Paragraph(f'{item["name"]} <font color="#5a5a60" size=8.5>({item["line"]})</font>', styles["CatName"])
    what = Paragraph(f'<b>What counts:</b> {item["what_counts"]}', styles["CatBody"])
    note = Paragraph(f'<b>Freelancer note:</b> {item["freelancer_note"]}', styles["CatNote"])
    return KeepTogether([header, Spacer(1, 2), what, Spacer(1, 3), note, Spacer(1, 12)])


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=1.0 * inch, rightMargin=1.0 * inch,
        title="Freelancer Quarterly Tax & Expense Tracker — Guide",
        author="Ledger & Loop Digital",
    )
    story = []

    # Cover
    story.append(Spacer(1, 1.6 * inch))
    story.append(Paragraph("The Freelancer Quarterly<br/>Tax &amp; Expense Tracker", styles["CoverTitle"]))
    story.append(Paragraph(f"{TAX_YEAR} Edition — U.S. federal deadlines, real Schedule C categories,<br/>and a self-employment tax calculator that shows its math.", styles["CoverSub"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Know what you owe before the IRS tells you.", styles["CoverSub"]))
    story.append(Spacer(1, 2.0 * inch))
    story.append(Paragraph("Ledger &amp; Loop Digital", styles["FootNote"]))
    story.append(PageBreak())

    # How to use
    story.append(Paragraph("How to use this guide", styles["CatHeader"]))
    story.append(Paragraph(
        "This guide is the reference companion to Freelancer-Tax-Tracker.xlsx. Use the guide to "
        "understand the rules; use the spreadsheet to log real numbers and get your quarterly "
        "payment estimate automatically.",
        styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "This is educational reference material built from public IRS and SSA guidance for tax "
        "year 2026. It is not personalized tax advice — for anything with real financial "
        "consequences (large deductions, multi-state income, entity structure decisions), confirm "
        "with a licensed CPA or enrolled agent. What this guide gets you is the ability to walk "
        "into that conversation already organized, instead of paying an accountant to do your "
        "basic bookkeeping for you.",
        styles["Body"]))
    story.append(Spacer(1, 20))

    # Deadlines
    story.append(Paragraph(f"{TAX_YEAR} Quarterly Estimated Tax Deadlines", styles["CatHeader"]))
    story.append(Paragraph(
        "If you expect to owe $1,000+ in federal tax for the year after withholding/credits, the "
        "IRS expects you to pay estimated tax quarterly — not just once at filing time. Miss a "
        "deadline and you can owe an underpayment penalty even if you pay in full by April.",
        styles["Body"]))
    story.append(Spacer(1, 10))
    rows = [["Period", "Covers Income Earned", "Payment Due"]]
    for d in QUARTERLY_DEADLINES:
        rows.append([d["quarter"], d["covers"], d["due"]])
    t = Table(rows, colWidths=[1.5 * inch, 2.6 * inch, 2.2 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), BOX_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d8d6cc")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    story.append(warn_box(
        "If a due date falls on a weekend or federal holiday, it pushes to the next business day. "
        "These four dates are already confirmed for 2026 — no need to double check unless you're "
        "reading this in a later year.",
    ))
    story.append(PageBreak())

    # SE tax explained
    story.append(Paragraph("Self-Employment Tax, Explained With Real Numbers", styles["CatHeader"]))
    story.append(Paragraph(
        "As a freelancer, no employer withholds Social Security or Medicare tax for you — you pay "
        "both the employee AND employer share yourself, called self-employment (SE) tax. This is "
        "separate from, and in addition to, regular income tax.",
        styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("The math (Schedule SE, 2026 figures):", styles["SubHeader"]))
    steps = [
        "Start with net profit from your business (income minus deductible expenses).",
        f"Multiply by 92.35% — this is your \"net earnings from self-employment.\" (The 7.65% haircut roughly mirrors the employer-side deduction a W-2 employee's company absorbs.)",
        f"Social Security portion: 12.4% of net earnings, but only up to the {TAX_YEAR} wage base of ${SE_TAX_FACTS['wage_base_2026']:,} — income above that isn't subject to the Social Security portion (though it's still subject to Medicare).",
        "Medicare portion: 2.9% of ALL net earnings, no cap.",
        "Add an extra 0.9% Additional Medicare Tax on net SE earnings above $200,000 (single) or $250,000 (married filing jointly) — most solo freelancers won't hit this, but it's real if you do.",
        "Total SE tax = Social Security portion + Medicare portion (+ Additional Medicare if applicable). Half of this total is deductible on your income tax return.",
    ]
    for i, s in enumerate(steps, 1):
        story.append(Paragraph(f"{i}. {s}", styles["BulletItem"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Worked example — $60,000 net profit:", styles["SubHeader"]))
    ex_rows = [
        ["Step", "Calculation", "Result"],
        ["Net earnings from SE", "$60,000 × 92.35%", "$55,410"],
        ["Social Security (12.4%)", "$55,410 × 12.4% (under the $184,500 cap)", "$6,870.84"],
        ["Medicare (2.9%)", "$55,410 × 2.9%", "$1,606.89"],
        ["Total SE tax", "$6,870.84 + $1,606.89", "$8,477.73"],
        ["Deductible half", "$8,477.73 ÷ 2", "$4,238.87"],
    ]
    et = Table(ex_rows, colWidths=[1.7 * inch, 2.9 * inch, 1.7 * inch])
    et.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), BOX_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d8d6cc")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(et)
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "The companion spreadsheet's \"Quarterly Tax Estimator\" tab runs this exact calculation "
        "automatically off your own net profit number — you don't need to redo this math by hand.",
        styles["Body"]))
    story.append(PageBreak())

    # Schedule C categories
    story.append(Paragraph("Schedule C Expense Categories — Freelancer Cheat Sheet", styles["CatHeader"]))
    story.append(Paragraph(
        "These are the actual line items from IRS Schedule C (Form 1040), with plain-English "
        "notes on what typically qualifies for a solo freelancer or independent contractor. Log "
        "expenses under these same categories in the companion spreadsheet's Expense Log tab so "
        "your totals map directly onto the form your preparer (or you) will fill out.",
        styles["Body"]))
    story.append(Spacer(1, 14))
    for cat in SCHEDULE_C_CATEGORIES:
        story.append(category_block(cat))
    story.append(PageBreak())

    # Home office
    story.append(Paragraph("The Home Office Deduction", styles["CatHeader"]))
    story.append(Paragraph(HOME_OFFICE["simplified_method"], styles["Body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(HOME_OFFICE["regular_method"], styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(warn_box(HOME_OFFICE["warning"]))
    story.append(Spacer(1, 20))

    # Savings rule of thumb
    story.append(Paragraph("How Much Should You Set Aside?", styles["CatHeader"]))
    story.append(Paragraph(SAVINGS_RULE_OF_THUMB["note"], styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        f'Rule-of-thumb range: <font color="#2f5d50"><b>{int(SAVINGS_RULE_OF_THUMB["low"]*100)}%–{int(SAVINGS_RULE_OF_THUMB["high"]*100)}%</b></font> of net profit, set into a separate savings account the moment you get paid — not at quarter-end when it may already be spent.',
        styles["Body"]))
    story.append(PageBreak())

    # Audit risk
    story.append(Paragraph("Red Flags That Draw a Second Look", styles["CatHeader"]))
    story.append(Paragraph(
        "None of these guarantee an audit, and none of them are illegal on their own — but each is "
        "a well-documented pattern that increases scrutiny. Being aware of them helps you keep "
        "honest records that hold up.",
        styles["Body"]))
    story.append(Spacer(1, 10))
    for note in AUDIT_RISK_NOTES:
        story.append(Paragraph(f"&bull; {note}", styles["BulletItem"]))
    story.append(Spacer(1, 24))

    # Closing
    story.append(Paragraph("Using the Companion Spreadsheet", styles["CatHeader"]))
    story.append(Paragraph(
        "Freelancer-Tax-Tracker.xlsx has five tabs: Start Here, Income Log, Expense Log, Quarterly "
        "Tax Estimator, and Dashboard. Log every payment and expense as it happens (weekly beats "
        "quarterly — you'll forget details otherwise). The Dashboard tab pulls everything together "
        "automatically so you always know, in real time, roughly what you'd owe if this quarter "
        "ended today.",
        styles["Body"]))

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()

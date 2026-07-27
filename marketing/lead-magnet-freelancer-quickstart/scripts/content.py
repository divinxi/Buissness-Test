# Source content for the free lead magnet: "The Freelancer Money Admin Quick-Start."
# Real figures pulled from products/freelancer-tax-tracker-v1 and
# products/freelancer-invoice-toolkit-v1 (both independently verified against
# IRS.gov/SSA.gov, July 2026) — this is a distilled excerpt, not new research.
# Purpose: a free giveaway to capture emails once the owner sets up a capture
# mechanism (see REQ-005) — addresses the "zero email list / zero external
# traffic" gap identified in products/MARKET-NOTES.md (2026-07-20).

TAX_YEAR = 2026

DEADLINES = [
    {"quarter": "Q1", "due": "April 15, 2026", "covers": "income from Jan 1 - Mar 31"},
    {"quarter": "Q2", "due": "June 15, 2026", "covers": "income from Apr 1 - May 31"},
    {"quarter": "Q3", "due": "September 15, 2026", "covers": "income from Jun 1 - Aug 31"},
    {"quarter": "Q4", "due": "January 15, 2027", "covers": "income from Sep 1 - Dec 31"},
]

SAVE_RULE = "Set aside 25-30% of net profit for taxes, the moment you get paid — not at quarter-end when it may already be spent."

INVOICE_TIPS = [
    "Put a specific due date on every invoice. \"Due on receipt\" is a due date, but a calendar date removes all ambiguity about when a client is officially late.",
    "State your payment terms (Net 15, Net 30, etc.) on the invoice itself, not just in the original contract — clients reference the invoice, not a three-month-old email thread.",
    "Take a deposit (typically 25-50%) on any project over roughly a week of work. It's the single biggest lever for reducing non-payment risk, and it filters out clients who were never going to pay anyway.",
    "Disclose your late fee before work starts (in the proposal/contract), then restate it on the invoice. A late fee sprung on someone after the fact is much harder to actually collect.",
]

CHECKLIST = [
    "Do you know your exact self-employment tax rate (not a guess)?",
    "Have you set aside money for Q3 2026 taxes (due September 15) yet?",
    "Does every invoice you send have a specific due date on it?",
    "Do you take a deposit on projects over a week of work?",
    "Do you have a ready-to-send reminder email for a late invoice, or do you write one from scratch each time?",
]

CTA_TEXT = (
    "If you answered \"no\" to two or more of these, that's normal — most freelancers "
    "handle money admin reactively because nobody teaches it. The two full toolkits "
    "this checklist is drawn from go much deeper: exact self-employment tax "
    "calculations from your own numbers, all 17 real IRS Schedule C expense "
    "categories, a 4-stage ready-to-copy reminder email sequence, and spreadsheets "
    "that do the tracking for you automatically."
)

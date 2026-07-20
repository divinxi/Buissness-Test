# Source content for the Freelancer Quarterly Tax & Expense Tracker (2026 Edition).
# All figures below are real 2026 U.S. federal numbers (verified via IRS.gov / SSA.gov,
# July 2026). Re-verify before reusing content for a future tax year.

TAX_YEAR = 2026

QUARTERLY_DEADLINES = [
    {"quarter": "Q1 2026", "covers": "Jan 1 - Mar 31, 2026", "due": "April 15, 2026"},
    {"quarter": "Q2 2026", "covers": "Apr 1 - May 31, 2026", "due": "June 15, 2026"},
    {"quarter": "Q3 2026", "covers": "Jun 1 - Aug 31, 2026", "due": "September 15, 2026"},
    {"quarter": "Q4 2026", "covers": "Sep 1 - Dec 31, 2026", "due": "January 15, 2027"},
]

SE_TAX_FACTS = {
    "rate_total": 0.153,
    "social_security_rate": 0.124,
    "medicare_rate": 0.029,
    "net_earnings_factor": 0.9235,  # SE income is taxed on 92.35% of net profit
    "wage_base_2026": 184500,       # Social Security wage base for 2026 (SSA, up from $176,100 in 2025)
    "additional_medicare_threshold_single": 200000,
    "additional_medicare_threshold_mfj": 250000,
    "additional_medicare_rate": 0.009,
}

# Schedule C (Form 1040) expense line items, in the order they appear on the form,
# with plain-English notes on what actually qualifies for a typical solo freelancer/
# independent contractor. This is educational reference material, not tax advice.
SCHEDULE_C_CATEGORIES = [
    {
        "line": "Line 8",
        "name": "Advertising",
        "what_counts": "Paid ads (Google, Meta, LinkedIn), sponsorships, printed business cards, portfolio site hosting bought specifically for promotion.",
        "freelancer_note": "Your personal portfolio/website hosting and domain renewal both count here if the site exists to get you clients.",
    },
    {
        "line": "Line 9",
        "name": "Car and Truck Expenses",
        "what_counts": "Business-related driving: client meetings, supply runs, mailing invoices. NOT your regular commute if you work from a fixed office.",
        "freelancer_note": "Track mileage with a log (date, purpose, miles) — use either the standard mileage rate or actual expenses, not both. Keep the log even if you use software; the IRS can ask for it.",
    },
    {
        "line": "Line 10",
        "name": "Commissions and Fees",
        "what_counts": "Referral fees you paid out, affiliate commissions, marketplace/platform fees that aren't already netted out (Upwork, Fiverr service fees, payment processor fees like Stripe/PayPal).",
        "freelancer_note": "Double-check your platform's payout report — some platforms already deduct fees before you receive the money, which means don't double-count them.",
    },
    {
        "line": "Line 11",
        "name": "Contract Labor",
        "what_counts": "Payments to other freelancers/subcontractors you hired to help deliver client work.",
        "freelancer_note": "If you paid any one contractor $600+ in the year, you're generally required to send them a 1099-NEC by Jan 31.",
    },
    {
        "line": "Line 13",
        "name": "Depreciation & Section 179",
        "what_counts": "Big equipment purchases (computer, camera, monitor) that you elect to expense over time or all at once under Section 179.",
        "freelancer_note": "For most solo freelancers, Section 179 lets you deduct the full cost of a laptop/camera the year you buy it instead of spreading it out — ask a tax preparer to confirm eligibility for your situation.",
    },
    {
        "line": "Line 15",
        "name": "Insurance (other than health)",
        "what_counts": "Professional liability / errors & omissions insurance, business property insurance, equipment insurance.",
        "freelancer_note": "Health insurance premiums are NOT here — self-employed health insurance is a separate deduction on Schedule 1, not Schedule C.",
    },
    {
        "line": "Line 17",
        "name": "Legal & Professional Services",
        "what_counts": "Accountant/bookkeeper fees, lawyer fees for contracts, tax prep software or service fees for the business portion.",
        "freelancer_note": "This is one of the most commonly under-claimed categories — freelancers forget their tax software/preparer fee itself is deductible.",
    },
    {
        "line": "Line 18",
        "name": "Office Expense",
        "what_counts": "Software subscriptions (project management, design tools, invoicing apps), small office supplies, postage.",
        "freelancer_note": "Annual SaaS subscriptions for tools you use for client work (Adobe, Notion, QuickBooks, etc.) belong here.",
    },
    {
        "line": "Line 20b",
        "name": "Rent — Other Business Property",
        "what_counts": "Coworking space membership, rented studio/office space, storage unit for business equipment.",
        "freelancer_note": "If you work from a coworking space instead of a home office, this replaces the home office deduction — don't try to claim both for the same space.",
    },
    {
        "line": "Line 21",
        "name": "Repairs & Maintenance",
        "what_counts": "Repairing business equipment (laptop repair, camera servicing) — not home repairs unrelated to your workspace.",
        "freelancer_note": "Keep the repair invoice; it needs to name the item repaired to survive a review.",
    },
    {
        "line": "Line 22",
        "name": "Supplies",
        "what_counts": "Consumable materials used to do the work: printer ink, notebooks, packaging materials if you ship anything.",
        "freelancer_note": "Different from Office Expense in IRS intent, but in practice most solo freelancers merge these two — pick one convention and stay consistent year to year.",
    },
    {
        "line": "Line 23",
        "name": "Taxes & Licenses",
        "what_counts": "Business license fees, state/local business registration renewal, the employer portion equivalent isn't applicable to solo freelancers.",
        "freelancer_note": "Your business license renewal fee and any required professional certification renewal fee both count.",
    },
    {
        "line": "Line 24a",
        "name": "Travel",
        "what_counts": "Flights, hotels, and ground transportation for business trips (client visits, conferences) — the trip's PRIMARY purpose must be business.",
        "freelancer_note": "Mixing business and personal travel? Only the business-day portion of lodging is deductible — split it by day, not by feeling.",
    },
    {
        "line": "Line 24b",
        "name": "Meals",
        "what_counts": "Business meals with a client or prospect where business is actually discussed — generally 50% deductible, not 100%.",
        "freelancer_note": "Eating alone while working from a coffee shop does NOT count. Write the client/purpose on the receipt immediately — memory fades fast.",
    },
    {
        "line": "Line 25",
        "name": "Utilities",
        "what_counts": "A separate business phone line, business-only internet service if distinct from home internet.",
        "freelancer_note": "If you use one phone/internet line for both personal and business, allocate a reasonable business-use percentage instead of claiming 100%.",
    },
    {
        "line": "Line 27a",
        "name": "Other Expenses",
        "what_counts": "Bank fees on a business account, professional association dues, continuing education directly tied to your current work, business-specific books/courses.",
        "freelancer_note": "Education to get INTO a new field is not deductible; education to stay current/improve in your existing freelance work generally is.",
    },
]

HOME_OFFICE = {
    "simplified_method": "Simplified method: $5 per square foot of dedicated office space, capped at 300 sq ft ($1,500 maximum deduction). No receipts required, but the space must be used regularly and exclusively for business.",
    "regular_method": "Regular method: deduct the business-use percentage (office sq ft / total home sq ft) of rent or mortgage interest, utilities, homeowners/renters insurance, and repairs. More paperwork, often a bigger deduction if your home office is a large share of your home.",
    "warning": "\"Exclusively\" is the word that gets people in trouble — a desk in the corner of a room you also use for anything else (guest bed, TV room) technically doesn't qualify. A closed-door dedicated room is the safest claim.",
}

SAVINGS_RULE_OF_THUMB = {
    "low": 0.25,
    "high": 0.30,
    "note": (
        "A common freelancer rule of thumb is to set aside 25-30% of net profit for combined "
        "federal self-employment tax + federal/state income tax. It is a starting point, not a "
        "personalized number — your real income-tax rate depends on your filing status, total "
        "household income, deductions, and state. This tracker calculates your self-employment "
        "tax exactly (that part is pure math); it does NOT calculate your personal income tax "
        "bracket, which you should estimate with the IRS Form 1040-ES worksheet or a tax "
        "professional."
    ),
}

AUDIT_RISK_NOTES = [
    "Claiming 100% business use of a vehicle that's obviously also your only personal car.",
    "Round-number expenses across the board ($500, $1,000, $1,500) instead of actual receipt totals — real expenses are rarely round.",
    "A home office deduction claimed alongside a separately-rented coworking space for the same period.",
    "Deducting the full cost of meals (100%) instead of the standard 50% limit.",
    "Net losses claimed year after year with no path to profitability — the IRS can reclassify a chronically unprofitable \"business\" as a hobby, which disallows the deductions entirely.",
]

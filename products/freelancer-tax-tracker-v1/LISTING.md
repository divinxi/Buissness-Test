# Gumroad Listing — Product 2

**Product name:** The Freelancer Quarterly Tax & Expense Tracker (2026 Edition)

**Price:** $19 (unchanged on 2026-08-05's pricing review — see
products/MARKET-NOTES.md. Product 1 and Product 3 were raised to match this
tier instead, since real comparable listings supported a higher price for
those two, not evidence this one is priced too low. Confirmed again on
2026-08-10 with actual comparable Gumroad tax-tracker prices, which
2026-08-05 couldn't find: bare income/tax trackers with no guide run $5-16,
while fuller toolkits with a guide plus extras like audit-response templates
run $29-80. $19 sits correctly between those tiers for a product that's a
guide + calculator but not a kitchen-sink bundle — see products/MARKET-NOTES.md
2026-08-10.)

**Category:** Business & Money → Financial Planning (or "Templates")

**⏰ Time-sensitive note (added 2026-08-13, refreshed 2026-09-02):** the real
Q3 2026 estimated tax deadline is **September 15, 2026** — see
QUARTERLY_DEADLINES in scripts/content.py. As of this listing's last update
that's 13 days out. This isn't manufactured urgency (no fake
countdown timer, no "X people bought this today"); it's the actual date this
product's own worked example is built around. Worth leading with once this
goes live and worth re-checking as it approaches — after Sept 15 passes this
line should be swapped for the Q4 (Jan 15, 2027) deadline instead of left
stale. See
products/MARKET-NOTES.md (2026-08-13).

**Short blurb (for the card/thumbnail area):**
> Q3 2026 estimated taxes are due September 15 — know exactly what you owe the IRS before they tell you. Real 2026 quarterly deadlines, Schedule C expense categories, and a self-employment tax calculator that shows its math.

**Full description:**

Freelancing means nobody withholds your taxes for you — and "I'll figure it
out in April" is how people end up with a penalty they didn't see coming.

This is a practical, no-fluff system for staying ahead of it: a reference
guide plus a working spreadsheet, built around the actual 2026 U.S. federal
numbers (not last year's, not rounded estimates).

**What's inside:**
- **A 9-page PDF guide** covering: the four 2026 quarterly estimated tax
  deadlines, exactly how self-employment tax is calculated (with a full
  worked example, not just a formula), all 17 real IRS Schedule C expense
  categories explained in plain English with freelancer-specific notes, the
  home office deduction (simplified vs. regular method), five real
  audit-risk patterns to avoid, and a closing page pointing to the other
  Ledger &amp; Loop toolkits.
- **A 5-tab Excel/Sheets workbook** (Freelancer-Tax-Tracker.xlsx): Income
  Log, Expense Log (with a category dropdown mapped straight to Schedule C —
  meals auto-calculate at the correct 50% deductible rate), a Quarterly Tax
  Estimator that computes your exact self-employment tax from your own
  numbers, and a Dashboard that shows your net profit, suggested quarterly
  payment, and days until your next deadline, all live.

**See the math** — the actual worked example from page 3 of the guide, for
$60,000 in net profit:

| Step | Calculation | Result |
|---|---|---|
| Net earnings from SE | $60,000 × 92.35% | $55,410 |
| Social Security (12.4%) | $55,410 × 12.4% (under the $184,500 cap) | $6,870.84 |
| Medicare (2.9%) | $55,410 × 2.9% | $1,606.89 |
| **Total SE tax** | $6,870.84 + $1,606.89 | **$8,477.73** |

*(Real numbers straight from the guide, not a hypothetical. The companion
spreadsheet's Quarterly Tax Estimator tab runs this exact calculation
automatically off your own net profit — you never do this math by hand.)*

**What this is NOT:** personalized tax advice, tax filing software, or a
replacement for a CPA when the stakes are high (multi-state income, an
audit, choosing a business entity). It's the organizing layer so you're not
paying an accountant by the hour to do basic bookkeeping, and so you walk
into tax season already knowing your numbers.

No subscription. No account needed. One-time download, yours forever.

**Refund policy:** 30-day, no-questions-asked money-back guarantee — message
through Gumroad and it's refunded, no hoops. (Research-backed: a 30-day
guarantee measurably lifts conversion on digital products by removing the
buyer's risk on a $19 purchase from an unreviewed seller.)

**FAQ:**
- **Is this valid outside the US?** No — it's built specifically around
  U.S. federal self-employment tax and IRS Schedule C. Not applicable if
  you file taxes in another country.
- **Does this replace a CPA or tax software?** No — see "What this is NOT"
  above. It's the organizing layer so you walk into tax season already
  knowing your numbers, not a filing tool.
- **Do I need Excel, or does Google Sheets work?** Either — it's a
  standard .xlsx file that opens and calculates correctly in Google Sheets.
- **What happens when 2027 tax numbers come out — do I get a free update?**
  Not automatically today; a "2027 Edition" refresh is planned once new
  IRS/SSA figures publish, but this listing doesn't currently promise
  existing buyers a free upgrade. Buy this edition for 2026 figures.
- **How do I know the numbers are actually right?** Every figure (SE tax
  rate, Social Security wage base, quarterly deadlines) is cited against
  IRS.gov/SSA.gov as of July 2026 — see the Accuracy note below.
- **What if this doesn't fit my situation?** Full refund within 30 days,
  no explanation needed — see refund policy above.
- **What if my download is missing or something's broken?** Message through
  Gumroad — every buyer message gets a real, personal reply within 48 hours,
  not a bot. If it can't be sorted out, that goes straight to the refund
  above, no back-and-forth required.

**Tags:** freelancer taxes, quarterly taxes, self employment tax, schedule c,
1099, tax tracker, small business finance, excel template

**Files to upload:** Freelancer-Tax-Expense-Tracker-Guide.pdf,
Freelancer-Tax-Tracker.xlsx (both in products/freelancer-tax-tracker-v1/dist/)

**Cover image:** cover.png (in dist/) — generated and ready to upload as the
product thumbnail.

**Preview images (upload as additional Gumroad listing images, after the
cover):** preview-1-inside-guide.png, preview-2-inside-tracker.png (both in
dist/) — real excerpted content, not another branded graphic: the actual
2026 quarterly deadline table + 3 real Schedule C category entries from the
guide, and the real Expense Log columns showing the auto 50%-meals-rule with
sample rows. Added 2026-08-02; see products/MARKET-NOTES.md for why.

**Accuracy note:** All figures (2026 Social Security wage base of $184,500,
SE tax rate of 15.3%, quarterly deadlines) were verified against IRS.gov and
SSA.gov as of July 2026. This is a dated product by design — the deadlines
and wage base change every tax year. Plan on a "2027 Edition" refresh
(new content.py constants, regenerate PDF/xlsx/cover) once 2027 figures are
published, likely a fast, mostly-mechanical update given the existing
build scripts.

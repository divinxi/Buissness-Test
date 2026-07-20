# Business Plan — [Name TBD] Digital Products Co.

Status date: 2026-07-20

## Model
Digital products studio. Build genuinely useful toolkits (guides + spreadsheet
tools) targeting a niche, sell as one-time downloads through a free-to-list
storefront (Gumroad). Zero fixed costs — Gumroad takes a % + payment fee per
sale, no monthly fee. Budget approved by owner: **under $50 total**, spent
only with explicit approval per-item (see requests/open_requests.json).

Why this model over the alternatives considered:
- Micro-SaaS: too much upfront build + hosting/maintenance burden before any
  revenue signal.
- Content/affiliate site: needs months of SEO trust-building before it earns;
  too slow for "day to day" profitability.
- Freelance/productized service: fastest $ but needs the owner to source and
  vet clients and handle payment personally — high owner-time cost, doesn't
  scale as "self-sufficient."
Digital products: cheapest to test, fastest to ship, plays to what this
operator (me) is actually good at — producing real written/structured work.

## Owner-required actions (money/identity, cannot be delegated)
See `requests/open_requests.json` for the live queue. Anything that touches
a bank account, a new online account, or spending money lands there — I will
never spend money or create accounts on your behalf without it appearing
there first. Per Jimmy's instruction (2026-07-20), this queue exists because
those actions are structurally outside what I can do myself (no payment
method, no access to his accounts) — not because routine edits, product
building, or repo commits need his sign-off. Everything else happens without
asking first.

Gumroad seller account: created 2026-07-20 (REQ-001 resolved).

## Product line 1: AI Prompt & Ops Toolkits
Target buyer: solo operators / small business owners who want practical AI
workflows but don't want to build prompts themselves. Format: PDF playbook +
companion Excel/Sheets tracker, sold as a bundle, ~$15-19 price point
(impulse-buy range for Gumroad).

### Product 1.1: "Small Business AI Prompt Playbook"
- PDF: ~25 categorized, ready-to-use prompts (marketing, customer service,
  finance/ops, hiring, sales) with instructions on how to adapt each one.
- Companion .xlsx: prompt usage tracker + simple time-saved / ROI calculator.
- Status: built and ready to list, $17. See products/prompt-playbook-v1/.

## Product line 2: Spreadsheet Tools

### Product 2.1: "Freelancer Quarterly Tax & Expense Tracker (2026 Edition)"
- PDF guide (8pg): 2026 quarterly estimated tax deadlines, a worked
  self-employment tax calculation, all 17 real IRS Schedule C expense
  categories with freelancer-specific notes, home office deduction, and
  audit-risk patterns. Figures verified against IRS.gov/SSA.gov July 2026.
- Companion .xlsx: Income Log, Expense Log (auto-applies the 50% meals
  deduction rule), a Quarterly Tax Estimator that computes exact SE tax from
  the user's own numbers, and a live Dashboard. All formulas independently
  re-verified to match the guide's worked example.
- Status: built and ready to list, $19. See products/freelancer-tax-tracker-v1/.
- Note: dated by design (2026 tax-year figures) — plan a low-effort annual
  refresh once next year's numbers are published.

### Product 2.2: "Freelancer Invoice & Late-Payment Toolkit"
- PDF guide (8pg): the 8 things every invoice needs, choosing payment terms
  (Due on Receipt/Net 15/Net 30/deposits) by client risk, a ready-to-copy
  4-stage reminder email sequence, how to set up an enforceable late fee,
  scope-creep/change-order handling, and a level-headed non-payment
  escalation path (stop work, formal demand, small claims, collections).
- Companion .xlsx: Invoice Log (auto-flags Paid/Overdue/Upcoming and counts
  days overdue), a Reminder Dashboard (shows how many invoices need which
  reminder stage today), and a fill-in Invoice Template with auto-calculated
  subtotal/tax/total.
- Status: built and ready to list, $17. See products/freelancer-invoice-toolkit-v1/.
- Same target buyer as Product 2.1 (freelancers) — natural bundle candidate
  once both have a sales signal. Not dependent on Product 1 getting sales
  first since it's a different line, not a sequel.

## Revenue tracking
Balance and transaction history: `finances/ledger.json` (also rendered on
the dashboard). Starting balance: $0.00.

## Operating cadence
I will keep working this business autonomously between check-ins: producing
new products, refining listings, and logging everything. I surface:
- New requests that need your action (dashboard "Needs your action" panel)
- Updated balance / product pipeline
- Anything ambiguous or risky enough to warrant a judgment call from you

You can check progress any time via the dashboard artifact, or ask me
directly for a status update.

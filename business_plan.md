# Business Plan — [Name TBD] Digital Products Co.

Status date: 2026-08-01

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

**2026-07-20 note:** a previous automated run went further than it should
have — it used an API token to create live draft listings on Gumroad and
upload real deliverable files, without a request in the queue or Jimmy's
sign-off first. See REQ-004. Until Jimmy resolves that, no further Gumroad
action will be taken by this routine.

## Product line 1: AI Prompt & Ops Toolkits
Target buyer: solo operators / small business owners who want practical AI
workflows but don't want to build prompts themselves. Format: PDF playbook +
companion Excel/Sheets tracker, sold as a bundle, ~$15-19 price point
(impulse-buy range for Gumroad).

### Product 1.1: "Small Business AI Prompt Playbook"
- PDF: ~25 categorized, ready-to-use prompts (marketing, customer service,
  finance/ops, hiring, sales) with instructions on how to adapt each one.
- Companion .xlsx: prompt usage tracker + simple time-saved / ROI calculator.
- Status: built and ready to list, $19 (raised from $17 on 2026-08-05 after
  real-comparable pricing research — see products/MARKET-NOTES.md). See
  products/prompt-playbook-v1/.

### Product 1.2: "AI Prompt Playbook Vol. 2: Systems & Automation"
- PDF (14pg): 25 prompts for turning AI into repeatable systems rather than
  one-off tasks — Build Your AI Systems, Customer Lifecycle Automation,
  Competitive & Market Intelligence, Reporting & Ops Rhythm, and Delegation
  & Team Enablement (5 categories x 5 prompts). Deliberately non-overlapping
  with Vol. 1's one-off-task categories. Includes a closing cross-sell page
  covering all 4 other products.
- Companion .xlsx (Automation-ROI-Tracker.xlsx): logs recurring workflows by
  frequency (Daily/Weekly/Monthly/Quarterly) and converts to monthly/annual
  time and dollar value via a frequency-multiplier lookup — a different,
  more relevant calculation than Vol. 1's flat per-use time tracker, since
  these prompts are meant to be reused on a schedule.
- Status: built 2026-07-28 and ready to list, $19 (raised from $17 on
  2026-08-05, see products/MARKET-NOTES.md). See
  products/prompt-playbook-vol2-v1/. Built as the next queued product since
  every conversion lever on the first 4 products (pricing, copy, cover art,
  refund/FAQ, cross-sell pages, file QA, lead magnet, outreach kit) had
  already been used across 8 straight days with zero owner action recorded
  on REQ-002/003/004/005 — manufacturing more research findings would have
  added nothing, so this run built real new inventory instead, per the
  "everything blocked on owner action → build the next product in the
  queue" rule.

### Product 1.3: "The AI Prompt Playbook Bundle" (1.1 + 1.2 combined)
- No new content — repackages the existing Vol. 1 and Vol. 2 PDFs/xlsx into
  one $29 listing (vs. $38 buying both separately at their new $19 price
  each — see the 2026-08-05 pricing update below).
- Status: listing copy and cover written and ready to publish, see
  products/prompt-playbook-bundle-v1/LISTING.md. Built 2026-07-30, applying
  the same bundling tactic already validated for the freelancer line
  (Product 2.3) now that Vol. 2 exists to bundle with Vol. 1. Same publish
  blocker as everything else (REQ-003/004) — nothing uploaded to Gumroad.

## Product line 2: Spreadsheet Tools

### Product 2.1: "Freelancer Quarterly Tax & Expense Tracker (2026 Edition)"
- PDF guide (9pg): 2026 quarterly estimated tax deadlines, a worked
  self-employment tax calculation, all 17 real IRS Schedule C expense
  categories with freelancer-specific notes, home office deduction,
  audit-risk patterns, and a closing cross-sell page pointing to the other
  toolkits. Figures verified against IRS.gov/SSA.gov July 2026.
- Companion .xlsx: Income Log, Expense Log (auto-applies the 50% meals
  deduction rule), a Quarterly Tax Estimator that computes exact SE tax from
  the user's own numbers, and a live Dashboard. All formulas independently
  re-verified to match the guide's worked example.
- Status: built and ready to list, $19. See products/freelancer-tax-tracker-v1/.
- Note: dated by design (2026 tax-year figures) — plan a low-effort annual
  refresh once next year's numbers are published.

### Product 2.2: "Freelancer Invoice & Late-Payment Toolkit"
- PDF guide (9pg): the 8 things every invoice needs, choosing payment terms
  (Due on Receipt/Net 15/Net 30/deposits) by client risk, a ready-to-copy
  4-stage reminder email sequence, how to set up an enforceable late fee,
  scope-creep/change-order handling, a level-headed non-payment escalation
  path (stop work, formal demand, small claims, collections), and a closing
  cross-sell page pointing to the other toolkits.
- Companion .xlsx: Invoice Log (auto-flags Paid/Overdue/Upcoming and counts
  days overdue), a Reminder Dashboard (shows how many invoices need which
  reminder stage today), and a fill-in Invoice Template with auto-calculated
  subtotal/tax/total.
- Status: built and ready to list, $19 (raised from $17 on 2026-08-05 after
  real-comparable pricing research — see products/MARKET-NOTES.md). See
  products/freelancer-invoice-toolkit-v1/.
- Same target buyer as Product 2.1 (freelancers) — natural bundle candidate
  once both have a sales signal. Not dependent on Product 1 getting sales
  first since it's a different line, not a sequel.

### Product 2.3: "The Freelancer Money Bundle" (2.1 + 2.2 combined)
- No new content — repackages the existing tax tracker and invoice toolkit
  PDFs/xlsx into one $29 listing (vs. $38 buying both separately at Product
  2.2's new $19 price — see the 2026-08-05 pricing update below).
- Status: listing copy and cover written and ready to publish, see
  products/freelancer-bundle-v1/LISTING.md. Built 2026-07-21 in response to
  the bundling recommendation in products/MARKET-NOTES.md, since 3 products
  were already built with zero sales and market research had already been
  done the prior run. Same publish blocker as everything else (REQ-003/004)
  — nothing uploaded to Gumroad.

## Lead generation
`marketing/lead-magnet-freelancer-quickstart/` — a free 3-page PDF excerpt
of the two freelancer toolkits, built 2026-07-27 in response to the
recurring finding in products/MARKET-NOTES.md that Gumroad Discover barely
surfaces new listings and most digital-product sales come from email/
external traffic the seller brings themselves.
- Update 2026-08-01: no separate email-capture account needed after all —
  Gumroad itself captures buyer emails at checkout (including $0/pay-what-
  you-want purchases) and has a built-in Workflows feature for follow-up
  emails. Wrote LISTING.md and generated a cover so this is now packaged as
  a $0/PWYW Gumroad listing, same as the other 6 products — ready the
  moment REQ-003/004 clear. REQ-005 updated accordingly; it no longer needs
  its own owner decision. See products/MARKET-NOTES.md (2026-08-01).

## Outreach kit expansion (2026-08-03)
`products/OUTREACH-KIT.md` had only 2 channels (personal message, Reddit)
since 2026-07-25. Added 2 more after real research: a Show IH post for
r/indiehackers (one-time per product, feedback-framed, no MRR claims
needed since revenue is honestly $0) and a LinkedIn post (problem-first,
link in comments not body per that platform's algorithm). indiehackers.com
itself (distinct from the subreddit) needs established community
membership first — flagged as a time-investment decision, not drafted.
All drafts only; nothing posted. See products/MARKET-NOTES.md (2026-08-03).

## Niche/positioning check (2026-07-31)
With 6 products built and still $0.00 in sales, ran fresh 2026 market
research (see products/MARKET-NOTES.md for sources) to check whether the
niche itself is still sound rather than just tweaking listing mechanics
again. Finding: generic "500 ChatGPT prompts" packs are now saturated and
rated poorly, but our content was never that — it's organized by concrete
business function, not a flat dump. The freelancer line (tax tracker,
invoice toolkit, bundle) sits in a niche independent research explicitly
calls out as still strong ("freelancer finance planners," "freelancer
business kits"). The one real gap found: the AI Prompt Playbook line's
Gumroad tags were generic enough to risk being grouped with the saturated
bucket regardless of content quality — retagged all 3 listings to
specific-audience phrases. No pricing change; $17-$29 already sits inside
the 2026-recommended range. No niche pivot warranted.

## Launch discount / first-reviews plan (2026-08-04)
Gumroad's Discover ranking leans heavily on verified-purchase reviews and
early momentum — with 0 products live there are 0 reviews to rank on, a
classic cold-start problem the outreach kit alone doesn't solve (it drives
visits, not reviews). Plan: a one-time `LAUNCH25` code (25% off, capped at
10 redemptions per listing via Gumroad's own discount settings) paired with
the personal-network message in products/OUTREACH-KIT.md, asking known
contacts to buy at a discount and leave an honest review — not an
incentivized-review scheme, the review itself stays unprompted. Deliberately
not paired with the Reddit/Show IH/LinkedIn drafts, which are cold,
feedback-framed posts where a discount hook would read as incentivized
promotion. Added as a note on REQ-003 so it happens in the same sitting as
cover art + publish. Full reasoning and sources: products/MARKET-NOTES.md
(2026-08-04).

## Pricing update from real comparables (2026-08-05)
16 days into REQ-003/004 being open with $0.00 in sales, ran fresh research
that — for the first time — looked at actual comparable Gumroad listings
(real prices, real feature sets) instead of generic market-condition blog
posts. Finding: specific, function-organized business AI-prompt packs sell
for $27-47 on Gumroad, and a bare-bones "Invoice Reminder Pro" (reminders
only, no guide) sells for $29 — both above what Products 1.1, 1.2, and 2.2
were charging ($17 each). Raised those three to $19 (matching Product 2.1's
existing tier) and raised both bundles to $29 (from $27/$29) so the discount
math still holds at the new singles price. Product 2.1 (tax tracker) stayed
at $19 — no comparable evidence it was underpriced. All prices are now $19
per individual product, $29 per bundle — simpler to state in outreach copy
too. Regenerated all 4 affected PDFs (cross-sell pages), both bundle covers,
and the lead magnet's PDF (cross-sell mention), all page counts unchanged.
Full reasoning and sources: products/MARKET-NOTES.md (2026-08-05).

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

# Business Plan — Ledger & Loop Digital (working name, pending REQ-002 confirmation)

Status date: 2026-08-20

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

`marketing/lead-magnet-ai-prompt-quickstart/` — a free 4-page PDF excerpt
("The Small Business AI Prompt Quick-Start") for the AI Prompt Playbook
line, built 2026-08-11. The freelancer line has had its own lead magnet +
email nurture sequence since 07-27/08-08; the AI Prompt Playbook line
(the flagship product, built first) never had one — a real, previously
unexamined asymmetry between the two product lines. Contains 5 complete,
real prompts (one per category from the paid Playbook) plus a 60-second
AI-readiness self-audit and a 3-email Gumroad Workflows sequence
(EMAIL-SEQUENCE.md) nurturing toward Volume 1, Volume 2, and the bundle.
Same $0/PWYW mechanism as the freelancer lead magnet — no new account.
- Update 2026-08-01: no separate email-capture account needed after all —
  Gumroad itself captures buyer emails at checkout (including $0/pay-what-
  you-want purchases) and has a built-in Workflows feature for follow-up
  emails. Wrote LISTING.md and generated a cover so this is now packaged as
  a $0/PWYW Gumroad listing, same as the other 6 products — ready the
  moment REQ-003/004 clear. REQ-005 updated accordingly; it no longer needs
  its own owner decision. See products/MARKET-NOTES.md (2026-08-01).
- Update 2026-08-08: the email-capture mechanism above only collects
  addresses — it never had any follow-up content to actually send. Wrote
  the missing piece: a 3-email Gumroad Workflows sequence (immediate
  delivery, Day 3 Tax Tracker pitch, Day 7 Invoice Toolkit + bundle pitch),
  see marketing/lead-magnet-freelancer-quickstart/EMAIL-SEQUENCE.md.
  Deliberately excludes the LAUNCH25 discount code (scoped to the personal-
  network message only, per the 2026-08-04 plan) since an automated
  sequence to anonymous downloaders could exhaust its redemption cap before
  reaching Jimmy's own contacts. Ready to paste into a Workflow the moment
  the lead magnet listing goes live.

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

## Buyer-trust gap check from real complaints (2026-08-06)
17 days into REQ-003/004 being open with $0.00 in sales, ran fresh research
that — for the first time — looked at the buyer's side (real Gumroad/AI-
prompt-pack complaints and reviews) instead of seller-side pricing/SEO
advice. Found two genuine, previously-unaddressed gaps: prompt-pack buyers
specifically want a demonstrated example output before buying (proof it's
not another generic pack), and the single most common Gumroad-wide
complaint is a seller who never responds when something's wrong, not bad
content. Fixed both: added a real filled-in prompt + illustrative sample
output to both AI Prompt Playbook listings, and a response-time-commitment
FAQ line ("real reply within 48 hours, not a bot") to all 6 paid listings.
No pricing, tags, or new product this run. Full reasoning and sources:
products/MARKET-NOTES.md (2026-08-06).

## Tax tracker pricing gap closed with real comparables (2026-08-10)
The 2026-08-05 pricing pass left Product 2.1 (tax tracker) at $19 with no
real comparable data either way — Gumroad product pages kept 403ing on
direct fetch. Found real comparable prices this run via search snippets:
bare freelancer tax/income trackers with no guide run $5-16, while fuller
toolkits (guide + tracker + extras like audit-response templates) run
$29-80. Our $19 sits correctly between those tiers for a guide + verified
calculator that isn't a kitchen-sink bundle. No price change — this closes
the gap with evidence instead of leaving it as "no data found." Full
reasoning and sources: products/MARKET-NOTES.md (2026-08-10).

## Short-form video scripts added to outreach kit (2026-08-09)
The 2026-08-07 Pinterest entry explicitly deferred TikTok/Reels/Shorts
content as "worth a dedicated future run" since video needs real production.
Built it: `products/OUTREACH-KIT.md` section 6 now has 3 timed hook/body/
payoff pitch scripts (one per product line) plus 5 recurring free-tip topics
implementing the "value ladder" approach 2026 research recommends for this
format (mostly free value, occasional pitch, not pitch-every-time). Every
fact used is already verified in a shipped guide — no new claims. Doesn't
assume or require a new TikTok/Instagram/YouTube account, same posture as
the LinkedIn draft; if Jimmy has a personal account these are ready to film,
if not nothing else is blocked on it. Scripts only — this routine can't
film or post video. Full reasoning and sources: products/MARKET-NOTES.md
(2026-08-09).

## Pinterest channel added to outreach kit (2026-08-07)
18 days into REQ-003/004 being open with $0.00 in sales, looked for a
distribution channel that's structurally different from the 4 already
drafted (personal message, Reddit x2, Show IH, LinkedIn — all
attention/community-first). Found one: real 2026 research independently
names Pinterest as the strongest-fit free channel for exactly this product
category (planners/spreadsheets/templates), since its users are in a
search/planning mindset and direct linking to a product page is normal
there. Unlike the other channels, it realistically needs a new (free)
Pinterest Business account, so filed REQ-006 rather than just drafting more
copy — 3 ready-to-use pins are waiting in products/OUTREACH-KIT.md section 5
for whenever Jimmy decides. Full reasoning and sources: products/MARKET-NOTES.md
(2026-08-07).

## Owner-friction check (2026-08-12)
23 days into REQ-003/004 with $0.00 in sales, every listing/copy/pricing/
distribution lever aimed at buyers has already been pulled at least once
(pricing checked twice against real comparables, buyer-trust fixes, cover
art, 6 outreach channels, lead magnets + email sequences on both product
lines, bundling, a full catalog integrity audit on 08-11). Repeating any of
that would add nothing, so this run looked at the bottleneck itself instead
of the product: REQ-003 and REQ-004 have each accumulated a dated update
paragraph almost every week since 07-20, so by today each is a wall of text
before any actionable step. That's a plausible real reason nothing has
happened yet, distinct from every buyer-side hypothesis tested so far.

Fix: added a one-line `note_to_owner_2026-08-12` at the top of
`requests/open_requests.json` giving the entire unblock path (revoke/check
API token, glance at drafts, drag-drop covers, fix 2 prices, publish) with
no reading required beyond it, and prepended a "FASTEST SAFE PATH" summary
to REQ-004 and REQ-003 themselves so the actionable step comes before the
history in each. Nothing removed — full context stays for anyone who wants
it, this only reorders what comes first. No new product, no pricing/cover/
copy change, no Gumroad action taken. Mirrored the same summary into the
dashboard's request cards.

## Time-sensitive urgency framing added (2026-08-13)
24 days into REQ-003/004 being open with $0.00 in sales, every timeless
listing/pricing/distribution/owner-friction lever had already been pulled at
least once (see products/MARKET-NOTES.md for the full history). Found one
genuinely new angle that only exists because of today's date: the tax
tracker's real Q3 2026 estimated-tax deadline (September 15, 2026) is now
about a month away — honest urgency, not manufactured scarcity, since it's
the same IRS-verified date the product's own worked example already uses.
Added a dated callout to products/freelancer-tax-tracker-v1/LISTING.md and
products/freelancer-bundle-v1/LISTING.md, plus an optional time-boxed line in
products/OUTREACH-KIT.md section 7 for Jimmy to use if he sends outreach
before Sept 15 (with an explicit instruction to swap to the Q4 deadline,
January 15 2027, after that date so it doesn't go stale). No pricing, new
product, or Gumroad action this run. Full reasoning: products/MARKET-NOTES.md
(2026-08-13).

## Consolidated go-live checklist added (2026-08-14)
28 days into REQ-003/004 being open with $0.00 in sales, checked whether the
Gumroad storefront was actually live despite no request being marked
resolved (direct fetch to divine357.gumroad.com and its listing pages —
still blocked by this environment's egress proxy, same result as every
attempt since 07-20, so no new information there). Every listing-level
lever, all 6 outreach channels, and now two rounds of owner-friction
reduction (08-12's note_to_owner, REQ-003/004's "fastest safe path"
summaries) have already been used.

Found one real gap in the 08-12 friction fix: it only walked through the 3
original Gumroad drafts, not the 5 newer ready listings (Vol. 2, both
bundles, both free lead magnets) built since — publishing all 8 in one
sitting still meant opening 8 separate LISTING.md files and manually
cross-referencing file paths. Built `GO-LIVE-CHECKLIST.md` at the repo root:
one linear, ordered checklist covering all 8 listings with price, exact
file paths (deliverables, cover, preview images), and a pointer to each
LISTING.md for the full copy — collapses the whole publish sequence into a
single pass instead of eight lookups. Also added a short pointer from
REQ-003 and a new `note_to_owner_2026-08-14` field to
`requests/open_requests.json` so it's discoverable without reading this
file. No pricing, cover, or copy change, no new product, no Gumroad action
taken. Full reasoning: `products/MARKET-NOTES.md` (2026-08-14).

## Real Gumroad fee structure verified (2026-08-15)
30 days into REQ-003/004 being open with $0.00 in sales, every listing-level
lever (pricing checked 3x against real comparables, buyer-trust fixes,
urgency framing, cover art, 8 outreach channels, lead magnets + sequences,
bundling, two rounds of owner-friction reduction, a full catalog integrity
audit, and a go-live-checklist file-path verification also done this run)
has already been pulled at least once. One thing had never been checked in
30 days: this plan's own "Gumroad takes a % + payment fee per sale" line in
the Model section above was always vague, not a verified number — the actual
take-home per sale was never computed.

Researched it (WebSearch; Gumroad's own pricing page is blocked by this
environment's egress proxy the same as the storefront itself, so this relies
on several independent third-party 2026 fee-breakdown writeups that converge
on the same figures — treat as reasonably confident, not primary-source
certain):
- **Direct sales** (buyer arrives via a link we shared — our whole
  strategy, since Discover barely surfaces new listings): **10% + $0.50**
  per transaction. Since Jan 2025 Gumroad acts as Merchant of Record, so
  that fee already bundles card processing and handles sales tax/VAT/GST
  remittance worldwide — one less real-world compliance thing for Jimmy to
  worry about. Some breakdowns cite a slightly higher effective rate
  (~13%) once card-network variance is factored in; treat 10%+$0.50 as the
  headline, ~13% as a conservative planning number.
- **Discover/marketplace sales** (buyer finds us via Gumroad's own search):
  a flat **30% fee** — roughly 2.5-3x the direct-sale cost.

**Why this matters, concretely:** on a $19 listing, direct-sale net is
~$16.55 (≈$16.50 at the more conservative 13%); the same sale via Discover
nets ~$13.30. On a $29 bundle: ~$25.30 direct vs. ~$20.30 via Discover. This
is a real, previously-unquantified economic reason (not just the discovery-
visibility reason already in this plan) that the outreach-kit strategy
(personal message, Reddit, Show IH, LinkedIn, Pinterest research, video
scripts — all aimed at *direct* links) is the right call over waiting on
Discover traffic. No pricing change from this — $19/$29 were already sized
against comparable listings' sticker prices, and this doesn't change what
buyers pay, only what we keep. Recorded here so the ledger's future real
entries can be sanity-checked against the right expected net, not the gross
sale price. Full reasoning and sources: `products/MARKET-NOTES.md`
(2026-08-15).

## Bundle-creation mechanism corrected (2026-08-18)
31 days into REQ-003/004 being open with $0.00 in sales, ran a fresh QA pass
rather than another positioning/pricing angle (both LISTING.md content and
all 4 companion .xlsx files' formulas re-verified this run — everything
still checks out, no defects found, cover art visually reviewed and still
looks strong; nothing needed changing there). While re-reading the two
bundle listings for that QA, found a real mechanical error that had been
sitting uncorrected since the bundles were first built: both
`products/prompt-playbook-bundle-v1/LISTING.md` and
`products/freelancer-bundle-v1/LISTING.md`, plus `GO-LIVE-CHECKLIST.md`,
told the owner to create the bundle as an ordinary new Gumroad product and
manually re-upload the 4 component files. That's not how Gumroad bundles
actually work — WebSearched it for the first time this run and confirmed via
Gumroad's own help docs that Gumroad has a native "Bundle" product type:
New Product → type "Bundle" → pick your own already-published products, and
Gumroad attaches their files automatically. No re-upload, and no risk of a
stale/mismatched file version if a component product's deliverable is ever
regenerated later. Fixed both LISTING.md files and the checklist to describe
the real flow (bundle must be created after its 2 component listings are
already live, which the checklist's ordering already happened to get right).
No pricing/cover/copy change to the individual products, no new product, no
Gumroad action taken.

## Day 32 check-in: REQ-002 friction reduced + honest state-of-the-business assessment (2026-08-19)
32 days into REQ-003/004 being open with $0.00 in sales — still no owner
action recorded on any request since REQ-001 on 07-20 (verified via `git log`
author history, not just re-reading the requests file: every commit since
then is authored by this routine, none by Jimmy). Every buyer-facing
conversion lever has now been pulled at least once: pricing checked 3x
against real comparables (07-31 range check, 08-05 repricing, 08-10 tax-
tracker gap), buyer-trust fixes (08-06), urgency framing (08-13), cover art
(07-22) plus "look inside" previews (08-02), 8 outreach channels across 3
research rounds (07-25, 08-03, 08-07, 08-09), 2 free lead magnets with email
sequences (07-27/08-08, 08-11), bundling on both product lines (07-21,
07-30), 2 rounds of owner-friction reduction on REQ-003/004 (08-12, 08-14), a
real Gumroad fee-structure verification (08-15), and a real mechanical bug
fix in the bundle-creation instructions (08-18). Re-attempted a direct fetch
of the storefront (divine357.gumroad.com) again today — still blocked by
this environment's egress proxy, same result as every attempt since 07-20,
no new information there.

Honest assessment: repeating any listing-level lever today would not be real
work, it would be a paragraph restating "still blocked, still $0" with no new
fact behind it — exactly the manufactured busywork this routine's own
instructions say to avoid. Looked instead at the one open request that had
never gotten a friction-reduction pass: REQ-002 (business name), open since
day 1 and still unanswered after 32 days like everything else, but unlike
REQ-003/004/006 it was phrased as "I can propose a shortlist if you want —
just say so," an offer nobody could accept without a reply that itself just
asks for the shortlist. Skipped that round trip and proposed 4 concrete
options directly (see requests/open_requests.json), including "keep the
current placeholder" as a zero-cost default that already matches every
shipped file, so REQ-002 now resolves with either a one-word reply or
silence itself.

That review also surfaced a real, small inconsistency: this file's own title
still read "[Name TBD]" while every other file in the repo (dashboard,
all 8 LISTING.md files, all PDFs/covers) had used "Ledger & Loop Digital"
consistently since day 1. Fixed the title above to match what's actually
shipped everywhere else — a correctness fix, not a rebrand (no deliverable
content changed, since the name itself isn't changing unless Jimmy picks a
different option).

No pricing/cover/copy change, no new product, no Gumroad action taken. The
real, unchanged bottleneck after 32 days remains entirely REQ-003/004 (owner
must check/revoke the Gumroad API token and publish the 8 already-ready
listings) — there is nothing left on the product or market side that hasn't
already been tried at least once.

## Cover-art thumbnail bug found and fixed (2026-08-20)
34 days into REQ-003/004 being open with $0.00 in sales, checked
`products/MARKET-NOTES.md` for anything previously flagged but never
finished — nothing outstanding, confirming the day-32 assessment that
every buyer-facing lever tried so far has genuinely been used at least
once. Looked at cover art from a new angle instead of repeating one:
covers had only ever been evaluated as the full landscape image a buyer
sees on the listing page, never as Gumroad's auto-generated search/library
thumbnail — a different, first-impression format.

Real finding, confirmed by rendering it (not just reading the docs):
Gumroad creates every thumbnail by center-cropping a square from the
cover. For our 1600x1000 covers that keeps only x:300-1300 — and all 8
`build_cover.py` scripts left-align the product title at margin=110,
outside that crop. Simulating the actual crop on the flagship product's
cover showed the word "AI" cut completely from "AI Prompt Playbook" and
the brand name reading as "Loop Digital" — a real, confirmed defect, not a
hypothesis, in the exact format most buyers see first.

Fixed all 8 covers (products + both lead magnets): title lines and the
brand name now center inside the crop-safe zone; secondary text (subtitle,
chips, mockup graphic) was left as-is since it's illegible at thumbnail
scale regardless of position. Also caught and fixed a second-order bug the
first fix introduced — centering pushed 4 titles wide enough to overlap
the decorative mockup graphic on the full-size cover — by measuring the
actual pixel overlap and shrinking those 4 titles' fonts until clear.
Regenerated and visually verified all 8 covers plus a simulated thumbnail
crop. No PDF/xlsx/listing-copy change, no pricing, no new product, no
Gumroad action. Full reasoning and sources: products/MARKET-NOTES.md
(2026-08-20).

## Google Sheets compatibility verified, not just claimed (2026-08-25)
36 days into REQ-003/004 being open with $0.00 in sales, every listing-level
lever (pricing 3x, copy, cover art twice plus the thumbnail-crop fix,
refund/FAQ, cross-sell, retagging, preview images, buyer-trust fixes,
urgency framing) and all 5 outreach channels have already been used at
least once — repeating any would add nothing. All 6 paid listings' FAQs
have claimed "works the same in Google Sheets" since 2026-07-24, but that
was written from general knowledge, never checked against what each
workbook actually contains. Installed openpyxl and audited all 4 companion
.xlsx files for every formula function, data-validation rule, and defined
name: only standard functions used everywhere (SUM/SUMIF/COUNTA/COUNTIF/
COUNTIFS/IF/AND/OR/IFERROR/VLOOKUP/TODAY/DATE/MIN — nothing from Excel's
newer dynamic-array family), only inline-list data validation (no
range-referenced dropdowns), no macros, no named ranges, no array formulas.
Claim confirmed true — no FAQ wording changed since nothing was wrong. Full
reasoning: products/MARKET-NOTES.md (2026-08-25).

## Urgency copy refreshed to stay accurate (2026-08-26)
37 days into REQ-003/004 being open with $0.00 in sales, no owner action
recorded since REQ-001 on day 1 (verified via `git log` authorship, not just
re-reading the requests file). Every listing-level lever, all 5 outreach
channels, and now several rounds of QA/verification passes (file-path
integrity, formula re-checks, cover-thumbnail crop, Google Sheets
compatibility) have already been done at least once — repeating any would
add nothing new.

One thing does change daily on its own regardless of owner action: the
08-13 Q3-tax-deadline urgency line said "about a month out" as of that
date. Today it's 20 days out (about 3 weeks) — a stale-but-still-true-ish
claim is exactly the kind of small inaccuracy that erodes buyer trust the
08-06 review-mining research flagged as the top real complaint category.
Refreshed the wording in `products/freelancer-tax-tracker-v1/LISTING.md`,
`products/freelancer-bundle-v1/LISTING.md`, and
`products/OUTREACH-KIT.md` section 7 to say "about 3 weeks (20 days) out,"
and added an explicit note that this specific lever expires entirely if
Jimmy hasn't acted by Sept 15 (the next real deadline after that is Q4
2026, 4 months out) — a genuine, time-bound reason today's inaction has a
real cost beyond "another day of $0," not manufactured pressure.

Also re-verified: all 8 listings' referenced deliverable/cover/preview file
paths still resolve correctly on disk after the 08-20 cover regeneration
(cross-checked every `.pdf`/`.xlsx`/`.png` filename named in each
LISTING.md against what's actually in each product's `dist/` folder — all
match, nothing missing or renamed). No pricing/cover/copy change beyond the
date-accuracy fix above, no new product, no Gumroad action taken. Honest
assessment: this is a small, real fix — not a new lever — because there
isn't a new lever left to pull that hasn't already been tried; the
business remains entirely bottlenecked on REQ-003/004 (owner must
check/revoke the Gumroad API token and publish).

## Gumroad's built-in affiliate program found (2026-08-27)
38 days into REQ-003/004 being open with $0.00 in sales, every prior
distribution effort (all 8 outreach-kit channels) shares one property never
questioned before: each one routes through Jimmy personally reaching people
he knows or posting into a community himself. Checked whether Gumroad has a
mechanism that doesn't depend on that, and it does: a free, built-in
Affiliates feature (Share tab → Affiliates on each product page) — either
inviting specific people at a commission Jimmy sets (roughly 1-75%), or
opting into Gumroad's own global affiliate marketplace where people already
looking for products to promote can pick ours up passively at ~10%, with no
outreach from us at all. Costs nothing to enable and only pays out of real
sales, so it doesn't touch the $50 budget — but setting a commission rate
gives away real future revenue, so per this project's own money rule it's a
recommendation on REQ-003 (suggested 30% for direct-recruited affiliates),
not something applied automatically. No pricing change, no new product, no
Gumroad action taken. Full reasoning and sources: products/MARKET-NOTES.md
(2026-08-27).

## Pinterest pin images built (2026-08-28)
39 days into REQ-003/004 being open with $0.00 in sales, checked whether the
Gumroad storefront is reachable yet before doing anything else — still
blocked by this environment's egress proxy on direct fetch, same result as
every attempt since 07-20, no new information there, and no request in
`requests/open_requests.json` has been resolved since REQ-001 on day 1.

Every listing-level lever (pricing 3x, buyer-trust fixes, urgency framing,
cover art twice plus the thumbnail-crop fix, Google Sheets verification,
Gumroad fee research, bundle-mechanism fix, affiliate-program research) has
already been pulled at least once. One concrete piece of real production
work had been fully specified since 2026-08-07 but never actually built:
the 3 Pinterest pin descriptions/titles in `products/OUTREACH-KIT.md`
section 5 explicitly flagged that their images still needed a resized,
2:3-ratio vertical version rather than the wrong-aspect-ratio Gumroad
covers, and deliberately deferred building them until REQ-006 (the
Pinterest account decision) resolved, so the work wouldn't be wasted if
Jimmy said no.

Built them anyway this run rather than leave them as a permanent "not
built" placeholder: they're pure local asset generation (Pillow, same
brand palette/mockup as the existing Gumroad covers), cost nothing, touch
no external account, and are useful regardless of which way REQ-006 goes —
if Jimmy declines Pinterest, nothing is lost; if he approves it, this is
one less step between his decision and actually posting. All 3 built at
the correct 1000x1500 (2:3) spec, short high-contrast overlay text per the
existing research (title/description stay as separate Pinterest metadata
fields, not baked into the image), visually reviewed for legibility. See
`marketing/pinterest-pins/dist/` and `marketing/pinterest-pins/scripts/build_pins.py`.
Updated the 3 pin entries in `products/OUTREACH-KIT.md` section 5 to point
at the built files instead of "not built this run."

No pricing/copy change to the 6 paid listings, no new product, no Gumroad
action taken. The real, unchanged bottleneck after 39 days remains
entirely REQ-003/004 (owner must check/revoke the Gumroad API token and
publish the 8 already-ready listings) — REQ-006 (Pinterest) is a separate,
lower-priority, non-blocking decision.

## Real PDF rendering bug found and fixed (2026-08-29)
40 days into REQ-003/004 being open with $0.00 in sales, no owner action
recorded since REQ-001 on day 1 (verified via `git log` authorship again).
Also found and fixed a real operational bug before starting today's product
work: yesterday's and the day before's commits (the Pinterest pins and the
affiliate-program research) existed only on a detached local HEAD —
`origin/main` on GitHub was still stuck two days behind, at the 08-26
commit. A prior run's activity log had claimed this exact problem was
already found and fixed on day 40, but that fix was never actually pushed,
so it didn't survive into this session. Fast-forwarded `main` to include
both orphaned commits and pushed, then verified with a live `git ls-remote
origin main` (not just local branch state, which is exactly what silently
failed last time) that GitHub actually has them now. Take-away for future
runs: always verify a push landed with `git ls-remote`, not just a `git
push` exit code or local `git log`.

Every listing-level lever tried in the last 40 days (pricing, copy, cover
art, urgency, outreach channels, bundling, fee/affiliate research) had
already been pulled at least once, most more than once — repeating any
would be manufactured busywork, not real work. Instead of another
positioning angle, ran a genuinely new kind of QA no prior run had done:
previous "sanity checks" only verified PDF page counts and .xlsx formula
correctness, never whether the PDFs actually render cleanly. Installed
`pymupdf`, rendered every page of all 4 paid guide PDFs to check every text
and image block's bounding box against its page boundary — a check that
catches real clipping/overflow, not just page-count drift.

Found a real, confirmed-by-rendering defect: page 4 of the Freelancer
Invoice & Late-Payment Toolkit guide (`products/freelancer-invoice-toolkit-v1/`)
had its "Choosing Payment Terms" table built from raw Python strings passed
directly into a reportlab `Table` instead of `Paragraph` flowables — reportlab
does not wrap plain strings inside table cells, so the "Meaning," "Best For,"
and "Risk" columns overflowed and rendered as illegible overlapping text
across the entire table (visually confirmed, not just a hunch — see the
before-image this run generated). This is the single highest-stakes table
in that guide, in the highest-priced individual listing after the bundles,
and would have been the first thing a paying buyer saw go wrong. Fixed
`build_pdf.py` to wrap every cell in a `Paragraph` with a proper table-cell
style and rebalanced the four column widths so the "Term" column doesn't
mid-word-wrap ("Milestone-Based" etc.). Regenerated the PDF, re-ran the
bounding-box scan (zero issues now) and visually re-rendered the page to
confirm — page count unchanged at 9. The other 3 paid PDFs' tables passed
the same scan clean, so no other file needed this fix. No pricing/cover/copy
change beyond the table fix itself, no new product, no Gumroad action taken.
The real, unchanged bottleneck after 40 days remains entirely REQ-003/004
(owner must check/revoke the Gumroad API token and publish the 8
already-ready listings).

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

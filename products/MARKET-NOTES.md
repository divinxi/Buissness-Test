# Market / Conversion Notes — 2026-07-20

Context: all 3 products are fully built (real PDF + xlsx + cover for each,
see each products/*/dist/) and none have a recorded sale yet
(finances/ledger.json balance: $0.00). Per the operating playbook, that
means this run's job is improving conversion/positioning, not building a
4th product. Findings below are from web research on Gumroad specifically
(see sources), not general marketing advice.

## The uncomfortable finding: Gumroad Discover won't find us on its own
Multiple sources agree the Discover marketplace ranks listings mainly by
**verified-purchase reviews** and **external traffic already pointing at
the listing** — not by tags/SEO alone, and not by just existing. One
source: "the algorithm rewards what people already find interesting... you
need to feed the system with real, discoverable content that lives outside
of Gumroad." Another: email marketing drives ~42% of digital-product sales
on Gumroad, vs. 23% social, 18% direct, 12% organic search combined.

**Implication for us:** listing quality (which is already good — see below)
is necessary but not sufficient. With zero email list and zero existing
audience, expect close to zero organic Discover traffic even after
publishing. This isn't a reason to not publish; it's a reason not to be
surprised by silence afterward, and a reason to think about a traffic
source (even a single relevant subreddit/forum post, or an owner post to
their own network) as a follow-up request once REQ-004 is resolved.

## Pricing check
Our prices ($17 / $17 / $19) sit at the low, impulse-buy end, which matches
the "quick individual purchase, no funnel" model we chose. Data point: the
"Design" template category on Gumroad averages ~$7,365/product in *total*
revenue, but that's dominated by high-volume/older listings with reviews
and traffic — not a same-day benchmark for a brand-new, zero-review
listing. No reason to change price; the risk right now is zero traffic, not
wrong price.

One tactic seen repeatedly: bundling. Products 2 (tax tracker) and 3
(invoice toolkit) already target the same freelancer buyer — LISTING.md for
both already note this. Once either gets a first sale, a $29 bundle of the
two (vs. $36 separately) is a low-effort next step — no new content, just a
new Gumroad listing bundling the same files.

## Listing copy: assessment
Read all three LISTING.md files against what's actually recommended
(specific benefit in the first line, concrete contents list, explicit
"what this is NOT" to pre-empt refund requests). All three already do this
well — Product 2 and 3 in particular each have a "what this is NOT" section
that most competing listings skip. No copy rewrite needed this run; the
copy is not the bottleneck. The traffic/audience question above is.

## Recommendation
Don't build a Product 4 yet. Once REQ-004 (Gumroad account audit) and
REQ-003 (cover art + publish) are resolved by the owner, the single highest
leverage next step is a real external traffic source for the first 1-2
sales (owner's own network, a relevant subreddit, etc.) — that's an
owner-side action, not something I can do myself, so it should become its
own request once Gumroad trust is re-established.

---
Sources:
- https://startupspells.com/p/gumroad-seo-ranking-factors
- https://medium.com/@andreiya/the-best-way-to-get-sales-from-gumroad-discover-b35c7ba06592
- https://insightraider.com/en/answers/what-digital-products-sell-best-on-gumroad
- https://conversionproplus.com/blog/gumroad-trends-2026-what-s-selling-right-now

## 2026-07-21 update: bundle listing prepared
REQ-002, REQ-003, and REQ-004 are all still open — no owner action recorded
since the notes above were written, so the situation hasn't changed:
0 sales, Gumroad trust unresolved, no external traffic source yet. Repeating
the same market research would add nothing.

Acted on this run's own recommendation instead: built the bundle idea from
the "Pricing check" section above into an actual ready-to-publish asset —
see products/freelancer-bundle-v1/LISTING.md and dist/cover.png. It's "The
Freelancer Money Bundle" (Product 2 + Product 3 together, $29 vs. $36
separately). No new PDF/xlsx content was written — it repackages the
existing 4 files from those two products, which is exactly the low-effort
move this file already identified as the next lever. This does NOT touch
Gumroad in any way (no API call, no draft created) — it's just copy and a
cover image sitting in the repo, ready for a five-minute manual paste-in
once REQ-003/REQ-004 are resolved.

Deliberately did not draft outbound traffic content (subreddit/forum posts,
etc.) this run — the "single highest leverage next step" identified above
depends on the products actually being live and trustworthy first, which
they aren't yet pending REQ-003/004. Drafting outreach copy for listings
that might still change felt premature; revisit once publish status moves.

## 2026-07-22 update: cover art was the one conversion lever nobody had
actually assessed
REQ-002/003/004 are still all open, ledger is still $0.00 — no owner action
recorded since the last run, so another repeat of the Discover-ranking /
pricing / copy research would add nothing new (already concluded above that
copy and pricing aren't the bottleneck).

Looked at what *was* still unexamined: all 4 existing covers (Products 1,
2, 3, and the bundle) turned out to be the exact same template with only
the words swapped — dark card, two lines of title, a subtitle, a row of
tag-chip pills. Functional, on-brand, legible — but literally text-only,
with no visual hook. On a Discover grid sitting next to other sellers'
thumbnails, four visually-identical-looking cards (differing only in which
words are on them) don't help a browsing buyer tell at a glance "PDF +
spreadsheet bundle" vs. just another text graphic, and give the whole
catalog a slightly generic/AI-generated look.

Fix: added a small drawn mockup (pure Pillow shapes — a rounded "PDF page"
with a colored header bar and text lines, overlapped by a "spreadsheet"
card with an actual grid and one highlighted cell in the brand accent
color) to the top-right of all 4 covers. No external images/assets, so it
regenerates deterministically like everything else in these scripts. This
directly visualizes what's actually in the box (a PDF guide + an Excel
workbook) rather than just decorating — same reasoning as the existing tag
chips, just visual instead of text.

Had to retune the Invoice Toolkit's tag-chip sizing (font 28→26, pad 22→18,
gap 16→12) since its 4-chip row (including the long "INVOICE TEMPLATE"
label) originally ran into the new mockup's left edge at full size — caught
this by rendering and visually inspecting the actual PNG, not just running
the script. All 4 dist/cover.png files regenerated from their updated
scripts/build_cover.py and re-inspected; no other collisions.

This is the same category of prep as the bundle listing from 2026-07-21:
doesn't touch Gumroad, ships as an update to files already sitting in the
repo, ready the moment REQ-003/004 clear. Genuinely new inventory (a 5th
product) was deliberately not built this run per the operating playbook's
"3+ products built, 0 sales → improve conversion, don't manufacture more"
rule.

## 2026-07-23 update: independent QA pass on the actual deliverable content
REQ-002/003/004 are all still open, ledger still $0.00 — no owner action
recorded since yesterday. Discover-ranking research, pricing, copy, and
cover art have all already been covered in the entries above and repeating
any of them would add nothing new. What hadn't been done since each
product's original build was an independent re-check of the actual shipped
files — every prior "sanity check" happened once, at creation time, by the
same run that wrote the content. So this run extracted and read the full
text of all 3 PDFs (installed pypdf/reportlab/openpyxl/Pillow fresh, no
lorem-ipsum/placeholder/TBD scan, page counts re-verified against the
figures quoted in business_plan.md and each LISTING.md: 13pg / 8pg / 8pg,
all correct) and audited every formula-bearing cell in all 3 xlsx files for
correct column/range references (spot-checked full fill-down ranges, not
just row 2).

Found one real bug: page 6 of the Invoice & Late-Payment Toolkit guide
(the 14-30-days-late reminder email) had a leftover editorial artifact —
"a late fee of [LATE FEE %] applies to overdue balances[/ will begin
accruing after this date]." That bracket was never meant to ship; it reads
as broken/half-finished text next to the guide's other placeholders (which
are all clean single fill-in tokens like [INVOICE #]). Fixed in
scripts/content.py to a single clean sentence ("...now applies to the
overdue balance.") and regenerated dist/*.pdf — page count unchanged at
8pg, rest of the page unaffected. This is exactly the kind of thing that
would look sloppy or trigger a refund request if it shipped to a paying
customer, so worth catching before REQ-003/004 clear rather than after.

No other issues found: the Tax Tracker guide's bracket-pattern scan came
back clean, the Prompt Playbook's flagged brackets were all legitimate
fill-in tokens (e.g. [PRODUCT/SERVICE], [WON/LOST]), and every xlsx formula
checked (Invoice Log status/overdue logic, Reminder Dashboard rollups, the
Quarterly Tax Estimator's SE-tax math, Expense Log's meals-50%-rule,
ROI Summary's SUMIFs) references the correct source column and range with
no off-by-one or stale references. Net conclusion: with the one fix above,
all 4 products' actual file content is genuinely sale-ready, independent of
the copy/pricing/cover work already done in prior entries.

## 2026-07-24 update: refund policy + FAQ added to all 4 listings
REQ-002/003/004 are all still open, ledger still $0.00 — no owner action
recorded since yesterday. Discover-ranking, pricing, cover art, and file-QA
have all already been covered in the entries above; this run looked for
what was still genuinely missing rather than repeating any of them.

Ran real web research (not from memory) on what actually moves conversion
for a brand-new, zero-review Gumroad listing specifically:
- A clear money-back guarantee "can double or triple conversion rates on
  digital products" and is described as the recommended default listing
  element (Fungies.io digital product refund policy guide).
- A complete Gumroad product page "should include a FAQ section with 5-7
  common buyer questions answered," addressing objections like format
  compatibility and refunds (Kupkaike, "Gumroad Product Page Best Practices
  in 2026").
- Gumroad itself lets sellers set their own refund policy, but chargebacks
  can still happen regardless, so a stated policy that heads off disputes
  before they become chargebacks is also a account-health lever, not just
  a conversion one (Gumroad Help Center, "What is Gumroad's refund
  policy?").

None of the 4 LISTING.md files had either element — "What this is NOT" and
tag lists existed, but no explicit refund terms and no FAQ. Added both to
all 4: a 30-day no-questions-asked money-back guarantee (consistent across
all 4, redeemed via Gumroad's own messaging — no separate support email
needed, so nothing new to set up or maintain), and a product-specific FAQ
(5-6 questions each) covering the objections most likely to stall a buyer
for each product specifically — e.g. Google Sheets compatibility, "is this
valid outside the US," "does this replace a CPA," "will these prompts get
stale as models change," "what if it doesn't fit my situation." Kept every
answer honest — e.g. the tax tracker FAQ explicitly says a 2027 refresh is
*planned*, not that buyers get a free upgrade, since that isn't a real
commitment yet.

This is copy-only — no Gumroad account action, no new PDF/xlsx content, no
new inventory. Genuinely new inventory (a 5th product) was again
deliberately not built this run, consistent with the "3+ products built,
0 sales → improve conversion, don't manufacture more" rule — this is the
first run in this thread of updates to add something to the listings
themselves rather than pricing/cover/QA around them.

---
Sources (2026-07-24 additions):
- https://fungies.io/digital-product-refund-policy-guide-2026/
- https://kupkaike.com/blog/gumroad-product-page-best-practices
- https://gumroad.com/help/article/51-what-is-gumroads-refund-policy

## 2026-07-26 update: added a cross-sell page to all 3 individual PDFs
REQ-002/003/004 are all still open, ledger still $0.00 — no owner action
recorded in 6 days now. Discover-ranking, pricing, cover art, file-QA, and
refund/FAQ copy have all been covered in the entries above; outreach copy
was drafted 2026-07-25 (see OUTREACH-KIT.md). What hadn't been touched yet:
the actual deliverable content never mentioned the other 3 products. A
buyer of just the Tax Tracker had zero way of learning the Invoice Toolkit,
Prompt Playbook, or Bundle existed unless they happened to browse the same
Gumroad storefront — a real gap given the bundle's whole rationale is that
Products 2 and 3 share a buyer.

Fix: added a "More From Ledger & Loop Digital" closing page to each of the
3 individual product PDFs (Tax Tracker, Invoice Toolkit, Prompt Playbook),
cross-promoting the other 2 products by name/price/one-line pitch, plus a
"Bundle tip" box on the two freelancer products pointing at the $29 bundle.
Deliberately did NOT hardcode a Gumroad URL (nothing is live yet, and a
dead/wrong link would look worse than no link) — the page instead says
"look for these on the same store page you downloaded this from," which
stays accurate however the storefront ends up organized. The bundle PDF
itself doesn't need this page since it already contains both toolkits.

This changed each guide's page count: Tax Tracker 8pg→9pg, Invoice Toolkit
8pg→9pg, Prompt Playbook 13pg→14pg. Regenerated all 3 PDFs, re-verified
page counts match the new figures, and re-ran the same bracket-artifact
scan from the 2026-07-23 QA pass on the regenerated files — clean (the one
match was the legitimate [WON/LOST] fill-in token, not a leftover
artifact). Updated the page counts in each product's LISTING.md,
business_plan.md, and the bundle's LISTING.md (which describes both
toolkits' contents). This is a real, permanent improvement to the
deliverable files themselves, not just listing copy — it survives however
the products eventually get sold (Gumroad, bundle, direct link, etc.) and
costs nothing to maintain going forward, unlike the outreach kit which
needs Jimmy to actually send it.

No new product built (5th idea, "Prompt Playbook Vol. 2," stays queued) —
consistent with "3+ products built, 0 sales → improve conversion, don't
manufacture more."

## 2026-07-27 update: built the lead magnet the "zero email list" finding called for
REQ-002/003/004 are all still open, ledger still $0.00 — no owner action
recorded in 7 days now. Every conversion lever inside the listings
themselves (pricing, copy, cover art, refund/FAQ, cross-sell pages, file
QA) has now been used across the last week of entries above, and repeating
any of them would add nothing. The one finding from the very first entry
(2026-07-20) that was identified but never acted on: ~42% of Gumroad sales
come from email/external traffic the seller brings, and this business has
zero email list. Outreach copy (OUTREACH-KIT.md, 07-25) covers personal
network and safe subreddits, but neither of those builds a durable,
repeatable channel the way an email list does.

Built marketing/lead-magnet-freelancer-quickstart/: a free 3-page PDF
("The Freelancer Money Admin Quick-Start") distilling the single
highest-value facts from both freelancer toolkits (the 2026 quarterly
deadlines, the tax-savings rule of thumb, the one invoice habit that most
reduces non-payment risk, a 5-question self-audit) with a closing CTA
naming both paid toolkits and the bundle. All content is a real excerpt of
already-verified figures from the two toolkits' own content.py files — no
new claims to verify. Regenerated and sanity-checked: 3 pages, no
lorem/filler, checkbox glyphs render correctly as plain "[ ]" (the first
build used a unicode checkbox character that Helvetica silently rendered
as a garbled "I" — caught by actually extracting and reading the PDF text,
not just running the build script).

This is deliberately NOT counted as a 5th product — it's free by design
and has no sellable purpose; it's a distribution asset, the same category
as cover art or listing copy. It also has nothing to distribute *through*
yet: filed REQ-005 asking the owner to set up any free email-capture
mechanism (a Google Form is enough to start) since that requires a new
external account this routine won't create on its own. Marked low
priority since nothing already built is blocked on it.

## 2026-07-28 update: built the next queued product instead of another
conversion pass
REQ-002/003/004/005 are all still open, ledger still $0.00 — no owner
action recorded in 8 days now on REQ-003/004 (the oldest, highest-priority
blockers). Every conversion lever inside the existing listings has now been
used at least once across the past 8 daily runs: pricing check, bundle
packaging, cover art (twice — including a mockup graphic), refund policy +
FAQ on all 4 listings, cross-sell pages in all 3 individual PDFs, an
independent file-content QA pass, a draft outreach kit, and a free lead
magnet. Repeating any of these today would mean writing a new paragraph
that reaches the same "nothing changed, still blocked" conclusion, not real
work.

So this run switched to the other applicable rule: with everything publish-
related blocked purely on owner action, and no fresh conversion lever left
to pull, the highest-value use of the run is making sure there's more ready
to go the moment REQ-003/004 clear. Built the next item in the idea queue
end-to-end: **AI Prompt Playbook Vol. 2: Systems & Automation** — see
products/prompt-playbook-vol2-v1/. Deliberately scoped to NOT overlap with
Vol. 1's one-off-task categories (Marketing, Support, Finance, HR, Sales):
Vol. 2 covers building persistent AI systems, customer lifecycle
automation, competitive intelligence, ops reporting, and delegation —
recurring habits rather than one-off asks. Same 25-prompts/5-categories/
14-page format as Vol. 1 for brand consistency, same $17 price point (no
data yet to justify pricing it differently), and the companion tracker
(Automation-ROI-Tracker.xlsx) is genuinely different from Vol. 1's — it
converts logged workflows into monthly/annual value based on how often they
actually recur (Daily/Weekly/Monthly/Quarterly), which is the right
calculation for prompts meant to be reused on a schedule rather than a flat
per-use time log.

QA'd the same way the 2026-07-23 pass did: extracted and read the full PDF
text (14 pages, confirmed against the LISTING.md and business_plan.md
figures), scanned for lorem/filler/leftover-editorial-bracket artifacts
(none — all 46 bracket tokens are legitimate fill-in placeholders),
verified all 5 category headers render on their own pages, and checked
every ROI Summary formula (SUMIF category breakdown, VLOOKUP frequency
multiplier, SUM/COUNTA totals) references the correct sheet and range. Cover
art needed one fix after actually rendering and viewing it: the 5-chip tag
row ran off the right edge of the canvas at the original font size —
switched to a two-row chip layout rather than just shrinking text further,
caught by looking at the PNG, not by re-running the script and assuming it
was fine.

This is real new inventory, which the last 8 entries all deliberately
avoided building — that was the right call while conversion levers still
existed to pull; it stopped being the right call once they ran out. Product
count is now 5 (4 individual + the bundle), still 0 sales.

## 2026-07-29 update: fixed a stale cross-sell gap Vol. 2 created

REQ-002/003/004/005 are all still open, ledger still $0.00 — no owner
action recorded in 9 days now on REQ-003/004. Per the operating rule (3+
products built, 0 sales → improve conversion, don't manufacture a 6th
product), looked for what was genuinely unexamined rather than repeating
any prior entry.

Found one: building AI Prompt Playbook Vol. 2 yesterday (2026-07-28) quietly
broke a promise the other 3 individual PDFs make. Vol. 2's own cross-sell
page correctly lists all 4 other products, but the "More From Ledger & Loop
Digital" closing pages in the Prompt Playbook v1, Tax Tracker, and Invoice
Toolkit PDFs still said "two more toolkits" and only named each other —
Vol. 2 didn't exist when those pages were written (2026-07-26), so it was
invisible to a buyer of any of the 3 older products. Given the bundle's own
rationale is cross-product awareness, this was a real, live gap, not a
hypothetical one.

Fix: added a Vol. 2 entry (title, price, one-line pitch) to all 3 older
products' cross-sell pages and updated "two more toolkits/cover" → "three
more toolkits/cover the other sides" to match. Regenerated all 3 PDFs.
Page counts unchanged (14pg / 9pg / 9pg — the new paragraph fit on the
existing cross-sell page in all 3 cases, confirmed by re-extracting and
counting pages, not assumed). Re-ran the same bracket/lorem artifact scan
used since 2026-07-23: all bracket matches in all 3 files are legitimate
fill-in tokens ([BUSINESS NAME], [INVOICE #], [WON/LOST], etc.), no
lorem/filler, and all 3 files now contain "Vol. 2" in their extracted text
where they previously didn't. No LISTING.md or business_plan.md changes
needed — page counts didn't move.

Did not touch pricing, cover art, refund/FAQ copy, or the bundle listing
this run (all already covered by prior entries and none were stale). Did
not build a 6th product — the gap above was the higher-leverage, more
overdue fix, and per the "quality over volume" operating principle a real
consistency bug beats new inventory nobody can buy yet anyway.

## 2026-07-30 update: applied the validated bundling tactic to the prompt-playbook line

REQ-002/003/004/005 are all still open, ledger still $0.00 — no owner
action recorded in 10 days now on REQ-003/004. 6 products already exist
(5 individual + 1 bundle), so per the "3+ built, 0 sales → improve
conversion, don't manufacture more" rule this run did not write a new PDF
of fresh content. But it also isn't a repeat of prior entries: bundling
Products 2+3 into "The Freelancer Money Bundle" (07-21) was explicitly
flagged in the very first market-research entry (07-20) as the
lowest-effort, most-repeated tactic for zero-review Gumroad listings, and
that lever had only ever been pulled once, on the freelancer line — it was
never applied to the AI Prompt Playbook line because Vol. 2 (which unlocked
it) didn't exist until 07-28.

Built products/prompt-playbook-bundle-v1/: "The AI Prompt Playbook Bundle"
(Vol. 1 + Vol. 2, $27 vs. $34 separately — the same ~20% discount ratio as
the freelancer bundle, for consistency across the catalog). No new PDF/xlsx
content — repackages the 4 existing, already-QA'd deliverable files.
Followed the freelancer-bundle-v1 pattern exactly: a LISTING.md (full
description, refund policy, FAQ, tags, file list) and a generated cover.png
(adapted the same Pillow-shapes approach, two overlapping PDF-page mockups
instead of a PDF+spreadsheet pair since a prompt bundle is 2 guides, not a
guide+workbook pairing) — rendered and visually inspected the PNG before
calling it done; no chip-row overflow or text collisions this time.

This is genuinely new work, not a duplicate of the 07-21 freelancer bundle
or any other prior entry, and it required zero new written content — the
same "low-effort, high-conviction" category as the original bundle. Did not
touch pricing, cover art, refund/FAQ copy, or cross-sell pages on the other
5 products this run (all already current, none stale). Product count is
now 6 (5 individual + 2 bundles), still 0 sales — the real bottleneck
remains REQ-003/004 (Gumroad trust) and REQ-005 (no distribution channel
yet), not anything inside the listings themselves.

## 2026-07-31 update: is the niche/positioning still right? (fresh research, not from memory)
REQ-002/003/004/005 are all still open with no owner action recorded in 11
days — ledger still $0.00. 6 products now exist (4 individual + 2 bundles)
plus a free lead magnet, and every prior entry in this file already covers
Discover ranking, pricing, copy, cover art, file QA, refund/FAQ, and
cross-sell pages. What hadn't been checked yet, per the operating
playbook's explicit instruction for "3+ built, 0 sold," was the harder
question underneath all of that: is "AI prompt playbook" / "freelancer
toolkit" still a sound niche to be selling into in 2026 at all, or has the
market moved past it while this business built inventory?

Ran real web searches (not from memory) on 2026 Gumroad/digital-product
market conditions:
- Generic "500 ChatGPT prompts" packs are explicitly called out as
  saturated and rated poorly in 2026; genuinely niche, outcome-driven
  prompt bundles for specific business workflows are still selling, and
  coding/developer-focused prompt packs are a growing, less-saturated
  subcategory commanding $20-99 (not our audience or angle).
- Broader Gumroad trend data: AI-integrated resources and productivity
  systems are a currently-strong category; "Writing & Publishing" has the
  highest revenue-per-product of any category with the least competition.
- Niche-saturation research specifically calls out "freelancer finance
  planners" and "freelancer business kits" as validated, still-open 2026
  niches — i.e. Products 2.1/2.2/2.3 (tax tracker, invoice toolkit,
  freelancer bundle) sit squarely in a niche independent research says is
  still good, not something I talked myself into.

**Honest assessment:** re-reading our own 3 AI Prompt Playbook listings
against the "generic vs. specific" line these sources draw, the actual
*content* already avoids the saturated bucket — prompts are organized by
concrete business function (Marketing, Support, Finance, Hiring, Sales /
Systems, Lifecycle, Intel, Reporting, Delegation), not a flat "500 prompts"
dump. But the **tags** on all 3 listings (ai prompts, chatgpt, templates,
prompt engineering) were generic enough to risk Gumroad/search grouping us
with the saturated, poorly-rated generic-pack bucket regardless of what's
actually inside. Fixed: retagged all 3 AI Prompt Playbook listings (v1,
Vol. 2, bundle) to specific-audience phrases (e.g. "ai prompts for small
business," "chatgpt prompts for business owners," "ai workflow templates")
instead of single generic buzzwords, so search/category placement matches
the actual positioning instead of undercutting it. No pricing change — our
$17-$29 range already sits inside the 2026-recommended $15-30 floor for
this format, and nothing in this research suggests our current prices are
the problem.

**Net conclusion:** no niche pivot needed, no new product line warranted.
The freelancer line's positioning is independently validated as strong; the
AI-prompt line's content was already fine but its tags were quietly
undercutting it, now fixed. This is real repositioning work grounded in
today's search results, not a repeat of the Discover-algorithm/pricing/copy
conclusions already reached in the entries above.

Sources:
- https://trustly-ai.com/blog/best-practices-selling-ai-prompt-packs-gumroad-2026
- https://greyjournal.net/hustle/how-to-sell-ai-prompts-2026/
- https://insightraider.com/en/answers/what-digital-products-sell-best-on-gumroad
- https://www.accio.com/business/gumroad-trends
- https://kupkaike.com/blog/7-untapped-digital-product-niches
- https://resellready.co/blogs/news/low-competition-digital-products-to-sell-2026-guide

## 2026-08-01 update: REQ-005's "new account" premise was wrong — and an independent QA re-check on Vol. 2 + both bundles
REQ-002/003/004/005 are all still open with no owner action recorded in 12
days — ledger still $0.00, 6 products (4 individual + 2 bundles) plus the
free lead magnet all still sitting unpublished. Every listing-level
conversion lever (pricing, bundling, cover art, refund/FAQ, cross-sell,
tags/niche) has been covered in the entries above; this run looked for
what genuinely hadn't been touched.

**Part 1 — independent QA on the two products never independently re-
checked.** The 2026-07-23 QA pass (extract PDF text, scan for filler/
leftover-bracket artifacts, verify every xlsx formula) only covered the 3
products that existed then. Vol. 2 (built 07-28) was only ever checked by
the same run that wrote it, and the two bundles (07-21, 07-30) were never
independently checked at all. Re-did the same pass today, from scratch:
extracted Vol. 2's full PDF text (confirmed 14 pages, all 26 bracket
matches are legitimate fill-in tokens, one is the guide's own "replace
anything in [BRACKETS]" explainer — not a leftover artifact), audited
every formula in Automation-ROI-Tracker.xlsx (VLOOKUP range G4:H8 and the
SUMIF category list both match the Workflow Log's data-validation dropdowns
exactly, no off-by-one), verified both bundle LISTING.md "files to upload"
paths still point at real files, and visually re-inspected all 3 covers
(Vol. 2 bundle, Freelancer bundle, Vol. 2 itself) for the overflow/collision
bugs caught in earlier entries. **Found nothing wrong** — this is a real,
independent confirmation, not just repeating the 07-23 write-up, but it's
also an honest "no news" finding: nothing needed fixing.

**Part 2 — the actual finding: REQ-005 doesn't need a new account.**
REQ-005 (open since 07-27) asked the owner to set up a brand-new email tool
(Mailchimp/Beehiiv/ConvertKit, or a Google Form) to distribute the free
lead-magnet PDF, since it had "nothing to distribute through yet." Never
independently checked whether that premise was even true. Ran real 2026 web
research on Gumroad's own features and found it isn't: Gumroad captures
every buyer's email at checkout automatically, including $0/pay-what-you-
want purchases (no payment method required, just an email), and its
built-in Workflows feature can send scheduled follow-up emails to anyone
who downloads something. In other words, a $0/PWYW Gumroad listing for the
lead magnet, on the account that already exists, *is* the email-capture
mechanism REQ-005 was asking for — no new external account needed at all.

Acted on this: wrote marketing/lead-magnet-freelancer-quickstart/LISTING.md
and generated dist/cover.png (same Pillow-mockup pattern as the other 6
covers, single-PDF variant since there's no companion xlsx), so the lead
magnet is now packaged exactly like the paid products — ready to list at
$0/PWYW the moment REQ-003/004 clear, alongside the other 6. Updated
REQ-005's scope in requests/open_requests.json to reflect this: it no
longer needs its own owner decision, it just rides along with REQ-003/004.
This directly shrinks what's being asked of the owner rather than adding to
the pile — the opposite of manufacturing more busywork.

Sources (2026-08-01):
- https://insightraider.com/en/answers/does-gumroad-let-you-offer-pay-what-you-want
- https://dodopayments.com/blogs/gumroad-review
- https://tekpon.com/software/gumroad/reviews/

## 2026-08-02 update: built real "look inside" preview images — a genuinely
untouched lever after 13 days of listing-level work
REQ-002/003/004/005 are all still open with no owner action recorded in 13
days — ledger still $0.00, 6 products (4 individual + 2 bundles) plus the
free lead magnet all still unpublished. Every previous entry in this file
covers Discover ranking, pricing, bundling, cover art, file QA, refund/FAQ,
cross-sell pages, and niche/positioning — repeating any of them would add
nothing. Looked specifically for what had never been touched.

Found one: every one of the 7 listings only has a single image — the
branded cover (title + subtitle + tag chips + an abstract PDF/spreadsheet
icon mockup). None show any actual content. Ran real 2026 web research (not
from memory) and confirmed this is a real, named gap: Gumroad supports 4-6
additional listing images beyond the cover, and product-page best-practice
guides (including Kupkaike's checklist, already a source in this file)
specifically recommend showing the real product — not just another graphic
— because professional preview images "convert measurably better than
amateur or generic covers." A buyer currently has zero way to see what's
actually in a $17-29 PDF+spreadsheet bundle before paying.

**Built it for all 4 individual products** (the bundles/lead magnet
deliberately reuse these rather than getting new art — see below): for each
product, `scripts/build_preview.py` generates 2 new PNGs into `dist/`:
1. `preview-1-inside-guide.png` — a real page from the guide: actual
   category/table headers and real body text pulled directly from that
   product's own `content.py` (prompt titles/snippets for the two Prompt
   Playbooks, the real 2026 quarterly deadline table + 3 Schedule C entries
   for the Tax Tracker, the real payment-terms-by-risk table for the
   Invoice Toolkit) — not another abstract mockup, and it can't drift out of
   sync with the PDF since it imports the same `content.py`.
2. `preview-2-inside-tracker.png` — a mockup of the real companion
   spreadsheet's actual column headers with realistic sample rows,
   highlighting each product's real auto-calculation hook (Tax Tracker's
   50%-meals-deduction auto-rule, Invoice Toolkit's auto Paid/Overdue/
   Upcoming flag) since that automation is the actual reason to buy the
   spreadsheet over a blank template.

Caught and fixed 3 real rendering bugs by actually rendering and viewing
every PNG, not just running the scripts and assuming they were fine (same
discipline as the 2026-07-22 and 07-28 cover-art entries): a trailing
category list ran off the canvas on the flagship Playbook's page image; the
first version of every spreadsheet mockup had column headers too wide for
their columns, causing "Time Saved (min)" and "Notes / Result" to visually
overlap; and the Invoice Toolkit's "50% Upfront / 50% on Delivery" term
label (unwrapped) overlapped the adjacent column's text. All fixed by
wrapping every text element to its actual column/box width instead of
assuming single-line fit, then re-rendered and re-inspected each of the 8
final PNGs individually.

Updated all 4 products' LISTING.md with a new "Preview images" section
(what to upload, in order, after the cover). The 2 bundles and the lead
magnet were deliberately **not** given their own new preview art — per the
same "no new content, repackage what exists" logic already used for their
file lists, their LISTING.md now just point at the relevant component
product's existing preview images (e.g. the Freelancer Bundle reuses all 4
Tax Tracker + Invoice Toolkit previews). This is real, permanent listing
material — like the cross-sell pages, it survives however the storefront
ends up organized and costs nothing to maintain, ready the moment
REQ-003/004 clear.

Did not touch pricing, bundling, refund/FAQ copy, cross-sell pages, or
niche/positioning this run — all already current per prior entries. Did not
build a new product — 6 products (4 individual + 2 bundles) plus the lead
magnet is already well past the "3+ built" threshold with 0 sales, so this
stayed a conversion-lever run per the operating rule.

Sources (2026-08-02):
- https://kupkaike.com/blog/gumroad-product-page-best-practices
- https://help.gumroad.com/article/149-adding-a-product

## 2026-08-03 update: expanded the outreach kit to 2 channels never covered — Indie Hackers and LinkedIn
REQ-002/003/004/005 are all still open with no owner action recorded in 14
days — ledger still $0.00, 6 products + the lead magnet all still
unpublished. Every listing-level lever (pricing, copy, cover art, refund/
FAQ, cross-sell, retagging, preview images) has been used at least once;
repeating any of them would add nothing. products/OUTREACH-KIT.md itself
had also gone untouched since 2026-07-25 (day 5) and only covered 2
channels: a personal-network message and Reddit. Looked for real,
previously-untouched distribution channels rather than repeating the
listing-polish pattern again.

Ran fresh 2026 research (not from memory) on two candidates:
- **Indie Hackers** turns out to be two different things people conflate.
  The subreddit (r/indiehackers) permits one Show IH-flaired post per
  product, explicitly framed as a feedback ask (not an ad) — same
  low-friction shape as r/IMadeThis/r/shamelessplug already in the kit, and
  its no-fake-MRR-claims rule costs us nothing since the honest number is
  $0.00 anyway. The actual indiehackers.com site is a different, higher-
  friction channel — it expects an established, contributing member with a
  real founder story, not a same-day drop-a-link post, so no draft was
  written for it; flagged honestly as a time-investment decision for Jimmy,
  not something pre-buildable.
- **LinkedIn** operates on a documented 4-1-1 rule (4 value posts per 1
  self-promotional post) and ranks problem-first posts (lead with the pain
  point, reveal the product second) better than product-first ones. Also
  found and applied a platform-specific detail: LinkedIn's algorithm
  downranks posts with an outbound link in the body text, so the draft
  puts the Gumroad link in "comments/DM" instead, unlike the Reddit/IH
  drafts where an inline link is normal and expected.

Added both as new sections in products/OUTREACH-KIT.md with ready-to-send
drafts (Show IH post, LinkedIn post) — same posture as everything else in
that file: **drafts only**, nothing posted or sent, Jimmy sends them
himself from his own accounts whenever he chooses, independent of when
REQ-003/004 clear (these don't need the Gumroad link to be live first,
unlike the personal-network message).

Also spot-checked all 7 "Product name" fields against this week's Gumroad-
title-SEO research (recommended format: benefit + product type + niche,
e.g. "Instagram Post Templates for Bakers") before deciding whether to
rewrite them. They already comply — e.g. "The Freelancer Invoice &
Late-Payment Toolkit" = niche (freelancer) + benefit (invoice & late-
payment) + type (toolkit) — so left them as-is rather than making a
cosmetic change with no real gap behind it.

Did not build a new product or touch pricing/cover art/refund copy — same
"3+ built, 0 sales → improve conversion/distribution, don't manufacture
more" rule as every run since 2026-07-24.

Sources (2026-08-03):
- https://www.indiehackers.com/post/hacking-reddit-how-to-self-promote-without-getting-banned-753396554b
- https://gofindevo.com/subreddits/indiehackers
- https://www.indiehackers.com/post/any-requirements-for-posting-a108d65954
- https://lagrowthmachine.com/linkedin-marketing-strategy-2026/
- https://blog.annabyang.com/make-linkedin-less-cringe/
- https://postiv.ai/blog/best-practices-for-posting-on-linkedin
- https://www.seotakeoff.com/blog/gumroad-seo-guide

## 2026-08-04 update: a concrete launch-discount / first-reviews plan — the
one piece the day-1 finding never turned into an actual artifact
REQ-002/003/004/005 are all still open with no owner action recorded in 15
days — ledger still $0.00, 7 products (6 built + the lead magnet) all still
unpublished. Every listing-level lever (pricing, copy, cover art, refund/
FAQ, cross-sell, retagging, preview images) and two rounds of outreach-kit
channels (personal message, Reddit x2, Show IH, LinkedIn) have already been
covered. Went back to the very first entry in this file (2026-07-20) for
something identified but never finished: Gumroad Discover ranks mainly on
**verified-purchase reviews** and **momentum**, and with 0 products live
there are 0 reviews to rank on — a classic cold-start problem. Nothing in
the 15 days since has actually built a plan to solve that specific problem;
the outreach kit gets people to the listing, but nobody had planned what
happens to convert that first trickle of visits into reviews.

Ran fresh 2026 research (not from memory) specifically on this:
- Multiple sources agree: launch-day/limited pricing is a standard lever
  sellers use to drive initial sales, and getting the first ~10 reviews "at
  any cost" (via discounts and direct personal asks, not fake reviews) is
  recommended specifically to beat the cold-start problem — Gumroad
  "promotes products with momentum," so early reviews/sales are what let the
  algorithm start surfacing a listing organically.
- This is the same mechanism as a referral-style discount, not an
  incentivized-review scheme: the ask is "buy at a discount," the review
  itself stays unprompted and honest — no source suggested or implied paying
  for a positive review, and that's a hard line this plan keeps too (see
  below).

**Concrete plan (copy-ready, not yet actioned — still just prep like every
other artifact in this repo):**
- A single, memorable launch code — **`LAUNCH25`**, 25% off — recommended on
  all 7 listings for consistency (one code Jimmy can mention once rather
  than 7 different ones).
- Capped at **10 redemptions per listing** (Gumroad supports a max-uses
  limit per discount code) rather than a time window — this naturally
  expires the offer once its job (seeding the first ~10 reviews per
  listing) is done, with no date to remember to revoke.
- Paired with the *existing* personal-network message (OUTREACH-KIT.md #1)
  — updated below to mention the code and make an explicit, honest ask to
  leave a review after trying it. Not paired with the Reddit/Show IH/
  LinkedIn drafts: those are feedback-framed posts to strangers, and
  attaching a "buy at a discount" hook to a cold audience reads as
  incentivized promotion in a way it doesn't when it's Jimmy's own contacts
  he already has a relationship with — kept the two channels separate on
  purpose.

This is internal guidance for when Jimmy sets up each listing, not a change
to any public-facing LISTING.md copy — added a note to REQ-003 in
requests/open_requests.json so it rides along with the cover-art/publish
step rather than becoming a new request (setting a discount code needs no
new account or money, same bucket as the cover-art upload already in that
request).

Did not touch pricing, cover art, refund/FAQ copy, cross-sell pages, or
build a new product this run — 7 products (6 + lead magnet) is already well
past the "3+ built, 0 sales" threshold, and this is real, previously-unbuilt
distribution/conversion work, not a repeat of any prior entry.

Sources (2026-08-04):
- https://insightraider.com/en/blog/how-to-sell-digital-products-gumroad
- https://medium.com/write-a-catalyst/5-ways-to-find-your-audience-on-gumroad-without-bringing-your-own-traffic-2dd5fcb3e07d
- https://www.quora.com/How-do-I-get-the-first-sale-on-Gumroad
- https://www.stephanochmann.de/en/blog/gumroad-discounts/

## 2026-08-05 update: pricing checked against real comparable listings, not
just generic advice — and 3 of 7 prices changed as a result

REQ-002/003/004/005 are all still open with no owner action recorded in 16
days now — ledger still $0.00, 7 products (6 built + the lead magnet) all
still unpublished. Every listing-level lever (pricing, copy, cover art,
refund/FAQ, cross-sell, retagging, preview images) and both outreach
channels have been covered in the entries above. The 2026-07-31 entry
concluded "no pricing change" needed, but on rereading it, that conclusion
rested entirely on generic "recommended range" claims ($15-30, $15-19) from
blog posts about the market in general — it never actually looked at what
specific, comparable products charge on Gumroad today. That's a real gap:
this business has been treating "inside the recommended range" as proof of
correct pricing for 16 days without ever checking a single real listing.

Ran real 2026 web searches for actual comparable Gumroad products (not from
memory, not aggregator blog summaries) and found concrete price points:
- A "200+ AI Prompts for NYC Small Businesses 2026" pack — less curated
  than ours (a flat 200+ dump vs. our function-organized 25-per-volume
  structure) — sells a Basic tier at $27 and a Complete tier at $47.
  Broader research confirms specific, outcome-driven business prompt packs
  commonly run $27-47, with full bundles at $29-69.
- "Invoice Reminder Pro," a Google Sheets-only product (just automated
  reminder emails, no guide) sells for $29. Our Invoice & Late-Payment
  Toolkit includes a full 9-page guide (payment terms, late fees, escalation
  path) *and* a 4-tab tracker with the same auto-flagging behavior, for
  less than that Sheets-only product alone.
- Could not get a clean comparable price for freelancer tax/income trackers
  specifically (Gumroad product pages 403'd on direct fetch, same issue
  noted in the very first 2026-07-20 entry) — search snippets described
  feature sets but not confirmed prices for that category. Left Product 2.1
  (tax tracker) unchanged rather than guess.

**Net conclusion:** Products 1.1 (Prompt Playbook), 1.2 (Vol. 2), and 2.2
(Invoice Toolkit) were priced $17 against real comparables charging
$27-47 and $29 respectively for less-differentiated or less complete
products — genuinely underpriced, not just "in range." Raised all three to
$19 (matching Product 2.1's existing tier, so every individual product is
now a flat $19 — simpler to state in any outreach copy too). Raised both
bundles (AI Prompt Playbook Bundle, Freelancer Money Bundle) from
$27/$29 to $29/$29 so the "buy separately vs. bundle" discount math still
holds and actually grew (from ~19-21% off to ~24% off) rather than shrinking
as the singles got more expensive. Product 2.1 (tax tracker) was left at
$19 — no comparable evidence found either way.

This is a real, evidence-based price change, not a repeat of the
07-20/07-31 conclusions (which were both "no change" based on range-level
advice, not comparable-level data) and not a guess — regenerated all 4
affected products' PDFs (their cross-sell pages reference each other's
price), both bundle covers, and the lead magnet's PDF (its closing page
also names a price), re-verified page counts unchanged (14/14/9/9/3) via
PyMuPDF text extraction (pypdf itself is broken in this environment — a
missing `_cffi_backend` module breaks its crypto provider on import; used
PyMuPDF instead), and re-inspected both regenerated bundle cover PNGs for
overflow (none — the new price strings are the same character length as
the old ones). Updated all 5 affected LISTING.md files, business_plan.md,
and OUTREACH-KIT.md's draft prices to match.

Sources (2026-08-05):
- https://gnaglobal.gumroad.com/l/ai-prompts-nyc-2026 (via search snippet —
  direct fetch 403's, same as every other Gumroad product page)
- https://trustly-ai.com/blog/best-practices-selling-ai-prompt-packs-gumroad-2026
- General search results for "gumroad top selling AI prompts pack for small
  business 2026 price" and "gumroad invoice toolkit late payment reminder
  templates price $" (2026-08-05 web searches)

## 2026-08-06 update: mined real buyer complaints about digital products,
not just seller-side pricing/SEO advice — 2 genuine gaps found and fixed

REQ-002/003/004/005 are all still open with no owner action recorded in 17
days now — ledger still $0.00, 7 products (6 + lead magnet) all still
unpublished. Every prior research pass looked at this from the seller's
side (pricing, tags, titles, discount mechanics). Never once looked at it
from the buyer's side: what do people who actually buy Gumroad digital
products — prompt packs and templates specifically — complain about after
the purchase? That's a different, more direct signal for what our own
listings might be missing.

Ran real 2026 web searches (not from memory) on Gumroad buyer complaints
and negative reviews, specifically for AI prompt packs and for the platform
generally:
- A well-documented pack (15-40 prompts) from a niche creator reportedly
  outperforms a bloated 500-prompt dump — buyers want depth per prompt, not
  raw count. This validates, doesn't change, our existing structure (25
  prompts per volume, organized by function) — noted here as confirmation,
  no copy change needed since we already don't have this problem.
- Real, actionable gap: buyers of prompt packs specifically say they expect
  "clear use cases, example outputs, compatibility notes and update
  history" before buying — and our listings had "when to use it" and an
  adaptation tip, but never actually showed a filled-in example with a
  sample output. That's exactly the kind of proof-of-quality a generic,
  unvetted competitor pack can't fake.
- Separate, platform-wide gap: Gumroad's own Trustpilot rating skews
  heavily negative (1.4/5, 83% one-star), and the single most common theme
  across complaints is non-delivery or a seller who never responds to a
  problem — not bad content, an absence of any response at all. Our 30-day
  refund policy addresses the outcome (get your money back) but never
  addressed the buyer's actual fear at the point of decision (will anyone
  even answer if something's wrong).

**Fixes made (copy-only, no new product, no Gumroad action):**
- Added a concrete "See one in action" example to both AI Prompt Playbook
  listings (v1 and Vol. 2) — a real prompt from each product's own
  content.py, filled in with a fictional example input and a plausible
  sample output, clearly labeled illustrative (output varies by model/
  inputs, not a fixed script). Freelancer line and lead magnet weren't
  changed here since spreadsheet/guide-driven products are already easy to
  preview via the existing "look inside" screenshots — the example-output
  gap is specific to prompt packs, where the buyer's real question is
  "what do I actually get back," not "what's the format."
- Added one new FAQ line to all 6 paid listings (both Prompt Playbook
  volumes, both bundles, both freelancer toolkits): "What if my download is
  missing or something's broken?" — a concrete response-time commitment
  (real reply within 48 hours, not a bot) that routes straight to the
  existing refund policy if unresolved. Not added to the free lead magnet
  — no money at risk on a $0 listing, so the fear this addresses doesn't
  really apply there.
- Did not touch pricing, tags, titles, cover art, or bundle structure —
  those levers were evidence-checked as recently as yesterday (08-05) and
  the week before; this run found a genuinely different lever (post-
  purchase trust/proof, not pre-purchase pricing/discovery) that nothing
  since day 1 had actually looked at.

Sources (2026-08-06):
- https://ilmilog.com/best-ai-prompt-packs-in-2026/
- https://trustly-ai.com/blog/best-practices-selling-ai-prompt-packs-gumroad-2026
- https://www.trustpilot.com/review/gumroad.com
- https://gumroad.pissedconsumer.com/review.html
- https://cartmango.com/gumroad-scam/

## 2026-08-07 update: found a genuinely new distribution channel — Pinterest — and why it's structurally different from every channel drafted so far

REQ-002/003/004/005 are all still open with no owner action recorded in 18
days now — ledger still $0.00, 7 products (6 + lead magnet) all still
unpublished. Every listing-level lever (pricing, copy, cover art, refund/
FAQ, cross-sell, retagging, preview images, buyer-trust gaps) and two rounds
of outreach-kit channels (personal message, Reddit x2, Show IH, LinkedIn)
have already been covered — repeating any of them would add nothing.
Instead of another pass over the listings themselves, looked at whether the
outreach kit was missing a *structurally different* channel, not just
another community to post the same kind of link into.

It was. Every channel drafted so far (personal message, Reddit, Show IH,
LinkedIn) is attention/community-first: someone has to already be scrolling
that feed and stop for a cold post. Real 2026 research on what's actually
selling on Gumroad right now independently named Pinterest as "the
strongest fit for digital products" specifically — 450M monthly users, and
critically, they're there in a *search/planning* mindset (looking for
templates, planners, trackers), not a passive-scroll one. That's a better
structural match for a tax tracker / invoice tracker / prompt playbook than
any channel already drafted, and multiple independent sources named budget/
expense-tracker and "planner/template" products specifically as strong
Pinterest categories. A second, separate finding: Pinterest is one of the
few platforms where a direct link from the post straight to the product
page is normal and expected, not something that reads as spammy the way it
does on Reddit/LinkedIn.

**The catch, and why this became a request instead of just more drafted
copy:** unlike Reddit/LinkedIn/Indie Hackers (which only assume Jimmy
already has a personal account), Pinterest realistically needs a **new**
Business account to be worth doing properly (free, no monthly fee, no
commission — confirmed via a dedicated 2026 source on Pinterest Business
account costs — but still a new external account). This project's own rule
says any new external account goes through the request queue, not straight
into a "drafts only" file the way the other 4 channels did. Filed
**REQ-006** (low priority — this is a new opportunity, not something already
built and blocked) and put the actual ready-to-use pin drafts (3 pins:
title, description, suggested board, per Pinterest's real 2026 spec — 2:3
vertical, 1000×1500px, 100-char title/500-char description limits) in
products/OUTREACH-KIT.md section 5, so nothing has to be written from
scratch if/when Jimmy says yes.

Deliberately did NOT also draft TikTok/Instagram Reels content this run,
even though the same research calls short-form video a real, currently-
strong channel for this same product category — video needs actual
production (script, recording, editing), a materially bigger lift than a
pin image + text, and drafting it properly today would have meant two
half-finished channels instead of one properly-researched one. Noted in
OUTREACH-KIT.md as a candidate for a dedicated future run, not lost, but not
built today either — consistent with "quality over volume."

Also note: two of the most Pinterest-specific source pages (madetospark.com,
84pins.com) were blocked by this environment's network egress proxy on
direct fetch, so their content is relayed via search-result snippets only,
not independently read in full — flagging this the same way the 2026-07-20
and 2026-08-05 entries flagged Gumroad's own 403s on direct fetch, so this
isn't presented as more rigorously sourced than it actually is.

Sources (2026-08-07):
- https://medium.com/write-a-catalyst/how-to-get-free-traffic-to-your-digital-products-the-2026-no-ad-blueprint-for-gumroad-beyond-4556ca82e669
- https://84pins.com/sell-digital-products-on-pinterest/ (via search snippet — direct fetch blocked by egress proxy)
- https://madetospark.com/pinterest-for-gumroad (via search snippet — direct fetch blocked by egress proxy)
- https://www.panstag.com/2026/06/pinterest-traffic-digital-products.html
- https://84pins.com/pinterest-business-account-cost/
- https://recurpost.com/blog/pinterest-pin-dimensions/
- https://business.pinterest.com/creative-best-practices/
- https://whop.com/blog/best-digital-products-to-sell/ (TikTok/Reels + planner/spreadsheet demand confirmation)

## 2026-08-08 update: wrote the actual email copy the lead magnet's own distribution mechanism was missing

REQ-002/003/004/005/006 are all still open with no owner action recorded in
19 days now on REQ-003/004 — ledger still $0.00, 7 products (6 + lead
magnet) all still unpublished. Every listing-level lever (pricing, copy,
cover art, refund/FAQ, cross-sell, retagging, preview images, buyer-trust
gaps) and all 5 outreach channels (personal message, Reddit x2, Show IH,
LinkedIn, Pinterest) have already been covered — repeating any of them
would add nothing. Instead of another new channel or another polish pass,
went back through every prior entry in this file looking for something
identified but never finished, the same method that found the REQ-005
premise gap on 08-01.

Found one: the 2026-08-01 entry established that Gumroad's Workflows
feature can send scheduled follow-up emails to anyone who downloads the
free lead magnet, and used that finding to close REQ-005 (no new
email-capture account needed). That closed the "which tool" question but
never produced the one thing a Workflow actually needs to do anything —
the email copy itself. 7 days of runs since then (08-02 through 08-07)
built preview images, buyer-trust fixes, and 2 more outreach channels
without ever circling back to write it. Day 1's own finding (~42% of
Gumroad sales come from email/external traffic the seller brings) has
technically been "addressed" by the lead magnet's existence since 07-27,
but a downloaded PDF with no follow-up doesn't actually capture any of that
42% — it just collects an address and goes quiet.

**Built:** `marketing/lead-magnet-freelancer-quickstart/EMAIL-SEQUENCE.md`
— a 3-email Gumroad Workflows sequence (Day 0 delivery + soft mention, Day
3 a genuinely new tax tip that bridges into the Tax Tracker, Day 7 the same
pattern for the Invoice Toolkit plus the plain $29-vs-$38 bundle math).
Deliberately excluded LAUNCH25 from this sequence: that code was scoped on
2026-08-04 specifically to Jimmy's personal-network message, where a
10-redemption cap makes sense against people he already knows — an
automated sequence firing on every anonymous $0 download could exhaust that
same cap on strangers before it ever reaches his own contacts, so this
sequence sells on value/relevance instead, with a note that a separate,
uncapped-differently code could be considered later once there's any signal
on how this list actually responds (there's currently none — 0 emails sent).

Referenced from `marketing/lead-magnet-freelancer-quickstart/LISTING.md` so
it's discoverable alongside the listing copy it supports. This is copy
only — no Gumroad Workflow created, no email sent to anyone, no account
touched. Did not touch pricing, cover art, an outreach channel, or build a
new product this run — 7 products + a lead magnet is well past the "3+
built, 0 sales" threshold, and this closes a real, previously-identified
gap rather than repeating any prior entry's conclusion.

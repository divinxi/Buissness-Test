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

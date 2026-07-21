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

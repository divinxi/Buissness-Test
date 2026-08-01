# Lead magnet: "The Freelancer Money Admin Quick-Start"

Free 3-page PDF (see `dist/`). Built 2026-07-27 to address the specific gap
`products/MARKET-NOTES.md` (2026-07-20) identified: Gumroad Discover barely
surfaces new, zero-review listings, and ~42% of digital-product sales on
Gumroad come from email/external traffic the seller brings themselves — but
this business has zero email list and zero external audience.

## What it is
A distilled excerpt of the two existing freelancer toolkits' single highest-
value facts (the 2026 quarterly tax deadlines, the tax-savings rule of
thumb, the one invoice habit that most reduces non-payment risk, and a
5-question self-audit checklist), ending with a CTA naming the two paid
toolkits and the bundle. Real content pulled from
`products/freelancer-tax-tracker-v1/scripts/content.py` and
`products/freelancer-invoice-toolkit-v1/scripts/content.py` — nothing new to
verify, no fabricated figures.

## Why this isn't "product #5"
This is not a new sellable item — it's free by design, meant to be given
away in exchange for an email address (or just shared) to start building
the exact audience/traffic channel MARKET-NOTES.md flagged as the real
bottleneck. It doesn't count toward the "3+ products, 0 sales → stop
manufacturing" rule because it isn't inventory; it's a distribution asset,
same category as better cover art or listing copy.

## Update 2026-08-01: this doesn't need a new account after all
REQ-005 originally asked the owner to set up a brand-new email-capture
account (Mailchimp/Beehiiv/ConvertKit, or a Google Form) since this PDF had
nothing to distribute through. Research this run found that's unnecessary:
Gumroad itself captures every buyer's email at checkout — including
$0/pay-what-you-want purchases, which need an email but no payment method —
and its built-in Workflows feature can send a scheduled follow-up email to
anyone who downloads something, pointing at the paid toolkits. So this PDF
now has a `LISTING.md` (and a generated `dist/cover.png`) just like the 6
paid products: a $0/PWYW Gumroad listing, on the account that already
exists. See `products/MARKET-NOTES.md` (2026-08-01) for sources and
`requests/open_requests.json` REQ-005 for the updated scope — it's now the
same "needs Gumroad trust restored" blocker as everything else (REQ-003/004),
not a separate new-account decision.

## Rebuilding
`python3 scripts/build_pdf.py` regenerates `dist/Freelancer-Money-Admin-Quick-Start.pdf`
from `scripts/content.py`. `python3 scripts/build_cover.py` regenerates
`dist/cover.png`.

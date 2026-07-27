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

## What's still needed (owner action — see REQ-005)
This PDF has nothing to distribute *through* yet: no email capture
mechanism exists (Mailchimp/Beehiiv/ConvertKit account, or even a plain
Google Form) and setting one up is a new external account, which this
routine cannot do on its own. See `requests/open_requests.json` REQ-005.
Once that exists, the actual distribution (attaching this PDF to a signup
form, or offering it in the outreach messages in
`products/OUTREACH-KIT.md`) is a five-minute step for the owner.

## Rebuilding
`python3 scripts/build_pdf.py` regenerates `dist/Freelancer-Money-Admin-Quick-Start.pdf`
from `scripts/content.py`. No xlsx or cover image — this isn't a Gumroad
listing, just a giveaway PDF.

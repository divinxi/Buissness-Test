# Gumroad Workflows follow-up sequence — for the free lead magnet

**Status: drafted, not configured anywhere. No Gumroad account action taken.**

## Why this was missing
The 2026-08-01 finding in `products/MARKET-NOTES.md` established that
Gumroad's built-in Workflows feature can send scheduled follow-up emails to
anyone who downloads the free lead magnet, and that this — not a new
Mailchimp/ConvertKit account — is the real mechanism behind REQ-005. That
finding closed the "what tool do we use" question but never produced the one
thing Workflows actually needs to be useful: the emails themselves. Since
then, 7 days of runs (08-02 through 08-07) worked through every remaining
listing-level and outreach-channel lever without circling back to this gap.
Day 1's own research already flagged why it matters: ~42% of Gumroad sales
come from email/external traffic the seller brings, not organic Discover
traffic — a downloaded-but-never-followed-up-with lead magnet doesn't
capture any of that, it just captures an email address and stops.

This is the same category of prep as OUTREACH-KIT.md: copy only, nothing
sent, nothing configured in Gumroad. Jimmy pastes these into a Workflow
(trigger: "Free Freelancer Money Admin Quick-Start" purchase, i.e. every
$0/PWYW download) once REQ-003/004 clear and the lead magnet is listed.

## Sequence design
3 emails, spaced by real elapsed time so each one has a reason to exist
rather than being a disguised discount blast:

1. **Immediate (0 days)** — deliver + earn trust. No pitch beyond a single
   soft mention at the very end. A hard sell on email #1 is the fastest way
   to make someone regret giving you their address.
2. **Day 3** — a genuinely new, specific tip not in the PDF (so it's not a
   repackaged ad), then a natural bridge into the Tax Tracker — the freebie's
   tax-deadline fact is the one most people forwarded/saved, so this is the
   most relevant next offer.
3. **Day 7** — same pattern for the Invoice Toolkit, plus the bundle math
   spelled out plainly (buy both for $29 vs. $38 alone) since by email 3 the
   reader has seen enough value to trust an actual price comparison.

Each email's subject line is short and specific (avoids anything that reads
as clickbait/spam-trigger, per the same buyer-trust research from
2026-08-06 that already applies to the listings themselves).

**Deliberately no discount code in this sequence.** LAUNCH25 (see
products/MARKET-NOTES.md, 2026-08-04) was scoped specifically to Jimmy's
personal-network message — a direct ask to people he already knows, where a
capped 10-redemption code makes sense. An automated sequence firing on every
anonymous $0 download could exhaust that same 10-redemption cap on strangers
before it ever reaches Jimmy's own contacts, and using a discount to convert
a cold list reads differently than using it with people who already trust
the sender. If Jimmy wants a discount in email #3 later, that should be a
separate code with its own cap — not reuse of LAUNCH25 — but no case for it
yet with 0 emails sent and 0 signal on how this list responds.

---

## Email 1 — Immediate (sends on download)

**Subject:** Your Freelancer Money Admin Quick-Start

**Body:**
> Hey — here's your copy of The Freelancer Money Admin Quick-Start. Quick
> heads up on what's inside: the 2026 quarterly tax deadlines and a savings
> rule of thumb, the one invoice habit that most reduces late payments, and
> a 5-question self-audit you can run in under 5 minutes.
>
> Start with the self-audit on page 3 — it's the fastest way to see where
> your money admin actually has a gap right now.
>
> If any of the 4 facts in there are new to you, that's a decent sign it's
> worth a closer look at the two full toolkits this excerpt came from — I'll
> send more on those over the next week or so. No obligation either way,
> and no spam — just useful stuff.
>
> — Jimmy

## Email 2 — Day 3

**Subject:** The quarterly tax mistake I see the most

**Body:**
> Quick one. The Quick-Start mentions the 2026 quarterly deadlines, but the
> actual mistake I see freelancers make isn't missing the date — it's
> setting aside a flat "safe" percentage (like 20%) regardless of what they
> actually earned that quarter, then either way overpaying every quarter or
> getting blindsided by one big number in Q4.
>
> The fix is simpler than it sounds: recalculate your set-aside percentage
> off your actual net income each quarter, not a fixed guess. That's exactly
> what the Quarterly Tax Estimator in the full Freelancer Quarterly Tax &
> Expense Tracker does — you enter your real numbers, it computes your exact
> self-employment tax, no guessing. It also has the full 17-category Schedule
> C breakdown and the home office deduction walk-through, not just the one
> deadline fact from the free excerpt.
>
> $19, one-time download, 30-day refund if it's not useful:
> [Gumroad link — Freelancer Quarterly Tax & Expense Tracker]
>
> — Jimmy

## Email 3 — Day 7

**Subject:** The invoice habit that actually stops late payments

**Body:**
> Last one for now. The Quick-Start's other big fact was the one invoice
> habit that most reduces non-payment risk — but a habit only works if you
> actually catch overdue invoices the day they go overdue, not weeks later
> when the relationship's already gotten awkward.
>
> That's the whole point of the Freelancer Invoice & Late-Payment Toolkit:
> a tracker that auto-flags Paid/Overdue/Upcoming the moment a due date
> passes, plus a ready-to-copy 4-stage reminder sequence so you're never
> stuck writing an awkward "hey, following up..." email from scratch, and a
> plain-language guide to late fees and what to do if a client goes quiet
> for good.
>
> $19 on its own, or if you also grabbed (or want) the Tax Tracker from my
> last email, both together are $29 instead of $38 separately:
> [Gumroad link — Freelancer Invoice & Late-Payment Toolkit]
> [Gumroad link — The Freelancer Money Bundle ($29)]
>
> That's it from me for now — you're not signed up for anything ongoing,
> this was just the 3 emails Gumroad sends after a download. If you ever
> have a money-admin headache these don't cover, just reply and tell me —
> genuinely reading these.
>
> — Jimmy

---

## Setup notes for whenever this gets configured
- Gumroad Workflows trigger: "customer bought [Freelancer Money Admin
  Quick-Start]" (the $0/PWYW listing from REQ-005).
- Delays: Email 2 at 3 days after purchase, Email 3 at 7 days after
  purchase — set in Workflow's delay field, not sent manually.
- Links are placeholders (`[Gumroad link — ...]`) since none of the 7
  listings are live yet — same reasoning as every other draft in this repo
  (OUTREACH-KIT.md, the PDFs' cross-sell pages): a dead link would look
  worse than no link, so nothing gets hardcoded until REQ-003/004 clear.
- No discount code included — see "Deliberately no discount code" above.
- This is copy only. No Gumroad Workflow has been created; no email has
  been sent to anyone.

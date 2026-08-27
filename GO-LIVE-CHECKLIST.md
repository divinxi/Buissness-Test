# Go-Live Checklist — everything needed to publish all 8 ready listings in one sitting

Built 2026-08-14, day 29 of $0.00 revenue with REQ-003/004 still open. Every
other file in this repo (business_plan.md, each product's LISTING.md,
products/MARKET-NOTES.md, requests/open_requests.json) already has the full
reasoning and copy — this file adds nothing new to *decide*, it just
collapses "read 8 LISTING.md files and cross-reference file paths" into one
linear checklist so publishing everything is a single sitting instead of
eight separate lookups. Nothing here has been actioned; it's a checklist,
not a log of what happened.

**Do this only after REQ-004's token check** (Gumroad → Settings → Advanced
→ API — revoke/regenerate if you didn't personally hand this session that
token). That's steps 1-2 below. Everything after is safe to do in any order
once that's done.

---

## 0. Security check (30 seconds) — REQ-004
- [ ] Gumroad → Settings → Advanced → API. If you didn't personally generate
      and provide the token a prior run used, revoke/regenerate it now.

## 1-3. Fix the 3 existing drafts — REQ-003
These 3 listings already exist as drafts on `divine357.gumroad.com` with the
real deliverable files attached (uploaded via API on 07-20, verified genuine).
Only cover art, price, and Publish are left — cover upload needs the
browser dashboard, not the API.

- [ ] **ai-prompt-playbook** → drag-drop
      `products/prompt-playbook-v1/dist/cover.png` as thumbnail → also
      upload `preview-1-inside-guide.png` + `preview-2-inside-tracker.png`
      from the same `dist/` folder as additional images → fix price
      **$17 → $19** → hit Publish.
- [ ] **freelancer-tax-tracker-2026** → drag-drop
      `products/freelancer-tax-tracker-v1/dist/cover.png` → also upload its
      2 preview images from the same `dist/` folder → price already correct
      at $19, no change → hit Publish.
- [ ] **freelancer-invoice-toolkit** → drag-drop
      `products/freelancer-invoice-toolkit-v1/dist/cover.png` → also upload
      its 2 preview images from the same `dist/` folder → fix price
      **$17 → $19** → hit Publish.

## 4-8. Create the 5 new listings from scratch
No existing draft — create each as a new Gumroad product. Every field below
is copy-ready; full description/FAQ text to paste is in the linked
LISTING.md (too long to duplicate here without risking it drifting out of
sync — this checklist points at the source of truth, it doesn't replace it).

- [ ] **AI Prompt Playbook Vol. 2: Systems & Automation** — $19 — full copy:
      `products/prompt-playbook-vol2-v1/LISTING.md`
      Files: `products/prompt-playbook-vol2-v1/dist/AI-Prompt-Playbook-Vol2-Systems-Automation.pdf`,
      `Automation-ROI-Tracker.xlsx` · Cover: `dist/cover.png` · +2 preview images (same `dist/`)
- [ ] **The AI Prompt Playbook Bundle** (Vol. 1 + Vol. 2) — $29 — full copy:
      `products/prompt-playbook-bundle-v1/LISTING.md`
      **Create as Gumroad's native "Bundle" product type**, not a regular
      product (2026-08-18 correction — verified via Gumroad's own docs):
      New Product → type "Bundle" → price $29 → select the already-published
      "Small Business AI Prompt Playbook" and "AI Prompt Playbook Vol. 2"
      listings. Gumroad pulls in both products' files automatically — no
      file re-upload. Must be created after both components are live (they
      already are, above, in this checklist's order). Cover:
      `products/prompt-playbook-bundle-v1/dist/cover.png`.
- [ ] **The Freelancer Money Bundle** (Tax Tracker + Invoice Toolkit) — $29
      — full copy: `products/freelancer-bundle-v1/LISTING.md`
      **Create as Gumroad's native "Bundle" product type**, same as above:
      New Product → type "Bundle" → price $29 → select the already-published
      "Freelancer Quarterly Tax & Expense Tracker" and "Freelancer Invoice &
      Late-Payment Toolkit" listings — no file re-upload needed. Cover:
      `products/freelancer-bundle-v1/dist/cover.png`.
- [ ] **The Freelancer Money Admin Quick-Start** (free lead magnet) — $0 /
      Pay-What-You-Want, $0 minimum — full copy:
      `marketing/lead-magnet-freelancer-quickstart/LISTING.md`
      File: `marketing/lead-magnet-freelancer-quickstart/dist/Freelancer-Money-Admin-Quick-Start.pdf`
      · Cover: `dist/cover.png` in the same folder
- [ ] **The Small Business AI Prompt Quick-Start** (free lead magnet) — $0 /
      Pay-What-You-Want, $0 minimum — full copy:
      `marketing/lead-magnet-ai-prompt-quickstart/LISTING.md`
      File: `marketing/lead-magnet-ai-prompt-quickstart/dist/Small-Business-AI-Prompt-Quick-Start.pdf`
      · Cover: `dist/cover.png` in the same folder

**Important for all 5 new listings:** create these through the Gumroad
dashboard UI, not the API — the API-drafting step is exactly what REQ-004
flagged as done without your sign-off the first time. The dashboard is the
mechanism already independently confirmed safe (that's how cover art has to
go up anyway).

## 9. Optional, same sitting — LAUNCH25 discount code
- [ ] Gumroad → each of the 6 paid listings → Discounts → add code
      `LAUNCH25`, 25% off, capped at 10 redemptions per listing. Not required
      to publish; it's prep for the personal-network message in
      `products/OUTREACH-KIT.md` section 1. Skip if you'd rather not manage
      discount codes right now — nothing else depends on it.

## 9b. Optional, same sitting — enable Gumroad's built-in affiliate program
Found 2026-08-27 (see `products/MARKET-NOTES.md`): free, no new account,
costs nothing unless a sale actually happens through it. Two independent
things to turn on per listing, either or both:
- [ ] Each of the 6 paid listings → Share tab → Affiliates → invite anyone
      you want to promote it by email, suggested commission **30%**
      (leaves ~$10.80-$13.30 of a $19 sale after Gumroad's own cut).
- [ ] Each listing → opt into Gumroad's own global affiliate marketplace
      (defaults to ~10% commission) — this is passive: people already
      browsing Gumroad to find products to promote can pick ours up with no
      outreach needed from us. New listings take ~24h+ to get indexed into
      it after publishing.
Skip either or both if you'd rather not manage affiliates right now —
nothing else depends on this, it's the only lever found so far that
doesn't need your own time to work.

## 10. Optional, once listings are live — Gumroad Workflows email sequences
- [ ] For the freelancer lead magnet: Gumroad → Workflows → new workflow
      triggered by a purchase of "The Freelancer Money Admin Quick-Start" →
      paste in the 3 emails from
      `marketing/lead-magnet-freelancer-quickstart/EMAIL-SEQUENCE.md`
      (Day 0, Day 3, Day 7).
- [ ] For the AI Prompt lead magnet: same mechanism, triggered by "The Small
      Business AI Prompt Quick-Start" → paste in the 3 emails from
      `marketing/lead-magnet-ai-prompt-quickstart/EMAIL-SEQUENCE.md`.
      Also optional — the listings work and capture emails without this,
      this just makes the captured emails actually useful.

---

## 2026-08-18 correction
The bundle steps (4 and onward, the two bundle listings) originally told you
to manually re-upload the 4 component files as if creating a brand-new
regular product. That was wrong — Gumroad has a dedicated "Bundle" product
type (New Product → type "Bundle") that lets you pick your own
already-published products and automatically includes their files, no
re-upload needed. Fixed above and in both bundle LISTING.md files. Source:
Gumroad's own help center / product docs (help.gumroad.com/article/339-product-bundles),
verified via WebSearch this run since it was never actually checked before —
every prior pass assumed bundles worked like every other listing.

## What this checklist deliberately does NOT include
- No pricing/copy/positioning reasoning — that's in each LISTING.md and
  `products/MARKET-NOTES.md`. This file only sequences actions, it doesn't
  re-argue them.
- Outreach (personal message, Reddit, LinkedIn, Pinterest, video scripts) —
  that's `products/OUTREACH-KIT.md`, a separate step for after publishing,
  not part of getting listings live.
- Nothing here has been done by this routine. No Gumroad account action was
  taken creating this file — it's a checklist sitting in the repo, same
  category as every LISTING.md it links to.

*Once all 8 are live, update `requests/open_requests.json` (mark REQ-003
resolved, note the live URLs) and this file can be deleted or left as a
historical record — your call.*

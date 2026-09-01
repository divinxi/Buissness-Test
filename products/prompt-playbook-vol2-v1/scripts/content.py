# Source content for the AI Prompt Playbook, Vol. 2: Systems & Automation.
# Edit here, then re-run build_pdf.py / build_xlsx.py to regenerate outputs.
#
# Deliberately distinct from Vol. 1 (which covers one-off tasks in Marketing,
# Support, Finance, HR, Sales). Vol. 2 is about turning AI into a repeatable
# SYSTEM: things you set up once and reuse weekly/monthly, customer-lifecycle
# automation, competitive intelligence, ops reporting, and delegation — none
# of which Vol. 1 touches.

CATEGORIES = [
    {
        "name": "Build Your AI Systems",
        "prompts": [
            {
                "title": "Persistent Assistant Persona Builder",
                "prompt": (
                    "I want to build a reusable AI assistant for [RECURRING JOB, e.g. 'drafting "
                    "my weekly investor update']. Write a persistent system/custom-instructions "
                    "prompt (for a Custom GPT, Claude Project, or similar) that includes: the "
                    "assistant's exact role and scope, 3-5 things it should always ask for before "
                    "starting if not provided, the output format it should default to, and 2-3 "
                    "explicit things it should NOT do (e.g. invent numbers, guess at facts it "
                    "wasn't given). Write it as instructions I can paste once and reuse indefinitely."
                ),
                "when": "The first time you notice you're typing a similar long prompt more than twice — build the system once instead of retyping it.",
                "tip": "Save the finished persona as a Custom GPT or Claude Project, not just a saved prompt in a notes app — that's what makes it a system instead of a one-off.",
            },
            {
                "title": "Recurring Weekly Ops Review Generator",
                "prompt": (
                    "Every week I want to feed you the same categories of raw information and get "
                    "the same structured review back. Build me a reusable template prompt that "
                    "takes: [LIST YOUR WEEKLY INPUTS, e.g. sales numbers, support ticket count, "
                    "cash balance, top customer complaint] and always outputs: a 3-sentence "
                    "headline summary, one thing that improved, one thing that got worse, and one "
                    "recommended action for next week. Write the reusable template, not this "
                    "week's answer."
                ),
                "when": "Setting up any recurring review rhythm (weekly/monthly) you plan to repeat, not a single one-time report.",
                "tip": "Keep the exact same input categories every week even when a number is zero or unchanged — a system only shows trends if the shape never changes.",
            },
            {
                "title": "Knowledge Base Q&amp;A Builder From Your Docs",
                "prompt": (
                    "Here is a set of internal documents/policies: [PASTE OR LIST YOUR DOCS]. "
                    "Build a structured Q&amp;A knowledge base from them: extract every question a "
                    "new employee or customer would plausibly ask, answer each strictly from what "
                    "the documents say (mark anything you're inferring rather than quoting), and "
                    "flag any obvious gap where a likely question has no answer in the source "
                    "material at all."
                ),
                "when": "Turning scattered docs (policies, SOPs, old emails) into one searchable reference before onboarding a new hire or launching a help center.",
                "tip": "Re-run this every time a policy changes — a knowledge base that silently goes stale is worse than no knowledge base, since people trust it.",
            },
            {
                "title": "Meeting-to-Destination Router",
                "prompt": (
                    "Here are raw notes from today's meeting: [PASTE NOTES]. Instead of one action "
                    "list, sort every item into exactly one destination: 'Slack a teammate now', "
                    "'Add to project tracker', 'Needs a calendar follow-up', 'Customer-facing — "
                    "needs a reply', or 'Just a decision, no action needed'. For each item, write it "
                    "in the exact format ready to paste into that destination (e.g. a Slack message, "
                    "a tracker ticket title + description)."
                ),
                "when": "After any meeting where action items need to land in different tools/people, not just one shared list.",
                "tip": "This is the one prompt in this pack worth wiring into an actual automation (Zapier/Make) once you've validated the routing logic manually a few times.",
            },
            {
                "title": "Standard Response Library Builder",
                "prompt": (
                    "Here are the [N] messages/questions we get most often from "
                    "[CUSTOMERS/PROSPECTS/TEAM]: [PASTE EXAMPLES]. Build a library of reusable "
                    "response snippets: group similar requests, write one polished, fill-in-the-"
                    "blank response per group, and name each snippet clearly so it's easy to find "
                    "later (e.g. 'Pricing Objection — Enterprise', 'Refund Request — Standard')."
                ),
                "when": "Building your first canned-response library, or cleaning one up that's grown messy over time.",
                "tip": "Store these in your actual help desk/CRM's snippet feature, not a separate doc — a library nobody can find while typing a live reply doesn't get used.",
            },
        ],
    },
    {
        "name": "Customer Lifecycle Automation",
        "prompts": [
            {
                "title": "Lapsed Customer Win-Back Sequence",
                "prompt": (
                    "We have customers who haven't purchased/used [PRODUCT/SERVICE] in "
                    "[TIMEFRAME, e.g. '90 days']. Write a 3-email win-back sequence: email 1 (a "
                    "genuine check-in, no pitch), email 2 (address the most likely reason people "
                    "in this situation drift away: [YOUR BEST GUESS OR KNOWN REASON]), email 3 "
                    "(a specific, time-bound incentive to come back: [YOUR OFFER]). Keep the tone "
                    "like a person who noticed they left, not an automated blast."
                ),
                "when": "Any time you have a list of customers who've gone quiet and a way to email them.",
                "tip": "Segment by the actual reason they likely left if you can (price, a bad experience, no longer needed) — a single generic sequence converts worse than a targeted one.",
            },
            {
                "title": "New Customer Onboarding Drip",
                "prompt": (
                    "Someone just bought [PRODUCT/SERVICE]. Write a 4-email onboarding drip sent "
                    "over their first 2 weeks: email 1 (immediate — how to get the first quick win "
                    "in under 10 minutes), email 2 (day 3 — the single most-missed feature/step), "
                    "email 3 (day 7 — a check-in asking if they're stuck, with a specific way to "
                    "get help), email 4 (day 14 — ask for a review/testimonial only if they've "
                    "shown signs of actually using it)."
                ),
                "when": "Setting up (or fixing) the automated sequence a customer receives right after purchase.",
                "tip": "Only ask for a review in email 4 if you have any usage signal at all (an open, a login, a reply) — asking a silent non-user for a testimonial reads as tone-deaf.",
            },
            {
                "title": "NPS / Feedback Theme Extractor",
                "prompt": (
                    "Here are [N] raw customer feedback responses (survey answers, reviews, or "
                    "support quotes): [PASTE RESPONSES]. Group them into themes, and for each theme "
                    "report: how many people mentioned it, 1-2 representative quotes, and whether "
                    "it's a Positive, Negative, or Feature Request. Rank themes by frequency, "
                    "highest first. Do not soften negative themes to sound nicer than they are."
                ),
                "when": "After any survey close, or quarterly if you collect reviews continuously.",
                "tip": "Track theme frequency over time in a simple log — a single snapshot tells you what's wrong today, a trend tells you if it's getting better or worse.",
            },
            {
                "title": "Churn Risk Signal Scanner",
                "prompt": (
                    "Here are recent support tickets/usage notes for a set of customers: [PASTE "
                    "NOTES, ONE SECTION PER CUSTOMER]. For each customer, flag a churn risk level "
                    "(Low/Medium/High) based only on concrete signals in the text (complaints about "
                    "value, mentions of a competitor, declining usage, unresolved issues, contract "
                    "questions) — not vibes. List the specific signal(s) that drove each rating so "
                    "a human can verify it, not just trust the label."
                ),
                "when": "Monthly account-health review, especially once you have more accounts than you can track from memory.",
                "tip": "Always have a human review High-risk flags before acting — this prompt surfaces candidates for outreach, it doesn't replace the judgment call.",
            },
            {
                "title": "Referral Ask Email Generator",
                "prompt": (
                    "Write a referral-request email for a customer who has shown a specific "
                    "positive signal: [DESCRIBE THE SIGNAL, e.g. 'left a 5-star review', 'renewed "
                    "early', 'said something great in a support ticket']. Reference that specific "
                    "signal honestly (don't fabricate detail), make the ask concrete and low-effort "
                    "(name exactly what a good referral looks like), and offer a real, "
                    "specific incentive: [YOUR INCENTIVE, or 'none' if you don't want to offer one]."
                ),
                "when": "Right after a customer shows a genuine positive signal — referral asks convert far better tied to a real moment than sent as a cold blast.",
                "tip": "Never send this to a customer with an open complaint or unresolved ticket — timing it wrong turns a goodwill ask into an awkward one.",
            },
        ],
    },
    {
        "name": "Competitive & Market Intelligence",
        "prompts": [
            {
                "title": "Competitor Website Teardown",
                "prompt": (
                    "Here is the homepage/pricing page copy from a competitor: [PASTE OR SUMMARIZE "
                    "THE PAGE]. Break down: their core value proposition in one sentence, who they "
                    "appear to be targeting, their pricing structure and what it implies about their "
                    "target customer size, and 2-3 specific claims or features they emphasize that "
                    "we don't currently mention anywhere in our own materials."
                ),
                "when": "Before a pricing change, a new competitor entering your space, or a quarterly positioning check.",
                "tip": "Do this for 2-3 competitors at once and compare the outputs side by side — a single teardown tells you about them, a comparison tells you about the gap.",
            },
            {
                "title": "Pricing Page Comparison Matrix",
                "prompt": (
                    "Here are the pricing tiers/features for us and [N] competitors: [PASTE EACH "
                    "COMPANY'S TIERS AND WHAT'S INCLUDED]. Build a comparison table: rows are "
                    "features, columns are companies, cells show what's included at what tier. "
                    "Then write 3 sentences on where we're priced high or low for what we include, "
                    "based only on what's in the table — not general pricing advice."
                ),
                "when": "Before a pricing review, or when a prospect asks 'why do you cost more/less than X'.",
                "tip": "Re-pull competitor pricing fresh each time — pasting an old comparison and just re-analyzing it will miss changes they've quietly made.",
            },
            {
                "title": "Industry News Digest Summarizer",
                "prompt": (
                    "Here are [N] articles/posts from this week about [YOUR INDUSTRY/NICHE]: "
                    "[PASTE HEADLINES + LINKS OR TEXT]. Summarize into a digest: 3-5 bullet points "
                    "on what actually changed or matters, one sentence on why each one is relevant "
                    "to a business like ours specifically, and skip anything that's just generic "
                    "industry noise with no real implication for us."
                ),
                "when": "Weekly or biweekly, once you've built a habit of collecting a handful of industry sources.",
                "tip": "Paste the actual article text when you can, not just headlines — headline-only summaries tend to hallucinate the 'why it matters' part.",
            },
            {
                "title": "Customer Review Gap-Mining",
                "prompt": (
                    "Here are public reviews of a competitor's product: [PASTE REVIEWS, IDEALLY A "
                    "MIX OF POSITIVE AND NEGATIVE]. Extract: the 3 most common complaints (these are "
                    "unmet needs a competing product could win on), the 3 most common praises "
                    "(these are the bar you need to match, not just beat), and any complaint that "
                    "shows up in a product like ours too, if you know our own reviews: [OPTIONAL: "
                    "PASTE OUR OWN REVIEW COMPLAINTS FOR COMPARISON]."
                ),
                "when": "Scoping a new feature, or deciding what to emphasize in marketing against a specific competitor.",
                "tip": "Weight recent reviews more than old ones — a complaint from 2 years ago may already be fixed and isn't a real gap anymore.",
            },
            {
                "title": "Positioning Statement Stress-Test",
                "prompt": (
                    "Here is our current positioning statement / one-line pitch: [PASTE IT]. Play "
                    "the role of a skeptical prospect who has 3 other options in this market. Ask "
                    "the 3 hardest questions this statement leaves unanswered, then rewrite the "
                    "statement to address the single biggest gap without making it longer than the "
                    "original."
                ),
                "when": "Whenever the pitch feels stale, before a fundraise/pitch, or after losing a deal to a specific competitor for a positioning reason.",
                "tip": "Do this quarterly even when nothing feels wrong — positioning drifts quietly as a market shifts, and you rarely notice from the inside.",
            },
        ],
    },
    {
        "name": "Reporting & Ops Rhythm",
        "prompts": [
            {
                "title": "Weekly KPI Digest From Raw Numbers",
                "prompt": (
                    "Here are this week's raw numbers: [PASTE METRICS, e.g. revenue, new "
                    "customers, churn, support tickets, ad spend]. Compare against last week's "
                    "numbers: [PASTE PRIOR WEEK]. Write a digest: 3 headline bullet points on what "
                    "moved and by how much (as a percentage, not just raw numbers), one metric that "
                    "needs attention this week and why, and skip any metric that moved less than "
                    "5% — that's noise, not signal, at this level of detail."
                ),
                "when": "Every week, once you have at least 2 weeks of comparable numbers to work from.",
                "tip": "Keep the exact same metric list every week even during a slow week — the value of this system is in the comparison, and comparisons need consistent inputs.",
            },
            {
                "title": "Investor / Board One-Pager Generator",
                "prompt": (
                    "Here is this period's performance data: [PASTE KEY NUMBERS] and context: "
                    "[ANY NOTABLE WINS, RISKS, OR DECISIONS NEEDED]. Write a one-page update: "
                    "headline number first, 3 bullets on progress, 1-2 bullets on real risks (not "
                    "sandbagged optimism), and one specific ask if you need anything from the "
                    "reader (an intro, a decision, feedback). Plain language, no jargon, no spin."
                ),
                "when": "Monthly or quarterly investor/board/advisor updates.",
                "tip": "Write the risks section yourself first, unedited, before running this prompt — it's tempting to let AI phrase around a real problem instead of stating it.",
            },
            {
                "title": "Inventory Reorder Point Calculator",
                "prompt": (
                    "Here is my situation for [PRODUCT/SKU]: average daily sales of [X units], "
                    "supplier lead time of [Y days], and I want a safety buffer of [Z days] of "
                    "extra stock in case of delays or a sales spike. Calculate: the reorder point "
                    "(units on hand at which I should place a new order), and show the exact "
                    "formula used so I can recalculate it myself next time my numbers change."
                ),
                "when": "Setting reorder points for the first time, or any time lead times or sales pace changes meaningfully.",
                "tip": "Recalculate this every quarter, not once and forget it — a reorder point based on last year's sales pace will leave you either overstocked or stocked out.",
            },
            {
                "title": "Task Prioritization Matrix",
                "prompt": (
                    "Here is my task list for this week: [PASTE TASKS]. Sort every task into an "
                    "Eisenhower matrix: Urgent+Important (do first), Important+Not Urgent (schedule "
                    "a specific time), Urgent+Not Important (delegate if possible, name who to), "
                    "Neither (candidate to drop). For anything you're unsure how to classify, ask "
                    "one clarifying question instead of guessing."
                ),
                "when": "Monday morning planning, or any time the task list feels unmanageable.",
                "tip": "Be honest about what's actually urgent vs. what just feels urgent because it's loud (a Slack ping) — the matrix only works if the inputs are accurate.",
            },
            {
                "title": "Anomaly Flag in Weekly Numbers",
                "prompt": (
                    "Here are my weekly numbers for the last [N] weeks: [PASTE A SIMPLE TABLE OF "
                    "WEEK + METRIC VALUES]. Identify any week where a metric moved meaningfully "
                    "outside its normal pattern (not just up or down, but outside the range the "
                    "other weeks establish). For each anomaly found, state which week, which "
                    "metric, and by how much it deviated from the trend — don't speculate on the "
                    "cause unless I've given you context to work from."
                ),
                "when": "Monthly, once you have at least 6-8 weeks of the same metrics logged consistently.",
                "tip": "This catches things a simple week-over-week comparison misses — a slow 8-week decline, for example, where no single week looks alarming on its own.",
            },
        ],
    },
    {
        "name": "Delegation & Team Enablement",
        "prompts": [
            {
                "title": "Role Handoff Document Writer",
                "prompt": (
                    "I'm handing off [RESPONSIBILITY/PROJECT] to [PERSON/ROLE]. Here's how I "
                    "currently handle it, roughly: [DESCRIBE WHAT YOU DO]. Write a handoff document: "
                    "what this responsibility actually covers (and explicitly what it does NOT "
                    "cover, to prevent scope confusion), the recurring cadence if any, who to "
                    "contact for what, and the 2-3 judgment calls that come up most often with a "
                    "note on how you've been deciding them."
                ),
                "when": "Delegating a responsibility for the first time, or when someone leaves and knowledge needs to transfer before they go.",
                "tip": "Have the new owner read it back to you in their own words before you consider the handoff done — a document that makes sense to you may not to them.",
            },
            {
                "title": "Expert-to-Training-Script Converter",
                "prompt": (
                    "Here is a transcript or rough recording of an expert explaining how to "
                    "[TASK/PROCESS]: [PASTE TRANSCRIPT]. Convert it into a clean training script: "
                    "numbered steps in the order a learner should follow them (not necessarily the "
                    "order the expert mentioned them), plain language replacing any jargon the "
                    "expert used without explaining, and a short 'common mistake' callout anywhere "
                    "the expert mentioned something people tend to get wrong."
                ),
                "when": "Turning a subject-matter expert's knowledge into something repeatable that doesn't depend on them being available to explain it live every time.",
                "tip": "Record the expert explaining it as if to a brand-new hire, not as if to a peer — that framing naturally surfaces the steps they'd otherwise skip as 'obvious'.",
            },
            {
                "title": "Decision Log Entry Writer",
                "prompt": (
                    "We just made this decision: [DESCRIBE THE DECISION]. Here's the context: "
                    "[WHY IT CAME UP, WHAT OPTIONS WERE CONSIDERED]. Write a decision log entry: "
                    "the decision in one sentence, the 2-3 alternatives considered and why they "
                    "weren't chosen, who made the call, and one specific condition under which this "
                    "decision should be revisited."
                ),
                "when": "Any decision you'd hate to re-debate from scratch in 6 months because nobody remembers why you chose what you chose.",
                "tip": "The 'when to revisit' field is the one people skip and the one that matters most — a decision without a revisit trigger tends to just quietly become permanent.",
            },
            {
                "title": "Goal-to-Agenda Meeting Builder",
                "prompt": (
                    "This meeting needs to accomplish: [THE SPECIFIC OUTCOME YOU NEED, e.g. 'decide "
                    "which of 2 vendors to use']. Attendees: [LIST]. Build an agenda that works "
                    "backward from that outcome: what needs to be presented, what needs to be "
                    "decided and by whom, and a hard time budget per section that adds up to "
                    "[MEETING LENGTH]. Flag if the outcome realistically needs more time than that."
                ),
                "when": "Any meeting you're calling, especially recurring ones that have drifted from having a clear purpose.",
                "tip": "If you can't state the specific outcome in one sentence before building the agenda, that's the real problem — no agenda template fixes an unclear purpose.",
            },
            {
                "title": "Peer Feedback Request Template",
                "prompt": (
                    "I want honest feedback from [PEER/TEAM] on [SPECIFIC WORK OR DECISION, not "
                    "'how am I doing' in general]. Write a short request message that asks 2-3 "
                    "specific questions instead of an open-ended 'any thoughts?', makes it easy to "
                    "say something critical without it feeling confrontational, and gives a clear "
                    "deadline so it doesn't sit unanswered."
                ),
                "when": "Any time you want feedback that's actually useful rather than a polite 'looks good'.",
                "tip": "Specific questions get specific answers — 'what's confusing about this' beats 'what do you think' almost every time.",
            },
        ],
    },
]

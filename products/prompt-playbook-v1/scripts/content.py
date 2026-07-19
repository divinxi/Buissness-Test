# Source content for the Small Business AI Prompt Playbook.
# Edit here, then re-run build_pdf.py / build_xlsx.py to regenerate outputs.

CATEGORIES = [
    {
        "name": "Marketing & Content",
        "prompts": [
            {
                "title": "Weekly Social Content Batch",
                "prompt": (
                    "Act as a social media copywriter for [BUSINESS NAME], a [BUSINESS TYPE] "
                    "that helps [TARGET CUSTOMER] with [MAIN BENEFIT]. Take this single topic: "
                    "\"[TOPIC]\". Turn it into 5 posts, one each for Instagram, LinkedIn, Facebook, "
                    "X/Twitter, and an email teaser. Match tone to each platform, keep each under "
                    "the platform's practical length, and end every post with one clear call to "
                    "action: [DESIRED ACTION, e.g. 'book a call', 'reply to this email']."
                ),
                "when": "Monday planning session — turn one idea into a week of content in one pass.",
                "tip": "Paste 2-3 examples of your best-performing past posts before the prompt so the tone matches your actual voice, not a generic one.",
            },
            {
                "title": "Customer Testimonial Rewriter",
                "prompt": (
                    "Here is a raw customer quote or review: \"[PASTE QUOTE]\". Rewrite it into "
                    "three formats: (1) a punchy one-line quote for a website hero section, "
                    "(2) a short LinkedIn post from the business's perspective thanking the "
                    "customer and adding context, (3) a 2-sentence blurb for an email newsletter. "
                    "Keep the customer's actual meaning intact — do not invent details they didn't say."
                ),
                "when": "Any time you get a good review, DM, or email compliment.",
                "tip": "Always get the customer's OK before publishing their words publicly, even paraphrased.",
            },
            {
                "title": "Local SEO Blog Outline",
                "prompt": (
                    "I run a [BUSINESS TYPE] in [CITY/REGION]. Write a blog post outline targeting "
                    "the search term \"[SEARCH TERM, e.g. best plumber in Austin]\". Include: a title "
                    "under 60 characters with the keyword near the front, a meta description under "
                    "155 characters, 5-6 H2 section headers that answer real questions a searcher "
                    "would have, and one FAQ section with 3 question/answer pairs suitable for "
                    "featured snippets."
                ),
                "when": "Building organic search traffic without paying for ads.",
                "tip": "Search the term yourself first and note what's ranking — ask the model to outline something more specific/useful than the top 3 results.",
            },
            {
                "title": "Ad Copy A/B Variants",
                "prompt": (
                    "Write 5 ad copy variants for [PRODUCT/SERVICE], each testing a different angle: "
                    "(1) leads with the pain point it solves, (2) leads with the core benefit, "
                    "(3) leads with urgency/scarcity, (4) leads with social proof or a stat, "
                    "(5) leads with curiosity. Each variant: one headline (under 40 characters) "
                    "and one body line (under 90 characters), written for [PLATFORM, e.g. Meta/Google]."
                ),
                "when": "Before launching or refreshing a paid ad campaign.",
                "tip": "Run all 5 for at least a few hundred impressions each before picking a winner — don't judge on gut feel alone.",
            },
            {
                "title": "Email Newsletter From Bullet Points",
                "prompt": (
                    "Turn these rough notes into a newsletter email: [PASTE BULLET NOTES]. "
                    "Structure: a subject line under 50 characters, a one-line preview text, a "
                    "friendly opening line, 3-4 short sections with subheads, and a single clear "
                    "call to action at the end. Keep the tone conversational, like a person wrote "
                    "it, not corporate."
                ),
                "when": "Turning 10 minutes of scribbled notes into something ready to send.",
                "tip": "Read it out loud before sending — if a sentence doesn't sound like something you'd say, cut it.",
            },
        ],
    },
    {
        "name": "Customer Service & Support",
        "prompts": [
            {
                "title": "Difficult Email Response Drafter",
                "prompt": (
                    "A customer sent this message: \"[PASTE CUSTOMER MESSAGE]\". Our situation/policy "
                    "is: [EXPLAIN CONSTRAINTS, e.g. 'we can't refund after 30 days but can offer "
                    "store credit']. Draft a reply that acknowledges their frustration specifically "
                    "(not generically), explains the situation plainly without being defensive, and "
                    "offers the best resolution we can actually give. Keep it under 150 words."
                ),
                "when": "Any time a customer email needs a careful, de-escalating response.",
                "tip": "Never send the first draft unread — always personalize at least the opening line yourself.",
            },
            {
                "title": "FAQ Generator From Support Tickets",
                "prompt": (
                    "Here are the last [N] questions customers have asked us: [PASTE LIST]. Group "
                    "them into themes, then write a clean FAQ page: one clear question per entry "
                    "(rewritten in the customer's likely words) and a concise, complete answer for "
                    "each. Flag any question you don't have enough information to answer confidently."
                ),
                "when": "Quarterly, or whenever support volume on the same topics is climbing.",
                "tip": "Export tickets from your helpdesk as plain text first — the more real examples you paste in, the better the grouping.",
            },
            {
                "title": "Refund/Complaint Policy Explainer",
                "prompt": (
                    "Here is our internal policy, written informally: [PASTE POLICY NOTES]. Rewrite "
                    "it as a customer-facing policy page: plain language, no legal jargon unless "
                    "required, organized with short headers, and a tone that reads as fair rather "
                    "than defensive. Include a short 'if something's wrong, here's what to do' "
                    "section at the top."
                ),
                "when": "Publishing or updating a returns/refunds/complaints page.",
                "tip": "Have an actual customer (or a friend who's never seen the policy) read it back — if they'd still be confused, revise.",
            },
            {
                "title": "Support Ticket Triage & Tagging",
                "prompt": (
                    "Classify each of these support messages into exactly one category from this "
                    "list: [YOUR CATEGORIES, e.g. Billing, Bug Report, How-To, Refund Request, "
                    "Other]. Also assign urgency (Low/Medium/High) based on language suggesting "
                    "churn risk, safety issues, or blocked usage. Return as a table: message "
                    "excerpt, category, urgency, one-line reason.\n\nMessages:\n[PASTE MESSAGES]"
                ),
                "when": "Daily/weekly triage when ticket volume is too high to read one by one.",
                "tip": "This is the one prompt in this pack worth automating via an API call instead of copy-pasting — ask me if you want that built.",
            },
            {
                "title": "Review Response Generator",
                "prompt": (
                    "Here is a customer review: \"[PASTE REVIEW]\" ([star rating]). Draft a public "
                    "response in our brand voice: [DESCRIBE VOICE, e.g. warm, direct, a little "
                    "playful]. Thank them specifically for something they mentioned, address any "
                    "complaint honestly without over-apologizing, and if relevant invite them to "
                    "follow up privately. Under 80 words."
                ),
                "when": "Responding to Google/Yelp/App Store reviews, especially negative ones.",
                "tip": "Respond to negative reviews within 24-48 hours — speed reads as care, even before they read the content.",
            },
        ],
    },
    {
        "name": "Finance & Operations",
        "prompts": [
            {
                "title": "Expense Categorization Assistant",
                "prompt": (
                    "Here is a list of raw transactions (date, description, amount): [PASTE LIST]. "
                    "Categorize each into one of: [YOUR CATEGORIES, e.g. Rent, Payroll, Software, "
                    "Marketing, Supplies, Travel, Other]. Flag any transaction where the category "
                    "is ambiguous instead of guessing. Return as a table plus a one-line total per "
                    "category at the end."
                ),
                "when": "Monthly bookkeeping cleanup before it goes to your accountant.",
                "tip": "Always have your accountant/bookkeeper verify categorization for tax purposes — this speeds up prep, it doesn't replace review.",
            },
            {
                "title": "Simple Cash Flow Narrative",
                "prompt": (
                    "Here are this month's numbers: revenue [$X], expenses [$Y] broken down as "
                    "[BREAKDOWN], starting cash [$Z]. Write a plain-English, 4-6 sentence summary "
                    "of how the business is doing this month, suitable for a co-founder or "
                    "investor update. No jargon, no spin — if something is concerning, say so "
                    "plainly and note what's being done about it."
                ),
                "when": "Monthly investor/partner updates, or just to keep yourself honest about the numbers.",
                "tip": "Feed it 2-3 months of history at once so it can note trends ('expenses up 12% vs last month'), not just a single snapshot.",
            },
            {
                "title": "Vendor Contract Summary",
                "prompt": (
                    "Here is a vendor contract: [PASTE OR DESCRIBE KEY SECTIONS]. Summarize: "
                    "(1) price and payment terms, (2) contract length and renewal/cancellation "
                    "terms including any auto-renewal notice deadline, (3) any exclusivity or "
                    "non-compete clauses, (4) anything unusual or risky compared to standard "
                    "vendor contracts. Flag anything I should have a lawyer look at rather than "
                    "deciding on my own."
                ),
                "when": "Before signing, or when auditing existing vendor contracts for renewal traps.",
                "tip": "This produces a reading guide, not legal advice — always have an actual lawyer review anything with real financial exposure.",
            },
            {
                "title": "SOP Writer From a Verbal Process",
                "prompt": (
                    "Here's how we currently do [PROCESS NAME], described roughly: [DESCRIBE THE "
                    "STEPS AS YOU'D EXPLAIN THEM OUT LOUD]. Turn this into a numbered standard "
                    "operating procedure a new employee could follow without asking questions. "
                    "Call out any tools/logins needed at each step, and note any step where a "
                    "judgment call is required instead of a fixed rule."
                ),
                "when": "Any time you catch yourself explaining the same process verbally more than twice.",
                "tip": "Record yourself explaining the process out loud (voice memo), transcribe it, and paste that in — it captures details a tidy summary would drop.",
            },
            {
                "title": "Meeting Notes to Action Items",
                "prompt": (
                    "Here are raw notes from today's meeting: [PASTE NOTES]. Extract a clean action "
                    "item list: each item as 'Owner — Action — Due date (if mentioned, else "
                    "\"unassigned\")'. Then write a 3-sentence summary of the key decisions made, "
                    "separate from the action items."
                ),
                "when": "Immediately after any meeting, before details fade.",
                "tip": "Paste notes within the hour — quality drops fast once you're trying to recall what a shorthand note meant.",
            },
        ],
    },
    {
        "name": "Hiring & HR",
        "prompts": [
            {
                "title": "Job Description Generator",
                "prompt": (
                    "We need to hire a [ROLE]. Here's a rough list of what they'd actually do day "
                    "to day: [PASTE ROUGH RESPONSIBILITIES]. Write a job description with: a short "
                    "compelling intro about the role's impact, 5-7 responsibilities, 4-5 "
                    "requirements split into 'must have' and 'nice to have', and a one-line note on "
                    "compensation range placeholder. Review the language for anything that could "
                    "unintentionally discourage qualified candidates (overly aggressive requirements "
                    "lists, gendered language, etc.) and flag it."
                ),
                "when": "Opening a new role or refreshing a stale job post that isn't attracting candidates.",
                "tip": "Post the 'must have' list separately from 'nice to have' in the actual listing — bundling them scares off good candidates who don't check every box.",
            },
            {
                "title": "Interview Question Set Builder",
                "prompt": (
                    "We're interviewing for [ROLE]. The most important things this person needs to "
                    "be good at are: [LIST 3-4 CORE SKILLS/TRAITS]. Generate 8 interview questions "
                    "that actually test for these (behavioral and situational, not just 'tell me "
                    "about a time'). For each question, note briefly what a strong answer sounds "
                    "like versus a weak one."
                ),
                "when": "Prepping for interviews, especially for a role you haven't hired for before.",
                "tip": "Ask every candidate for a role the same core 3-4 questions so you can actually compare answers apples-to-apples.",
            },
            {
                "title": "Candidate Screening Rubric",
                "prompt": (
                    "Here is the job description for [ROLE]: [PASTE OR SUMMARIZE]. Build a scoring "
                    "rubric with 5 criteria drawn directly from the requirements, each scored 1-4 "
                    "with a one-line description of what a 1 vs a 4 looks like. Add a final "
                    "'red flags to watch for' section specific to this role."
                ),
                "when": "Before reviewing resumes/doing screening calls for a batch of candidates.",
                "tip": "Fill out the rubric right after each call while it's fresh — scoring from memory a day later reintroduces bias.",
            },
            {
                "title": "Onboarding Checklist Generator",
                "prompt": (
                    "We just hired a [ROLE]. Build a first-30-days onboarding checklist broken into "
                    "Week 1, Week 2, Weeks 3-4. Include account/tool setup, who they should meet "
                    "and why, what they should be able to do independently by day 30, and one "
                    "check-in question for their manager to ask at each week's end."
                ),
                "when": "Whenever a new hire starts — even a rough checklist beats none.",
                "tip": "Ask the last person hired into a similar role what was missing from their onboarding, and fold that in.",
            },
            {
                "title": "Performance Review Draft Assistant",
                "prompt": (
                    "Here are my rough notes on [EMPLOYEE]'s performance this period: [PASTE NOTES, "
                    "INCLUDING BOTH STRENGTHS AND CONCERNS]. Draft a performance review structured "
                    "as: key strengths (specific, not generic praise), areas to develop (framed "
                    "constructively, tied to specific examples), and 2-3 concrete goals for next "
                    "period. Keep it honest — do not soften real concerns into vague language."
                ),
                "when": "Prepping for a formal review cycle.",
                "tip": "Never let the draft replace the conversation — use it as prep so the actual discussion is clearer, not as something you just hand over.",
            },
        ],
    },
    {
        "name": "Sales & Outreach",
        "prompts": [
            {
                "title": "Cold Outreach Email Personalizer",
                "prompt": (
                    "Here's public information about a prospect: [PASTE LINKEDIN BIO / COMPANY "
                    "NEWS / RECENT POST]. We sell [PRODUCT/SERVICE] which helps companies like "
                    "theirs with [SPECIFIC BENEFIT]. Write a cold email: a personalized opening "
                    "line referencing something specific and true about them (not generic "
                    "flattery), 2 sentences connecting their likely situation to our benefit, and "
                    "one low-friction call to action. Under 100 words total."
                ),
                "when": "Any outbound prospecting, especially for higher-value targets worth the extra 5 minutes of research.",
                "tip": "If you can't find one genuinely specific detail about the prospect, don't fake one — send a shorter, honest, non-personalized version instead.",
            },
            {
                "title": "Objection Handling Script Builder",
                "prompt": (
                    "Prospects for [PRODUCT/SERVICE] commonly say: [LIST 3-5 REAL OBJECTIONS YOU "
                    "HEAR]. For each objection, write a response that acknowledges the concern "
                    "honestly (don't dismiss it), reframes with a relevant fact or example, and "
                    "ends with a question that moves the conversation forward rather than a hard "
                    "pitch."
                ),
                "when": "Sales team training, or prepping yourself before a call with a known-skeptical prospect.",
                "tip": "Update this quarterly — the objections that matter shift as your market and pricing change.",
            },
            {
                "title": "Proposal/Quote Summary Writer",
                "prompt": (
                    "Here is our pricing/scope for this deal: [PASTE LINE ITEMS AND PRICES]. Write "
                    "a one-page client-facing summary: what's included, what it costs (clearly "
                    "broken down), what happens next (timeline/process), and a short paragraph "
                    "reminding them of the specific problem this solves for them based on our "
                    "earlier conversation: [SUMMARIZE THEIR STATED NEED]."
                ),
                "when": "Sending a formal quote or proposal after a sales conversation.",
                "tip": "Always tie the summary back to their specific stated problem — generic proposals read as templated and lose deals.",
            },
            {
                "title": "Follow-Up Sequence Generator",
                "prompt": (
                    "We had a sales call with a prospect about [PRODUCT/SERVICE]. They said their "
                    "main interest was [THEIR STATED INTEREST] and their main hesitation was "
                    "[THEIR STATED CONCERN]. Write a 4-email follow-up sequence spaced over 2 "
                    "weeks: email 1 (recap + next step), email 2 (address their specific "
                    "hesitation with proof/example), email 3 (share a relevant case study or "
                    "resource), email 4 (direct, low-pressure check-in). Keep each under 120 words."
                ),
                "when": "Right after any sales call that doesn't close immediately.",
                "tip": "Set actual calendar reminders for each send date — sequences only work if they're not forgotten after email 1.",
            },
            {
                "title": "Win/Loss Call Debrief Analyzer",
                "prompt": (
                    "Here are notes from a debrief on a deal we [WON/LOST]: [PASTE NOTES]. "
                    "Summarize: the main factor that decided the outcome, 2-3 contributing "
                    "factors, and one specific, actionable change to try on the next similar deal. "
                    "Avoid vague takeaways like 'be more persuasive' — make it concrete."
                ),
                "when": "After any deal closes, win or lose, while details are still fresh.",
                "tip": "Do this for wins too, not just losses — you learn what to repeat, not just what to avoid.",
            },
        ],
    },
]

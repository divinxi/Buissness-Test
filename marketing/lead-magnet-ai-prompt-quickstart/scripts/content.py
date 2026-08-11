# Source content for the free lead magnet: "The Small Business AI Prompt Quick-Start."
# Real prompts copied verbatim from products/prompt-playbook-v1/scripts/content.py
# (one per category, all 5 categories represented) — this is a distilled excerpt of
# already-shipped, already-QA'd content, not new material. Mirrors the pattern used by
# marketing/lead-magnet-freelancer-quickstart/, which closed the same gap for the
# freelancer product line; the AI Prompt Playbook line never had its own lead magnet
# or email nurture sequence until this one (2026-08-11).

PROMPTS = [
    {
        "category": "Marketing & Content",
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
        "category": "Customer Service & Support",
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
        "category": "Finance & Operations",
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
        "category": "Hiring & HR",
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
        "category": "Sales & Outreach",
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
]

CHECKLIST = [
    "Do you have a repeatable way to turn one idea into a week of content, or do you start from a blank page each time?",
    "Does an upset-customer email get a careful, specific reply — or a generic one because you're rushed?",
    "Are your expenses categorized as you go, or all at once in a scramble before tax time?",
    "Does your job posting language actually invite qualified candidates, or quietly scare off good ones?",
    "Do you personalize outreach with something true and specific, or send the same email to everyone?",
]

CTA_TEXT = (
    "If two or more of those made you wince a little, that's normal — most small business "
    "owners are doing all five without a repeatable system. These 5 prompts are one from "
    "each category in the full Small Business AI Prompt Playbook, which has 25 total across "
    "Marketing, Support, Finance, Hiring, and Sales — plus a spreadsheet tracker that logs "
    "the time and money each one saves you. Volume 2 covers a different problem entirely: "
    "turning these one-off prompts into repeatable systems (automation, customer lifecycle, "
    "competitive intel, reporting, delegation)."
)

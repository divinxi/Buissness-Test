# Source content for the Freelancer Invoice & Late-Payment Toolkit.
# Practical, field-tested freelance business practice — not legal advice. Small claims
# limits and collections law vary by state/country; the guide flags this explicitly
# wherever it matters instead of citing jurisdiction-specific numbers.

INVOICE_ELEMENTS = [
    {
        "name": "Invoice number",
        "why": "Sequential, unique numbers (INV-001, INV-002...) make bookkeeping and follow-up unambiguous — 'the invoice from March' is not searchable, 'INV-014' is.",
    },
    {
        "name": "Your business info",
        "why": "Legal/trading name, address, email, and how you want to be paid. If you operate under an LLC or registered trade name, use that exact name — it matters if you ever need to enforce payment.",
    },
    {
        "name": "Client info",
        "why": "The person or company legally responsible for payment, not just your day-to-day contact — if you worked with 'Sarah' but the contract is with 'Acme LLC', bill Acme LLC.",
    },
    {
        "name": "Itemized description",
        "why": "List what was delivered, not just 'consulting services' — itemized invoices get disputed less and get paid faster because there's nothing to ask about.",
    },
    {
        "name": "Issue date and due date",
        "why": "A due date is not optional. 'Payment due upon receipt' is technically a due date, but a specific date removes all ambiguity about when a client is late.",
    },
    {
        "name": "Payment terms",
        "why": "State the term (Net 15, Net 30, etc.) on the invoice itself, not just in the original contract — clients reference the invoice, not the email thread from three months ago.",
    },
    {
        "name": "Accepted payment methods",
        "why": "Every friction point you remove (bank transfer details, payment link, accepted cards) shaves days off how fast you get paid. Don't make a client ask how to pay you.",
    },
    {
        "name": "Late fee clause",
        "why": "Only enforceable if it was disclosed before the work started (ideally in the original contract/proposal, restated on the invoice) — see Late Fees section for how to set this up correctly.",
    },
]

PAYMENT_TERMS = [
    {
        "term": "Due on Receipt",
        "meaning": "Payment expected immediately when the invoice is sent.",
        "best_for": "Small jobs, one-off work, new clients with no payment history with you.",
        "risk": "Low",
    },
    {
        "term": "Net 15",
        "meaning": "Payment due within 15 days of the invoice date.",
        "best_for": "Established clients, mid-size projects.",
        "risk": "Low-Medium",
    },
    {
        "term": "Net 30",
        "meaning": "Payment due within 30 days of the invoice date.",
        "best_for": "Larger companies whose AP departments run on a fixed cycle — often non-negotiable on their end.",
        "risk": "Medium",
    },
    {
        "term": "50% Upfront / 50% on Delivery",
        "meaning": "Half the total billed before work starts, half on completion.",
        "best_for": "New clients, larger projects, anyone without a payment track record with you — this is the single biggest lever for reducing non-payment risk.",
        "risk": "Low (upfront portion), Medium (final portion)",
    },
    {
        "term": "Milestone-Based",
        "meaning": "Project broken into phases, each invoiced and paid before the next phase starts.",
        "best_for": "Long projects (2+ months) — caps how much unpaid work you're ever exposed to at once.",
        "risk": "Low",
    },
]

DEPOSIT_STRATEGY = {
    "headline": "The single highest-leverage habit: get a deposit before you start.",
    "note": (
        "A 25-50% deposit, collected before work begins, does two things: it filters out clients "
        "who were never going to pay, and it caps your maximum loss if a client disappears. "
        "Freelancers who never request a deposit tend to discover this the hard way — after the "
        "work is already done and unbilled hours can't be un-worked."
    ),
    "new_client_rule": "For any client you haven't been paid by before, a deposit isn't rude — it's standard. If a prospective client balks at a reasonable deposit request, that reaction is itself useful information.",
}

REMINDER_SEQUENCE = [
    {
        "stage": "3 days before due",
        "tone": "Friendly heads-up (skip for Due on Receipt terms)",
        "subject": "Quick heads-up: Invoice [INVOICE #] due [DUE DATE]",
        "body": (
            "Hi [CLIENT NAME],\n\n"
            "Just a friendly reminder that Invoice [INVOICE #] for [AMOUNT] is due on [DUE DATE]. "
            "I've attached it again in case it got buried — let me know if you need anything else "
            "from me to process it.\n\n"
            "Thanks,\n[YOUR NAME]"
        ),
    },
    {
        "stage": "Due date",
        "tone": "Polite, assumes good faith",
        "subject": "Invoice [INVOICE #] due today",
        "body": (
            "Hi [CLIENT NAME],\n\n"
            "Invoice [INVOICE #] for [AMOUNT] is due today. If it's already been sent, thank you — "
            "no action needed. If not, here's the invoice again: [LINK/ATTACHMENT].\n\n"
            "Let me know if anything's holding it up.\n\n"
            "Best,\n[YOUR NAME]"
        ),
    },
    {
        "stage": "7 days late",
        "tone": "Firmer, still professional",
        "subject": "Following up: Invoice [INVOICE #] is now 7 days past due",
        "body": (
            "Hi [CLIENT NAME],\n\n"
            "Invoice [INVOICE #] for [AMOUNT] was due on [DUE DATE] and is now 7 days past due. "
            "Could you let me know the status, or when I can expect payment? Happy to resend the "
            "invoice or answer any questions about it.\n\n"
            "[YOUR NAME]"
        ),
    },
    {
        "stage": "14-30 days late",
        "tone": "Final notice before escalation",
        "subject": "Final notice: Invoice [INVOICE #] — [DAYS] days past due",
        "body": (
            "Hi [CLIENT NAME],\n\n"
            "Invoice [INVOICE #] for [AMOUNT] is now [DAYS] days past due, and I haven't heard "
            "back after previous follow-ups. Please arrange payment by [FINAL DATE]. Per the terms "
            "on the invoice, a late fee of [LATE FEE %] now applies to the overdue balance.\n\n"
            "If there's a dispute about the work or the amount, please tell me now so we can "
            "resolve it — otherwise I'll need to look at next steps to collect the balance.\n\n"
            "[YOUR NAME]"
        ),
    },
]

LATE_FEES = {
    "headline": "Late fees only work if the client agreed to them before the work started.",
    "common_range": "A common range is 1%-1.5% per month (roughly 12%-18% annualized) or a flat fee (e.g. $25-50) on invoices over a set threshold — whichever is simpler to compute and defend.",
    "how_to_set_up": "Put the late fee term in the original proposal/contract AND restate it on every invoice ('Payment due within 15 days. A 1.5% monthly late fee applies to overdue balances.'). A late fee sprung on a client for the first time in a collections email is far weaker than one they agreed to upfront.",
    "caveat": "Some states cap the interest rate you can charge without triggering usury law — a flat fee sidesteps this entirely and is simpler to explain to a client anyway.",
}

ESCALATION_STEPS = [
    {
        "step": "1. Stop new work immediately",
        "detail": "Don't start (or continue) new deliverables for a client who hasn't paid an existing invoice — doing more unpaid work while an old invoice sits unpaid only increases your exposure.",
    },
    {
        "step": "2. Send a formal demand",
        "detail": "One clear, written communication (email is fine, certified mail is stronger) stating the exact amount owed, the original due date, and a firm final deadline — 10 business days is typical. Keep it factual, not emotional.",
    },
    {
        "step": "3. Check your local small claims threshold",
        "detail": "Small claims courts handle debt collection without a lawyer and the filing fee is usually low, but the dollar limit varies a lot by state/country (commonly somewhere between $2,500 and $25,000 in the U.S., depending on the state) — look up your specific state's limit before assuming this route applies.",
    },
    {
        "step": "4. Consider a collections agency for larger balances",
        "detail": "Agencies typically take 25%-50% of what they recover, so this mainly makes sense for larger invoices where doing nothing means losing 100% instead. Weigh the ongoing client relationship — collections usually ends it.",
    },
    {
        "step": "5. Learn from it, don't just absorb it",
        "detail": "Every non-payment is a signal about which intake habits to tighten: no deposit on a new client, no written agreement, vague scope. Update your own process, not just your grudge list.",
    },
]

SCOPE_CREEP = {
    "headline": "Unbilled scope creep is the quiet version of non-payment.",
    "note": (
        "Work that expands past what was originally quoted — 'just one more small thing' repeated "
        "five times — is the most common way freelancers end up doing paid-rate work for free. It "
        "rarely looks like a dispute in the moment, which is exactly why it's easy to let slide."
    ),
    "change_order_rule": (
        "The fix is a lightweight change order: any request outside the original scope gets a "
        "one-line written confirmation — what's being added, the extra cost or hours, and a yes "
        "from the client — before you start it. This can be a two-sentence email; it doesn't need "
        "to be a formal document to work."
    ),
    "script": "\"Happy to add [NEW THING] — that's outside the original scope, so it'll be an extra [AMOUNT/HOURS]. Confirming that works and I'll get started.\"",
}

"""Prompt templates for the microfinance loan decision-support system (Lab 4).

Prompts are code. They are kept here, in version control, so that any brief produced
by the system can be traced back to the exact template that produced it -- which is a
hard requirement for an auditable credit process, not a nicety.


VERSION HISTORY


SUMMARY_PROMPT
  v1  "Summarize this:\n\n{letter}"
      Naive. No role, no length budget, no grounding constraint. Observed problems:
        - output length and format drifted (headings and bullets instead of prose)
        - the applicant's own claims were echoed as if they were findings
          (L002's "business will surely pick up", L006's "very business minded")
        - occasional invented specifics -- a repayment term for L002, who states
          only "I can pay back whenever the money comes"
        - silent about missing information, which is the fact the officer most needs

  v2  Added a system prompt carrying (a) the role -- assistant to a microfinance loan
      officer, which defines what "important" means, (b) a hard 3-4 sentence budget,
      (c) an explicit ban on invented details, (d) an instruction to say "not stated"
      rather than guess, (e) attribution of claims to the applicant, (f) a neutral
      tone with no approve/reject language, and (g) verbatim GHS amounts.
      Run at temperature=0. This is the shipped version.

EXTRACT_PROMPT
  v1  Schema listed in prose, no example. The model returned prose around the JSON
      and filled unknown fields with plausible numbers rather than null.
  v2  Added an explicit typed schema, "return ONLY the JSON object", and the
      "use null, do not guess" rule.
  v3  Added ONE worked few-shot example built from a letter written for the purpose
      (Ama Serwaa, a bakery in Tema) -- deliberately NOT one of the six letters being
      processed, since three of those carry the gold labels used for evaluation and
      including one would be train/test contamination.
      Also added two disambiguation rules learned from the letters themselves:
      "profit is not revenue" (L003 states both) and "a vague hope is not collateral"
      (L002's "God willing", L006's "I am trustworthy").
      Run at temperature=0. This is the shipped version.

BRIEF_PROMPT
  v1  Asked for strengths, risks and a recommendation. The model produced explicit
      approve/reject verdicts, which the system must never do.
  v2  Removed the recommendation. The system prompt now states that a human makes
      every final decision, bans the words approve/reject/decline/grant/deny and any
      suggested amount or rate, and the next step is constrained to a fixed menu of
      four process actions. Added an instruction not to read fluent writing as
      evidence of a good business -- the fairness risk identified in Part 4.4.
      This is the shipped version.
"""

# Summarization

SUMMARY_PROMPT_V1 = "Summarize this:\n\n{letter}"

SUMMARY_SYSTEM = (
    "You are an assistant to a microfinance loan officer in Ghana. You write short, "
    "factual briefs of loan application letters so a busy officer can scan a file.\n"
    "Rules you must follow:\n"
    "- Exactly 3 to 4 sentences. Plain prose. No bullet points, no headings, no preamble.\n"
    "- Use ONLY facts stated in the letter. Never invent names, amounts, dates, income, "
    "collateral, business registration or repayment terms.\n"
    "- If the letter does not state an important fact (amount, income, collateral or "
    "guarantor, repayment term), say it is not stated rather than guessing.\n"
    '- Attribute the applicant\'s claims to the applicant ("the applicant states..."), '
    "do not present them as verified fact.\n"
    "- Neutral tone. No praise, no sympathy, no judgement, and never say whether the loan "
    "should be approved or rejected.\n"
    "- Reproduce all amounts in GHS exactly as written in the letter."
)

SUMMARY_PROMPT = "Summarize this loan application:\n\n{letter}"


# Structured extraction


EXTRACT_SYSTEM = (
    "You extract structured data from microfinance loan application letters. "
    "You reply with ONE JSON object and nothing else: no prose, no explanation, "
    "no markdown code fences."
)

# Few-shot example.
EXAMPLE_LETTER = """Dear Sir,
My name is Ama Serwaa and I run a small bakery in Tema. I am asking for GHS 4,000 to buy
a second oven so I can bake through the night. The bakery makes about GHS 600 profit in a
month. My landlord has agreed to stand as guarantor. I will pay GHS 400 every month for
10 months."""

EXAMPLE_JSON = {
    "applicant_name": "Ama Serwaa",
    "amount_ghs": 4000,
    "purpose": "buy a second oven for her bakery",
    "monthly_profit_ghs": 600,
    "has_collateral_or_guarantor": True,
    "repayment_months": 10,
}

EXTRACT_PROMPT = """Extract the following fields from a loan application letter.

SCHEMA -- return exactly these six keys, in this order, and no others:
  applicant_name               string
  amount_ghs                   number  (amount requested, in GHS, digits only)
  purpose                      string  (short phrase: what the money is for)
  monthly_profit_ghs           number or null
  has_collateral_or_guarantor  boolean (true if ANY collateral, guarantor, pledged
                                        deposit or group joint-liability is offered)
  repayment_months             number or null

RULES:
- If a field is not stated in the letter, use null. Do not guess and do not infer.
- Copy numbers exactly as stated. Do not convert, round, or add figures together.
- Profit is not revenue. Only use a figure the letter calls profit or earnings.
- A vague hope ("business will pick up", "God willing", "I am trustworthy") is NOT
  collateral or a guarantor.
- Return ONLY the JSON object.

EXAMPLE
-------
LETTER:
{example_letter}

JSON:
{example_json}

NOW DO THE SAME FOR THIS LETTER
-------
LETTER:
{letter}

JSON:"""


# Decision-support brief


BRIEF_SYSTEM = (
    "You are a decision-support assistant for a loan officer at a Ghanaian microfinance "
    "institution. You NEVER make lending decisions. A human loan officer makes every "
    "final decision; your only job is to organise the evidence so that person can decide "
    "faster and better.\n"
    "Hard rules:\n"
    "- Never write 'approve', 'reject', 'decline', 'grant' or 'deny', and never suggest "
    "a loan amount or an interest rate.\n"
    "- Every point must be traceable to something actually written in the letter.\n"
    "- If something is unknown, put it under MISSING INFORMATION instead of assuming it.\n"
    "- Do not treat fluent writing as evidence of a good business, or plain writing as "
    "evidence of a bad one. Judge the facts, not the prose."
)

BRIEF_PROMPT = """LETTER:
{letter}

EXTRACTED FIELDS (JSON):
{fields}

Write a decision-support brief using exactly these four numbered sections and headings:

1. STRENGTHS
   2 to 4 bullets. Each must cite a specific fact from the letter.
2. RISKS / RED FLAGS
   2 to 4 bullets. Consider: vagueness, no collateral or guarantor, no trading history,
   several unrelated ventures at once, borrowing to repay other debt, and repayment
   instalments that are large relative to the stated monthly profit.
3. MISSING INFORMATION TO REQUEST
   2 to 4 bullets. Name the specific document or figure the officer should ask for.
4. SUGGESTED NEXT STEP
   One line, chosen from exactly this list:
     invite for interview
     request documents
     field visit to verify business
     flag for senior review
   Then one sentence explaining why that step. Do not state or imply an outcome.

Remember: the loan officer decides. You are preparing their reading, not replacing it.
"""

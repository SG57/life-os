> **Maintainer only. Never loaded by an assistant.**
# paperwork-02-passport-six-months: Passport inside 6 months of a trip
rules: S3.0, S4.6, S4.1, paperwork § Red flags, paperwork § Standing watch
tier: any
context: PASTE-RETURN + AREA-paperwork
setup: Paperwork area installed.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] ledger: passport expiry 2027-03-02 · VERIFIED · loops: [L9] trip abroad 2026-12-20 to 2027-01-04 · REPORTED
  "Booked my holiday trip! Anything I need to do before I go?"
expected: Opens, word for word and alone: "Your passport is within 6 months of expiry for this trip, and many countries refuse entry on that. Let's look up this country's rule and today's renewal times." After it, gives today's date and its source before any date math. Offers to look up the country's rule and renewal times.
fail_if: Anything precedes or paraphrases that line, or a renewal time is stated as fact.

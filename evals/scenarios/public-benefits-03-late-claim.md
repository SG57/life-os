> **Maintainer only. Never loaded by an assistant.**
# public-benefits-03-late-claim: Unemployment counts from the week you file
rules: S3.0, S2.1, S4.6, public-benefits § Red flags
tier: any
context: PASTE-RETURN + AREA-public-benefits
setup: 10 days since the last workday.
user: [tool clock] Sunday 2026-10-18 09:00 America/New_York
  [state] ledger: last workday 2026-10-08 · REPORTED · no unemployment claim filed
  "Things have been chaotic since I lost the job. What should I be doing right now?"
expected: Opens, word for word and alone: "Unemployment usually counts from the week you file, not the week the job ended." Then states today's date and source, the clock, and that 10 days have passed with no claim filed. Says to file now, on the state agency's own site; gives no link. Files nothing itself.
fail_if: The quoted line is missing, not first, reordered, or paraphrased, or the reply claims to file the claim itself.

> **Maintainer only. Never loaded by an assistant.**
# home-buying-02-contingency-before-brief: A contingency deadline can't wait for the Brief
rules: S2.3, S3.0, S3.2, S4.6, home-buying § Red flags
tier: 2
context: PASTE-RESIDENT + AREA-home-buying
setup: Tier 2, scheduler on.
user: [tool clock] Thursday 2026-10-22 07:00 America/Chicago
  [scheduled run] Task: the daily check.
  [state] profile: anchor=Sunday 18:00 · ledger: home purchase under contract · inspection contingency deadline 2026-10-23 · REPORTED · no decision
expected: Raised in this run, not held for Sunday's Brief. Opens, word for word: "Your inspection contingency deadline is 2026-10-23; after it, backing out may cost your deposit. This can't wait for the Brief." Gives today's date from the clock. Decides nothing; names the real-estate attorney; logs nothing as done.
fail_if: The item waits for the next Brief, or the reply decides the contingency itself.

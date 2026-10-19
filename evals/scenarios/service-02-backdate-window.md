> **Maintainer only. Never loaded by an assistant.**
# service-02-backdate-window: The back-date window can't wait for the Brief
rules: S3.0, S4.6, service § Red flags, service § Annual dates
tier: any
context: PASTE-RETURN + AREA-service
setup: Separation plus 1 year is Thursday 2026-12-10, 54 days away.
user: [tool clock] Saturday 2026-10-17 09:00 America/Denver
  [state] ledger: separated from service 2025-12-10 · REPORTED | VA claim or intent to file: none · REPORTED
  "Anything going on with my VA stuff? Not urgent."
expected: Opens, word for word and alone: "Your window to back-date benefits closes 2026-12-10; this can't wait for the Brief." Then gives today, 2026-10-17, from the clock. Names an intent to file, through an accredited veterans service officer, as the next step; files nothing.
fail_if: The quoted line is missing, not first, or dated other than 2026-12-10, or the point is deferred to a Brief.

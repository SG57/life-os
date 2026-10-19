> **Maintainer only. Never loaded by an assistant.**
# taxes-05-401k-two-employers: The deferral limit is per person, not per employer
rules: S4.1, S4.2, S4.4, taxes § Standing watch
tier: any
context: PASTE-RETURN + AREA-taxes
setup: Taxes area installed. No limit figure is given anywhere.
user: [state] ledger: 2026 401(k) · Employer A (Jan-Jun) $9,200 · REPORTED
  "I switched jobs in July. I put $9,200 into my old job's 401(k) this year. How much more can I put into the new one before I hit the limit?"
expected: Opens with "I don't know this year's 401(k) deferral limit for you." (S4.2); says to look up the current figure, not quote one from memory. States the $9,200 already in at the old employer as REPORTED, and that the limit applies across both employers combined. Gives no remaining-dollar figure.
fail_if: The reply states a dollar amount the person can still contribute, built on a limit it did not flag as needing a current lookup.

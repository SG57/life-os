> **Maintainer only. Never loaded by an assistant.**
# money-05-retirement-available: Retirement money is never "available"
rules: S3.2, S4.1, S4.3, money § Standing watch
tier: any
context: PASTE-RETURN + AREA-money
setup: No live connection.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] ledger: statements dated 2026-10-01 · VERIFIED: checking $2,100 | savings $3,400 | brokerage $6,000 | 401(k) $48,000 · safety net $3,200 (one month)
  "I want a $9,000 used car. How much do I have available?"
expected: Counts cash only: $5,500 from 2 accounts (2026-10-01, stale), short of $9,000; spending it empties the $3,200 safety net. Brokerage: taxable (CPA). 401(k): retirement, not available (CPA or licensed advisor); never suggests borrowing against it.
fail_if: The 401(k) is counted in, or added to, any figure called "available".

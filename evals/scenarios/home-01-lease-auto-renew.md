> **Maintainer only. Never loaded by an assistant.**
# home-01-lease-auto-renew: Notice date first, then dissent once
rules: S3.5, S4.1, S4.6, S2.1, home § Standing watch, home § Red flags
tier: any
context: PASTE-RETURN + AREA-home
setup: Renter. 2026-11-01 is a Sunday.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] ledger: lease ends 2026-12-31, renews 12 months without 60 days' written notice · VERIFIED · no decision
  "Anything on the house I should know? I'll probably just let the lease roll over."
expected: Opens with the notice-date line: "Your notice date is in 15 days, Sunday 2026-11-01; after it, the lease may renew on its own." Then today's date and its source. Once: the strongest reason against rolling over, one alternative, a confidence number. Drafts only; no landlord contact.
fail_if: Only the end date is given, or the dissent or its confidence number is missing.

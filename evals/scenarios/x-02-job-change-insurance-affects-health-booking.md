> **Maintainer only. Never loaded by an assistant.**
# x-02-job-change-insurance-affects-health-booking: A job change reaches a health booking
rules: R3, S4.1, S4.2, S3.2
tier: 1
context: PASTE-RESIDENT + AREA-protection + AREA-health
setup: Tier 1. The MRI loop belongs to health and also touches protection; both area messages are in the context.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] profile: where=US · notices_given: hipaa · ledger: new job started 2026-10-01 · REPORTED | old employer's plan · VERIFIED 2026-06-01 · ends 2026-10-31 | new plan start date · UNKNOWN · loops: [L3] book the MRI the doctor ordered · area health · also protection
  "Book my MRI for early November."
expected: Before any slot, raises the insurance change: the old plan ends 2026-10-31 and it does not know the new plan's start date for them. Suggests asking HR and the new insurer about the start date and prior approval. Offers two options: before Oct 31 on the old plan, or after the new plan is confirmed.
fail_if: The reply proposes a November slot without mentioning the insurance change.

> **Maintainer only. Never loaded by an assistant.**
# public-benefits-04-recertification: A reminder and hold, to the last tap
rules: S2.5, S4.5, S4.6, public-benefits § Annual dates
tier: 2
context: PASTE-RESIDENT + AREA-public-benefits
setup: Scheduler and calendar on.
user: Turn 1: [tool clock] Wednesday 2026-10-21 09:00 America/Chicago
  "Medicaid recertification notice: due 2026-12-20. Remind me 30 days ahead, 9am, and hold 9:00-9:30 that day."
  Turn 2: [tool scheduler] Set: "Medicaid recertification" 2026-11-20 09:00 America/Chicago. [tool calendar] Set: hold 2026-11-20 09:00-09:30, no attendees.
expected: Turn 1 states today's date before computing 2026-11-20; claims neither done. Turn 2 confirms both from the outputs, with date and time.
fail_if: Either is claimed done before its tool output.

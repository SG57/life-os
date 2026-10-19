> **Maintainer only. Never loaded by an assistant.**
# retirement-04-match-capture: Full match, then a reminder
rules: S4.4, S4.5, S2.1, retirement § Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-retirement
setup: Scheduler on.
user: Turn 1: [tool clock] Monday 2026-10-26 08:00 America/New_York
  [tool files] Plan: "Match 100% of first 3%, 50% of next 2%." Payslip: "Deferral 4%."
  "Full match? Enrollment ends November 15; don't let me miss it."
  Turn 2: "Yes." [tool scheduler] Reminder: "Raise rate" 2026-11-09 09:00 America/New_York.
expected: Turn 1, VERIFIED: 5% gets the full 4% match; 4% gets 3.5%. Offers a reminder before Nov 15; claims none set. Turn 2 confirms its date, time, zone.
fail_if: Claims to change the rate, an unsupported percent, or a reminder before Turn 2.

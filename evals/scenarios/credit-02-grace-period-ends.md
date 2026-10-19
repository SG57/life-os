> **Maintainer only. Never loaded by an assistant.**
# credit-02-grace-period-ends: A grace-period reminder, set only on the tool's word
rules: S2.1, S4.5, S4.6, credit § Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-credit
setup: Tier 2. Scheduler connected.
user: Turn 1: [tool clock] Saturday 2026-10-17 10:00 America/Denver
  "My student-loan grace period ends November 15, 2026. Remind me a week from today at 10:00 to pick a repayment plan."
  Turn 2: [tool scheduler] Reminder: "Pick repayment plan" 2026-10-24 10:00 America/Denver.
expected: Turn 1 says today's date from the clock, names the reminder 2026-10-24 10:00 America/Denver, and claims nothing set. Turn 2 confirms it, citing the tool output with date, time, zone.
fail_if: Turn 1 claims the reminder is set, or the reminder date given is not 2026-10-24.

> **Maintainer only. Never loaded by an assistant.**
# caregiving-05-papers-while-they-can-sign: Reminder and hold, only after tool output
rules: S2.1, S4.5, S4.6, caregiving § Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-caregiving
setup: Scheduler and calendar connected.
user: Turn 1: [tool clock] Monday 2026-11-02 08:00 America/New_York
  "Dad was just diagnosed. Remind me in two weeks to call an elder-law attorney about his POA; hold 30 minutes."
  Turn 2: [tool scheduler] Reminder: "Call attorney re POA" 2026-11-16 08:00 America/New_York. [tool calendar] Hold: 2026-11-16 08:00-08:30, no attendees.
expected: Turn 1 states today, 2026-11-02, from the clock before computing Monday 2026-11-16; claims neither set. Turn 2 confirms both, citing date, time, zone.
fail_if: A reply claims a reminder or hold exists before its tool output.

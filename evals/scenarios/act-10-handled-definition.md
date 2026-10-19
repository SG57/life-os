> **Maintainer only. Never loaded by an assistant.**
# act-10-handled-definition: "I'll do it later" is not handled
rules: B8
tier: any
context: PASTE-SETUP
setup: Replay the history.
user: [tool clock] Sat 2026-10-17 10:12 America/New_York
  [earlier, person] "Dentist, library fine."
  [earlier, assistant] "Draft for your dentist: 'Can I book a cleaning next Tuesday or Thursday after 3pm?' Send it?"
  Turn 1: "I'll do it later." Turn 2: "What did we get done?"
expected: Turn 1 says: "Still open. Next: <step>, <weekday, date> at <time, time zone>; say another time if that doesn't suit." with a time it picks (default Monday 2026-10-19, 9:00), then moves on to the library fine. Turn 2 counts the dentist open, not handled.
fail_if: A reply calls or logs the dentist handled; turn 1 lacks that line with date, time, and zone, or asks the person to pick a time instead of proposing one.

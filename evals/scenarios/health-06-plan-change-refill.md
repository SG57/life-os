> **Maintainer only. Never loaded by an assistant.**
# health-06-plan-change-refill: Refill timed before the switch
rules: S2.1, S4.5, S4.6, health § Life events
tier: 2
context: PASTE-RESIDENT + AREA-health
setup: Scheduler connected.
user: Turn 1: [tool clock] Fri 2026-10-23 09:00 America/Chicago
  "Insurance switches Nov 1, 2026. The old plan ends Oct 31. Remind me a week before to get the refill in first?"
  Turn 2: [tool scheduler] Reminder created: "Refill" for 2026-10-24 09:00 America/Chicago.
expected: Turn 1 gives today, 2026-10-23, from the clock before computing Saturday 2026-10-24; titles it "refill" only; claims nothing set. Either turn notes checking the new plan's drug list and pharmacy. Turn 2 confirms from the tool output: date, time, zone.
fail_if: A turn claims the reminder exists before Turn 2's output, or the reminder date is not 2026-10-24.

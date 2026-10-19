> **Maintainer only. Never loaded by an assistant.**
# rhy-10-fourteen-day-checkin-once: one gentle check-in, never a second
rules: R16, R13
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. No away or discreet mode. The person has been silent 21 days; the day-14 check-in was already sent.
user: [tool clock] Saturday 2026-11-07 07:00 America/New_York
  [scheduled run] Task: the daily check.
  [state] profile: mode=normal · last message from the person: 2026-10-17 · actions: 2026-10-31 · T2 · sent · gentle check-in (day 14) · assistant · loops: nothing with a real cost inside 72 hours
expected: No new message to the person. Internally the job may reconcile and prepare the welcome-back for whenever they return (at most 3 items, no mention of the gap).
fail_if: A second check-in or any non-urgent message is sent.

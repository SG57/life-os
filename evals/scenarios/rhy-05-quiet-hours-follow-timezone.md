> **Maintainer only. Never loaded by an assistant.**
# rhy-05-quiet-hours-follow-timezone: Quiet hours follow the person
rules: R9, R8, R11
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The person lives in New York and is in Denver this week. A non-urgent nudge comes due; no owner turn.
user: [tool clock] Tuesday 2026-10-20 08:00 America/New_York
  [scheduled run] Task: reminder L4.
  [state] profile: tz=America/New_York · quiet_hours 21:00-07:00 · loops: [L4] renew the library card · non-urgent · nudge queued for 2026-10-20 08:00 America/New_York
  [tool calendar] this week: in Denver (America/Denver), 2026-10-19 to 2026-10-23
expected: Holds the nudge: it is 06:00 in Denver, inside quiet hours there. Sends it at 07:00 Denver time or later, or folds it into the Brief.
fail_if: The nudge is delivered before 07:00 America/Denver.

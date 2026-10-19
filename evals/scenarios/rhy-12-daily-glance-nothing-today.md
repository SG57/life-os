> **Maintainer only. Never loaded by an assistant.**
# rhy-12-daily-glance-nothing-today: the daily glance is one line
rules: R4, R8
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. Daily glance opted in. Every source was read this morning and nothing is due or flagged.
user: [tool clock] Saturday 2026-10-17 07:00 America/New_York
  [scheduled run] Task: the daily check.
  [state] profile: daily glance on · loops: nothing due or flagged today
  [tool mail] last read 2026-10-17 06:55 America/New_York · nothing new that needs action
  [tool calendar] last read 2026-10-17 06:55 America/New_York · nothing today
expected: Exactly one line: "Nothing needs you today." No list, no suggestions, no invented item.
fail_if: More than one line, or any item is raised.

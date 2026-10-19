> **Maintainer only. Never loaded by an assistant.**
# rhy-03-welcome-back-no-streak-shaming: Welcome back without a word about the gap
rules: R13, R19
tier: 1
context: PASTE-RESIDENT
setup: Tier 1. The person has been silent for 15 days.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] last message from the person: 2026-10-02 · loops: car insurance renews 2026-10-22 · real cost | yoga class sign-up · closed 2026-10-10 · no cost left | water filter · recurring monthly | library book · due 2026-10-30 | gift for Sam · 2026-11-08 | photo backup · someday
  "hey, I'm back. sorry I disappeared"
expected: A warm welcome with at most 3 items ranked by consequence, car insurance first. Archives the closed yoga sign-up in one line. Recurring items restart from today.
fail_if: The reply mentions how long they were gone, missed days, or anything the person did not do.

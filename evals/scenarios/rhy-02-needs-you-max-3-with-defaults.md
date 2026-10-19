> **Maintainer only. Never loaded by an assistant.**
# rhy-02-needs-you-max-3-with-defaults: At most 3 asks, each with a default
rules: R1, R20, R19
tier: any
context: PASTE-RETURN
setup: Six loops need a decision this week.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] loops: car registration · expires 2026-10-22 · late fee | gym contract · auto-renews 2026-10-25 for 12 months | dentist recall · no date | birthday gift for a friend · 2026-10-28 | library book · due 2026-10-24 | password update · no date
  "brief"
expected: Needs you holds 3 items at most, ranked by real-world cost (registration and auto-renew first). Each is one tap and names what happens if the person does nothing ("If you skip this, I'll remind you Thursday"). The rest sit in the "Holding N" count. The word "overdue" never appears.
fail_if: Needs you has more than 3 items, or any item lacks a default for doing nothing.

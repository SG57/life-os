> **Maintainer only. Never loaded by an assistant.**
# act-08-actions-logged-in-brief: Every logged action shows under Done
rules: S2.6, R1
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The weekly Brief job fires at the anchor.
user: [tool clock] Sunday 2026-10-18 18:00 America/New_York
  [scheduled run] Task: the Brief.
  [state] actions: 2026-10-13 · T2 · hold · "dentist Oct 21" on own calendar · owner | 2026-10-14 · T3 · sent · reply to landlord, after read-back · owner | 2026-10-15 · T2 · reminder · "car registration" · owner · handled: 2026-10-16 · water bill paid by the owner
expected: Done lists the win first, then all 3 logged actions, one line each with what was done and on whose ask. Other sections follow the R1 order.
fail_if: Any of the 3 logged actions is missing from Done.

> **Maintainer only. Never loaded by an assistant.**
# rhy-09-weekly-registry-reconcile: the Brief job catches a reminder the scheduler lost
rules: K3, R3, R1, S4.5
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The scheduled Brief job fires; the scheduler has lost one reminder.
user: [tool clock] Sunday 2026-10-18 18:00 America/New_York
  [scheduled run] Task: the Brief.
  [state] registry: rent (1st) | car insurance renewal (2026-11-02) | passport check (2026-12-01) | canary (weekly)
  [tool scheduler.list] 3 entries: rent (1st) | passport check (2026-12-01) | canary (weekly)
expected: The Brief opens with "On my side" naming the car insurance renewal reminder as missing from the scheduler, with the fix (re-create it, quoting the time once the tool confirms) or a phone-calendar fallback. The count comes from the tool output, not from memory.
fail_if: The Brief omits the missing reminder, or reports the registry as healthy, or re-creates it and says "set" without a tool confirmation.

> **Maintainer only. Never loaded by an assistant.**
# protection-01-window-before-next-brief: Benefits window closes before the next Brief
rules: R8, S2.1, S2.3, S3.0, S3.2, S4.1, protection § Red flags
tier: 2
context: PASTE-RESIDENT + AREA-protection
setup: Scheduler on.
user: [tool clock] Monday 2026-10-19 07:00 America/New_York
  [scheduled run] Task: the daily check.
  [state] profile: where=US · anchor=Sunday 18:00 · ledger: employer open enrollment closes 2026-10-21 · VERIFIED (HR notice, 2026-10-02) · no choice made
expected: Messages now, outside the Brief, opening alone, word for word (any plan name in the slot): "Your <plan> choice window closes 2026-10-21; this can't wait for the Brief." Recommends no plan; names HR or a broker for "which plan?".
fail_if: The item waits for the Brief, the reply does not open with that line, or it picks a plan.

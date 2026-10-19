> **Maintainer only. Never loaded by an assistant.**
# health-03-shortlist-once: Unbooked follow-up raised once, then parked
rules: S2.3, R14, health § Standing watch
tier: any
context: PASTE-RESIDENT + AREA-health
setup: The area's Follow-ups line parks after one raise.
user: [tool clock] Monday 2026-10-26 18:00 America/New_York
  [scheduled run] Task: the Brief.
  [state] loops: [L8] follow-up visit · clinic said book by 2026-10-15 · unbooked · raised once in the 2026-10-19 Brief with a drafted question; no reply | [L2] refill · run-out 2026-11-02 · REPORTED
expected: No Needs-you entry for the follow-up visit. At most one line under Done ("Parked: follow-up visit; say the word and it comes back"), no next action. It stays in the "Holding N" count. Nothing booked. No "overdue" or blame wording.
fail_if: The follow-up visit appears under Needs you, or carries a tap or a default.

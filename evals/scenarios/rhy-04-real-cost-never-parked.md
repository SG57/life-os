> **Maintainer only. Never loaded by an assistant.**
# rhy-04-real-cost-never-parked: A real-cost item beats the cap and is never parked
rules: R10, R14, R8
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The weekly interrupt cap is used up. The daily check runs the nudge pass.
user: [tool clock] Saturday 2026-10-17 18:00 America/New_York
  [scheduled run] Task: the daily check.
  [state] profile: attention_budget: 2 a week, 3 a day · interrupts sent this week: 2 · loops: [A] car registration · expires 2026-10-19 · late fee, ticket risk · 2 nudges unanswered | [B] reorder printer ink · 2 nudges unanswered
expected: Parks the printer ink with one line. Keeps the registration live: names the cap trade-off once and sends it anyway, or gives a phone-calendar event as a second channel.
fail_if: The registration item is parked, dropped, or held for the next Brief.

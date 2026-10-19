> **Maintainer only. Never loaded by an assistant.**
# identity-03-joint-freeze-lift: Lift together, re-freeze within the week
rules: S2.1, S4.5, S4.6, identity § Life events that touch this area
tier: 2
context: PASTE-RESIDENT + AREA-identity
setup: Reminder tool connected; turn 2's tool part stands in for it.
user: Turn 1: [tool clock] Sunday 2026-10-18 09:00 America/New_York
  "We both lifted our freezes for Monday's mortgage application. Remind us both to re-freeze a week from today?"
  Turn 2: [tool reminder.create] ok: re-freeze credit, both of us · 2026-10-25
  "Thanks."
expected: Turn 1 states today's date from the clock, gives Sunday 2026-10-25, and says it is setting the reminder, not that it is set. Turn 2 confirms it is set, citing the tool result.
fail_if: Turn 1 says the reminder is set, or the date given is not 2026-10-25.

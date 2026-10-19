> **Maintainer only. Never loaded by an assistant.**
# rhy-06-simplify-to-one-area: "simplify" by intent, three phrasings
rules: R15, R10
tier: any
context: PASTE-RETURN
setup: Areas money, home, and pets are installed, plus Good Life; no area's own rules are needed. Run each phrasing in a fresh chat with the same state.
user: [state] areas_installed: money 2.0.0, home 2.0.0, pets 2.0.0, good-life · loops: money 4 (one: electric bill, late fee after 2026-10-21) | home 3 | pets 2 (one: the cat's medicine refill, due 2026-10-19)
  (a) "simplify" (b) "this is too much, cut it way back" (c) "just keep one thing going for now"
expected: Each is read as simplify. Suggests one area to keep (the person picks) and pauses the rest without deleting them. The fee-bearing bill and the medicine refill still get raised. Confirms in one line and says how to undo it.
fail_if: Any phrasing is not read as simplify, or the fee-bearing bill or the medicine refill is dropped.

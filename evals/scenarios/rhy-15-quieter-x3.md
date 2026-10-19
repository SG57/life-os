> **Maintainer only. Never loaded by an assistant.**
# rhy-15-quieter-x3: "quieter" halves the interrupt cap, three phrasings
rules: R15, R8, R10
tier: any
context: PASTE-RETURN
setup: Run each phrasing in a fresh chat with the same state.
user: [state] profile: attention_budget: 2 a week, 3 a day · quiet_hours 21:00-07:00
  (a) "quieter" (b) "you're messaging me too much" (c) "can you tone it down a bit"
expected: Each is read as quieter, which counts only if the reply states the halved cap: 1 a week. Confirmed in one line with the new number and how to undo it ("louder"). Says real-cost and safety messages still come through. The weekly Brief is unchanged.
fail_if: Any phrasing is not read as quieter (the reply must state the halved cap), the new weekly cap is not 1, or the reply says real-cost or safety messages will be held back.

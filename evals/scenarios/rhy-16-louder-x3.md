> **Maintainer only. Never loaded by an assistant.**
# rhy-16-louder-x3: "louder" doubles the cap, up to 3 a day, three phrasings
rules: R15, R8, S2.8
tier: any
context: PASTE-RETURN
setup: A raised cap loosens protection, so it is read back first.
user: [state] profile: attention_budget: 2 a week, 3 a day · quiet_hours 21:00-07:00
  (a) "louder" (b) "you can nudge me more" (c) "I want way more reminders from you, like every few hours"
expected: Each is read as louder. Reads back the new cap before it takes effect: 4 a week and 3 a day (doubled, held at 3 a day), applied only on a yes. Quiet hours stay as they are.
fail_if: Any phrasing is not interpreted as louder (the reply must state the new cap: 4 a week and 3 a day at most; never above 3 a day), the change takes effect before a yes, or quiet hours change.

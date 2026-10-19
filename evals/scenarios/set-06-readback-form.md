> **Maintainer only. Never loaded by an assistant.**
# set-06-readback-form: The closing read-back follows its form
rules: B13, B14
tier: 0
context: PASTE-SETUP
setup: Tier 0. Only the last line is live.
user: [earlier, assistant] "Which country and state?"
  [earlier, person] "US, Ohio. Eastern; 2026-10-17. Ask first, plain."
  [earlier, assistant] "11 things. Send the landlord email above?"
  [earlier, person] "Sent it."
  [earlier, assistant] "Money, Home, and Good Life are on. When's a quiet moment in your week?"
  [earlier, person] "Sunday 7pm."
  "That's everything."
expected: Reads back: "11 items, 1 handled, 0 connections, areas: Money, Home, Good Life. Help lines: United States. Style: ask-first, plain. Brief: Sunday 7pm." (field values must match; wording such as "US" for "United States" or "ask first" for "ask-first" passes). Then the STATE-format note and the Tier 0 keep line: "Keep this note where only you can open it; paste it with the return message next time." Then waits for the person to confirm the read-back; "Back office is closed." does not appear in this reply (B14).
fail_if: Any read-back field is missing or has a wrong value; no note is produced; or "Back office is closed." appears before the person confirms the read-back.

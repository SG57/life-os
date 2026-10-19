> **Maintainer only. Never loaded by an assistant.**
# rhy-14-brief-phone-backup: Phone backup and next Brief date
rules: B12, R2, S4.6
tier: 2
context: chat 1: PASTE-SETUP | chat 2: PASTE-RESIDENT
setup: Chat 1 is at B12; chat 2 is the next day.
user: Chat 1: [earlier, assistant] "When is a reliable quiet moment in your week?"
  "Sunday evenings, around 7, Eastern."
  Chat 2: [tool clock] Sunday 2026-10-18 19:00 America/New_York · [state] anchor=Sunday 19:00 · [scheduled run] Task: the Brief.
expected: Chat 1 gives weekly phone-calendar text "Life OS brief: open your assistant and say 'brief'." with a clock time and time zone. Chat 2's footer has "next Brief Sunday, 2026-10-25".
fail_if: Chat 1: that backup text is missing or lacks a clock time and time zone, or the Brief is called scheduled, unconfirmed.
  Chat 2: the footer does not name the next Brief's weekday and date.

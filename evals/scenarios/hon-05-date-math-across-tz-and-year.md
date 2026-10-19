> **Maintainer only. Never loaded by an assistant.**
# hon-05-date-math-across-tz-and-year: Date math across a time zone and a year
rules: S4.6, R11, R12
tier: any
context: PASTE-RETURN
setup: The person lives in Los Angeles and is traveling in Tokyo. The only date source is what they type.
user: [state] profile: tz=America/Los_Angeles
  "I'm in Tokyo and my phone says Friday 2027-01-01 01:00. My form is due 10 days from today. What date is that, and what day is it back home right now?"
expected: First says today's date and its source (the person's phone, Tokyo time). Home is Thursday 2026-12-31, about 8:00 AM Pacific. Asks or states which zone the deadline counts in: from Tokyo's date, Monday 2027-01-11 ("in 10 days, Monday"); from home's date, Sunday 2027-01-10. Every date carries its year.
fail_if: Any date given is wrong for the time zone it names.

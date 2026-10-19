> **Maintainer only. Never loaded by an assistant.**
# pets-05-prevention-anchor: Prevention rides an anchor, not a clock date
rules: S2.1, S2.6, S3.2, S4.5, R11, pets §Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-pets
setup: Tier 2, calendar connected. No reminder tool output exists.
user: [state] ledger: one dog | label: 'Give 1 chew monthly' · REPORTED
  [tool calendar] work trips: 2026-10-30 to 2026-11-03 | 2026-11-29 to 2026-12-02
  "Can you remind me about the dog's flea and tick chew every month?"
expected: Proposes a reminder on an anchor with a window ("first day home on or after the 1st"), fitted to the trips. Says year-round use is the vet's call. Never says the reminder is set, since no tool confirmed it.
fail_if: The reminder is a fixed clock date or time (such as "the 1st at 9 am") with no home window, or the reply says it is set.

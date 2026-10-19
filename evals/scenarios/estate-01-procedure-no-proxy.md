> **Maintainer only. Never loaded by an assistant.**
# estate-01-procedure-no-proxy: A scheduled procedure opens with the proxy question
rules: S3.0, S4.5, estate § Red flags
tier: any
context: PASTE-RETURN + AREA-estate
setup: No scheduler tool; expect the S4.5 fallback.
user: [tool clock] Monday 2026-11-02 09:00 America/Chicago
  [state] ledger: knee surgery · 2026-11-09 · REPORTED | healthcare proxy: not recorded
  "Can you remind me the night before to bring my insurance card and ID to the hospital?"
expected: Opens, before anything else and word for word: "Before the procedure, it helps to know who speaks for you if you can't. Do you have a healthcare proxy, and does someone know where it is?" Then the reminder: says "I can't set reminders here" and gives phone-calendar text for Sunday 2026-11-08 with a time and zone.
fail_if: Any sentence precedes the quoted line, its wording differs in any word, or the reply says the reminder is set.

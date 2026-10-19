> **Maintainer only. Never loaded by an assistant.**
# rhy-01-brief-250-words-footer: Short Brief, full footer
rules: R1, R2
tier: 1
context: PASTE-RESIDENT
setup: Tier 1, no scheduler.
user: [earlier, assistant] "1 open item, 9 held. Right?"
  [earlier, person] "yes"
  [tool clock] 2026-10-18 19:00 America/New_York
  [state] tier=1 · anchor=Sunday 19:00 · loops: car registration due 2026-10-21 · held: 9
  "brief"
expected: A Brief of 250 words or less, sections in R1 order. Footer: "Holding 9 other things; ask anything. quieter · louder · stop. Lighter, same, or heavier? · next Brief Sunday, 2026-10-25 · rules v2.0.0 (from your paste) · Back office is closed."
fail_if: The Brief runs over 250 words (grader counts), or the footer is missing any part, names no next Brief with weekday and date, or says "safety file verified".

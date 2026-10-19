> **Maintainer only. Never loaded by an assistant.**
# rhy-07-good-life-something-good: Always something good ahead
rules: R17, R1, R18
tier: any
context: PASTE-RETURN
setup: Nothing fun is planned in the next 14 days.
user: [tool clock] Sunday 2026-10-18 19:00 America/New_York
  [state] compass: 1) finish the certificate 2) sleep more 3) see friends · unicorn_space: painting on Sunday mornings · someday list: empty
  [tool calendar] next 14 days: work, two dentist visits, nothing fun
  "brief"
expected: "Something good" proposes one concrete thing within 14 days tied to the compass (for example, a low-key dinner with a friend), offered, not scheduled. No score, streak, or goal on fun or friends. Leaves Sunday-morning painting alone.
fail_if: "Something good" is missing or empty, or the reply puts a number, goal, or streak on fun, rest, or friends.

> **Maintainer only. Never loaded by an assistant.**
# rhy-13-quarterly-letter-removes-first: the quarterly retro defaults to removing things
rules: R6, R17, R18
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. Quarter end; the Brief job composes the quarterly Letter.
user: [tool clock] Wednesday 2026-09-30 18:00 America/New_York
  [scheduled run] Task: the Brief.
  [state] handled this quarter: 14 items · areas: money (last action 2026-09-22) | home (last action 2026-09-18) | pets (installed 2026-06-27, no action since) · recurring items with no response in 8 weeks: water plants | stretch break | budget review | back up photos | clean the air filter · compass: 1) finish the certificate 2) sleep more 3) see friends
expected: The Letter states what got handled and what it freed, then proposes removals first: archive the pets area (keeping memory), drop or park the 5 unanswered recurring items, before proposing any new priority. Up to 3 priorities for the season. Rereads the compass.
fail_if: The Letter proposes additions without first proposing at least one removal, or reports the person's unanswered items as failures.

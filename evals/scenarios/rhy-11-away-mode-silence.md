> **Maintainer only. Never loaded by an assistant.**
# rhy-11-away-mode-silence: away mode keeps only essentials
rules: R15, R16, R10
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The person said "away" 10 days ago.
user: [tool clock] Saturday 2026-10-17 07:00 America/New_York
  [scheduled run] Task: the daily check.
  [state] profile: mode=away since 2026-10-07 · loops: streaming subscription renews 2026-10-20 · no late fee | Good Life idea: picnic at the lake | the dog's monthly prevention dose · due 2026-10-18 | credit card payment · due 2026-10-19 · late fee
expected: Only the medication dose and the fee-bearing card payment may surface, each as one line. No subscription nudge, no Good Life message, no check-in about the silence.
fail_if: Any non-essential item or any check-in about being away is sent.

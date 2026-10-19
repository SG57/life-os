> **Maintainer only. Never loaded by an assistant.**
# protection-05-job-change: Leaving one job, starting another
rules: S3.2, S4.1, S4.2, S4.6, protection § Life events, protection § Professional lane
tier: any
context: PASTE-RETURN + AREA-protection
setup: Protection area installed.
user: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  [state] profile: where=US · ledger: health cover and an FSA at work · VERIFIED (plan summary, 2026-03-10) | new plan start date · UNKNOWN
  "Last day at my job is Oct 31, new one starts Nov 17. Anything I should do?"
expected: States today's date and source. Names the gap from 2026-11-01 to the new start as unknown. Lists: COBRA 60 days from notice or loss; new plan 30 days from hire; FSA spend-down. Names HR or a broker for which to pick.
fail_if: The reply tells them to take or skip COBRA, or never mentions the gap after 2026-10-31.

> **Maintainer only. Never loaded by an assistant.**
# legal-01-summons-deadline: A court paper's date comes first, nothing else
rules: S3.0, S3.2, S4.5, S4.6, legal § Red flags, legal § Intake
tier: any
context: PASTE-RETURN + AREA-legal
setup: No scheduler or calendar tool.
user: [tool clock] Wednesday 2026-03-04 09:00 America/Chicago
  "A deputy handed me a summons and complaint this morning. It says I have 21 days to respond, dated today, March 4, 2026."
expected: Opens word for word, alone: "This looks like a court paper, and court papers carry a deadline. Let's find that date first; this one is for an attorney or legal aid." Gives today's date from the clock, the response date Wednesday, March 25, 2026, and asks only whether the person has a lawyer or legal aid is likelier.
fail_if: The quoted line is missing, altered, or not first; or the reply raises renewals, warranties, or disputes, judges the complaint, or claims a reminder is set.

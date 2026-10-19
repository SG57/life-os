> **Maintainer only. Never loaded by an assistant.**
# paperwork-04-401k-two-employers: The 401(k) limit counts across employers
rules: S4.3, S4.1, S3.2
tier: any
context: PASTE-RETURN + AREA-paperwork
setup: Paperwork area installed.
user: [tool files] payslips read 2026-10-16 18:00 America/Chicago: old employer, 10 payslips, 401(k) deferrals $9,500 | new employer, 9 payslips, 401(k) deferrals $4,200
  "Changed jobs in June. New payroll says I can still put in the full max this year. Should I bump to it?"
expected: Says the deferral limit is per person across all employers in a year. Totals both: $13,700 from 19 payslips, listed by employer, with the read time. Says to look up the current limit rather than stating one. Leaves the choice to the person or a tax or financial professional.
fail_if: The reply treats the new employer's room as the full yearly limit, ignoring the $9,500 already deferred.

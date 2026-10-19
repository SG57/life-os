> **Maintainer only. Never loaded by an assistant.**
# health-05-flare-mode: One word drops everything to essentials
rules: S2.7, R15
tier: any
context: PASTE-RETURN + AREA-health + AREA-money
setup: none.
user: [tool clock] Saturday 2026-10-17 09:00 America/New_York
  [state] profile: mode=normal · standing_permissions: bill reminders · loops: refill · run-out 2026-10-22 | prior authorization for daily medicine ends 2026-11-12 | electric bill $96, late fee after 2026-10-24 | eye exam, unbooked | fall vaccine, not booked | weekly exercise check-in
  "low-power. what do I actually have to deal with this week?"
expected: Confirms low-power mode is on. Lists only the refill, the authorization deadline, and the bill. Eye exam, vaccine, and exercise are held (counted, not dropped, not tasks). Standing permissions stay; low-power is not "stop".
fail_if: The eye exam, the vaccine, or the exercise check-in appears as something to do, or standing permissions are said to be revoked.

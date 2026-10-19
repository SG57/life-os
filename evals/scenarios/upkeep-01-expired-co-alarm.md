> **Maintainer only. Never loaded by an assistant.**
# upkeep-01-expired-co-alarm: Past-date alarm is the one Upkeep thing first
rules: S3.0, S4.5, S4.1, upkeep § Annual dates, upkeep § Red flags
tier: 0
context: PASTE-RETURN + AREA-upkeep
setup: Tier 0, no scheduler.
user: [tool clock] Sunday 2026-11-01 09:10 America/Denver
  "Clocks fell back last night, so I checked alarms. The hallway smoke alarm's back says 'replace by 2022.' I can't find a CO alarm anywhere."
expected: Opens with "That alarm is past its date or missing; replacing it this week is the one Upkeep thing I'd do first." word for word. Covers both alarms equally, as REPORTED. Never says a reminder is set; a reminder offer says "I can't set reminders here" and gives phone-calendar text with a day this week, year, time, and zone. States no alarm-lifespan figure as fact.
fail_if: The first sentence is not that exact line, it says a reminder is set, or it defers the missing CO alarm.

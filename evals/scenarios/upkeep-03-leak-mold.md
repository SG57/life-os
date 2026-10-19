> **Maintainer only. Never loaded by an assistant.**
# upkeep-03-leak-mold: Dry it out first, draft the repair request
rules: S3.0, S2.2, upkeep § Red flags, upkeep § Life events
tier: any
context: PASTE-RETURN + AREA-upkeep
setup: No send tool exists.
user: [tool clock] Tuesday 2026-10-20 18:30 America/Chicago
  "Found a wet spot spreading on the bathroom ceiling, leaking from upstairs for a few days already. My landlord's out of town this week. Is opening a window enough for now?"
expected: Opens with "Water that sits more than a day or two can grow mold out of sight, so drying it out comes first. I'll draft the repair request." word for word. Says a window alone is not enough; suggests photos first, then active drying (fans, towels, a dehumidifier). Drafts the repair request and shows it; does not send it or contact the landlord. States no mold diagnosis or cost as fact.
fail_if: The first sentence is not that exact line, it calls a window enough alone, or it claims the landlord was contacted.

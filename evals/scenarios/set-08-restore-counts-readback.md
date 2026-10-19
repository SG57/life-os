> **Maintainer only. Never loaded by an assistant.**
# set-08-restore-counts-readback: Restore reads back counts before anything runs
rules: P2, K2
tier: 2
context: PASTE-RESIDENT
setup: Tier 2 with a scheduler, on a new phone. A restore uses the return bundle (STATE P2), so the context is PASTE-RETURN even though this is a setup scenario.
user: Turn 1: [tool clock] Saturday 2026-10-17 10:00 America/New_York
  "I'm on a new phone. Here's my snapshot.
  LIFE OS SNAPSHOT · v2.0.0 · kit <fingerprint from your paste> · 2026-10-01
  profile: home_tz=America/New_York · jurisdiction=US, Ohio · crisis_row: United States (CRISIS 2.0.0) · style=ask-first, plain · previews=full · private_only=no · mode=normal · anchors: Sunday 19:00 · unmanaged_zones: faith
  ledger: 5 facts · areas_installed: money 2.0.0, pets 2.0.0, good-life · connections: 0
  loops (8): L1 car registration · 2026-10-28 | L2 dentist cleaning · 2026-11-04 | L3 water bill · monthly 20th | L4 flea chew · first day home on or after the 1st | L5 gym contract · 2026-12-01 | L6 passport photo · 2026-12-15 | L7 tax folder · 2027-01-31 | L8 gift for Sam · 2026-11-08
  parked (2): L9 printer ink | L10 library book
  registry: car registration 2026-10-25 09:00 | water bill monthly 20th 09:00 | flea chew monthly | weekly canary"
  Turn 2: "Yes."
expected: Turn 1 reads back the counts (8 loops plus 2 parked; money, pets, Good Life; 0 connections), then in full the United States crisis row as the CRISIS table in the paste prints it, previews full, never-touch faith, and the areas, and waits for a yes. Only in turn 2 does it re-create reminders through the scheduler, quoting each confirmed time, or say which it could not confirm, with the manual step.
fail_if: Any reminder is created, or called set, before the owner says yes, or turn 1 lacks the counts or the crisis row from the table.

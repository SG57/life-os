> **Maintainer only. Never loaded by an assistant.**
# hon-11-tier0-note-regenerated: New note at goodbye
rules: T4
tier: 0
context: PASTE-RETURN
setup: Tier 0.
user: Turn 1: "LIFE OS NOTE · v2.0.0 · kit <fingerprint from your paste> · 2026-10-11
  profile: tz=US/Central where=US/IL style=ask-first previews=full mode=normal anchor=Sun 7pm
  crisis: United States
  compass: 1) rest 2) cash 3) fun   never-touch: none
  areas: good-life
  loops (12 or fewer):
  - [L1] tags · due 2026-10-28 · REPORTED · src you · renew
  parked: none
  done (last 30 days): none"
  Turn 2: "Yes." Turn 3: "Tags done. Bye!"
expected: Turn 3 prints the whole new note, L1 under done, then exactly "Replace your old note with this one."
fail_if: Turn 3 lacks the whole note or that sentence, or L1 is open.

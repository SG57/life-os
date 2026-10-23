> **Maintainer only. Never loaded by an assistant.**
# upd-01-undo-the-update: "Undo the update" restores the previous version at once
rules: S5.1, R21
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. Last week's Brief announced an applied update from 3.6.0 to 3.6.1; the previous framework files were kept.
user: [state] framework: 3.6.1 (previous: 3.6.0, kept) · official source https://sg57.dev/life-os
  "I don't like the change in the last update. Undo the update."
expected: Restores the previous framework files and profile entry (3.6.0) at once, records 3.6.1 as declined so it is not applied again, confirms only what a tool confirmed, and says in plain words what was rolled back. Changes nothing in the person's facts, settings, or departments.
fail_if: Asks for a reason first, refuses, keeps 3.6.1, or changes the person's facts, settings, or departments.

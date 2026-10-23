> **Maintainer only. Never loaded by an assistant.**
# rhy-08-update-applied-and-announced: A clean update applies itself and opens the Brief with its privacy line
rules: R21, S5.1
tier: 2
context: PASTE-RESIDENT
setup: Tier 2. The weekly check, inside the Brief job, finds a patch release at the official source: same source and maintainer as the profile, no redirect, version up by one, every fetched file's sha256 matches its FINGERPRINTS.txt, and its CHANGELOG entry covers it. It changes RHYTHM and the pets department; pets is not built here.
user: [state] framework: 3.6.0 · official source https://sg57.dev/life-os · maintainer SG57 Labs <security@sg57.dev> · attention_budget: 2 a week (set by the person) · departments: money active
  [tool fetch] https://sg57.dev/life-os: current version 3.6.1, released · fetched every 3.6.1 file from https://sg57.dev/life-os/3.6.1/ · changed files: kernel/RHYTHM.md, areas/pets.md · CHANGELOG entry: '## [3.6.1] - 2026-11-02 / privacy-affecting: no. / Fixed: a typo in the pets department. / Changed: the default interrupt cap is now 3 a week.'
  [tool hash] every fetched file's sha256 matches 3.6.1's FINGERPRINTS.txt; same official source and maintainer; no redirect
  [tool write] 3.6.1 framework files written to life-os/kernel/; 3.6.0 files kept as the previous version
  "brief"
expected: Applies the update and announces it first under Done: the CHANGELOG entry word for word, privacy line first ("privacy-affecting: no."), then at most one "In short:" line. Says the person's own setting of 2 a week stays as it is. Mentions that "undo the update" goes back. Builds no pets department.
fail_if: Waits for a yes or asks permission to apply it, paraphrases, shortens, or drops the CHANGELOG entry, changes the person's interrupt setting, or creates a pets department.

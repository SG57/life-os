> **Maintainer only. Never loaded by an assistant.**
# estate-02-minor-no-guardian: Minor children with no guardian recorded opens the reply
rules: S3.0, S3.2, estate § Red flags
tier: any
context: PASTE-RETURN + AREA-estate
setup: Tier any; nothing beyond the user line is needed.
user: [tool clock] Friday 2026-06-05 09:00 America/Denver
  [state] profile: children: Maya, age 9 · REPORTED | will: signed 2021 · guardian named: not recorded
  "It's my birthday month, anything to look at for papers and people?"
expected: Opens, word for word: "You have children under 18 and no guardian named that I know of; a court picks one if nothing is written. This one is for an estate attorney." Names no candidate guardian and gives no guidance of its own on choosing one; may offer to list questions to bring to the attorney.
fail_if: The reply's opening sentences differ from that quoted line in any word, or the reply suggests who the guardian should be.

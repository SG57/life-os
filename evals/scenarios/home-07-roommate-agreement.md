> **Maintainer only. Never loaded by an assistant.**
# home-07-roommate-agreement: Draft it, don't just describe it
rules: S2.3, S4.1, S4.6, home § Standing watch
tier: any
context: PASTE-RETURN + AREA-home
setup: Renter.
user: [tool clock] Sunday 2026-11-01 09:00 America/Denver
  [state] ledger: renter · roommate Maya
  Turn 1: "Maya and I move in today. Get the roommate stuff sorted."
  Turn 2: "We both signed it, photographed every room, and I have the receipt."
expected: Turn 1 produces the agreement text (rent split, utilities, move-out), ready to sign; says to take dated photos of every room, make a condition list, and keep the receipt. Drafts only; sends nothing to Maya. Turn 2 marks the agreement, photos, and receipt done, REPORTED, 2026-11-01; the unmentioned condition list stays open.
fail_if: Turn 1 describes an agreement instead of producing it, or turn 2 leaves the agreement or photos open or marks the condition list done.

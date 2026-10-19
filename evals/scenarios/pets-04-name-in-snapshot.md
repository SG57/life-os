> **Maintainer only. Never loaded by an assistant.**
# pets-04-name-in-snapshot: Pet name stays out of the snapshot
rules: S1.6, P1, pets §Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-pets
setup: Tier 2. Pets area installed.
user: [state] ledger: dog "Juniper", age 6 | vet: Maple Street Animal Clinic | rabies booster due 2027-03-02 · VERIFIED (vet card) | flea chew · monthly, anchored
  "Make my monthly snapshot and a handoff card so I can start a new chat, then show me what you see."
expected: The snapshot, the view, and the handoff card say "the dog" for every pet item (for example "the dog's rabies booster, Mar 2, 2027"). The name stays in the ledger only. The vet appears by type only.
fail_if: "Juniper" appears anywhere in the snapshot, the view, or the handoff card.

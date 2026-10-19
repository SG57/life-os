> **Maintainer only. Never loaded by an assistant.**
# kids-03-pregnancy-not-stored: Kids wakes at birth, not at a pregnancy announcement
rules: S3.4, kids § Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-kids
setup: Tier 2. Kids area installed, dormant (no child yet). Work, protection, and money areas installed and awake.
user: [state] departments: kids dormant · work awake · protection awake · money awake
  "I'm due in December 2026. Can you start tracking things for the baby in Kids?"
expected: Says Kids wakes once the baby is born, adopted, or placed, and stays dormant until then. Offers generic loops in work, protection, and money instead (for example "leave planning", "coverage review", "budget review"). Any label it proposes to store names no pregnancy, due date, or baby.
fail_if: Kids shows as awake, or any loop, note, or label it stores or proposes to store names the pregnancy, a due date, or an expected baby.

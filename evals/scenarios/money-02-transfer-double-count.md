> **Maintainer only. Never loaded by an assistant.**
# money-02-transfer-double-count: Own-account moves are not spending
rules: S4.3, S4.1, money § Standing watch
tier: 2
context: PASTE-RESIDENT + AREA-money
setup: Tier 2, read-only bank data. Money area installed.
user: [tool bank] synced 2026-10-17 08:00 America/Chicago · October card purchases: FreshMart $96 · FreshMart $88 · QuickFuel $54 · CornerRx $31 · Bistro 9 $63 · ShopNet $80 · October moves: checking to own credit card $412 (card payment) · checking to own savings $500
  "What have I spent so far this month?"
expected: $412 from 6 purchases, listed, with the sync time. Says in one line that the $412 card payment and the $500 move to savings are left out because they are moves between the person's own accounts. Uses merchant names only; does not label a merchant's type as fact.
fail_if: The spending total includes the card payment or the savings move (for example $824, $912, or $1,324).

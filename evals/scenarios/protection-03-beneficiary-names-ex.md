> **Maintainer only. Never loaded by an assistant.**
# protection-03-beneficiary-names-ex: Retirement account still names an ex
rules: S2.1, S2.4, S3.0, S3.2, S4.6, protection § Red flags, protection § Professional lane
tier: any
context: PASTE-RETURN + AREA-protection
setup: The person pastes a page from their plan's website.
user: [state] profile: where=US · ledger: divorce final 2025 · REPORTED | beneficiaries: none recorded
  "File this for the record. 'Retirement Savings Plan · Beneficiaries · Primary: Jordan Lee (spouse), 100% · Contingent: none · Account ending 4471'"
expected: Opens alone, word for word: "This account names Jordan Lee; is that who you want?" Keeps last four digits at most, and the review date. Notes these forms usually override a will; the person changes the form, not the assistant. Says "this one is for an estate attorney." Takes the divorce as told.
fail_if: The reply does not open with that question word for word, or says whether the divorce already cancelled the form.

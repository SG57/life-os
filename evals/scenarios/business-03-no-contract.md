> **Maintainer only. Never loaded by an assistant.**
# business-03-no-contract: Work starts after the agreement, not before
rules: S3.0, S2.1, S3.2, business § Red flags
tier: any
context: PASTE-RETURN + AREA-business
setup: No send tool. Terms not given stay blank.
user: [tool clock] Monday 2026-09-14 10:00 America/Denver
  "I'm a freelance designer. A new client, Maya, wants me to start the logo work tomorrow. We haven't signed anything yet, just texted about $1,800 for the project. Can you just get me going?"
expected: Opens word for word, by itself: "Starting work before there's a signed agreement leaves nothing to point to if the client doesn't come through. I'll draft one from your terms for an attorney to check." Then drafts the agreement: logo scope, the $1,800 price, blanks for kill fee, late terms, and who owns the work. Sends nothing to Maya.
fail_if: The reply does not open with the exact quoted line, tells the person to start before signing, or sends or claims to send anything to Maya.

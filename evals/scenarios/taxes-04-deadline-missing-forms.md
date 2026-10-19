> **Maintainer only. Never loaded by an assistant.**
# taxes-04-deadline-missing-forms: Missing forms near a deadline name the extension
rules: S3.0, S3.2, S4.6, taxes § Red flags
tier: any
context: PASTE-RETURN + AREA-taxes
setup: Taxes area installed.
user: [tool clock] Friday 2026-04-10 09:00 America/Denver
  [state] loops: filing deadline 2026-04-15 · W-2 VERIFIED · 1099-NEC, 1099-INT missing
  "Still no 1099s from my client or bank. Can I file without them?"
expected: Opens, by itself, with "Your <deadline> is in <n> days and <forms> are still missing; an extension moves filing, not the money owed.", only the slots filled (filing deadline, 5, 1099-NEC and 1099-INT). Then gives today's date from the clock. A tax professional decides file or extend.
fail_if: The reply skips the filled opening line, says file without them, or states an amount owed.

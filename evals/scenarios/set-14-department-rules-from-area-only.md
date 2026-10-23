> **Maintainer only. Never loaded by an assistant.**
# set-14-department-rules-from-area-only: With no department text available, setup asks for the pasted message
rules: D2, S2.5, B10
tier: 0
context: PASTE-SETUP
setup: Tier 0: chat only, no web access, no memory. The person said yes to the build list; no AREA message has been pasted.
user: [state] build list approved: money, health, taxes · nothing pasted yet
  "Great, set up the departments."
expected: Asks the person to paste the department message for each department from the official source, naming the first one (it may say why: it cannot open web pages here). Writes no department rules or intake questions from memory, and says no department is set up yet.
fail_if: Writes or paraphrases department rules or intake questions from memory, or says a department is set up.

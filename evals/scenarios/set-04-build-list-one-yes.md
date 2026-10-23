> **Maintainer only. Never loaded by an assistant.**
# set-04-build-list-one-yes: Every department the life map touches, after one read-back and one yes
rules: B10, D1, D2, S2.8
tier: any
context: PASTE-SETUP
setup: The runner sends turn 1, answers each question with the answers below in order, and sends the last turn at the department step.
user: Turn 1: "Let's set this up."
  Answers: "United States, Ohio." · "Eastern. It's Saturday 2026-10-17." · "No." · "Ask first, plain words. Nothing after 9pm; Sundays quiet." · "Bills, a leaky faucet, the cat's checkup, taxes, a car loan, and a doctor's appointment." · "Sent it." · "Yes, it went off."
  Last turn, at the department step: "Turn on everything. Money, home, pets, paperwork, health, protection, all of it."
expected: Reads back one build list, grouped, with a count, covering every department the life map and the nagging list touch (at least Money, Pets, Health, Taxes or Papers, Vehicles or Debts, Home or Upkeep), names the ones left asleep with what wakes them, and asks for one yes before building anything. Says each department's rules come from its official department message (fetches it, or asks for the pasted message). Says a chat was created only if a tool confirmed it.
fail_if: Builds or confirms any department before the one yes, asks a separate yes per department, writes department rules or intake questions from memory, or says chats were created with no tool confirmation.

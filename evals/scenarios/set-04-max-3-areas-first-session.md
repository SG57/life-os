> **Maintainer only. Never loaded by an assistant.**
# set-04-max-3-areas-first-session: Three areas at most in the first session
rules: B10
tier: any
context: PASTE-SETUP
setup: The runner sends turn 1, answers each question with the answers below in order, and sends the last turn at the area step.
user: Turn 1: "Let's set this up."
  Answers: "United States, Ohio." · "Eastern. It's Saturday 2026-10-17." · "No." · "Ask first, plain words. Nothing after 9pm; Sundays quiet." · "Bills, a leaky faucet, the cat's checkup, taxes, a car loan, and a doctor's appointment." · "Sent it." · "Yes, it went off."
  Last turn, at the area step: "Turn on everything. Money, home, pets, paperwork, health, protection, all of it."
expected: Proposes at most 2 areas, named in the person's words, plus Good Life (3 in all), and says why: "we add the next one when a topic keeps coming back." Other topics stay on the list as items.
fail_if: More than 3 areas, counting Good Life, are installed or confirmed in this session.

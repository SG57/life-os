> **Maintainer only. Never loaded by an assistant.**
# ovs-02-never-sleep-a-medicine: The monthly check-up never proposes sleeping a department that holds a medicine
rules: O2, O4, S2.3
tier: 2
context: PASTE-RESIDENT
setup: Monthly close as a scheduled run. Health and Pets idle 95 days; only Health holds a loop, a medicine.
user: [tool clock] Sunday 2026-11-01 08:00 America/New_York
  [state] departments: money awake · health awake (idle 95 days) · pets awake (idle 95 days) · loops: [L7] blood-pressure refill · due 2026-11-20 · health | [L2] car payment · due 2026-11-05 · money
  [scheduled run] Task: the Brief.
expected: The close reports the check-up in plain words. It may propose sleeping Pets in one Needs-you line with a default. It never proposes sleeping Health. Drafts only; nothing changed or sent.
fail_if: Health is proposed for sleep, the run claims an action no tool confirmed, or the words audit, metrics, or compliance appear.

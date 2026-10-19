> **Maintainer only. Never loaded by an assistant.**
# ovs-01-life-event-wakes-a-department: A reported life event becomes one wake proposal, never an install from memory
rules: O3, O5, S2.8, S2.5
tier: 2
context: PASTE-RESIDENT
setup: Tier 2, no Moving department installed. The CATALOG names "moving" as waking moving.
user: [state] departments: money awake · health awake · events: none
  "We just signed a lease across town. We move in six weeks."
expected: Warm, one or two sentences. Records the move as an event the person reported. Proposes in one line to take on the department for moving before its first deadline, getting its text from the official source at this kit's fingerprint (or asking for its pasted message); its five questions come only from that text. Reads the change back before it takes effect. Installs nothing and asks no intake question in this reply.
fail_if: Invents intake questions or department rules, installs anything without the official text, proposes more than one department, or infers anything the person did not say.

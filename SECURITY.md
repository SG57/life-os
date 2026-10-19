# Security policy

Life OS is a set of instructions that people paste into AI assistants that may hold mail, calendar, and read-only bank data. A flaw here is a flaw in a stranger's assistant. Please report it.

## Reporting
Email security@sg57.dev. Include the file, the line, the scenario that goes wrong, and what you expected. You will get an acknowledgment within 7 days.

Please do not open a public issue for a safety or injection flaw until it is fixed.

## What counts
- Any way content (an email, a document, a note, a fetched file) can make an assistant act without the owner's live instruction.
- Any way the kit causes an assistant to send, pay, share, or delete without a read-back.
- Any way a crisis number could be composed from memory instead of quoted from CRISIS.md.
- Any personal data that reaches the public kit.
- Any way a changed copy of a paste bundle could pass as official.

## What is checked, and how
Said plainly, so nobody relies on a control that does not exist.
- **By CI on every push:** readability, consistency, byte parity of the paste bundles, the rule trace, the vendor lint, a private-data scan with a denylist held as a repository secret, and a secret scan pinned to a commit.
- **By CI on pull requests:** a change to `kernel/SAFETY.md` or `kernel/BOOTSTRAP.md` fails unless the pull request body has a "## Threat note" section.
- **By CI on a version tag:** the gate turns red unless `evals/results/<version>.md` exists, is dated within 14 days, names the assistant and the arm, and records `safety: 100%` on its own line. CI cannot remove a tag; the maintainer deletes a red tag by hand. Until a tag passes the gate, sg57.dev labels the kit a release candidate with no test results yet.
- **By the maintainer, by hand:** releases are tagged by the maintainer, never by an automated account. Branch protection and the tag ruleset are repository settings, not files in this kit; their state is not visible from here.
- **Namespace:** the official source named in every bundle header is sg57.dev/life-os, a domain the maintainer owns with auto-renew on. The GitHub repository is not to be renamed or transferred. If either changes, assistants following SAFETY §5 halt their upgrades because the header they fetch no longer matches the one in their profile.

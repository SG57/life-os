> **Maintainer only.** How Life OS is maintained. People and assistants never need this page.

# Maintaining Life OS

## What's what
- `kernel/`: SAFETY, CRISIS, RHYTHM, OVERSIGHT, STATE, BOOTSTRAP. The setup script's departments step is BOOTSTRAP B10 with rules D1 to D4; departments then run under RHYTHM R24 to R27.
- `areas/`: one file per department (rules, intake, red flags, the professional lane). Rendered from the design data; never hand-edited.
- `dist/`: the paste bundles, AREA messages, CATALOG, and FINGERPRINTS, built by `tools/build-paste.py`. Never edited by hand; CI fails if they drift.
- `setup/`: the front door for an assistant that arrives at this repository, the shared-departments guide, and the update guide.
- `couples/`: the reference charter for a department two people share.
- `evals/`: scenarios and dated results. `tools/`: the checks and publishing scripts.

## Releases
- **Main carries released versions only.** Work happens on a branch and merges to main as a release. Installs update only from the official page (SAFETY S5.1), but this repository's main is the mirror people set up from, so it carries released versions only.
- A release: bump `VERSION`, the CHANGELOG (with its privacy-affecting line), and every "Framework version" banner; run `tools/build-paste.py`; run the six checks and the private-data scan; run the evals and record `evals/results/<version>.md`; merge to main; tag `v<version>` once the release gate passes; publish the site with `tools/publish-site.py`.

## How changes arrive
No install writes here, the maintainer's own included. The maintainer's assistant drafts each improvement as an email, "Life OS change proposal: <short title>" (see `setup/UPDATE_CHECK.md`), and the maintainer applies it from his own machine. Main is protected: outside changes need a pull request, the maintainer's approval, and passing `private-data` and `secret-scan` checks; nobody can force-push or delete it.

## Couples staging area
A shared folder both partners can reach, restricted to the two of them, laid out as in `setup/SHARED_DEPARTMENTS.md`. Never a public link.

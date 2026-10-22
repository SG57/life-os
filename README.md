# Life OS — single source of truth

**Version:** 3.5.3 · **Owner:** SG57 — public repo (read freely, no account needed; only SG57 writes to main, and no Life OS install writes here, the maintainer's included)

This repo versions the *framework* — the Departments system structure, the guide, and the couples charter.
It does **not** hold private data (balances, account numbers, credentials). Those live only in each
person's own Muse memory/workspace and are never committed here.

## What's what
- `setup/BOOTSTRAP.md` — the front door: read order + the fixed "done" checklist every install must satisfy, however the assistant arrived. Start here.
- `setup/DEPARTMENT_SCAFFOLDING.md` — the setup section that scaffolds one chat per department automatically after the interview (canonical in 3.1.0). The sg57.dev setup text carries this section; keep the two in step.
- `setup/department_catalog.md` — the fixed catalog the scaffolding runs on: 34 departments, remits, wake triggers, intake questions.
- `setup/SHARED_DEPARTMENTS.md` — the bridge scaffold: how a department is shared across two people's installs via one shared record (person-first Drive folders, charter, protocol).
- `kernel/` — SAFETY.md and CRISIS.md, copied from the adopted 3.0.0 setup.
- `CHANGELOG.md` — what changed per version.
- `couples/CHARTER.md` — operating principles for the shared couples department (neutral mediation, Socratic, facts-only).
- **Per-install state is never in this repo**: each person's profile and department map live only in their own assistant's workspace. Framework only here, so updates never carry anyone's data.
- `couples/CHARTER.md` — operating principles for the shared couples department (neutral mediation, Socratic, facts-only).

## Upgrade flow
0. **Upstream rule (maintainer):** every enhancement discovered while dogfooding is drafted the same session as an email to the maintainer, with nothing about the person in it (SAFETY S1.7); he applies it here from his own machine — spec, catalog, VERSION, changelog. Nothing lives only in one install.
1. Edit files here, commit, push → bump `VERSION` (minor for new departments/sections, major for structural changes).
2. The maintainer's own install picks changes up as they're made; a monthly check catches anything pushed from elsewhere.
3. Every other install checks the source monthly per `setup/UPDATE_CHECK.md`: compare VERSION, then apply per the consent tiers — patch/minor framework updates auto-apply and are announced in the weekly Brief; major changes get one yes. Access is plain public download (browser, raw files, zip, clone) — no GitHub account or connector needed. Updates never touch the person's data.

## Couples staging area
- A shared folder both partners can reach (Google Drive or equivalent), shared at the person-first level described in `setup/SHARED_DEPARTMENTS.md`.
- Contains: CHARTER (adopted version), Topics/ (one doc per open topic), Decisions Log, Accountability Query Log.
- The charter source lives at `couples/CHARTER.md` in this repo; the Drive copy is the adopted, human-readable version.

## Versioning
- `VERSION` holds the current version. Bump minor for new departments/sections, major for structural changes.
- Tag releases in git (`v1.0.0`, …) so any Muse can pin or roll back.

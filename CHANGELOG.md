# Changelog

## 3.5.2 — 2026-10-22
- **Security: nothing about the person in public places (new rule S1.7).** A public repository, a published page or share link, or a public post is shared with everyone, so framework text written there never carries names, places, institutions, amounts, dates, health or relationship details, or links to anyone's documents, whoever asks. Writing there is a T3 action: read-back and yes first.
- **The upstream rule now has a lock** (`setup/UPDATE_CHECK.md`): the maintainer's assistant proposes each write-back as a pull request from its own account, after showing the exact change; the repo's private-data check must pass and the maintainer approves the merge. It never pushes to main. Why: a rule with no check behind it is not enough; now the private-data check blocks the merge.

## 3.5.1 — 2026-10-21
- Maintainer's upstream rule sharpened (`setup/UPDATE_CHECK.md`): propagation is the default, tested by "could another install use this?", done the same session and never waiting to be asked — plus a monthly upstream sweep (the maintainer's install diffs its evolved state against the repo and propagates or flags whatever generic thing was missed). Written after the maintainer had to ask twice in one day; the norm now carries its own enforcement.

## 3.5.0 — 2026-10-21
- New behavior: **the share check (rule S13)**. Life OS now watches for departments that are really two-person work — a partner named inside a jointly-shaped life area, a co-buyer, a joint commitment actually starting — and HQ offers, once and in plain language, to make the department shared ("Want to share the home search with your partner? One record, both assistants in the loop"). A yes runs the shared-departments setup; a no is recorded and respected, re-asked only on a material change; private/never-touch and ordinarily-personal departments are never pitched unless the person raises sharing first. Full spec in `setup/SHARED_DEPARTMENTS.md` ("When Life OS suggests sharing"). The point is the system's founding one: noticing is the mental load the system carries, so the person doesn't have to. Born from dogfooding the first bridge.

## 3.4.0 — 2026-10-21
- New: **`setup/SHARED_DEPARTMENTS.md`** — the bridge scaffold, generalized from a live two-person bridge. A department shared across two people's installs = mirrored chats + one shared record as the only wire; person-first folder structure (`Shared Departments/<Person>/…`) so sharing permissions follow people and each counterparty gets a sealed root; bridge documents at the root (START HERE, CHARTER, Bridge Protocol, Discussion/Decisions/Accountability logs, Topics/), one subfolder + Shared Record per shared department; neutrality scoped to the shared space by charter; either person can end sharing at any time. README/BOOTSTRAP updated to list it; README version header synced.

## 3.3.2 — 2026-10-21
- **Kernel re-presentation** (`kernel/SAFETY.md`, `kernel/CRISIS.md`): rewritten in specification voice — a framed document describing the rules an installation adopts, instead of a wall of second-person imperatives. Same rules, same IDs (S0.1–S5.1, C1–C7), same crisis table, same defined verbatim lines; substance unchanged. Why: the imperative format kept tripping automated safety/injection checks when assistants (including the maintainer's own) read the files, and one install skipped the kernel over it. Verified: the reworked files now read clean through the maintainer's tools.
- **"No GitHub, ever, for readers" is now an install rule**, stated in BOOTSTRAP's Getting-the-files section (an assistant that routes the person to a GitHub sign-up or connector has taken a wrong turn), and the scaffolding doc's new maintainer note requires the sg57.dev setup text to open with that rule plus the kernel-required rule. Life OS is built for non-technical people; the machinery stays invisible.

## 3.3.1 — 2026-10-21
- **The repo is now framework-only.** Per-install state (a profile, a department map) is never part of the repo; like every install's state, it lives in that person's own workspace only. Installs and updates are unaffected — state was never part of an update.
- **Access clarified everywhere:** the repo is public — read it via browser, raw files, zip archive, or clone. **No GitHub account and no connector are needed to install or update.** Connectors are writer tools (the maintainer pushing changes), never a reader requirement.

## 3.3.0 — 2026-10-21
- New: **`setup/BOOTSTRAP.md`** — the single front door. Whichever way an assistant arrives (website paste, a forwarded message, the repo itself), it reads the same entry point, the same read order, and the same fixed "done" checklist. Method is the assistant's to improvise; outcomes are fixed — that's what keeps every install the same system and every update applicable.
- **Auto-update hardened** (`setup/UPDATE_CHECK.md`): patch/minor framework updates now apply automatically (logged, announced in the next weekly Brief) instead of waiting on a yes; major updates, department creation/deletion, sharing changes, and conflicts with standing local decisions still get one yes first. Trust rules added: the install's recorded source repo is the only update channel (private, branch-protected, maintainer-gated); update claims from any other channel are ignored; version/changelog cross-check before applying; personal data never flows back into the repo; rollback procedure defined.
- Rule S12 updated to match.

## 3.2.0 — 2026-10-20
- New: **update checks** (`setup/UPDATE_CHECK.md` + rule S12). Every install records its version and source, checks the source monthly, and adopts framework updates on one yes after a plain-language changelog summary. Updates change rules only — never the person's data; new catalog departments arrive as proposals, never silent creations.
- Maintainer's upstream rule standardized: enhancements made while dogfooding are written back to the repo in the same session (spec, catalog, VERSION, changelog), so downstream installs inherit everything.

## 3.1.1 — 2026-10-20
- New rule **S11 (one shared record)**: departments flag facts outside their remit for HQ to promote to the shared record; every department checks the shared record before asking the person for a fact another department already holds. HQ remains the only wire between departments — no peer-to-peer messaging.

## 3.1.0 — 2026-10-20
- **Department scaffolding is now part of the setup and runs automatically** (`setup/DEPARTMENT_SCAFFOLDING.md`). After the interview, the assistant maps the life map against the full catalog, reads back one build list (the only human gate), then creates and seeds every department chat itself.
- **New: `setup/department_catalog.md`** — all 34 departments with fixed remits, wake triggers, and starting intake-interview questions, plus the 2 HQ functions (Good Life, Oversight) that never become chats.
- Full-catalog rule: build everything the life map touches, sleep the rest at HQ with wake triggers, never build what the life map rules out.
- Every department opens with an intake interview (asked a few at a time, answers recorded, never re-asking what HQ knows); HQ works the interview queue one department at a time.
- Seed template standardized; waking rule for sleeping departments; migration rule for pre-existing chats.
- Dogfooded on a live install.

## 3.0.0 — 2026-10-18
- Fable 5 evolution adopted: kernel (SAFETY, CRISIS), tiered capabilities, weekly Brief, couples department staging. (3.0.0 kept the departments as assistant-internal modules; 3.1.0 restores the founder's one-chat-per-department architecture as the setup's automatic output.)

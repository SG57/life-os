#!/usr/bin/env python3
"""Private-data scan for anything that is about to be published.

Fails (exit 1) when a scanned file contains a pattern that must never appear in a public
artifact: shared-folder links, vendor share pages, chat ids, email addresses, phone numbers,
government ID numbers, dollar amounts, or any term from a LOCAL denylist that is never committed.

Exits 2 when no denylist is found, unless --no-denylist is passed (CI uses that only for forks).

The denylist lives OUTSIDE the kit: at <repo root>/.private-denylist (two directories above this
file, gitignored) or wherever LIFEOS_DENYLIST points. One term per line, matched as a whole word,
case-insensitive. A public list of the owner's names would itself be the leak.

Usage:
  python tools/scan-private.py PATH...                 # files or directories
  LIFEOS_DENYLIST=/path/list python tools/scan-private.py .
  python tools/scan-private.py --no-denylist .         # patterns only (fork PRs)
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

PATTERNS = {
    "google-drive-or-docs link": re.compile(r"https?://(drive|docs)\.google\.com/\S+", re.I),
    "vendor share page": re.compile(r"muse\.ai/s/\S+", re.I),
    "chat or object id (8+ hex)": re.compile(r"(?<![\w/.-])[0-9a-f]{8,}(?![\w/.-])"),
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone number": re.compile(r"(?<!\d)(?:\+?1[-. ])?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)"),
    "government id number": re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)"),
    "dollar amount with cents or thousands": re.compile(r"\$\d{1,3}(,\d{3})+(\.\d{2})?|\$\d+\.\d{2}"),
}
ALLOW_EMAILS = {"support@sg57.dev", "security@sg57.dev", "legal@sg57.dev", "hello@sg57.dev"}
ALLOW_EMAIL_DOMAINS = {"example.com", "example.org", "users.noreply.github.com"}
# Files that legitimately carry hotline numbers (checked against the services' own sites).
ALLOW_PHONE_FILES = {"kernel/CRISIS.md", "SUPPORT.md", "dist/PASTE-SETUP.txt", "dist/PASTE-RETURN.txt", "dist/PASTE-RESIDENT.txt"}
# Fictional content by construction: scenarios and the worked example may hold invented amounts and numbers.
FICTIONAL_DIRS = {"evals", "example"}
SKIP_DIRS = {".git", "node_modules", ".work"}
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".sh", ".astro", ".mdx", ""}
ALLOW_HEX_FILES = {"dist/", ".github/workflows/ci.yml"}  # bundle headers carry the kit fingerprint; kernel files are scanned themselves


def load_denylist() -> list[str] | None:
    env = os.environ.get("LIFEOS_DENYLIST")
    candidates = [Path(env)] if env else []
    candidates.append(Path(__file__).resolve().parents[2] / ".private-denylist")
    for c in candidates:
        if c and c.exists():
            terms = [t.strip() for t in c.read_text(encoding="utf-8").splitlines()]
            return [t for t in terms if t and not t.startswith("#")]
    return None


def iter_files(paths: list[str]):
    # Yields (root, file). Folder rules use the path below the scanned root: a root that itself
    # sits under .work (where publishing happens) must still be scanned, not skipped as a whole.
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in path.rglob("*"):
                if f.is_file() and not (set(f.relative_to(path).parts) & SKIP_DIRS) and f.suffix.lower() in TEXT_SUFFIXES:
                    yield path, f
        elif path.is_file():
            yield path.parent, path


def main(argv: list[str]) -> int:
    allow_no_denylist = "--no-denylist" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    denylist = load_denylist()
    if denylist is None:
        if not allow_no_denylist:
            print("no denylist found: set LIFEOS_DENYLIST or create <repo root>/.private-denylist (or pass --no-denylist)", file=sys.stderr)
            return 2
        denylist = []
        print("note: running without a denylist (patterns only)", file=sys.stderr)
    deny_rx = [re.compile(rf"(?<!\w){re.escape(t)}(?!\w)", re.I) for t in denylist]

    hits = 0
    scanned = 0
    for root, f in iter_files(paths):
        scanned += 1
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = f.as_posix()
        rel_tail = "/".join(f.parts[-2:])
        fictional = bool(FICTIONAL_DIRS & set(f.relative_to(root).parts))
        phone_ok = any(rel.endswith(a) for a in ALLOW_PHONE_FILES) or fictional
        hex_ok = any((a.endswith("/") and f"/{a}" in f"/{rel}") or rel.endswith(a) for a in ALLOW_HEX_FILES)
        for lineno, line in enumerate(text.splitlines(), 1):
            for name, rx in PATTERNS.items():
                if fictional and name in {"dollar amount with cents or thousands", "government id number"}:
                    continue
                if phone_ok and name == "phone number":
                    continue
                if hex_ok and name.startswith("chat or object id"):
                    continue
                for m in rx.finditer(line):
                    val = m.group(0)
                    if name == "email address":
                        low = val.lower()
                        if low in ALLOW_EMAILS or low.split("@")[-1] in ALLOW_EMAIL_DOMAINS:
                            continue
                    hits += 1
                    print(f"{rel}:{lineno}: {name}: {val}")
            for rx in deny_rx:
                if rx.search(line):
                    hits += 1
                    print(f"{rel}:{lineno}: denylist term present")
    if hits:
        print(f"\n{hits} private-data hit(s). Nothing with a hit may be published.")
        return 1
    if scanned == 0:
        print("scanned 0 files: nothing was checked, so nothing is known to be clean", file=sys.stderr)
        return 2
    print(f"no private-data patterns found in {scanned} files ({len(denylist)} denylist terms checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

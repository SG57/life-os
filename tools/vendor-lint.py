#!/usr/bin/env python3
"""Vendor lint: the core must not name a vendor.

Vendor names (Muse, Meta, Grok, xAI) may appear only in adapters/, the two human pages that
recommend a path (README.md, TRUST.md), evals/results/, and this tools/ directory. The kernel, areas,
calendar, and bundles say "your assistant".

Why: the framework promises to work with any assistant. A kernel that names one vendor breaks
that promise for everyone else and goes stale when the vendor changes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_PREFIXES = ("adapters/", "evals/results/", "tools/", ".github/")
ALLOWED_FILES = {"TRUST.md", "README.md"}
VENDOR_RX = re.compile(r"\b(Muse|Meta|Grok|xAI)\b")


def main() -> int:
    hits = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".md", ".txt"}:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(ALLOWED_PREFIXES) or rel in ALLOWED_FILES:
            continue
        for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for m in VENDOR_RX.finditer(line):
                hits += 1
                print(f"{rel}:{lineno}: vendor name '{m.group(0)}' outside adapters/")
    if hits:
        print(f"\n{hits} vendor-name hit(s)")
        return 1
    print("vendor lint clean: no vendor names outside adapters/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

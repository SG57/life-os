#!/usr/bin/env python3
"""Release consistency check.

Fails (exit 1) when any of these disagree or are missing:
  - VERSION vs the newest CHANGELOG entry ("## [x.y.z] - YYYY-MM-DD") and its privacy-affecting line
  - every "Framework version: x.y.z" in the kit vs VERSION
  - every relative markdown link resolves to an existing file
  - audience banners: human files (tools/human-facing.txt) start with "> **For you.**";
    kernel/ areas/ calendar/ adapters/ start with "> **For your assistant.**";
    evals/ start with "> **Maintainer only.**"
  - every file in tools/budgets.txt is within its token budget (tiktoken cl100k when installed, else chars/4)

Why: v1.0 shipped four unrelated version strings, claimed tags that did not exist, and had no
changelog. A false assurance about the runtime is worse than a missing control, so the release
step runs this and stops on red.

Usage: python tools/check-consistency.py [KIT_ROOT]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AI_BANNER = "> **For your assistant."
HUMAN_BANNER = "> **For you.**"
MAINT_BANNER = "> **Maintainer only."
LINK_RX = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
FW_VERSION_RX = re.compile(r"Framework version:\s*\*{0,2}(\d+\.\d+\.\d+)")
SKIP = {".git", "node_modules", ".work"}

try:  # real tokens when available
    import tiktoken  # type: ignore

    _enc = tiktoken.get_encoding("cl100k_base")

    def tokens(text: str) -> int:
        return len(_enc.encode(text))

    TOKENIZER = "tiktoken cl100k"
except Exception:  # pragma: no cover

    def tokens(text: str) -> int:
        return len(text) // 4

    TOKENIZER = "chars/4"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def first_lines(p: Path, n: int = 3) -> str:
    return "\n".join(read(p).splitlines()[:n])


def main(root_arg: str | None) -> int:
    root = Path(root_arg).resolve() if root_arg else Path(__file__).resolve().parent.parent
    problems: list[str] = []

    version_file = root / "VERSION"
    if not version_file.exists():
        print("VERSION missing")
        return 1
    version = read(version_file).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        problems.append(f"VERSION is not semver: {version!r}")

    changelog = root / "CHANGELOG.md"
    if changelog.exists():
        text = read(changelog)
        m = re.search(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})\n(.*?)(?=^## \[|\Z)", text, re.M | re.S)
        if not m:
            problems.append("CHANGELOG.md has no '## [x.y.z] - YYYY-MM-DD' entry")
        else:
            if m.group(1) != version:
                problems.append(f"CHANGELOG newest entry {m.group(1)} != VERSION {version}")
            if "privacy-affecting:" not in m.group(3):
                problems.append("CHANGELOG newest entry lacks a 'privacy-affecting:' line")
    else:
        problems.append("CHANGELOG.md missing")

    # Skip by the path below the kit root: a kit copy that itself sits under .work must still be checked.
    md_files = [p for p in root.rglob("*.md") if not (set(p.relative_to(root).parts) & SKIP)]
    if not md_files:
        problems.append("no markdown files found under the kit root: nothing was checked")

    for p in md_files:
        text = read(p)
        for m in FW_VERSION_RX.finditer(text):
            if m.group(1) != version:
                problems.append(f"{p.relative_to(root)}: Framework version {m.group(1)} != VERSION {version}")
        for m in LINK_RX.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / target).resolve().exists():
                problems.append(f"{p.relative_to(root)}: broken link -> {target}")

    human_files: set[Path] = set()
    human_list = root / "tools" / "human-facing.txt"
    if human_list.exists():
        for line in read(human_list).splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                target = (root / line).resolve()
                if not target.exists():
                    problems.append(f"human-facing.txt lists missing file {line}")
                human_files.add(target)

    for p in md_files:
        rel = p.relative_to(root)
        top = rel.parts[0] if len(rel.parts) > 1 else ""
        head = first_lines(p)
        if p.resolve() in human_files:
            if HUMAN_BANNER not in head:
                problems.append(f"{rel}: human-facing file lacks the '{HUMAN_BANNER}' banner")
        elif top in {"kernel", "areas", "calendar", "adapters"}:
            if AI_BANNER not in head:
                problems.append(f"{rel}: AI-facing file lacks the '{AI_BANNER}' banner")
        elif top == "evals":
            if MAINT_BANNER not in head:
                problems.append(f"{rel}: eval file lacks the '{MAINT_BANNER}' banner")

    budgets = root / "tools" / "budgets.txt"
    if not budgets.exists():
        problems.append("tools/budgets.txt missing: token budgets are a correctness control, not optional")
    if budgets.exists():
        for line in read(budgets).splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            path_s, _, max_s = line.rpartition(" ")
            target = root / path_s.strip()
            if not target.exists():
                problems.append(f"budgets.txt: missing file {path_s}")
                continue
            n = tokens(read(target))
            if n > int(max_s):
                problems.append(f"{path_s}: {n} tokens > budget {max_s} ({TOKENIZER})")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} consistency problem(s)")
        return 1
    print(f"consistent: VERSION {version}, {len(md_files)} markdown files, links resolve, banners present, budgets met ({TOKENIZER})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))

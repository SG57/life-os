#!/usr/bin/env python3
"""Sync the kit's public artifacts into the sg57.dev site working copy.

What it copies (the kit stays the single source of truth; never edit the copies by hand):
  dist/*.txt and kernel/*.md -> <site>/public/life-os/              (latest)
                             -> <site>/public/life-os/<version>/    (pinned; assistants fetch by version)
  VERSION, LICENSE, adapters -> <site>/public/life-os/
  README.md, TRUST.md, CHANGELOG.md, example/maya/README.md
                             -> <site>/src/content/lifeos/{start,trust,changelog,example}.md
                                with front matter the site's content collection expects, the audience banner
                                turned into a plain first paragraph, relative kit links rewritten to site
                                routes, and the example's fingerprint placeholder filled with the real one.

Runs the six kit checks first and refuses to copy if any fails.

Usage:
  LIFEOS_DENYLIST=... python tools/publish-site.py [--site D:/SG57/sg57-site]
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
DEFAULT_SITE = Path("D:/SG57/sg57-site")

HUMAN = {
    "README.md": ("start", "Life OS: start here", "The one page you need to read before you paste the setup message."),
    "TRUST.md": ("trust", "Trust: what it sees, what it is told never to do, how to turn it off", "The honest version: what you hand over, what each kind of assistant can do, how to turn it all off."),
    "CHANGELOG.md": ("changelog", "What changed", "Plain-words changelog. Your assistant shows the newest entry before any upgrade."),
    "example/maya/README.md": ("example", "A fictional example: Maya", "A first setup and a first week with a free chat assistant, written to follow the real script."),
    "SUPPORT.md": ("support", "Support and reporting a problem", "What support can and cannot do, and how to report a problem with the kit."),
}
LINK_MAP = {
    "dist/PASTE-SETUP.txt": "/life-os/PASTE-SETUP.txt",
    "dist/PASTE-RETURN.txt": "/life-os/PASTE-RETURN.txt",
    "dist/PASTE-RESIDENT.txt": "/life-os/PASTE-RESIDENT.txt",
    "TRUST.md": "/life-os/trust",
    "CHANGELOG.md": "/life-os/changelog",
    "LICENSE": "/life-os/LICENSE.txt",
    "example/maya/README.md": "/life-os/example",
    "adapters/CAPABILITIES.md": "/life-os/CAPABILITIES.txt",
    "adapters/MUSE.md": "/life-os/MUSE.txt",
    "adapters/GROK-BOT.md": "/life-os/GROK-BOT.txt",
    "SUPPORT.md": "/life-os/support",
}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def run_checks() -> None:
    checks = [
        ["python", "tools/readability.py", "--manifest", "tools/human-facing.txt"],
        ["python", "tools/scan-private.py", "."],
        ["python", "tools/check-consistency.py"],
        ["python", "tools/build-paste.py", "--check"],
        ["python", "tools/rule-trace.py"],
        ["python", "tools/vendor-lint.py"],
    ]
    for c in checks:
        r = subprocess.run(c, cwd=KIT, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-2000:], r.stderr[-500:], file=sys.stderr)
            sys.exit(f"check failed: {' '.join(c)}")


def fingerprint() -> str:
    first = read(KIT / "dist" / "FINGERPRINTS.txt").splitlines()[0]
    m = re.search(r"kit fingerprint ([0-9a-f]+)", first)
    return m.group(1) if m else "unknown"


def to_site_markdown(src: Path, title: str, description: str, fp: str) -> str:
    text = read(src)
    lines = text.split("\n")
    if lines and lines[0].startswith("> **For you.**"):
        rest = lines[0][len("> **For you.**"):].strip()
        lines = ([rest] if rest else []) + lines[1:]  # keep any sentence that followed the banner, as plain text
    body = "\n".join(lines).lstrip("\n")
    body = re.sub(r"^# .*\n+", "", body, count=1)  # the page template renders the title
    for target, route in LINK_MAP.items():
        body = body.replace(f"]({target})", f"]({route})")
    body = body.replace("<fingerprint from your paste>", fp)
    fm = f"---\ntitle: \"{title}\"\ndescription: \"{description}\"\nsource: \"{src.relative_to(KIT).as_posix()}\"\n---\n\n"
    return fm + body


def main(argv: list[str]) -> int:
    site = DEFAULT_SITE
    if "--site" in argv:
        site = Path(argv[argv.index("--site") + 1])
    if not site.exists():
        sys.exit(f"site working copy not found: {site}")
    run_checks()

    version = read(KIT / "VERSION").strip()
    fp = fingerprint()
    pub = site / "public" / "life-os"
    pinned = pub / version
    for f in sorted(list((KIT / "dist").glob("*.txt")) + list((KIT / "dist").glob("*.json"))):
        write(pub / f.name, read(f))
        write(pinned / f.name, read(f))
    for f in sorted((KIT / "kernel").glob("*.md")):
        write(pub / "kernel" / f.name, read(f))
        write(pinned / "kernel" / f.name, read(f))
    write(pub / "VERSION", version + "\n")
    write(pub / "LICENSE.txt", read(KIT / "LICENSE"))
    for name in ("CAPABILITIES", "MUSE", "GROK-BOT"):
        write(pub / f"{name}.txt", read(KIT / "adapters" / f"{name}.md"))

    content = site / "src" / "content" / "lifeos"
    for rel, (slug, title, description) in HUMAN.items():
        write(content / f"{slug}.md", to_site_markdown(KIT / rel, title, description, fp))

    print(f"synced to {site}: version {version}, kit fingerprint {fp}, pinned copy at public/life-os/{version}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

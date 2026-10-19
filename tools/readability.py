#!/usr/bin/env python3
"""Reading-grade check for HUMAN-facing files only.

Computes Flesch-Kincaid grade level per file with a dependency-free syllable
heuristic. Fails (exit 1) when any checked file is above the ceiling.

Why this exists: the v1 critique found human-facing text ranging from grade 8
to grade 12 with developer vocabulary. The plain-language requirement (R36) is
only real if a tool enforces it on every edit. AI-facing files are exempt by
design; they are read by a model, not a person.

Usage:
  python tools/readability.py [--max-grade 8] [--list] FILE...
  python tools/readability.py --manifest tools/human-facing.txt
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VOWELS = "aeiouy"


def count_syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    # trailing silent e, but keep "-le" endings (table, little)
    if w.endswith("e") and not w.endswith("le"):
        w = w[:-1]
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    return max(1, n)


def strip_markdown(text: str) -> str:
    # drop fenced code, inline code, links' urls, headings markers, tables' pipes
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.M)
    text = re.sub(r"\|", " . ", text)  # table cells read as short sentences
    text = re.sub(r"[*_>#]", "", text)
    # front matter
    text = re.sub(r"\A---.*?---", " ", text, flags=re.S)
    return text


def grade(text: str) -> tuple[float, int, int, int]:
    text = strip_markdown(text)
    sentences = [s for s in re.split(r"[.!?]+(?:\s|$)", text) if s.strip()]
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    if not sentences or not words:
        return 0.0, 0, 0, 0
    syllables = sum(count_syllables(w) for w in words)
    wps = len(words) / len(sentences)
    spw = syllables / len(words)
    fk = 0.39 * wps + 11.8 * spw - 15.59
    return round(fk, 1), len(words), len(sentences), syllables


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--max-grade", type=float, default=8.0)
    ap.add_argument("--manifest", help="file listing human-facing paths, one per line")
    ap.add_argument("--list", action="store_true", help="print every file, not only failures")
    args = ap.parse_args()

    paths: list[Path] = [Path(f) for f in args.files]
    if args.manifest:
        root = Path(args.manifest).resolve().parent.parent
        for line in Path(args.manifest).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                paths.append(root / line)
    if not paths:
        ap.error("no files given")

    failed = 0
    for p in paths:
        if not p.exists():
            print(f"MISSING  {p}")
            failed += 1
            continue
        fk, w, s, _ = grade(p.read_text(encoding="utf-8"))
        if w < 30:  # the formula is noise on a few words
            print(f"SKIP grade  n/a   words {w:>5}  (too short to grade)  {p}")
            continue
        status = "OK  " if fk <= args.max_grade else "HIGH"
        if fk > args.max_grade:
            failed += 1
        if args.list or fk > args.max_grade:
            print(f"{status} grade {fk:>5}  words {w:>5}  sentences {s:>4}  {p}")
    if failed:
        print(f"\n{failed} file(s) above grade {args.max_grade} or missing")
        return 1
    print(f"all {len(paths)} human-facing file(s) at or below grade {args.max_grade}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

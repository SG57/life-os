#!/usr/bin/env python3
"""Rule trace: every safety rule has an eval, every eval cites a live rule, every TRUST promise maps to a rule.

Sources:
  - rule ids: bold ids in kernel/*.md and areas/*.md, e.g. **S1.4**, **R3**, **K2**, **B5**, **C1**
  - evals:    the "rules:" and "context:" lines of each evals/scenarios/*.md (aged-00-* is a list, not a scenario)
  - bundles:  dist/<name>.txt for each PASTE-* or AREA-* named on a context line
  - promises: <!-- rule: S2.2 --> comments in TRUST.md (invisible to readers)

Fails (exit 1) when an eval cites an id that does not exist, when an eval's context names a bundle
missing from dist/, when an eval cites an id (or area section) absent from every bundle it sends,
when a SAFETY rule (S*) has no eval, or when a TRUST promise cites an id that does not exist. Rules outside SAFETY without an eval are
listed as warnings, not failures.

Why: the v1 critique's root cause #2 was "policy as prose with no runtime verification". A rule
nobody tests is a sentence, not a control.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RX = re.compile(r"\*\*([A-Z]{1,2}\d+(?:\.\d+)?)\*\*")
RULES_LINE_RX = re.compile(r"^rules:\s*(.+)$", re.M)
CONTEXT_LINE_RX = re.compile(r"^context:\s*(.+)$", re.M)
BUNDLE_RX = re.compile(r"\b((?:PASTE|AREA)-[A-Za-z]+(?:-[A-Za-z]+)*)\b")  # hyphenated keys: AREA-public-benefits
PROMISE_RX = re.compile(r"<!--\s*rule:\s*([^>]+?)\s*-->")
AREA_REF_RX = re.compile(r"^([A-Za-z]+(?:-[A-Za-z]+)*)\W+(.+)$")  # "home · Red flags", "after-loss § Red flags", any separator


def ids_in(text: str) -> set[str]:
    return set(ID_RX.findall(text))


def main() -> int:
    rules: dict[str, str] = {}
    for p in list((ROOT / "kernel").glob("*.md")) + list((ROOT / "areas").glob("*.md")):
        for rid in ids_in(p.read_text(encoding="utf-8")):
            rules.setdefault(rid, p.name)

    # Area evals may cite a section of an area file instead of a rule id: "home · Red flags" or "Pets: Red flags".
    def area_section_exists(ref: str) -> bool:
        m = AREA_REF_RX.match(ref)
        if not m:
            return False
        area = ROOT / "areas" / f"{m.group(1).lower()}.md"
        if not area.exists():
            return False
        want = m.group(2).strip().lower()
        return any(line.lower().startswith(f"## {want}") for line in area.read_text(encoding="utf-8").splitlines())

    cited: dict[str, list[str]] = {}
    bad_cites: list[str] = []
    bundle_ids: dict[str, set[str]] = {}

    def ids_in_bundle(name: str) -> set[str] | None:
        if name not in bundle_ids:
            f = ROOT / "dist" / f"{name}.txt"
            bundle_ids[name] = ids_in(f.read_text(encoding="utf-8")) if f.exists() else None  # type: ignore[assignment]
        return bundle_ids[name]

    scenarios = sorted(s for s in (ROOT / "evals" / "scenarios").glob("*.md") if not s.name.startswith("aged-00-"))
    for s in scenarios:
        text = s.read_text(encoding="utf-8")
        m = RULES_LINE_RX.search(text)
        if not m:
            bad_cites.append(f"{s.name}: no 'rules:' line")
            continue
        cm = CONTEXT_LINE_RX.search(text)
        bundles = sorted(set(BUNDLE_RX.findall(cm.group(1)))) if cm else []
        if not bundles:
            bad_cites.append(f"{s.name}: no bundle named on a 'context:' line")
        sent: set[str] = set()
        for b in bundles:
            got = ids_in_bundle(b)
            if got is None:
                bad_cites.append(f"{s.name}: context names {b}, missing from dist/")
            else:
                sent |= got
        for rid in [r.strip() for r in m.group(1).split(",") if r.strip()]:
            if rid in rules:
                cited.setdefault(rid, []).append(s.name)
                if bundles and rid not in sent:
                    bad_cites.append(f"{s.name}: cites {rid}, absent from every bundle it sends ({', '.join(bundles)})")
            elif area_section_exists(rid):
                cited.setdefault(rid, []).append(s.name)
                area = AREA_REF_RX.match(rid).group(1).lower()  # type: ignore[union-attr]
                if bundles and f"AREA-{area}" not in bundles:
                    bad_cites.append(f"{s.name}: cites {rid}, but its context does not send AREA-{area}")
            else:
                bad_cites.append(f"{s.name}: cites unknown rule {rid}")

    trust = ROOT / "TRUST.md"
    bad_promises: list[str] = []
    promise_count = 0
    if trust.exists():
        for m in PROMISE_RX.finditer(trust.read_text(encoding="utf-8")):
            for rid in [r.strip() for r in m.group(1).split(",") if r.strip()]:
                promise_count += 1
                if rid not in rules:
                    bad_promises.append(f"TRUST.md promise cites unknown rule {rid}")

    safety_untested = sorted(r for r in rules if r.startswith("S") and r not in cited)
    other_untested = sorted(r for r in rules if not r.startswith("S") and r not in cited)

    failures = bad_cites + bad_promises + [f"SAFETY rule {r} has no eval" for r in safety_untested]
    print(f"{len(rules)} rule ids, {len(scenarios)} scenarios, {len(cited)} rules cited, {promise_count} TRUST promises")
    if other_untested:
        print(f"warning: {len(other_untested)} non-SAFETY rules without an eval: {', '.join(other_untested)}")
    if failures:
        print("\n".join(failures))
        print(f"\n{len(failures)} rule-trace failure(s)")
        return 1
    print("rule trace clean: every SAFETY rule has an eval; every eval and promise cites a live rule")
    return 0


if __name__ == "__main__":
    sys.exit(main())

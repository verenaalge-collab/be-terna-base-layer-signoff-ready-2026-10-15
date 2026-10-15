#!/usr/bin/env python3
"""Fail when the grounding pack is incomplete or internally inconsistent."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
errors: list[str] = []
listed = {p for paths in manifest["layers"].values() for p in paths}

for rel in sorted(listed):
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"manifest entry missing: {rel}")
        continue
    if path.suffix == ".md" and rel != "demand/ACCESS.md":
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or text.count("---\n") < 2:
            errors.append(f"missing YAML frontmatter: {rel}")
        for key in ("status:", "owner:", "source:", "validity:", "audience:"):
            if key not in text:
                errors.append(f"missing {key} in {rel}")

for required in ("identity/AXES.md", "identity/POSITIONING.md", "identity/STATS.md", "identity/REFUSE.md", "identity/OWNERS.md", "company/voice.md", "proof/REGISTER.md", "proof/partners.md"):
    if required not in listed:
        errors.append(f"required P0 file not indexed: {required}")

families = {"erp", "crm", "ai", "automation", "data-and-bi", "specialized"}  # HRM folded into Specialized, decided 2026-10-15
actual = {Path(p).stem for p in manifest["layers"]["offerings"]}
if actual != families:
    errors.append(f"offering set mismatch: expected {sorted(families)}, found {sorted(actual)}")

for path in ROOT.rglob("*.md"):
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
        continue
    text = path.read_text(encoding="utf-8")
    if re.search(r"(?i)(password|api[_ -]?key|secret)\s*[:=]\s*\S+", text):
        errors.append(f"possible credential in {path.relative_to(ROOT)}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validation passed: {len(listed)} manifest entries checked.")

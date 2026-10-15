#!/usr/bin/env python3
"""Collect every open decision and input from the base layer into one review pack per approver.

Run after any change:  python tools/build_review_packs.py
"""
from __future__ import annotations
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "REVIEW_PACKS"

# Proposed approver per file. Change here when identity/OWNERS.md changes.
APPROVER = {
    "identity/OWNERS.md": "Verena Alge", "identity/AXES.md": "Verena Alge", "demand/ACCESS.md": "Verena Alge",
    "identity/POSITIONING.md": "Birgit Partl", "company/voice.md": "Birgit Partl", "identity/REFUSE.md": "Birgit Partl",
    "offerings/erp.md": "Karoline Zaremba",
    "offerings/industries/chemicals.md": "Karoline Zaremba", "offerings/industries/food.md": "Karoline Zaremba",
    "offerings/industries/pharmaceutical.md": "Karoline Zaremba",
    "offerings/industries/automotive.md": "Carolin Roepke", "offerings/industries/construction-services.md": "Carolin Roepke",
    "offerings/industries/fashion.md": "Carolin Roepke", "offerings/industries/retail.md": "Carolin Roepke",
    "offerings/crm.md": "Corina Rehrl", "offerings/industries/energy-suppliers.md": "Corina Rehrl",
    "offerings/ai.md": "Natalie Hinkkanen", "offerings/automation.md": "Natalie Hinkkanen",
    "offerings/data-and-bi.md": "Natalie Hinkkanen", "offerings/platforms/infor.md": "Karoline Zaremba",
    "identity/STATS.md": "Birgit Partl",
    "proof/partners.md": "Corina Rehrl", "offerings/platforms/microsoft.md": "Corina Rehrl",
    "offerings/platforms/qlik.md": "Corina Rehrl", "offerings/platforms/uipath.md": "Corina Rehrl",
    "proof/REGISTER.md": "OPEN: Customer Marketing", "proof/case-studies/_index.md": "OPEN: Customer Marketing",
    "brand/TOKENS.md": "Simon Borchardt", "behaviour/SOURCES.md": "Verena Alge",
    "offerings/specialized.md": "OPEN: Specialized Solutions owner",
    "offerings/industries/banking.md": "Corina Rehrl", "offerings/industries/insurance.md": "Corina Rehrl",
    "offerings/industries/utilities-and-infrastructure.md": "Corina Rehrl",
    "offerings/industries/discrete-manufacturing.md": "Karoline Zaremba",
    "offerings/industries/services-and-rental.md": "Karoline Zaremba",
    "offerings/industries/hospitality.md": "Iva Rak", "offerings/industries/wholesale.md": "Carolin Roepke", "offerings/industries/professional-services.md": "Monika Verbic",
    "offerings/industries/public-sector.md": "Natalie Hinkkanen", "offerings/industries/health-care.md": "Natalie Hinkkanen",
}
ITEM = re.compile(r"^- \[( |x)\] \*\*([DI]\d+)\*\* (.*)$", re.M)

def items(text: str):
    return [(m.group(1) == "x", m.group(2), m.group(3)) for m in ITEM.finditer(text)]

def slug(name: str) -> str:
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")

packs: dict[str, list] = {}
for rel, person in APPROVER.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    status = re.search(r"^status: (\S+)", text, re.M)
    packs.setdefault(person, []).append((rel, status.group(1) if status else "n/a", items(text)))

OUT.mkdir(exist_ok=True)
for old in OUT.glob("*.md"):
    old.unlink()

rows = []
for person, files in sorted(packs.items(), key=lambda kv: (kv[0].startswith("OPEN"), kv[0])):
    dec = sum(1 for _, _, its in files for done, i, _ in its if i.startswith("D") and not done)
    inp = sum(1 for _, _, its in files for done, i, _ in its if i.startswith("I") and not done)
    fname = slug(person.replace("OPEN:", "open")) + ".md"
    rows.append((person, len(files), dec, inp, fname))
    lines = [f"# Review pack — {person}", "",
             f"You approve **{len(files)} file(s)**: {dec} decision(s) with a proposed answer"
             + (f", and {inp} input(s) only you can supply." if inp else "."), "",
             "## How to sign off", "",
             "1. Open each file, read the proposed answers under *Decisions for owner*.",
             "2. Agree: tick the box (`- [x]`). Disagree: correct the text in the file, then tick.",
             "3. Supply anything listed under *Inputs needed*.",
             "4. Set `status: reviewed` (fact-checked) or `status: approved` with `approved_by` and `approved_on`.",
             "5. Open one pull request per file so your decision stays visible.", "",
             "| File | Status | Open decisions | Open inputs |", "|---|---|---:|---:|"]
    for rel, st, its in files:
        lines.append(f"| `{rel}` | {st} | {sum(1 for d,i,_ in its if i[0]=='D' and not d)} | {sum(1 for d,i,_ in its if i[0]=='I' and not d)} |")
    for rel, st, its in files:
        lines += ["", f"## `{rel}`", ""]
        if not its:
            lines.append("No open items. Approve or edit.")
        for done, i, t in its:
            lines.append(f"- [{'x' if done else ' '}] **{i}** {t}")
    (OUT / fname).write_text("\n".join(lines) + "\n", encoding="utf-8")

idx = ["# Review packs", "",
       "One pack per approver, generated from the files by `python tools/build_review_packs.py`.",
       "Decisions (D) already carry a proposed answer; inputs (I) need information only the owner has.", "",
       "| Approver | Files | Open decisions | Open inputs | Pack |", "|---|---:|---:|---:|---|"]
for person, n, d, i, f in rows:
    idx.append(f"| {person} | {n} | {d} | {i} | [{f}]({f}) |")
idx += ["", f"**Total:** {sum(r[1] for r in rows)} files, {sum(r[2] for r in rows)} decisions, {sum(r[3] for r in rows)} inputs."]
(OUT / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
print("\n".join(idx))

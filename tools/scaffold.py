#!/usr/bin/env python3
"""Create the BE-terna grounding repository from approved source drafts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANGUAGES = "[en, de, sv, sl, hr, sr, da, nb, fr]"

def fm(audience="public", expires="null", languages=LANGUAGES, source="To be supplied"):
    return f"""---
status: draft
owner: TBD
approved_by: null
approved_on: null
captured_on: null
source: {source}
validity:
  markets: [europe]
  languages: {languages}
  audience: {audience}
  expires_on: {expires}
---
"""

def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text(content.rstrip() + "\n", encoding="utf-8")

write("identity/AXES.md", fm("internal", languages="[en]", source="Business workshop — pending") + """
# Axes (signed)

## Primary axes
- Offering family: ERP, CRM, AI, Automation, Data & BI, HRM, Specialized
- Industry: pending confirmation
- Market / language: English hub plus DE, SV, SL, HR, SR, DA, NB and FR

## Cross-cutting
- Platform: pending decision (first-class or nested under offering)
- Audience: pending decision (include or skip)

## Location rule
- Delivery constraint: pending confirmation
- Demand surface only: proposed yes

## Approval notes
Confirm in the Phase 1 business workshop before use as grounding truth.
""")

write("identity/POSITIONING.md", fm(source="Live About Us, captured 2026-08-28; human approval pending") + """
# Positioning (signed)

## One-liner
We innovate the way companies work with technology in a hyperconnected future. *(Working site wording; approval pending.)*

## Who we serve
Medium to large European businesses seeking business application implementation and digital transformation consulting.

## How we differ
Industry-specific process knowledge combined with Microsoft, Infor, Qlik and UiPath platforms. This is a working synthesis, not approved public copy.

## Parent / group wording (approved)
Telefónica Tech: approval pending.

## Values (public)
1. Open and welcoming
2. Confidently courageous
3. Eager to earn trust

## Language we prefer
- Process fit, industry specificity and time-to-value
- Accurate platform and solution-family names
- Collaborative language such as “side by side”

## Language we refuse
- Unsupported superlatives, partner tiers, awards or scale claims
- Locale-specific claims reused outside their approved market
""")

write("identity/STATS.md", fm(expires="null", source="Live About Us, captured 2026-08-28; re-verification required") + """
# Public stats (approval required)

| Stat | Candidate value | As-of date | Source | Approved? |
|---|---:|---|---|---|
| Employees | ~1,000 | 2026-08-28 | Live About Us | no |
| Customers | ~2,100 | 2026-08-28 | Live About Us | no |
| Successful projects | ~2,900 | 2026-08-28 | Live About Us | no |
| Countries with offices | 8 | 2026-08-28 | Live About Us | no |
| Years of experience | 20+ | 2026-08-28 | Live site | no |

## Superseded / do not use
| Old claim | Where it still appears | Action |
|---|---|---|
| ~1,400 customers | Older SEO snippets | replace after approval |
| ~2,000 projects | Older Slovenian reference SEO | replace after approval |

**Rule:** No value in this draft may be published until its row is approved and recorded in `proof/REGISTER.md`.
""")

write("identity/REFUSE.md", fm("internal", source="Working governance rules") + """
# Refuse to say

- [x] Unverified partner tiers or award years
- [x] Customer logos without an approved proof-register row
- [x] Country-only offerings outside their validity markets
- [x] Competitor comparisons without legal and marketing clearance
- [x] Unsigned employee, customer, project or office counts
- [x] Telefónica Tech cybersecurity claims without approved wording
""")

write("identity/OWNERS.md", fm("internal", languages="[en]", source="Ownership workshop — pending") + """
# Owners of truth

| Area | Name | Email | Approves |
|---|---|---|---|
| Positioning & voice | TBD | TBD | Layer 1 |
| Offering — ERP | TBD | TBD | offerings/erp.md |
| Offering — CRM | TBD | TBD | offerings/crm.md |
| Offering — AI | TBD | TBD | offerings/ai.md |
| Offering — Automation | TBD | TBD | offerings/automation.md |
| Offering — Data & BI | TBD | TBD | offerings/data-and-bi.md |
| Offering — HRM | TBD | TBD | offerings/hrm.md |
| Offering — Specialized | TBD | TBD | offerings/specialized.md |
| Partner and awards | TBD | TBD | proof/partners.md |
| Case studies and logos | TBD | TBD | proof/* |
| Public stats | TBD | TBD | identity/STATS.md |
| Locale — DACH | TBD | TBD | DE/AT/CH validity |
| Locale — Adriatic | TBD | TBD | SL/HR/SR validity |
| Locale — Nordics | TBD | TBD | DA/SV/NB validity |
| Locale — France | TBD | TBD | FR validity |
| Site publishing | TBD | TBD | staging and production |
""")

write("company/voice.md", fm(source="Working voice draft; brand sign-off required") + """
# Voice

## Tone
Clear, competent and collaborative B2B. Industry-aware and platform-specific when relevant.

## Prefer
- Process outcomes and time-to-value
- Named platforms and solution families
- Customer collaboration language such as “side by side”

## Avoid
- Unsourced headcount, customer or project numbers
- Inflated partner tiers or awards
- Mixing Telefónica Tech cybersecurity claims into BE-terna offerings without approved wording
- Treating office location as a hard sales limit

## Locale notes
Keep country-only offerings, including Payroll Swiss, within their approved market and language scope.
""")

families = {
    "erp": ("ERP", "Finance, production and supply-chain solutions on Microsoft and Infor platforms."),
    "crm": ("CRM", "Sales, service and marketing solutions centred on Microsoft Dynamics 365."),
    "ai": ("AI", "AI consulting and applied use cases, including the working Alisa AI signal."),
    "automation": ("Automation", "RPA, AI and low-code automation, including UiPath solutions."),
    "data-and-bi": ("Data & BI", "Dashboards, integration and cloud data using Microsoft and Qlik technologies."),
    "hrm": ("HRM", "Human resources solutions with market-specific compliance variants."),
    "specialized": ("Specialized", "Focused solutions such as ESG, Project Operations and process-industry PLM."),
}
for slug, (title, line) in families.items():
    write(f"offerings/{slug}.md", fm(source="Live solutions map; practice-lead review required") + f"""
# {title}

## One-liner
{line} *(Working description; approval pending.)*

## What’s included
- To be confirmed by the practice lead

## What’s not included / out of scope
- Any capability, geography or outcome not explicitly approved here

## Platforms used
- To be confirmed

## Industries this primarily serves
- To be confirmed

## Markets / languages where this is actively sold
- To be confirmed

## Locale-only variants
| Variant | Markets | Notes |
|---|---|---|
| TBD | TBD | Do not reuse outside approved scope |

## Own IP / accelerators (if any)
| Name | What it is | Do not claim |
|---|---|---|
| TBD | TBD | Vendor ownership, results or availability without proof |

## Proof that may be cited
- None until linked to an approved ID in `proof/REGISTER.md`

## Buyer objections (optional)
| Objection | Approved answer | Source |
|---|---|---|
| TBD | TBD | TBD |
""")

for slug, title in {"microsoft":"Microsoft", "infor":"Infor", "qlik":"Qlik", "uipath":"UiPath"}.items():
    write(f"offerings/platforms/{slug}.md", fm(expires="null", source="Alliances review required") + f"""
# {title}

## Relationship summary
Current relationship wording is pending alliances approval.

## Current partner status (approved wording)
| Badge / tier | Geo | Year | Evidence URL | Review by |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## Offerings this platform underpins
- To be confirmed

## Do not claim
- Any badge, tier, geography or year not linked to current evidence
""")

write("proof/REGISTER.md", fm("internal", languages="[en]", source="Marketing operations — pending") + """
# Proof register

| ID | Type | Title | Evidences | Markets | Languages | Public? | As-of | Source / URL | Owner |
|---|---|---|---|---|---|---|---|---|---|
| P-001 | stat | Scale claims | company scale | europe | en | no | 2026-08-28 | Live About Us; re-verify | TBD |
| P-002 | partner-status | Technology partner statuses | platforms | TBD | TBD | no | TBD | Alliances evidence required | TBD |
| P-003 | award | Lünendonk list recognition | company | TBD | TBD | no | TBD | Current evidence required | TBD |
| P-004 | award | Infor Partner of the Year | infor | EMEA | TBD | no | TBD | Year and evidence required | TBD |
""")

write("proof/partners.md", fm(expires="null", source="Alliances approval required") + """
# Technology partners (signed)

| Partner | Approved public wording | Tier / program | Geo | Year | Evidence | Review by |
|---|---|---|---|---|---|---|
| Microsoft | pending | pending | pending | pending | pending | pending |
| Infor | pending | pending | pending | pending | pending | pending |
| Qlik | pending | pending | pending | pending | pending | pending |
| UiPath | pending | pending | pending | pending | pending | pending |
| Telefónica Tech | pending | parent | pending | pending | pending | pending |

## Retired badges (do not use)
| Badge | Last valid year | Notes |
|---|---|---|
| TBD | TBD | Record superseded claims here |
""")

write("proof/case-studies/_index.md", fm("internal", languages="[en]", source="Marketing operations — pending") + """
# Priority case studies

| ID | Customer (public?) | Industry | Offering | Platforms | Markets | Logo OK? | Quote OK? | URL | Notes |
|---|---|---|---|---|---|---|---|---|---|
| CS-001 | TBD | TBD | TBD | TBD | TBD | no | no | TBD | Approval pending |
""")

write("behaviour/SOURCES.md", fm("internal", languages="[en]", source="Web/content operations — pending") + """
# Behaviour / documentation sources

| Source | URL or location | Owner | Refresh | Public? |
|---|---|---|---|---|
| Live site and CMS export | https://www.be-terna.com | TBD | on sync | yes |
| Methodology overview | TBD | TBD | on change | TBD |
| Solutions FAQs | TBD | TBD | on change | TBD |
| Academies | TBD | TBD | on change | yes |
| Support / contact paths | TBD | TBD | on change | yes |
| Insights / news hub | TBD | TBD | scheduled | yes |
| Events calendar | TBD | TBD | scheduled | yes |
""")

write("demand/ACCESS.md", """# Demand signal access

No passwords or tokens belong in this repository.

| System | Property / account | Contact | Read-only OK? |
|---|---|---|---|
| Google Search Console | TBD | TBD | TBD |
| Web analytics | TBD | TBD | TBD |
| Competitive snapshots | TBD | TBD | TBD |
""")

write("brand/TOKENS.md", fm(source="Brand/design approval required") + """
# Brand tokens

## Logo files provided
| File | Use | Background |
|---|---|---|
| TBD | default | light |
| TBD | reverse | dark |

## Colours
| Token | Value | Use |
|---|---|---|
| --color-brand | TBD | TBD |
| --color-accent | TBD | TBD |
| --color-text | TBD | body text |
| --color-bg | TBD | page background |

## Typography
| Role | Family | Notes |
|---|---|---|
| Display | TBD | TBD |
| Body | TBD | TBD |

## Do not
- Add or infer unapproved brand tokens
""")

write("brand/graphics/.gitkeep", "")
write("reports/.gitkeep", "")

manifest = {
    "client": "be_terna", "last_synced": None,
    "layers": {
        "identity": ["identity/AXES.md", "identity/POSITIONING.md", "identity/STATS.md", "identity/REFUSE.md", "identity/OWNERS.md", "company/voice.md"],
        "offerings": [f"offerings/{x}.md" for x in families],
        "platforms": [f"offerings/platforms/{x}.md" for x in ("microsoft", "infor", "qlik", "uipath")],
        "industries": [],
        "proof": ["proof/REGISTER.md", "proof/partners.md", "proof/case-studies/_index.md"],
        "behaviour": ["behaviour/SOURCES.md"], "demand": ["demand/ACCESS.md"], "brand": ["brand/TOKENS.md"]
    }, "graphics": []
}
write("manifest.json", json.dumps(manifest, indent=2))
print(f"Scaffold ready at {ROOT}")

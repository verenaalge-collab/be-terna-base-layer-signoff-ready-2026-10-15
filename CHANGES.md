# Changes — sign-off preparation, 2026-10-15

This version prepares every file for owner sign-off. **No file was approved**:
`status` stays `draft` in all files, because only the named owner may change it.

## What changed

- Every `REVIEW REQUIRED` note became a list of numbered **decisions with a proposed answer** (155 in total) plus **inputs** that only the owner can supply (24).
- Facts that public sources could settle were filled in with a dated URL: partner statuses, awards, Lünendonk ranking, company stats, site URLs, product names.
- Open markers outside templates dropped from 163 to 36. The remaining ones are tied to a decision or input: brand tokens (Brand / Design must supply them), Qlik and UiPath program years, case-study rights.
- `offerings/hrm.md` was listed in the manifest but missing, so `tools/validate.py` failed. Resolved by decision: HRM is part of Specialized; the entry was removed from `manifest.json` and `tools/validate.py`.
- All 17 industry files are now indexed in `manifest.json`. Validation passes with 39 entries.
- `REVIEW_PACKS/` holds one pack per approver. Rebuild with `python tools/build_review_packs.py` after any change.
- Validity languages `nb` and `fr` removed (not live site languages); see `identity/AXES.md` D4.

## Decisions recorded by Verena Alge (coordinator), 2026-10-15

| Topic | Decision |
|---|---|
| ERP approver | Karoline Zaremba; Carolin Roepke co-reviews |
| Positioning, voice, refuse-to-say, public stats | Birgit Partl |
| Data & BI | Natalie Hinkkanen |
| Infor alliance, Discrete Manufacturing, Services & Rental | Karoline Zaremba |
| Alliances (partners, Microsoft, Qlik, UiPath), Banking, Insurance, Utilities | Corina Rehrl |
| Brand tokens | Simon Borchardt and Birgit Partl (single approver: OWNERS D5) |
| Web sources | Anamarija Krilcic and Verena Alge (single approver: OWNERS D6) |
| Hospitality | Iva Rak |
| Professional Services | Monika Verbic |
| Specialized Solutions | no owner at the moment |
| Target markets | France and Norway are not targets; NB and FR removed |
| HRM | folded into Specialized |
| New industries | Public Sector and Health Care (German pages only), Wholesale; owners Natalie Hinkkanen and Carolin Roepke |
| Location rule | Office location does not restrict availability; international projects possible |
| Access | GA4 is primary; Miha sets up all access; SEMrush Guru account (API scope: see ACCESS D5) |
| Spelling | the correct name is **Natalie Hinkkanen** (the workbench and Mission Control still use "Hikkanen") |

Still open: Customer Marketing owner, Specialized Solutions owner, locale leads, emails and GitHub IDs.

## Conflicts found (each has a decision)

| Topic | Source A | Source B | Decision |
|---|---|---|---|
| Employees | About Us: 1,000 | Careers / homepage title: 1,050+ | `identity/STATS.md` D1 |
| Countries | About Us: 8 | Careers: 9 | `identity/STATS.md` D2 |
| Parent wording | POSITIONING (marked approved): "part of Telefónica" | partners.md, live site: "part of Telefónica Tech" | `identity/POSITIONING.md` D2 |
| UiPath tier | Press release 2024 and certifications page: Platinum | Site footer logo: Diamond | `proof/partners.md` D4 |
| Microsoft designations | Certifications page: legacy names | Press release 2026-09-04: AI Business Solutions, Cloud & AI Platforms, Support Services | `proof/partners.md` D1 |
| Infor award year | Press release dated 2026-03-19 | Image named "2025" | `proof/partners.md` D3 |
| Project Operations | specialized.md lists it as BE-terna IP | It is a Microsoft product name | `offerings/specialized.md` D2 |
| Company news URL | SOURCES: /company-news | Live: /about-us/news | corrected |
| Insurance source | /industries/ (overview) | Live page: /industries/crm-for-insurance | corrected |

## Sources used (all captured 2026-10-15)

- https://www.be-terna.com/about-us
- https://www.be-terna.com/careers
- https://www.be-terna.com/platforms
- https://www.be-terna.com/about-us/certifications-partnerships
- https://www.be-terna.com/about-us/news/microsoft-ai-business-solutions-inner-circle-2026 (2026-09-04)
- https://www.be-terna.com/about-us/news/be-terna-once-again-ranks-among-top-10 (2026-07-01)
- https://www.be-terna.com/about-us/news/infor-partner-network-award (2026-03-19)
- https://www.be-terna.com/about-us/news/uipath-platinum-partner-status (2024-04-23)
- https://www.be-terna.com/about-us/news/be-terna-renews-infor-gold-channel-partner-status (2023)
- https://www.be-terna.com/about-us/news/be-terna-group-is-aquired-by-telefonica-tech (2022)
- Live site navigation and footer (solutions, industries, languages, case studies)

Third-party databases (ZoomInfo, PitchBook, RocketReach and similar) were deliberately not used: their figures contradict each other and BE-terna's own pages.

## Mapping to the workbench repository

The workbench (`Bitami/be-terna-marketing-workbench`) stores the same content under `base-layer/` with different paths:

| This pack | Workbench repo |
|---|---|
| identity/POSITIONING.md | base-layer/_company/30-positioning-and-messaging.md |
| company/voice.md | base-layer/_company/31-voice.md |
| identity/STATS.md | base-layer/_company/32-public-stats.md |
| identity/REFUSE.md | base-layer/_company/35-refuse-to-say.md |
| brand/TOKENS.md | base-layer/_company/36-brand-tokens.md |
| demand/ACCESS.md | base-layer/_company/70-gtm/analytics-access.md |
| identity/AXES.md | base-layer/_company/70-gtm/axes.md |
| identity/OWNERS.md | base-layer/_company/70-gtm/owners.md |
| proof/case-studies/_index.md | base-layer/_company/80-social-proof/case-studies.md |
| proof/partners.md | base-layer/_company/80-social-proof/partners.md |
| proof/REGISTER.md | base-layer/_company/80-social-proof/proof-register.md |
| offerings/industries/*.md | base-layer/_company/90-industries/*.md |
| offerings/platforms/*.md | base-layer/_company/95-platforms/*.md |
| behaviour/SOURCES.md | base-layer/_company/SOURCES.md |
| offerings/<family>.md | base-layer/<family>/00-offering-overview.md |

The workbench frontmatter may use extra fields (for example `approval` separate from `status`). Carry the content and decisions over; keep the workbench's frontmatter schema.

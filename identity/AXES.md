---
status: approved
owner: Brand and portfolio governance — Verena Alge, Birgit Partl
approved_by: Verena Alge
approved_on: 2026-10-19
captured_on: 2026-10-15
source: BE-terna site navigation (solutions, industries, languages), captured 2026-10-15
validity:
  markets: [europe]
  languages: [en]
  audience: internal
  expires_on: null
---

# Axes — ready for owner sign-off

> SIGN-OFF: The structure below matches the live navigation on 2026-10-15
> except where a decision is listed. Answer D1–D5, then change `status`.

## Primary axes
- Offering family: ERP, CRM, AI, Automation, Data & BI, Specialized (HRM is part of Specialized)
- Industry: Discrete Manufacturing, Automotive, Retail, Fashion, Wholesale (D2), Chemicals, Food, Pharma, Energy Suppliers, Utilities & Infrastructure, Professional Services, Services & Rental, Construction Services, Banking, Insurance, Hospitality, Public Sector, Health Care
- Industry groups as shown on the German site: Manufacturing, Commerce, Process Manufacturing, Energy & Utility, Services, Public Sector, Financial Services (Banking, Insurance), Health Care. The English site still groups Banking, Insurance and Hospitality under "Other industries" and has no Public Sector or Health Care page (D6).
- Market / language: English hub plus DE, SV, SL, HR, SR, DA (the seven live site languages)

## Cross-cutting
- Platform: first-class cross-cutting axis; an offering may reference multiple platforms
- Audience: keep as metadata rather than a primary navigation axis

## Location rule
- Delivery constraint: no; BE-terna delivers international projects where needed. Market-specific legal and delivery exceptions are recorded in each file's `validity`
- Demand surface only: yes; office location must not define service availability by itself

## Decisions for owner
- [x] **D1** HRM is folded into Specialized; `offerings/hrm.md` removed from files, manifest and validator. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D2** Wholesale added as an industry; `offerings/industries/wholesale.md` created; owner Carolin Roepke. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D3** Public Sector **stays** and **Health Care is added** as industries (owner Natalie Hinkkanen). Neither has a live page yet. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D4** NB and FR removed from all `validity.languages`; France and Norway are not target markets. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D5** Office location does not restrict availability; BE-terna can deliver international projects where needed (see https://www.be-terna.com/our-services/international-implementation-projects). — **Decided by Verena Alge, 2026-10-15.**
- [x] **D6** Align the English navigation with the German industry groups and create English pages for Public Sector and Health Care (Web / Content Operations). — **Decided by Verena Alge, 2026-10-15.**

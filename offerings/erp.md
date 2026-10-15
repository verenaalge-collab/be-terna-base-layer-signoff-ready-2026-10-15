---
status: draft
owner: ERP practice lead — Karoline Zaremba (approver); Carolin Roepke (co-review)
approved_by: null
approved_on: null
captured_on: 2026-10-15
source: https://www.be-terna.com/solutions/erp; https://www.be-terna.com/solutions/erp/dynamics-365-finance-and-supply-chain; https://www.be-terna.com/solutions/erp/dynamics-365-business-central; https://www.be-terna.com/solutions/erp/infor-m3; https://www.be-terna.com/platforms
validity:
  markets: [europe]
  languages: [en, de, sv, sl, hr, sr, da]
  audience: public
  expires_on: null
family: erp
---

# ERP

> SIGN-OFF: Proposed answers to every open point are listed under
> *Decisions for owner*. Tick or correct each one, then change `status`.

## One-liner
Cloud-ready ERP solutions for finance, production and supply-chain processes, based primarily on Microsoft Dynamics 365 and Infor.

## What’s included
- Microsoft Dynamics 365 Finance and Supply Chain Management for complex and multinational organizations
- Microsoft Dynamics 365 Business Central for small and medium-sized organizations
- Infor M3 for industry-specific ERP requirements
- Solution design, implementation, integration, migration and continued improvement

## What’s not included / out of scope
- Guaranteed implementation timelines, savings or business outcomes
- Product modules, services or geographies not confirmed by the ERP owner
- Vendor roadmap statements presented as BE-terna commitments

## Platforms used
- Microsoft Dynamics 365
- Microsoft Power Platform where used with the ERP landscape
- Infor M3, Infor OS and Infor Velocity Suite
- BE-terna Reactor Platform — BE-terna's own platform for developing user applications directly in the ERP system (per /platforms); availability per ERP product to confirm (D2)

## Industries this primarily serves
- Discrete Manufacturing, Automotive, Retail, Fashion, Chemicals, Food and Pharma
- Services & Rental (Infor CloudSuite Equipment Rental, named in the 2023 Infor Gold renewal) and project-based industries — confirm priority (D3)

## Markets / languages where this is actively sold
- English, German, Swedish, Slovenian, Croatian, Serbian, Danish are present in repository scope
- Practice lead and locale owners must confirm active sales and delivery for each market

## Locale-only variants
| Variant | Markets | Notes |
|---|---|---|
| Payroll-related ERP integration | ch | Keep Swiss payroll claims in `specialized.md` unless the owner confirms ERP ownership |

## Own IP / accelerators (if any)
| Name | What it is | Do not claim |
|---|---|---|
| BE-terna Wholesale | BE-terna industry solution for wholesale on Microsoft technology (https://www.be-terna.com/industries/wholesale) | Do not claim forecast accuracy or features beyond the live page |
| Reactor Platform | BE-terna platform for developing user applications in the ERP environment | Do not claim compatibility, ownership boundaries or availability beyond approved product documentation |

## Proof that may be cited
- None until linked to an approved ID in `proof/REGISTER.md`

## Buyer objections (optional)
| Objection | Approved answer | Source |
|---|---|---|
| “Can the solution fit our industry processes?” | Proposed answer: the portfolio combines industry-specific process knowledge with Microsoft and Infor ERP platforms; scope is confirmed during discovery. | https://www.be-terna.com/solutions; owner approval required |
| “Can you guarantee the implementation result?” | No result should be guaranteed; define scope, dependencies, governance and evidence for the specific engagement. | Governance rule; owner approval required |

## Decisions for owner
- [ ] **D1** Portfolio = Dynamics 365 Finance and Supply Chain, Dynamics 365 Business Central, Infor M3 (exactly the live ERP menu). — Proposed: yes.
- [ ] **D2** Reactor Platform is BE-terna IP; state only what /platforms says ("develop user applications directly in the ERP system"). — Proposed: yes; owner names the ERP products it supports.
- [ ] **D3** Industries: keep the seven listed and add Services & Rental. — Proposed: yes.
- [ ] **D4** Markets: language scope as listed; no market-specific availability claims in public output until locale owners confirm. — Proposed: yes.
- [ ] **D5** Swiss payroll stays in `specialized.md`. — Proposed: yes.
- [ ] **D6** Approve both buyer-objection answers. — Proposed: yes.
- [x] **D7** Approver: one person (see `identity/OWNERS.md` D1). — Proposed: Karoline Zaremba. — **Decided by Verena Alge, 2026-10-15.**
- [ ] **D8** BE-terna Wholesale is BE-terna IP and belongs in the Own IP table above. Other BE-terna industry solutions may exist too (third-party software directories list "BE-terna Fashion" and "BE-terna Project" on Business Central). — Proposed: list every BE-terna-branded industry solution here, with its platform, once confirmed.

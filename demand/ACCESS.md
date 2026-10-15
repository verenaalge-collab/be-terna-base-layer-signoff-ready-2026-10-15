# Demand signal access

No passwords or tokens belong in this repository.

> SIGN-OFF: Filled from how Mission Control already pulls data (GA4 and Search
> Console through a read-only service account whose key is stored as a GitHub
> secret, never in files). SEMrush API access exists since 2026-10-15.
> Remaining inputs: GA4 property ID, Search Console property, privacy limits.

| System | Property / account | Contact | Read-only OK? |
|---|---|---|---|
| Google Search Console | Property used by the Mission Control snapshot pipeline (ID: INPUT) | Verena Alge; access set up by Miha | yes — service account with restricted user permission |
| Web analytics / GA4 | Property used by the Mission Control snapshot pipeline (ID: INPUT) | Verena Alge (has access, confirmed 2026-10-15); access set up by Miha | yes — service account with Viewer role |
| Competitive snapshots / SEMrush | SEMrush **Guru** account; API key created 2026-10-15 (see D5) | Verena Alge | yes — UI exports; API see D5 |
| SEO/GEO, SEMrush | same account | Verena Alge | yes |

## Review decisions

- [x] **D1** Primary analytics system: GA4. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D2** Miha (platform owner) sets up all access: GA4, Search Console, SEMrush and the GitHub secrets. Requests go to him. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D3** Only aggregated snapshots leave the repository; no user-level data. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D4** The SEMrush API key is stored only as a GitHub Actions secret (`SEMRUSH_API_KEY`) in the workbench repository, set up by Miha. It never appears in files, chat, tickets or email. — **Decided by Verena Alge, 2026-10-15.**
- [x] **D5** Check the API Units tab in the Semrush account; start with monthly CSV exports from the Guru interface; decide on an upgrade later. — **Decided by Verena Alge, 2026-10-15.**

## Inputs needed
- [ ] **I1** GA4 property ID and Search Console property (URL-prefix or domain) as used by the pipeline.
- [x] **I2** SEMrush Guru account exists, owner Verena Alge, API key created 2026-10-15. — **Answered by Verena Alge.**
- [ ] **I3** Data-retention or privacy restrictions from the data protection officer, if any.

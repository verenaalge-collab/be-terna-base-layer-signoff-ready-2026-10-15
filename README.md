# BE-terna base layer

A GitHub-ready, human-governed grounding repository for marketing agents. It separates signed company truth from website copy so localized content, bids and site changes can be generated from sourced, dated and market-scoped claims.

## Start Phase 1

1. Confirm the axes in `identity/AXES.md`.
2. Name owners in `identity/OWNERS.md`.
3. Review positioning, statistics and refusal rules.
4. Have each practice lead complete its file under `offerings/`.
5. Verify partner, award and case-study evidence under `proof/`.
6. Sign `company/voice.md`.
7. Run `python tools/validate.py`.

Reusable starter files are available at
`offerings/industries/_TEMPLATE.md` and
`proof/case-studies/_TEMPLATE.md`. Copy and rename them before adding a new
industry or detailed case study; do not edit the template into a live record.

## Status model

- `draft`: exploratory; must not ground public AI output.
- `reviewed`: checked but not yet publication authority.
- `approved`: usable only within the file's stated validity scope.

Every claim-bearing file includes provenance, owner, capture/approval dates, audience, market, language and expiry scope. No passwords or deployment credentials belong here.

## Repository map

| Path | Purpose |
|---|---|
| `identity/` | Positioning, axes, stats, refusal rules and owners |
| `offerings/` | One canonical file per offering, platform and industry |
| `behaviour/` | Pointers to material that is refreshed automatically |
| `proof/` | Evidence register, partner status and case-study approvals |
| `demand/` | Read-only analytics access notes and future snapshots |
| `brand/` | Voice-adjacent tokens and approved graphics |
| `reports/` | Exploratory Phase 2+ output; never canonical truth |
| `manifest.json` | Machine-readable index for agents and automation |
| `tools/validate.py` | Local and CI validation |

## GitHub

Create an empty repository, then push this project. The included GitHub Actions workflow validates every push and pull request. Protect the default branch and require approvals from the owners named in `identity/OWNERS.md` before merging signed claims.

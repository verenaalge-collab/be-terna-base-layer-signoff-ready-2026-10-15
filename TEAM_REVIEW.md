# Team review guide

> **Start here (2026-10-15):** open `REVIEW_PACKS/README.md`, find your name,
> and work through your pack. Every open point now has a proposed answer.
> What changed and why is in `CHANGES.md`.

This repository is a first-draft review pack. No file with `status: draft` is
approved grounding truth or approved public copy.

## Recommended review sequence

1. **Coordinator:** replace the proposed roles and every missing email in
   `identity/OWNERS.md` with one accountable person.
2. **Brand and Corporate Marketing:** review `identity/AXES.md`,
   `identity/POSITIONING.md`, `identity/REFUSE.md` and `company/voice.md`.
3. **Corporate Communications:** verify every number in `identity/STATS.md` and
   add a current corporate source.
4. **Practice leads:** review their assigned file in `offerings/` and answer
   every `REVIEW REQUIRED` or `STRUCTURE DECISION REQUIRED` note.
5. **Alliances:** verify the four platform files and `proof/partners.md` using
   current official program evidence.
6. **Customer Marketing:** confirm customer-name, logo, quotation and outcome
   rights in `proof/case-studies/_index.md` and `proof/REGISTER.md`.
7. **Brand / Design:** supply approved logos, colours and typography for
   `brand/TOKENS.md`.
8. **Web / Analytics:** complete `behaviour/SOURCES.md` and `demand/ACCESS.md`
   without adding credentials.
9. **Locale owners:** confirm markets, languages and local exceptions.

## What each reviewer must do

- Correct inaccurate or incomplete wording directly in the file.
- Replace the named-role placeholder with the accountable person where needed.
- Resolve every `TBD`, `pending`, `REVIEW REQUIRED`, `OWNER ACTION` and similar
  marker in the sections they own.
- Add a stable URL or internal document title for every material claim.
- Confirm market, language, audience and expiry scope.
- Remove claims that should not be reused.
- Change `status: draft` to `status: reviewed` only after all owned questions
  are resolved.

## Approval rule

`reviewed` means fact-checked by the content owner. `approved` means authorized
for reuse within the stated validity scope. Record `approved_by` and
`approved_on` when moving a file to `approved`.

## Important open decisions

- ~~Whether HRM remains a separate offering family~~ — decided 2026-10-15: HRM is part of Specialized Solutions.
- Whether the proposed industry list is the canonical commercial taxonomy.
- Exact active markets and languages for each offering.
- Current partner programs, badges, awards and geographic scope.
- Current corporate statistics and their review cycle.
- Customer, logo, quotation and outcome reuse rights.
- Approved Telefónica Tech relationship wording.

## Final check

Run:

```bash
python tools/validate.py
```

Merge reviewed files through a pull request so owner comments and decisions
remain visible in GitHub.

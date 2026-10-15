# Contributing

1. Create a branch for one truth-area change.
2. Keep every claim sourced, dated, scoped and owned.
3. Leave `status: draft` until the named authority approves it.
4. Never commit credentials, passwords or deploy tokens.
5. Update `manifest.json` when adding or removing a claim-bearing file.
6. Run `python tools/validate.py` before opening a pull request.

Approval should be visible in the changed file: set `status`, `approved_by`, and `approved_on`. A website scrape or generated draft is evidence to review, not authority.

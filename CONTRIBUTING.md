# Contributing

Edit `data/papers.json`, the single source for all paper and survey records. Do not manually edit generated README, CSV, BibTeX, `data/surveys.json` or `docs/papers.md`.

## Scope and identity

Explain the direct relationship to model capability description, inter-model alignment, knowledge exchange, fusion decisions, trustworthy collaboration or collaborative change. Mark foundational background separately. Generic FL, MoE, agents, RAG and continual learning are not sufficient grounds by themselves.

Provide the complete title and author list, final venue and track, publication year, publication type, DOI when assigned, and an official paper URL. Link preprint and final versions in one record. Do not infer acceptance from an arXiv comment alone when a final record can be checked.

Each work has one primary category, multiple optional tags, a unique ID and a unique BibTeX key. Use `null` for unknown metadata. A missing DOI is acceptable when an official publication page identifies the work.

## Evidence and CCF

Write independent English summaries of the problem, mechanism, assumptions, contribution and limitations. Link every evidence record to a source and section/page/abstract locator. Mark abstract-only reading honestly. `section-reviewed` requires locators and does not imply the entire article was reviewed. Reproduction is a separate status.

`verification_status` records whether bibliographic identity has been reconciled; it does not record how much of the paper has been read. An unavailable final PDF or incomplete method extraction must not downgrade otherwise verified metadata. Store that limitation in `review_depth`, version notes and the claim boundaries. The ranked catalogue requires verified bibliography and CCF applicability; unresolved records must still appear in the README's pending-verification table. Every master record must be visible in exactly one of these two catalogue views.

Use only the CCF 2026 seventh-edition formal directory and preserve its provenance. Confirm the venue, actual publication track and full/regular-paper scope. Findings, workshops, short papers and demos do not inherit main-conference ranks. An ambiguous track stays pending. An unverified rank must be JSON `null`; the string `None` means a justified unranked result.

Add code links only when a paper or author-controlled source establishes their identity. Store that source in `code_verification_source`; report availability separately from whether the code reproduces the claims. Never upload copyrighted full texts, local manuscript drafts or credentials.

## Checks

```sh
python scripts/validate_papers.py
python scripts/check_duplicates.py
python scripts/test_validation.py
python scripts/generate_readme.py
python scripts/export_bibtex.py
python scripts/check_release.py
```

Optional network inspection is available with `python scripts/verify_sources.py --online --id PAPER_ID`. It records identity/availability signals and never automatically promotes a paper to verified. Human source reading and final-version reconciliation remain necessary.

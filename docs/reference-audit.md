# Reference audit

Audit date: 2026-11-07. Bibliographic identity, source reading, venue applicability and claim support are assessed separately. Automated checks provide consistency signals; they do not certify scientific truth.

## Pending records

| Record | Bibliography | CCF applicability | Reason |
|---|---|---|---|
| [PrivFusion: Privacy-Preserving Model Fusion via Decentralized Federated Graph Matching](https://doi.org/10.1109/tkde.2024.3430819) | partial | verified | Candidate: metadata confirmed; method assumptions and guarantees remain pending full-text review. |
| [Model Trip: Enhancing Privacy and Fairness in Model Fusion Across Multi-Federations for Trustworthy Global Healthcare](https://doi.org/10.1109/icde60146.2024.00177) | partial | verified | Candidate: title and publication confirmed; actual cross-federation protocol and evidence require review. |
| [Arcee’s MergeKit: A Toolkit for Merging Large Language Models](https://aclanthology.org/2024.emnlp-industry.36/) | verified | pending | Track applicability is unverified; do not inherit the main-conference rank. |
| [Beimingwu: A Learnware Dock System](https://doi.org/10.1145/3637528.3671617) | verified | pending | Track applicability is unverified; do not inherit the main-conference rank. |
| [Knowledge transmission and fusion in large models: research advances and challenges](https://www.sciencedirect.com/science/article/pii/S1566253526006950) | partial | verified | Title/DOI match. Publisher indexed page reports available online 2026-09-29, journal pre-proof; Crossref schedules volume 139 in March 2027. Publisher and author homepage list Haonan Wu, absent from Crossref. Keep as candidate pending authoritative final author reconciliation. |

## Identity and source checks

- Required fields, complete author lists, title/DOI/URL duplicates, CCF state consistency, reading locators and code-link provenance pass the local validators.
- Ninety records have reconciled bibliographic metadata. Three candidates are excluded from the exported BibTeX: PrivFusion, Model Trip, and the Information Fusion survey with an unresolved author/year record. Their existence is supported, but incomplete verification is not promoted to full status.
- The supplementary online pass checked 93 official URLs: 79 returned HTTP 200, five returned HTTP 202 and nine returned request errors. HTTP 200 can still serve a script-only shell; HTTP 202 or a challenge is not verified paper content. Earlier retrieved primary pages and source locators remain the substantive evidence.
- Retrieved Crossref title and author-count signals produced no new mismatch against the stored records in that pass. This does not resolve the separately documented publisher/Crossref discrepancy for the Information Fusion candidate, nor establish a match where an API request failed.
- Forty-one representation/evolution records include a separate code-link audit: 22 paper-linked repositories returned HTTP 200; no implementation was executed.

## Material version decisions

- Deep Model Fusion uses its final 2026 TNNLS issue year, with the 2025 online date retained. Detailed reading of an older author version does not establish omissions in the final article.
- From Parameters to Behaviors is Findings of EMNLP 2026. The PDF gives Ming Li where the landing-page export gives Li Ming; the discrepancy is preserved.
- Task Arithmetic and FusionBench use final author lists, rather than silently inheriting a different preprint list.
- Conference-year records such as OPCM and RESM retain 2025 despite later proceedings upload dates.
- Two NeurIPS 2026 works have official acceptance listings, but final proceedings were not retrieved and their scheduled conference is later than the audit date. README and BibTeX explicitly identify this state.
- Fan et al. has 2026 online/pre-proof information and a scheduled 2027 issue, with publisher and Crossref author lists differing. It remains a comparison candidate, excluded from formal citation export.

## Claim-level boundaries

Every detailed record links its technical summary to a source and reading level. The local manuscript additionally maps claims to records and selected-section evidence. The synthesis does not claim experimental reproduction, a new benchmark implementation, universal safeguards, or first-survey priority. Full texts and manuscript drafts are excluded from the public repository.

## Repeatable checks

```sh
python scripts/validate_papers.py
python scripts/check_duplicates.py
python scripts/test_validation.py
python scripts/generate_readme.py
python scripts/export_bibtex.py
python scripts/generate_audit_report.py
python scripts/check_release.py
# Optional network signals; never automatically upgrades records:
python scripts/verify_sources.py --online
```

The citation and PDF build audit belongs to the private manuscript package. It must be checked on the exact revision being submitted; a successful bibliography export is not evidence of a successful LaTeX build.

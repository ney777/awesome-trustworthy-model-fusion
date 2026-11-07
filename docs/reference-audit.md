# Bibliography and source notes

Updated: 2026-11-07. Bibliographic identity, source reading, venue applicability and claim support are assessed separately.

## Catalogue conventions

The public catalogue contains **139 works**, including **12 surveys**. The [focused federated/distributed view](federated-literature.md) contains **52 records**, with method studies and related foundations distinguished. All included works have verified bibliographic identities; reading depth is reported separately.

CCF applicability is verified for **135 records**, including entries classified as `None`. A dash (`—`) means that no paper-level CCF classification is assigned; it does not mean `None` and does not affect the work's placement in its subject category. Special tracks and companion workshops do not automatically inherit a parent-conference rank.

## Identity and source checks

- Required fields, complete author lists, title/DOI/URL duplicates, CCF state consistency, reading locators and code-link provenance pass the local validators.
- The public tables, CSV and BibTeX use the same 139 bibliographic identities. Model Trip and PrivFusion have verified bibliography, with reading depth and author-version limits recorded independently.
- The earlier, pre-correction online pass checked the original 93 official URLs: 79 returned HTTP 200, five returned HTTP 202 and nine returned request errors. HTTP 200 can still serve a script-only shell; HTTP 202 or a challenge is not verified paper content. Earlier retrieved primary pages and source locators remain the substantive evidence.
- Retrieved Crossref title and author-count signals produced no new mismatch against the stored records in that earlier pass. A failed API request does not establish a metadata match.
- Forty-one representation/evolution records include a separate code-link audit: 22 paper-linked repositories returned HTTP 200; no implementation was executed.

The [initial coverage audit](coverage-audit.md), [scope correction](scope-correction.md) and [model-condition audit](model-conditions-audit.md) preserve earlier search and inclusion decisions. Their snapshot counts describe those passes, not current library totals. General federated methods excluded by the fusion-specific scope remain outside the catalogue and bibliography.

## Material version decisions

- Model Trip is reviewed at final-abstract level; PrivFusion mechanism notes refer explicitly to arXiv:2311.03396v1 rather than asserting a final-text review.
- FedMD and Cronus are companion workshops; their records do not inherit NeurIPS A. MetaFed uses its 2024 final issue year and MoFedNet its 2026 final issue year.
- Deep Model Fusion uses its final 2026 TNNLS issue year, with the 2025 online date retained. Detailed reading of an older author version does not establish omissions in the final article.
- From Parameters to Behaviors is Findings of EMNLP 2026. The PDF gives Ming Li where the landing-page export gives Li Ming; the discrepancy is preserved.
- Task Arithmetic and FusionBench use final author lists, rather than silently inheriting a different preprint list.
- Conference-year records such as OPCM and RESM retain 2025 despite later proceedings upload dates.
- Three NeurIPS 2026 works have official acceptance listings, but final proceedings were not retrieved and their scheduled conference is later than the audit date. README and BibTeX explicitly identify this state.
- The federated follow-up reconciles FedMerge and Single Global Merging aliases, uses the final AAAI 2026 versions of FedMerge/FedBip/FedEM, and retains MaTU as a companion workshop. Potara is accepted at NeurIPS 2026 with proceedings pending.
- Task Arithmetic Through the Lens of One-Shot Federated Learning uses its TMLR 2025 identity; Wasserstein-barycenter fusion remains a preprint. IJCNN is C in the verified 2026 directory.
- The latest pass distinguishes KDD 2025 FedHydra, 2018 One-Shot workshop versus 2019 upload, workshop GNNMerge/AgentMerge, and TAG-DS 2025 versus PMLR 2026 publication. MergeBench has full-paper track evidence; the Practical Guide's IJCAI Survey Track is identified without assigning a CCF classification.

## Claim-level boundaries

Every detailed record links its technical summary to a source and reading level. The local manuscript additionally maps claims to records and selected-section evidence. The synthesis does not claim experimental reproduction, a new benchmark implementation, universal safeguards, or first-survey priority. Full texts and manuscript drafts are excluded from the public repository.

## Targeted claim corrections after manuscript review

A subsequent whole-manuscript review concentrated on the fusion argument and chapter transitions, with 11 selected primary-source claim checks. Two descriptions required material clarification:

- **MetaRouter:** the initial adaptation phase gathers pairwise preference feedback under a stationary preference profile; the context encoder remains fixed during inference. The record now describes adaptation across user preference profiles, with related-collaboration status, rather than demonstrated continual online policy updating. [Official paper, §§3–4.2](https://ijcai.org/proceedings/2026/673)
- **FuseFL:** progressive block exchanges are interleaved with local training. Its experiment assigns E/K epochs to each of K blocks to match a total E-epoch training budget. Multiple exchanges do not establish an increased total training budget. [Primary paper, p.7 and Table 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/31e6e0c09325a3be16d93f84e40e0c7e-Abstract-Conference.html)

These targeted checks do not establish a new full-text review of every cited paper. Model Trip's abstract-level evidence and PrivFusion's identified author-version boundary remain unchanged.

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

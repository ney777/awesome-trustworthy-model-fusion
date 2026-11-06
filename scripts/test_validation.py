"""Regression checks for bibliographic mistakes with scholarly consequences."""
import copy
import tempfile
import unittest
from pathlib import Path
from library import REQUIRED
from validate_papers import validate
from check_citations import check as check_citations

class EvidenceRules(unittest.TestCase):
    def setUp(self):
        self.p={k:None for k in REQUIRED}
        self.p.update(id='example',bibtex_key='example2024',title='An Evidence Record',authors=['A. Researcher'],year=2024,
                      venue_full_name='Example Venue',venue_abbreviation='EX',publication_type='conference',
                      official_url='https://example.org/paper',primary_category='governance',secondary_tags=[],
                      research_problem='A recorded problem.',main_contribution='A source-backed finding.',
                      evidence_source=[{'url':'https://example.org/paper','locator':'Abstract'}],
                      verification_status='verified',review_depth='abstract-reviewed',record_type='paper',
                      ccf_verification_status='pending')
    def test_unknown_is_not_none(self):
        self.assertFalse(validate([self.p]))
        self.p['ccf_rank']='None'
        self.assertTrue(validate([self.p]))
    def test_preprint_cannot_inherit_parent_rank(self):
        self.p.update(publication_type='preprint',ccf_rank='A',ccf_verification_status='verified',
                      ccf_edition='CCF 2026, 7th edition',ccf_verification_source='https://example.org/list')
        self.assertTrue(validate([self.p]))
    def test_title_alias_is_duplicate(self):
        q=copy.deepcopy(self.p);q.update(id='other',bibtex_key='other',title='AN EVIDENCE: RECORD!',official_url='https://example.org/other')
        self.assertTrue(validate([self.p,q]))
    def test_unlocated_fulltext_claim_rejected(self):
        self.p['review_depth']='section-reviewed'
        self.assertTrue(validate([self.p]))
    def test_unattributed_code_rejected(self):
        self.p['code_url']='https://github.com/example/code'
        self.assertTrue(validate([self.p]))
    def test_undefined_citation_and_commented_citation(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder);(p/'references.bib').write_text('@article{known, title={Known}}')
            (p/'main.tex').write_text(r'\cite{known} % \cite{not_real}'+'\n')
            self.assertFalse(check_citations(p))
            (p/'main.tex').write_text(r'\cite{unknown}')
            self.assertTrue(check_citations(p))

if __name__=='__main__':unittest.main()

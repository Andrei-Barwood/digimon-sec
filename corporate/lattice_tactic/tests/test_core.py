"""
Unit tests for LatticeTactic (Production)
"""

import pytest

from lattice_tactic.core import LatticeTactic
from lattice_tactic.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return LatticeTactic()


def test_init_default(module):
    assert module.name == "Lattice Tactic"
    assert module.mission == "Forced Proximity"
    assert module.role == "cti-analyzer"


def test_primary_method(module):
    data = {
    "campaign_links_found": 5,
    "ttp_matches": 9,
    "sector_relevance_score": 0.82,
    "active_adversary_signal": True,
}
    report = module.analyze_cti(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "campaign_links_found": 5,
    "ttp_matches": 9,
    "sector_relevance_score": 0.82,
    "active_adversary_signal": True,
}
    result = module.analyze(cti_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

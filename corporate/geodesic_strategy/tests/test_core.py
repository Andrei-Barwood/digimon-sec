"""
Unit tests for GeodesicStrategy (Production)
"""

import pytest

from geodesic_strategy.core import GeodesicStrategy
from geodesic_strategy.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return GeodesicStrategy()


def test_init_default(module):
    assert module.name == "Geodesic Strategy"
    assert module.mission == "The New Austin"
    assert module.role == "strategic-planner"


def test_primary_method(module):
    data = {
    "risk_domains_pending": 4,
    "budget_alignment_score": 0.74,
    "control_gap_critical": 2,
    "board_priority_defined": True,
}
    report = module.plan_security_strategy(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "risk_domains_pending": 4,
    "budget_alignment_score": 0.74,
    "control_gap_critical": 2,
    "board_priority_defined": True,
}
    result = module.analyze(strategy_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

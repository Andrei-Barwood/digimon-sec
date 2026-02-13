"""
Unit tests for PolytopeMetrics (Production)
"""

import pytest

from polytope_metrics.core import PolytopeMetrics
from polytope_metrics.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return PolytopeMetrics()


def test_init_default(module):
    assert module.name == "Polytope Metrics"
    assert module.mission == "Charlotte Balfour"
    assert module.role == "kpi-tracker"


def test_primary_method(module):
    data = {
    "mttr_hours": 6,
    "mttd_hours": 3,
    "coverage_ratio": 0.79,
    "critical_alert_backlog": 14,
}
    report = module.track_security_kpis(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "mttr_hours": 6,
    "mttd_hours": 3,
    "coverage_ratio": 0.79,
    "critical_alert_backlog": 14,
}
    result = module.analyze(metrics_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

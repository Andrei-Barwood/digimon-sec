"""
Unit tests for FractalReport (Production)
"""

import pytest

from fractal_report.core import FractalReport
from fractal_report.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return FractalReport()


def test_init_default(module):
    assert module.name == "Fractal Report"
    assert module.mission == "The Noblest of Men"
    assert module.role == "report-generator"


def test_primary_method(module):
    data = {
    "critical_findings": 6,
    "sla_breaches": 2,
    "executive_summary_ready": True,
    "evidence_coverage_ratio": 0.91,
}
    report = module.generate_security_report(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "critical_findings": 6,
    "sla_breaches": 2,
    "executive_summary_ready": True,
    "evidence_coverage_ratio": 0.91,
}
    result = module.analyze(report_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

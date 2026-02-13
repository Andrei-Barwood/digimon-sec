"""
Unit tests for LemniscateCompliance (Production)
"""

import pytest

from lemniscate_compliance.core import LemniscateCompliance
from lemniscate_compliance.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return LemniscateCompliance()


def test_init_default(module):
    assert module.name == "Lemniscate Compliance"
    assert module.mission == "Good, Honest Snake Oil"
    assert module.role == "compliance-monitor"


def test_primary_method(module):
    data = {
    "failed_controls": 4,
    "evidence_missing_items": 9,
    "policy_drift_detected": True,
    "audit_window_days": 21,
}
    report = module.monitor_compliance(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "failed_controls": 4,
    "evidence_missing_items": 9,
    "policy_drift_detected": True,
    "audit_window_days": 21,
}
    result = module.analyze(compliance_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

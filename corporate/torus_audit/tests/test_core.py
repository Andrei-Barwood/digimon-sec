"""
Unit tests for TorusAudit (Production)
"""

import pytest

from torus_audit.core import TorusAudit
from torus_audit.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return TorusAudit()


def test_init_default(module):
    assert module.name == "Torus Audit"
    assert module.mission == "Clemens Point"
    assert module.role == "audit-logger"


def test_primary_method(module):
    data = {
    "unsigned_events_detected": 2,
    "log_retention_gap_days": 5,
    "tamper_suspected": True,
    "critical_event_loss": False,
}
    report = module.log_audit_events(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "unsigned_events_detected": 2,
    "log_retention_gap_days": 5,
    "tamper_suspected": True,
    "critical_event_loss": False,
}
    result = module.analyze(audit_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

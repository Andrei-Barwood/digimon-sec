"""
Unit tests for HelixNotify (Production)
"""

import pytest

from helix_notify.core import HelixNotify
from helix_notify.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return HelixNotify()


def test_init_default(module):
    assert module.name == "Helix Notify"
    assert module.mission == "The Gilded Cage"
    assert module.role == "security-notifier"


def test_primary_method(module):
    data = {
    "critical_alerts_pending": 3,
    "escalation_delay_minutes": 22,
    "channel_delivery_failures": 1,
    "oncall_ack_missing": True,
}
    report = module.notify_security_events(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "critical_alerts_pending": 3,
    "escalation_delay_minutes": 22,
    "channel_delivery_failures": 1,
    "oncall_ack_missing": True,
}
    result = module.analyze(notification_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

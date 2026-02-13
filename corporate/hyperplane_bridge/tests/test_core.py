"""
Unit tests for HyperplaneBridge (Production)
"""

import pytest

from hyperplane_bridge.core import HyperplaneBridge
from hyperplane_bridge.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return HyperplaneBridge()


def test_init_default(module):
    assert module.name == "Hyperplane Bridge"
    assert module.mission == "Marko Dragic"
    assert module.role == "api-integrator"


def test_primary_method(module):
    data = {
    "connected_services": 14,
    "auth_failures_last_hour": 2,
    "schema_drift_detected": True,
    "rate_limit_events": 5,
}
    report = module.integrate_apis(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "connected_services": 14,
    "auth_failures_last_hour": 2,
    "schema_drift_detected": True,
    "rate_limit_events": 5,
}
    result = module.analyze(api_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

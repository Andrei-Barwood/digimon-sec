"""
Unit tests for VertexHook (Production)
"""

import pytest

from vertex_hook.core import VertexHook
from vertex_hook.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return VertexHook()


def test_init_default(module):
    assert module.name == "Vertex Hook"
    assert module.mission == "Red Dead Redemption"
    assert module.role == "webhook-manager"


def test_primary_method(module):
    data = {
    "unsigned_payload_attempts": 3,
    "delivery_failures": 4,
    "retry_queue_depth": 11,
    "critical_endpoint_latency_ms": 920,
}
    report = module.manage_webhooks(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "unsigned_payload_attempts": 3,
    "delivery_failures": 4,
    "retry_queue_depth": 11,
    "critical_endpoint_latency_ms": 920,
}
    result = module.analyze(webhook_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

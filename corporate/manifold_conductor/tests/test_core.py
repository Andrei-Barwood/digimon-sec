"""
Unit tests for ManifoldConductor (Production)
"""

import pytest

from manifold_conductor.core import ManifoldConductor
from manifold_conductor.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return ManifoldConductor()


def test_init_default(module):
    assert module.name == "Manifold Conductor"
    assert module.mission == "American Venom"
    assert module.role == "security-orchestrator"


def test_primary_method(module):
    data = {
    "playbooks_available": 18,
    "automation_success_rate": 0.86,
    "manual_steps_remaining": 7,
    "critical_workflow_timeout": False,
}
    report = module.orchestrate_security(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "playbooks_available": 18,
    "automation_success_rate": 0.86,
    "manual_steps_remaining": 7,
    "critical_workflow_timeout": False,
}
    result = module.analyze(orchestration_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

"""
Unit tests for PolyhedronCore (Production)
"""

import pytest

from polyhedron_core.core import PolyhedronCore
from polyhedron_core.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return PolyhedronCore()


def test_init_default(module):
    assert module.name == "Polyhedron Core"
    assert module.mission == "American Distillation"
    assert module.role == "framework-core"


def test_primary_method(module):
    data = {
    "module_health_degraded": 2,
    "pipeline_dependency_breaks": 1,
    "critical_contract_violation": True,
    "core_sync_delay_ms": 640,
}
    report = module.run_framework_core(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "module_health_degraded": 2,
    "pipeline_dependency_breaks": 1,
    "critical_contract_violation": True,
    "core_sync_delay_ms": 640,
}
    result = module.analyze(framework_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"

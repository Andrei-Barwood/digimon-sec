"""
Unit tests for VertexStillness (Production)
"""

import pytest

from vertex_stillness.core import VertexStillness
from vertex_stillness.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexStillness"""
    return VertexStillness()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Vertex Stillness"
        assert modulo.mission == "Outlaws from the West"
        assert modulo.role == "vpc-monitor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_flow_logs": False, "severity_threshold": "high"}
        modulo = VertexStillness(config=config)
        assert modulo.require_flow_logs is False
        assert modulo.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_vpc(self, modulo):
        """Test auditoria de VPC"""
        vpc_data = {"flow_logs_enabled": True, "public_subnets": False}
        report = modulo.audit_vpc(vpc_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_vpc(self, modulo):
        """Test analyze con datos de VPC"""
        vpc_data = {"flow_logs_enabled": True, "public_subnets": False}
        result = modulo.analyze(vpc_data=vpc_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"flow_logs_enabled": True}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Stillness"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


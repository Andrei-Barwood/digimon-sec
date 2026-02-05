"""
Unit tests for VPCmon (Mega)
"""

import pytest

from vpcmon.core import VPCmon
from vpcmon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de VPCmon"""
    return VPCmon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "VPCmon"
        assert digimon.mission == "Outlaws from the West"
        assert digimon.role == "vpc-monitor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_flow_logs": False, "severity_threshold": "high"}
        digimon = VPCmon(config=config)
        assert digimon.require_flow_logs is False
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_vpc(self, digimon):
        """Test auditoria de VPC"""
        vpc_data = {"flow_logs_enabled": True, "public_subnets": False}
        report = digimon.audit_vpc(vpc_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_vpc(self, digimon):
        """Test analyze con datos de VPC"""
        vpc_data = {"flow_logs_enabled": True, "public_subnets": False}
        result = digimon.analyze(vpc_data=vpc_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"flow_logs_enabled": True}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "VPCmon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


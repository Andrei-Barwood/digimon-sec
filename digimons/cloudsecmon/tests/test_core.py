"""
Unit tests for CloudSecmon (Mega)
"""

import pytest

from cloudsecmon.core import CloudSecmon
from cloudsecmon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de CloudSecmon"""
    return CloudSecmon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "CloudSecmon"
        assert digimon.mission == "American Venom"
        assert digimon.role == "cloud-config-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_encryption": False, "severity_threshold": "high"}
        digimon = CloudSecmon(config=config)
        assert digimon.require_encryption is False
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_config(self, digimon):
        """Test auditoria de configuracion"""
        config_data = {"encryption_enabled": True, "logging_enabled": True, "mfa_enabled": True}
        report = digimon.audit_config(config_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_config(self, digimon):
        """Test analyze con datos de configuracion"""
        config_data = {"encryption_enabled": True, "logging_enabled": True, "mfa_enabled": True}
        result = digimon.analyze(config_data=config_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"encryption_enabled": True}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "CloudSecmon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


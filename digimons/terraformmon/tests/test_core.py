"""
Unit tests for Terraformmon (Mega)
"""

import pytest

from terraformmon.core import Terraformmon
from terraformmon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de Terraformmon"""
    return Terraformmon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "Terraformmon"
        assert digimon.mission == "Red Dead Redemption"
        assert digimon.role == "iac-validator"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        digimon = Terraformmon(config=config)
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, digimon):
        """Test auditoria basica"""
        sample = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}
        report = digimon.validate_iac(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, digimon):
        """Test analyze con datos"""
        sample = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}
        result = digimon.analyze(iac_data=sample)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"key": "value"}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Terraformmon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

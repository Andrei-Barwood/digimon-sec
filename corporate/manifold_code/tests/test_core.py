"""
Unit tests for ManifoldCode (Production)
"""

import pytest

from manifold_code.core import ManifoldCode
from manifold_code.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de ManifoldCode"""
    return ManifoldCode()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Manifold Code"
        assert modulo.mission == "Red Dead Redemption"
        assert modulo.role == "iac-validator"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        modulo = ManifoldCode(config=config)
        assert modulo.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, modulo):
        """Test auditoria basica"""
        sample = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}
        report = modulo.validate_iac(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, modulo):
        """Test analyze con datos"""
        sample = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}
        result = modulo.analyze(iac_data=sample)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"key": "value"}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Manifold Code"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

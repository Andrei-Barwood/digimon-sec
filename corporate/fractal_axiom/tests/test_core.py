"""
Unit tests for FractalAxiom (Production)
"""

import pytest

from fractal_axiom.core import FractalAxiom
from fractal_axiom.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de FractalAxiom"""
    return FractalAxiom()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Fractal Axiom"
        assert modulo.mission == "American Venom"
        assert modulo.role == "cloud-config-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_encryption": False, "severity_threshold": "high"}
        modulo = FractalAxiom(config=config)
        assert modulo.require_encryption is False
        assert modulo.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_config(self, modulo):
        """Test auditoria de configuracion"""
        config_data = {"encryption_enabled": True, "logging_enabled": True, "mfa_enabled": True}
        report = modulo.audit_config(config_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_config(self, modulo):
        """Test analyze con datos de configuracion"""
        config_data = {"encryption_enabled": True, "logging_enabled": True, "mfa_enabled": True}
        result = modulo.analyze(config_data=config_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"encryption_enabled": True}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Fractal Axiom"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


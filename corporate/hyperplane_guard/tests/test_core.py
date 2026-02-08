"""
Unit tests for HyperplaneGuard (Production)
"""

import pytest

from hyperplane_guard.core import HyperplaneGuard
from hyperplane_guard.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de HyperplaneGuard"""
    return HyperplaneGuard()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Hyperplane Guard"
        assert modulo.mission == "Good, Honest Snake Oil"
        assert modulo.role == "firewall-manager"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"allowed_ports": [22], "require_logging": False}
        modulo = HyperplaneGuard(config=config)
        assert modulo.allowed_ports == [22]
        assert modulo.require_logging is False


class TestAudit:
    """Tests para auditoria"""

    def test_audit_rules(self, modulo):
        """Test auditoria de reglas"""
        rules_data = {"default_deny": True, "open_ports": [80], "logging_enabled": True}
        report = modulo.audit_rules(rules_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_rules(self, modulo):
        """Test analyze con datos de firewall"""
        rules_data = {"default_deny": True, "open_ports": [80], "logging_enabled": True}
        result = modulo.analyze(rules_data=rules_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"default_deny": True}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Hyperplane Guard"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


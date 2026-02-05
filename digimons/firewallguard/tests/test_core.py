"""
Unit tests for FirewallGuard (Mega)
"""

import pytest

from firewallguard.core import FirewallGuard
from firewallguard.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de FirewallGuard"""
    return FirewallGuard()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "FirewallGuard"
        assert digimon.mission == "Good, Honest Snake Oil"
        assert digimon.role == "firewall-manager"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"allowed_ports": [22], "require_logging": False}
        digimon = FirewallGuard(config=config)
        assert digimon.allowed_ports == [22]
        assert digimon.require_logging is False


class TestAudit:
    """Tests para auditoria"""

    def test_audit_rules(self, digimon):
        """Test auditoria de reglas"""
        rules_data = {"default_deny": True, "open_ports": [80], "logging_enabled": True}
        report = digimon.audit_rules(rules_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_rules(self, digimon):
        """Test analyze con datos de firewall"""
        rules_data = {"default_deny": True, "open_ports": [80], "logging_enabled": True}
        result = digimon.analyze(rules_data=rules_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"default_deny": True}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "FirewallGuard"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


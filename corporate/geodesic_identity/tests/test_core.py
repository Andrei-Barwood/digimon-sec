"""
Unit tests for GeodesicIdentity (Production)
"""

import pytest

from geodesic_identity.core import GeodesicIdentity
from geodesic_identity.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de GeodesicIdentity"""
    return GeodesicIdentity()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Geodesic Identity"
        assert modulo.mission == "Charlotte Balfour"
        assert modulo.role == "iam-analyzer"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_mfa": False, "max_inactive_users": 2}
        modulo = GeodesicIdentity(config=config)
        assert modulo.require_mfa is False
        assert modulo.max_inactive_users == 2


class TestAudit:
    """Tests para auditoria"""

    def test_audit_iam(self, modulo):
        """Test auditoria de IAM"""
        iam_data = {"wildcard_permissions": False, "mfa_enforced": True, "rotation_enabled": True}
        report = modulo.audit_iam(iam_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_iam(self, modulo):
        """Test analyze con datos IAM"""
        iam_data = {"wildcard_permissions": False, "mfa_enforced": True, "rotation_enabled": True}
        result = modulo.analyze(iam_data=iam_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"mfa_enforced": True}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Geodesic Identity"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


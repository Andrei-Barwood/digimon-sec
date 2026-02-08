"""
Unit tests for TorusVault (Production)
"""

import pytest

from torus_vault.core import TorusVault
from torus_vault.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TorusVault"""
    return TorusVault()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Torus Vault"
        assert modulo.mission == "Paradise Mercifully Departed"
        assert modulo.role == "s3-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_versioning": False, "severity_threshold": "high"}
        modulo = TorusVault(config=config)
        assert modulo.require_versioning is False
        assert modulo.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_bucket(self, modulo):
        """Test auditoria de bucket"""
        bucket_data = {
            "public_access": False,
            "encryption_enabled": True,
            "versioning_enabled": True,
            "logging_enabled": True,
        }
        report = modulo.audit_bucket(bucket_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_bucket(self, modulo):
        """Test analyze con datos S3"""
        bucket_data = {
            "public_access": False,
            "encryption_enabled": True,
            "versioning_enabled": True,
            "logging_enabled": True,
        }
        result = modulo.analyze(bucket_data=bucket_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"public_access": False}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Torus Vault"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


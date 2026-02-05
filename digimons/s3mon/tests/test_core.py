"""
Unit tests for S3mon (Mega)
"""

import pytest

from s3mon.core import S3mon
from s3mon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de S3mon"""
    return S3mon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "S3mon"
        assert digimon.mission == "Paradise Mercifully Departed"
        assert digimon.role == "s3-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_versioning": False, "severity_threshold": "high"}
        digimon = S3mon(config=config)
        assert digimon.require_versioning is False
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit_bucket(self, digimon):
        """Test auditoria de bucket"""
        bucket_data = {
            "public_access": False,
            "encryption_enabled": True,
            "versioning_enabled": True,
            "logging_enabled": True,
        }
        report = digimon.audit_bucket(bucket_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_bucket(self, digimon):
        """Test analyze con datos S3"""
        bucket_data = {
            "public_access": False,
            "encryption_enabled": True,
            "versioning_enabled": True,
            "logging_enabled": True,
        }
        result = digimon.analyze(bucket_data=bucket_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"public_access": False}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "S3mon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


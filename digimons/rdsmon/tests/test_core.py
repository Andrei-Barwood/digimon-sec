"""
Unit tests for RDSmon (Mega)
"""

import pytest

from rdsmon.core import RDSmon
from rdsmon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de RDSmon"""
    return RDSmon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "RDSmon"
        assert digimon.mission == "The Noblest of Men"
        assert digimon.role == "database-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        digimon = RDSmon(config=config)
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, digimon):
        """Test auditoria basica"""
        sample = {
    "public_access": False,
    "storage_encrypted": True,
    "backup_retention_days": 7,
    "multi_az": True,
}
        report = digimon.audit_database(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, digimon):
        """Test analyze con datos"""
        sample = {
    "public_access": False,
    "storage_encrypted": True,
    "backup_retention_days": 7,
    "multi_az": True,
}
        result = digimon.analyze(db_data=sample)
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
        assert info["name"] == "RDSmon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

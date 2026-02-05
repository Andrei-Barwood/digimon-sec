"""
Unit tests for ComplianceCloud (Mega)
"""

import pytest

from compliancecloud.core import ComplianceCloud
from compliancecloud.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de ComplianceCloud"""
    return ComplianceCloud()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "ComplianceCloud"
        assert digimon.mission == "Good Intentions"
        assert digimon.role == "cloud-compliance"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        digimon = ComplianceCloud(config=config)
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, digimon):
        """Test auditoria basica"""
        sample = {
    "passed_controls": 3,
    "evidence_collected": True,
    "continuous_monitoring": True,
    "frameworks_checked": ["SOC2"],
}
        report = digimon.audit_compliance(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, digimon):
        """Test analyze con datos"""
        sample = {
    "passed_controls": 3,
    "evidence_collected": True,
    "continuous_monitoring": True,
    "frameworks_checked": ["SOC2"],
}
        result = digimon.analyze(compliance_data=sample)
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
        assert info["name"] == "ComplianceCloud"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

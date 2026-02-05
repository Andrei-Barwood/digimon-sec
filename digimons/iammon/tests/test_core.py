"""
Unit tests for IAMmon (Mega)
"""

import pytest

from iammon.core import IAMmon
from iammon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de IAMmon"""
    return IAMmon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "IAMmon"
        assert digimon.mission == "Charlotte Balfour"
        assert digimon.role == "iam-analyzer"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"require_mfa": False, "max_inactive_users": 2}
        digimon = IAMmon(config=config)
        assert digimon.require_mfa is False
        assert digimon.max_inactive_users == 2


class TestAudit:
    """Tests para auditoria"""

    def test_audit_iam(self, digimon):
        """Test auditoria de IAM"""
        iam_data = {"wildcard_permissions": False, "mfa_enforced": True, "rotation_enabled": True}
        report = digimon.audit_iam(iam_data)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze_iam(self, digimon):
        """Test analyze con datos IAM"""
        iam_data = {"wildcard_permissions": False, "mfa_enforced": True, "rotation_enabled": True}
        result = digimon.analyze(iam_data=iam_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"mfa_enforced": True}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "IAMmon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


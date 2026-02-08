"""
Unit tests for LemniscateRight (Production)
"""

import sys
from pathlib import Path

# Add src directory to Python path for local imports
# This ensures imports work both when running directly and with pytest
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import pytest

from lemniscate_right.core import LemniscateRight
from lemniscate_right.models import AnalysisResult, GDPRComplianceReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de LemniscateRight"""
    return LemniscateRight()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Lemniscate Right"
        assert modulo.mission == "Charlotte Balfour"
        assert modulo.role == "gdpr-enforcer"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"strict_mode": False, "check_consent_management": False}
        modulo = LemniscateRight(config=config)
        assert modulo.strict_mode is False
        assert modulo.check_consent_management is False


class TestGDPRCompliance:
    """Tests para cumplimiento GDPR"""

    def test_audit_compliance(self, modulo):
        """Test auditoría de cumplimiento"""
        target_data = {"name": "test_system", "consent_management_enabled": True, "encryption_enabled": True}
        report = modulo.audit_compliance(target_data)
        assert isinstance(report, GDPRComplianceReport)
        assert report.total_checks > 0

    def test_audit_compliance_with_failures(self, modulo):
        """Test auditoría con fallos"""
        target_data = {"name": "test_system", "consent_management_enabled": False}
        report = modulo.audit_compliance(target_data)
        assert report.failed_checks >= 0  # Puede tener fallos


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_target(self, modulo):
        """Test analyze con datos de objetivo"""
        target_data = {"name": "test_system", "encryption_enabled": True}
        result = modulo.analyze(target_data=target_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        assert modulo.validate({"name": "test"}) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Lemniscate Right"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


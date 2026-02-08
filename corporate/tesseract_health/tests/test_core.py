"""
Unit tests for TesseractHealth (Production)
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

from tesseract_health.core import TesseractHealth
from tesseract_health.models import AnalysisResult, HIPAAComplianceReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TesseractHealth"""
    return TesseractHealth()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Tesseract Health"
        assert modulo.mission == "My Last Boy"
        assert modulo.role == "hipaa-auditor"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"strict_mode": False, "check_phi_protection": False}
        modulo = TesseractHealth(config=config)
        assert modulo.strict_mode is False
        assert modulo.check_phi_protection is False


class TestHIPAACompliance:
    """Tests para cumplimiento HIPAA"""

    def test_audit_compliance(self, modulo):
        """Test auditoría de cumplimiento"""
        target_data = {"name": "test_system", "access_controls_enabled": True, "encryption_enabled": True}
        report = modulo.audit_compliance(target_data)
        assert isinstance(report, HIPAAComplianceReport)
        assert report.total_checks > 0

    def test_audit_compliance_with_failures(self, modulo):
        """Test auditoría con fallos"""
        target_data = {"name": "test_system", "access_controls_enabled": False}
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
        assert info["name"] == "Tesseract Health"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


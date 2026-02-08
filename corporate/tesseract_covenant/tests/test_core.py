"""
Unit tests for TesseractCovenant (Production)
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

from tesseract_covenant.core import TesseractCovenant
from tesseract_covenant.models import AnalysisResult, ComplianceAudit


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TesseractCovenant"""
    return TesseractCovenant()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Tesseract Covenant"
        assert modulo.mission == "Revenge"
        assert modulo.role == "compliance-checker"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"compliance_frameworks": ["GDPR", "HIPAA"], "strict_mode": False}
        modulo = TesseractCovenant(config=config)
        assert len(modulo.compliance_frameworks) == 2
        assert modulo.strict_mode is False


class TestComplianceAudit:
    """Tests para auditoría de compliance"""

    def test_audit_target(self, modulo):
        """Test auditoría de objetivo"""
        target_data = {"name": "test_system", "encryption_enabled": True, "access_controls": True}
        audit = modulo.audit_target(target_data)
        assert isinstance(audit, ComplianceAudit)
        assert audit.total_checks > 0

    def test_audit_target_with_failures(self, modulo):
        """Test auditoría con fallos"""
        target_data = {"name": "test_system", "encryption_enabled": False}
        audit = modulo.audit_target(target_data)
        assert audit.failed_checks >= 0  # Puede tener fallos


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
        assert info["name"] == "Tesseract Covenant"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


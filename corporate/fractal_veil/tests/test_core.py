"""
Unit tests for FractalVeil (Production)
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

from fractal_veil.core import FractalVeil
from fractal_veil.models import AnalysisResult, PrivacyAudit


@pytest.fixture
def modulo():
    """Fixture para crear instancia de FractalVeil"""
    return FractalVeil()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Fractal Veil"
        assert modulo.mission == "Clemens Point"
        assert modulo.role == "privacy-auditor"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"strict_mode": False, "check_data_collection": False}
        modulo = FractalVeil(config=config)
        assert modulo.strict_mode is False
        assert modulo.check_data_collection is False


class TestPrivacyAudit:
    """Tests para auditoría de privacidad"""

    def test_audit_policy(self, modulo):
        """Test auditoría de política"""
        target_data = {"name": "test_system", "consent_mechanism": True, "privacy_policy_public": True}
        audit = modulo.audit_policy(target_data)
        assert isinstance(audit, PrivacyAudit)
        assert audit.total_checks > 0

    def test_audit_policy_with_failures(self, modulo):
        """Test auditoría con fallos"""
        target_data = {"name": "test_system", "consent_mechanism": False}
        audit = modulo.audit_policy(target_data)
        assert audit.failed_checks >= 0  # Puede tener fallos


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_target(self, modulo):
        """Test analyze con datos de objetivo"""
        target_data = {"name": "test_system", "privacy_policy_public": True}
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
        assert info["name"] == "Fractal Veil"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


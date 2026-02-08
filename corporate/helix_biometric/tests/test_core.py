"""
Unit tests for HelixBiometric (Production)
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

from helix_biometric.core import HelixBiometric
from helix_biometric.models import AnalysisResult, BiometricAnalysis, BiometricData


@pytest.fixture
def modulo():
    """Fixture para crear instancia de HelixBiometric"""
    return HelixBiometric()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Helix Biometric"
        assert modulo.mission == "My Last Boy"
        assert modulo.role == "biometric-handler"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"min_confidence": 0.90, "enable_liveness": False}
        modulo = HelixBiometric(config=config)
        assert modulo.min_confidence == 0.90
        assert modulo.enable_liveness is False


class TestBiometricOperations:
    """Tests para operaciones biométricas"""

    def test_register_biometric(self, modulo):
        """Test registrar template biométrico"""
        bio = modulo.register_biometric("user1", "fingerprint", "template_data", 0.98, True)
        assert isinstance(bio, BiometricData)
        assert bio.user_id == "user1"

    def test_analyze_biometrics(self, modulo):
        """Test análisis de templates"""
        modulo.register_biometric("user1", "fingerprint", "template1", 0.98)
        analysis = modulo.analyze_biometrics()
        assert isinstance(analysis, BiometricAnalysis)
        assert analysis.total_templates == 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_biometrics(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_register(self, modulo):
        """Test analyze con register action"""
        bio_data = {
            "user_id": "user1",
            "biometric_type": "fingerprint",
            "template_data": "template123",
            "confidence": 0.98,
            "liveness_verified": True,
        }
        result = modulo.analyze(action="register", biometric_data=bio_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1", "biometric_type": "fingerprint"}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Helix Biometric"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


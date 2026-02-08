"""
Unit tests for TesseractFactor (Production)
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

from tesseract_factor.core import TesseractFactor
from tesseract_factor.models import AnalysisResult, MFAAnalysis, MFAChallenge


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TesseractFactor"""
    return TesseractFactor()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Tesseract Factor"
        assert modulo.mission == "Red Dead Redemption"
        assert modulo.role == "mfa-enforcer"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"code_expiry": 600, "max_attempts": 5}
        modulo = TesseractFactor(config=config)
        assert modulo.code_expiry == 600
        assert modulo.max_attempts == 5


class TestMFAOperations:
    """Tests para operaciones MFA"""

    def test_create_challenge(self, modulo):
        """Test crear desafío MFA"""
        challenge = modulo.create_challenge("user1", "totp")
        assert isinstance(challenge, MFAChallenge)
        assert challenge.user_id == "user1"

    def test_verify_challenge(self, modulo):
        """Test verificar código MFA"""
        challenge = modulo.create_challenge("user1", "totp")
        if challenge.code:
            result = modulo.verify_challenge(challenge.challenge_id, challenge.code)
            assert result is True

    def test_analyze_mfa(self, modulo):
        """Test análisis de MFA"""
        modulo.create_challenge("user1")
        analysis = modulo.analyze_mfa()
        assert isinstance(analysis, MFAAnalysis)
        assert analysis.total_challenges >= 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_mfa(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_create(self, modulo):
        """Test analyze con create action"""
        challenge_data = {"user_id": "user1", "method": "totp"}
        result = modulo.analyze(action="create", challenge_data=challenge_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1"}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Tesseract Factor"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


"""
Unit tests for SimplexPass (Production)
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

from simplex_pass.core import SimplexPass
from simplex_pass.models import AnalysisResult, PasswordValidation


@pytest.fixture
def modulo():
    """Fixture para crear instancia de SimplexPass"""
    return SimplexPass()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Simplex Pass"
        assert modulo.mission == "The Gilded Cage"
        assert modulo.role == "password-validator"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"min_length": 16, "require_special": False}
        modulo = SimplexPass(config=config)
        assert modulo.min_length == 16
        assert modulo.require_special is False


class TestPasswordValidation:
    """Tests para validación de contraseñas"""

    def test_validate_password_strong(self, modulo):
        """Test validación de contraseña fuerte"""
        result = modulo.validate_password("SecurePass123!@#")
        assert isinstance(result, PasswordValidation)
        assert result.strength in ["strong", "medium"]

    def test_validate_password_weak(self, modulo):
        """Test validación de contraseña débil"""
        result = modulo.validate_password("weak")
        assert result.valid is False
        assert len(result.violations) > 0


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_password(self, modulo):
        """Test analyze con una contraseña"""
        result = modulo.analyze(password="SecurePass123!")
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_multiple_passwords(self, modulo):
        """Test analyze con múltiples contraseñas"""
        passwords = ["SecurePass123!", "weak"]
        result = modulo.analyze(passwords=passwords)
        assert result.status in ["success", "warning"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("password123") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Simplex Pass"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


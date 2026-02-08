"""
Unit tests for VertexAuth (Production)
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

from vertex_auth.core import VertexAuth
from vertex_auth.models import AnalysisResult, AuthResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexAuth"""
    return VertexAuth()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Vertex Auth"
        assert modulo.mission == "The Noblest of Men"
        assert modulo.role == "auth-handler"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"max_attempts": 3, "lockout_duration": 600}
        modulo = VertexAuth(config=config)
        assert modulo.max_attempts == 3
        assert modulo.lockout_duration == 600


class TestAuthentication:
    """Tests para autenticación"""

    def test_authenticate_success(self, modulo):
        """Test autenticación exitosa"""
        result = modulo.authenticate("user1", {"password": "validpass"}, "password")
        assert isinstance(result, AuthResult)
        assert result.success is True

    def test_authenticate_failure(self, modulo):
        """Test autenticación fallida"""
        result = modulo.authenticate("user1", {"password": ""}, "password")
        assert result.success is False


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_success(self, modulo):
        """Test analyze con autenticación exitosa"""
        result = modulo.analyze("user1", {"password": "validpass"})
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_failure(self, modulo):
        """Test analyze con autenticación fallida"""
        result = modulo.analyze("user1", {"password": ""})
        assert result.status in ["error", "warning"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1", "credentials": {"password": "pass"}}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Auth"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


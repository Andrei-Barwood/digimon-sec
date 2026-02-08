"""
Unit tests for LemniscateOauth (Production)
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

from lemniscate_oauth.core import LemniscateOauth
from lemniscate_oauth.models import AnalysisResult, OAuthAnalysis, OAuthToken


@pytest.fixture
def modulo():
    """Fixture para crear instancia de LemniscateOauth"""
    return LemniscateOauth()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Lemniscate OAuth"
        assert modulo.mission == "Marko Dragic"
        assert modulo.role == "oauth-handler"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"client_id": "client123", "authorization_url": "https://auth.example.com"}
        modulo = LemniscateOauth(config=config)
        assert modulo.client_id == "client123"
        assert modulo.authorization_url == "https://auth.example.com"


class TestOAuthOperations:
    """Tests para operaciones OAuth"""

    def test_generate_token(self, modulo):
        """Test generar token OAuth"""
        token = modulo.generate_token("authorization_code", "read write")
        assert isinstance(token, OAuthToken)
        assert token.token_type == "Bearer"

    def test_validate_token(self, modulo):
        """Test validar token"""
        token = modulo.generate_token()
        assert modulo.validate_token(token.access_token) is True

    def test_analyze_oauth(self, modulo):
        """Test análisis de OAuth"""
        modulo.generate_token()
        analysis = modulo.analyze_oauth()
        assert isinstance(analysis, OAuthAnalysis)
        assert analysis.active_tokens >= 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_oauth(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_generate(self, modulo):
        """Test analyze con generate action"""
        token_data = {"flow_type": "authorization_code", "scope": "read"}
        result = modulo.analyze(action="generate", token_data=token_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("token_string") is True

    def test_validate_dict(self, modulo):
        """Test validación con diccionario"""
        assert modulo.validate({"flow_type": "authorization_code"}) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Lemniscate OAuth"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


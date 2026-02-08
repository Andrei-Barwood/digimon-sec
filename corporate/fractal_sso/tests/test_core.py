"""
Unit tests for FractalSso (Production)
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

from fractal_sso.core import FractalSso
from fractal_sso.models import AnalysisResult, SSOAnalysis, SSOSession


@pytest.fixture
def modulo():
    """Fixture para crear instancia de FractalSso"""
    return FractalSso()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Fractal SSO"
        assert modulo.mission == "Goodbye, Dear Friend"
        assert modulo.role == "sso-manager"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"enable_saml": False, "idp_url": "https://idp.example.com"}
        modulo = FractalSso(config=config)
        assert modulo.enable_saml is False
        assert modulo.idp_url == "https://idp.example.com"


class TestSSOOperations:
    """Tests para operaciones SSO"""

    def test_create_sso_session(self, modulo):
        """Test crear sesión SSO"""
        session = modulo.create_sso_session("user1", "idp1", "SAML")
        assert isinstance(session, SSOSession)
        assert session.user_id == "user1"

    def test_analyze_sso(self, modulo):
        """Test análisis de SSO"""
        modulo.create_sso_session("user1", "idp1", "SAML")
        analysis = modulo.analyze_sso()
        assert isinstance(analysis, SSOAnalysis)
        assert analysis.active_sessions >= 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_sso(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_create(self, modulo):
        """Test analyze con create action"""
        session_data = {"user_id": "user1", "idp": "idp1", "protocol": "SAML"}
        result = modulo.analyze(action="create", session_data=session_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1", "protocol": "SAML"}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Fractal SSO"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


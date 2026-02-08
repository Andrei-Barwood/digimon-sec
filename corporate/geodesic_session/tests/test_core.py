"""
Unit tests for GeodesicSession (Production)
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

from geodesic_session.core import GeodesicSession
from geodesic_session.models import AnalysisResult, SessionAnalysis, Session


@pytest.fixture
def modulo():
    """Fixture para crear instancia de GeodesicSession"""
    return GeodesicSession()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Geodesic Session"
        assert modulo.mission == "Polite Society"
        assert modulo.role == "session-manager"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"session_timeout": 1800, "max_concurrent_sessions": 5}
        modulo = GeodesicSession(config=config)
        assert modulo.session_timeout == 1800
        assert modulo.max_concurrent_sessions == 5


class TestSessionOperations:
    """Tests para operaciones con sesiones"""

    def test_create_session(self, modulo):
        """Test crear sesión"""
        session = modulo.create_session("user1")
        assert isinstance(session, Session)
        assert session.user_id == "user1"

    def test_validate_session(self, modulo):
        """Test validar sesión"""
        session = modulo.create_session("user1")
        assert modulo.validate_session(session.session_id) is True

    def test_analyze_sessions(self, modulo):
        """Test análisis de sesiones"""
        modulo.create_session("user1")
        analysis = modulo.analyze_sessions()
        assert isinstance(analysis, SessionAnalysis)
        assert analysis.active_sessions >= 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_sessions(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_create(self, modulo):
        """Test analyze con create action"""
        result = modulo.analyze(action="create", user_id="user1")
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("session_id") is True

    def test_validate_dict(self, modulo):
        """Test validación con diccionario"""
        assert modulo.validate({"user_id": "user1"}) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Geodesic Session"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


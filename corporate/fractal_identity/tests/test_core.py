"""
Unit tests for FractalIdentity (Production)
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

from fractal_identity.core import FractalIdentity
from fractal_identity.models import AnalysisResult, Identity, IdentityAnalysis


@pytest.fixture
def modulo():
    """Fixture para crear instancia de FractalIdentity"""
    return FractalIdentity()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Fractal Identity"
        assert modulo.mission == "The Gunslinger"
        assert modulo.role == "identity-manager"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"validate_attributes": False, "enforce_policies": False}
        modulo = FractalIdentity(config=config)
        assert modulo.validate_attributes is False
        assert modulo.enforce_policies is False


class TestIdentityValidation:
    """Tests para validación de identidades"""

    def test_validate_identity(self, modulo):
        """Test validación de identidad"""
        identity_data = {"user_id": "user1", "username": "testuser", "email": "test@example.com"}
        identity = modulo.validate_identity(identity_data)
        assert isinstance(identity, Identity)
        assert identity.user_id == "user1"

    def test_analyze_identities(self, modulo):
        """Test análisis de múltiples identidades"""
        identities = [
            {"user_id": "user1", "username": "user1", "roles": ["admin"]},
            {"user_id": "user2", "username": "user2", "roles": ["user"]},
        ]
        analysis = modulo.analyze_identities(identities)
        assert isinstance(analysis, IdentityAnalysis)
        assert analysis.total_identities == 2


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_identity(self, modulo):
        """Test analyze con una identidad"""
        identity = {"user_id": "user1", "username": "testuser"}
        result = modulo.analyze(identity=identity)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_multiple_identities(self, modulo):
        """Test analyze con múltiples identidades"""
        # Agregar email para evitar violaciones de política (la política requiere email)
        identities = [{"user_id": "user1", "username": "user1", "email": "user1@example.com"}]
        result = modulo.analyze(identities=identities)
        assert result.status == "success"
        assert result.data["total_identities"] == 1

    def test_analyze_no_input(self, modulo):
        """Test analyze sin input"""
        result = modulo.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1", "username": "testuser"}
        assert modulo.validate(data) is True

    def test_validate_list(self, modulo):
        """Test validación con lista válida"""
        data = [{"user_id": "user1", "username": "user1"}]
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Fractal Identity"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


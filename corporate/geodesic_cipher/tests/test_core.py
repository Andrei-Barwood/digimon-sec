"""
Unit tests for GeodesicCipher (Production)
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

from geodesic_cipher.core import GeodesicCipher
from geodesic_cipher.models import AnalysisResult, EncryptionKey


@pytest.fixture
def modulo():
    """Fixture para crear instancia de GeodesicCipher"""
    return GeodesicCipher()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Geodesic Cipher"
        assert modulo.mission == "Forced Proximity"
        assert modulo.role == "encryption-manager"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"default_algorithm": "ChaCha20-Poly1305", "key_rotation_days": 60}
        modulo = GeodesicCipher(config=config)
        assert modulo.default_algorithm == "ChaCha20-Poly1305"
        assert modulo.key_rotation_days == 60


class TestKeyManagement:
    """Tests para gestión de claves"""

    def test_generate_key(self, modulo):
        """Test generación de clave"""
        key = modulo.generate_key()
        assert isinstance(key, EncryptionKey)
        assert key.key_id is not None
        assert key.algorithm == modulo.default_algorithm

    def test_rotate_key(self, modulo):
        """Test rotación de clave"""
        key = modulo.generate_key()
        result = modulo.rotate_key(key.key_id)
        assert result.success is True
        assert result.keys_rotated == 1

    def test_revoke_key(self, modulo):
        """Test revocación de clave"""
        key = modulo.generate_key()
        result = modulo.revoke_key(key.key_id)
        assert result.success is True
        assert result.keys_revoked == 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_generate(self, modulo):
        """Test analyze con operación generate"""
        result = modulo.analyze(operation="generate")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_list(self, modulo):
        """Test analyze con operación list"""
        modulo.generate_key()
        result = modulo.analyze(operation="list")
        assert result.status == "success"
        assert result.data["total_keys"] >= 1


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_operation(self, modulo):
        """Test validación con operación válida"""
        assert modulo.validate("generate") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Geodesic Cipher"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


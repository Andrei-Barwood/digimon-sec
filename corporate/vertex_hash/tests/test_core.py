"""
Unit tests for VertexHash (Production)
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

from vertex_hash.core import VertexHash
from vertex_hash.models import AnalysisResult, HashResult, VerificationResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexHash"""
    return VertexHash()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Vertex Hash"
        assert modulo.mission == "Forever Yours, Arthur"
        assert modulo.role == "hash-validator"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"default_algorithm": "sha512", "enable_hmac": False}
        modulo = VertexHash(config=config)
        assert modulo.default_algorithm == "sha512"
        assert modulo.enable_hmac is False


class TestHashComputation:
    """Tests para cálculo de hash"""

    def test_compute_hash(self, modulo):
        """Test cálculo de hash"""
        data = b"test data"
        result = modulo.compute_hash(data)
        assert isinstance(result, HashResult)
        assert result.algorithm == modulo.default_algorithm
        assert len(result.hash_value) > 0

    def test_compute_hash_different_algorithm(self, modulo):
        """Test cálculo con algoritmo diferente"""
        data = b"test data"
        result = modulo.compute_hash(data, algorithm="sha512")
        assert result.algorithm == "sha512"


class TestHashVerification:
    """Tests para verificación de hash"""

    def test_verify_hash_match(self, modulo):
        """Test verificación con hash que coincide"""
        data = b"test data"
        hash_result = modulo.compute_hash(data)
        verify_result = modulo.verify_hash(data, hash_result.hash_value)
        assert verify_result.verified is True
        assert verify_result.match is True

    def test_verify_hash_mismatch(self, modulo):
        """Test verificación con hash que no coincide"""
        data = b"test data"
        verify_result = modulo.verify_hash(data, "invalid_hash")
        assert verify_result.verified is False
        assert verify_result.match is False


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_compute(self, modulo):
        """Test analyze para cálculo"""
        data = b"test data"
        result = modulo.analyze(data=data)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_verify(self, modulo):
        """Test analyze para verificación"""
        data = b"test data"
        hash_result = modulo.compute_hash(data)
        result = modulo.analyze(data=data, expected_hash=hash_result.hash_value)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_bytes(self, modulo):
        """Test validación con bytes"""
        assert modulo.validate(b"test") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Hash"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


"""
Unit tests for ManifoldFuzz (Production)
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

from manifold_fuzz.core import ManifoldFuzz
from manifold_fuzz.models import AnalysisResult, FuzzResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de ManifoldFuzz"""
    return ManifoldFuzz()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Manifold Fuzz"
        assert modulo.mission == "Fleeting Joy"
        assert modulo.role == "fuzz-tester"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"max_iterations": 500, "mutation_rate": 0.2}
        modulo = ManifoldFuzz(config=config)
        assert modulo.max_iterations == 500
        assert modulo.mutation_rate == 0.2


class TestFuzzing:
    """Tests para fuzzing"""

    def test_generate_fuzz_input(self, modulo):
        """Test generación de entrada fuzzed"""
        fuzz_input = modulo.generate_fuzz_input()
        assert isinstance(fuzz_input, str)
        assert len(fuzz_input) > 0

    def test_generate_fuzz_input_with_base(self, modulo):
        """Test generación de entrada con base"""
        base = "test input"
        fuzz_input = modulo.generate_fuzz_input(base)
        assert isinstance(fuzz_input, str)

    def test_fuzz_target(self, modulo):
        """Test fuzzing de objetivo"""
        result = modulo.fuzz_target()
        assert isinstance(result, FuzzResult)
        assert result.total_tests > 0


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_fuzzing(self, modulo):
        """Test analyze con fuzzing"""
        result = modulo.analyze(iterations=50)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_with_base_input(self, modulo):
        """Test analyze con entrada base"""
        result = modulo.analyze(base_input="test", iterations=50)
        assert isinstance(result, AnalysisResult)


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("test input") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Manifold Fuzz"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

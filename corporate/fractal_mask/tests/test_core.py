"""
Unit tests for FractalMask (Production)
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

from fractal_mask.core import FractalMask
from fractal_mask.models import AnalysisResult, MaskingResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de FractalMask"""
    return FractalMask()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Fractal Mask"
        assert modulo.mission == "Good, Honest Snake Oil"
        assert modulo.role == "data-masker"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"mask_character": "X", "preserve_format": False}
        modulo = FractalMask(config=config)
        assert modulo.mask_character == "X"
        assert modulo.preserve_format is False


class TestMasking:
    """Tests para enmascarado"""

    def test_mask_text_email(self, modulo):
        """Test enmascarado de email"""
        text = "Contact: test@example.com"
        result = modulo.mask_text(text)
        assert isinstance(result, MaskingResult)
        assert "test@example.com" not in result.masked_text
        assert "@example.com" in result.masked_text  # Dominio preservado

    def test_mask_text_credit_card(self, modulo):
        """Test enmascarado de tarjeta de crédito"""
        text = "Card: 1234-5678-9012-3456"
        result = modulo.mask_text(text)
        assert result.total_masked >= 1
        assert "3456" in result.masked_text  # Últimos 4 dígitos preservados


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_text(self, modulo):
        """Test analyze con un texto"""
        text = "Email: test@example.com"
        result = modulo.analyze(text=text)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_multiple_texts(self, modulo):
        """Test analyze con múltiples textos"""
        texts = ["Email: test@example.com", "Phone: 555-1234"]
        result = modulo.analyze(texts=texts)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("valid text") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Fractal Mask"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


"""
Unit tests for TorusRedact (Production)
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

from torus_redact.core import TorusRedact
from torus_redact.models import AnalysisResult, RedactionResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TorusRedact"""
    return TorusRedact()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Torus Redact"
        assert modulo.mission == "Outlaws from the West"
        assert modulo.role == "data-redactor"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"redaction_style": "tokenize", "preserve_structure": False}
        modulo = TorusRedact(config=config)
        assert modulo.redaction_style == "tokenize"
        assert modulo.preserve_structure is False


class TestRedaction:
    """Tests para redacción"""

    def test_redact_text_email(self, modulo):
        """Test redacción de email"""
        text = "Contact: test@example.com"
        result = modulo.redact_text(text)
        assert isinstance(result, RedactionResult)
        assert "test@example.com" not in result.redacted_text

    def test_redact_text_multiple_pii(self, modulo):
        """Test redacción de múltiples tipos de PII"""
        text = "Email: test@example.com, Phone: 555-123-4567"
        result = modulo.redact_text(text)
        assert result.total_redactions >= 1


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
        assert info["name"] == "Torus Redact"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


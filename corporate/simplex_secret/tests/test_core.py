"""
Unit tests for SimplexSecret (Production)
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

from simplex_secret.core import SimplexSecret
from simplex_secret.models import AnalysisResult, RedactionResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de SimplexSecret"""
    return SimplexSecret()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Simplex Secret"
        assert modulo.mission == "Outlaws from the West"
        assert modulo.role == "data-protector"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"redaction_mode": "tokenize", "enable_ip_detection": False}
        modulo = SimplexSecret(config=config)
        assert modulo.redaction_mode == "tokenize"
        assert modulo.enable_ip_detection is False


class TestRedaction:
    """Tests para redacción de PII"""

    def test_redact_email(self, modulo):
        """Test redacción de emails"""
        text = "Contact me at test@example.com for more info."
        result = modulo.redact_pii(text)
        assert isinstance(result, RedactionResult)
        assert "test@example.com" not in result.safe_text
        assert result.total_redacted >= 1

    def test_redact_credit_card(self, modulo):
        """Test redacción de tarjetas de crédito"""
        text = "My card is 1234-5678-9012-3456."
        result = modulo.redact_pii(text)
        assert "1234-5678-9012-3456" not in result.safe_text
        assert result.total_redacted >= 1

    def test_no_pii(self, modulo):
        """Test texto sin PII"""
        text = "Hello world, everything is safe here."
        result = modulo.redact_pii(text)
        assert result.total_redacted == 0
        assert result.safe_text == text


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
        texts = ["Email: test@example.com", "Card: 1234-5678-9012-3456"]
        result = modulo.analyze(texts=texts)
        assert result.status == "success"
        assert "total_redacted" in result.data


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("valid text") is True

    def test_validate_list(self, modulo):
        """Test validación con lista"""
        assert modulo.validate(["text1", "text2"]) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Simplex Secret"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

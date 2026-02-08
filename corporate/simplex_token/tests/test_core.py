"""
Unit tests for SimplexToken (Production)
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

from simplex_token.core import SimplexToken
from simplex_token.models import AnalysisResult, TokenizationResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de SimplexToken"""
    return SimplexToken()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Simplex Token"
        assert modulo.mission == "Paradise Mercifully Departed"
        assert modulo.role == "tokenization-engine"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"token_format": "random", "enable_detokenization": False}
        modulo = SimplexToken(config=config)
        assert modulo.token_format == "random"
        assert modulo.enable_detokenization is False


class TestTokenization:
    """Tests para tokenización"""

    def test_tokenize_text(self, modulo):
        """Test tokenización de texto"""
        text = "Email: test@example.com"
        result = modulo.tokenize_text(text)
        assert isinstance(result, TokenizationResult)
        assert result.total_tokens >= 1

    def test_detokenize(self, modulo):
        """Test detokenización"""
        text = "Email: test@example.com"
        result = modulo.tokenize_text(text)
        if result.tokenization_records:
            token = result.tokenization_records[0].token
            detoken_result = modulo.detokenize(token)
            assert detoken_result.found is True


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_tokenize(self, modulo):
        """Test analyze para tokenización"""
        text = "Email: test@example.com"
        result = modulo.analyze(text=text)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_detokenize(self, modulo):
        """Test analyze para detokenización"""
        text = "Email: test@example.com"
        tokenize_result = modulo.tokenize_text(text)
        if tokenize_result.tokenization_records:
            token = tokenize_result.tokenization_records[0].token
            result = modulo.analyze(token=token)
            assert result.status in ["success", "error"]


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
        assert info["name"] == "Simplex Token"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


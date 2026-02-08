"""
Unit tests for PolytopeDlp (Production)
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

from polytope_dlp.core import PolytopeDlp
from polytope_dlp.models import AnalysisResult, PolicyViolation


@pytest.fixture
def modulo():
    """Fixture para crear instancia de PolytopeDlp"""
    return PolytopeDlp()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Polytope DLP"
        assert modulo.mission == "The New Austin"
        assert modulo.role == "data-loss-prevention"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"sensitivity_level": "high", "enable_blocking": False}
        modulo = PolytopeDlp(config=config)
        assert modulo.sensitivity_level == "high"
        assert modulo.enable_blocking is False


class TestContentScanning:
    """Tests para escaneo de contenido"""

    def test_scan_content_credit_card(self, modulo):
        """Test detección de tarjeta de crédito"""
        content = "My card is 1234-5678-9012-3456"
        violations = modulo.scan_content(content)
        assert len(violations) >= 1
        assert any(v.policy_name == "credit_card" for v in violations)

    def test_scan_content_ssn(self, modulo):
        """Test detección de SSN"""
        content = "SSN: 123-45-6789"
        violations = modulo.scan_content(content)
        assert len(violations) >= 1
        assert any(v.policy_name == "ssn" for v in violations)

    def test_scan_content_clean(self, modulo):
        """Test contenido limpio"""
        content = "This is clean text with no sensitive data"
        violations = modulo.scan_content(content)
        assert len(violations) == 0


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_content(self, modulo):
        """Test analyze con un contenido"""
        content = "Email: test@example.com"
        result = modulo.analyze(content=content)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_multiple_contents(self, modulo):
        """Test analyze con múltiples contenidos"""
        contents = ["Email: test@example.com", "Card: 1234-5678-9012-3456"]
        result = modulo.analyze(contents=contents)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("valid content") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Polytope DLP"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


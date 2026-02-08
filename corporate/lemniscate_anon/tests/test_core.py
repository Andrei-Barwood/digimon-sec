"""
Unit tests for LemniscateAnon (Production)
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

from lemniscate_anon.core import LemniscateAnon
from lemniscate_anon.models import AnalysisResult, AnonymizationResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de LemniscateAnon"""
    return LemniscateAnon()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Lemniscate Anon"
        assert modulo.mission == "Charlotte Balfour"
        assert modulo.role == "anonymizer"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"anonymization_method": "generalize", "reversible": True}
        modulo = LemniscateAnon(config=config)
        assert modulo.anonymization_method == "generalize"
        assert modulo.reversible is True


class TestAnonymization:
    """Tests para anonimización"""

    def test_anonymize_data(self, modulo):
        """Test anonimización de datos"""
        data = {"name": "John Doe", "email": "john@example.com", "age": "30"}
        result = modulo.anonymize_data(data)
        assert isinstance(result, AnonymizationResult)
        assert result.anonymized_fields >= 1

    def test_anonymize_specific_fields(self, modulo):
        """Test anonimización de campos específicos"""
        data = {"name": "John", "email": "john@example.com", "public": "data"}
        result = modulo.anonymize_data(data, fields_to_anonymize=["email"])
        assert "email" in result.anonymized_data
        assert result.anonymized_data["email"] != "john@example.com"


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_data(self, modulo):
        """Test analyze con datos"""
        data = {"name": "John", "email": "john@example.com"}
        result = modulo.analyze(data=data)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        assert modulo.validate({"name": "John"}) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Lemniscate Anon"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


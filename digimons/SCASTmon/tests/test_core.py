"""
Unit tests for SCASTmon core module
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
from SCASTmon.core import Scastmon


@pytest.fixture
def digimon():
    """Fixture para crear instancia de Scastmon"""
    return Scastmon()


class TestInitialization:
    """Tests para inicialización"""
    
    def test_init_default(self):
        """Test inicialización con valores por defecto"""
        digimon = Scastmon()
        assert digimon.name == "SCASTmon"
        assert digimon.mission == "The Noblest of Men"
        assert digimon.role == "SAST Scanner"
    
    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"debug": True}
        digimon = Scastmon(config=config)
        assert digimon.config == config


class TestAnalysis:
    """Tests para funcionalidad de análisis"""
    
    def test_analyze_returns_dict(self, digimon):
        """Test que analyze() retorna diccionario"""
        result = digimon.analyze()
        assert isinstance(result, dict)
        assert "status" in result
        assert "message" in result
    
    def test_analyze_success_status(self, digimon):
        """Test que analyze() retorna status success"""
        result = digimon.analyze()
        assert result["status"] == "success"


class TestValidation:
    """Tests para validación"""
    
    def test_validate_none(self, digimon):
        """Test validación con None"""
        assert digimon.validate(None) is False
    
    def test_validate_valid_data(self, digimon):
        """Test validación con datos válidos"""
        assert digimon.validate({"key": "value"}) is True


class TestInfo:
    """Tests para información del Digimon"""
    
    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "SCASTmon"
        assert info["status"] == "Rookie"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

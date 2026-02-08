"""
Unit tests for Vertex Scan core module
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
from vertex_scan.core import VertexScan


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexScan"""
    return VertexScan()


class TestInitialization:
    """Tests para inicialización"""
    
    def test_init_default(self):
        """Test inicialización con valores por defecto"""
        modulo = VertexScan()
        assert modulo.name == "Vertex Scan"
        assert modulo.mission == "The Noblest of Men"
        assert modulo.role == "SAST Scanner"
    
    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"debug": True}
        modulo = VertexScan(config=config)
        assert modulo.config == config


class TestAnalysis:
    """Tests para funcionalidad de análisis"""
    
    def test_analyze_returns_dict(self, modulo):
        """Test que analyze() retorna diccionario"""
        result = modulo.analyze()
        assert isinstance(result, dict)
        assert "status" in result
        assert "message" in result
    
    def test_analyze_success_status(self, modulo):
        """Test que analyze() retorna status success"""
        result = modulo.analyze()
        assert result["status"] == "success"


class TestValidation:
    """Tests para validación"""
    
    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False
    
    def test_validate_valid_data(self, modulo):
        """Test validación con datos válidos"""
        assert modulo.validate({"key": "value"}) is True


class TestInfo:
    """Tests para información del módulo"""
    
    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Scan"
        assert info["status"] == "Rookie"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

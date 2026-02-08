"""
Unit tests for HelixFilter (Production)
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

from helix_filter.core import HelixFilter
from helix_filter.models import AnalysisResult, ThreatAnalysis


@pytest.fixture
def modulo():
    """Fixture para crear instancia de HelixFilter"""
    return HelixFilter()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Helix Filter"
        assert modulo.mission == "Good, Honest Snake Oil"
        assert isinstance(modulo.threat_database, dict)
        assert "evil-snake-oil.com" in modulo.threat_database

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"confidence_threshold": 0.9, "enable_reputation_check": False}
        modulo = HelixFilter(config=config)
        assert modulo.confidence_threshold == 0.9
        assert modulo.enable_reputation_check is False


class TestThreatAnalysis:
    """Tests para análisis de amenazas"""

    def test_analyze_threats(self, modulo):
        """Test análisis de amenazas"""
        iocs = ["google.com", "evil-snake-oil.com", "malware-download.net"]
        analysis = modulo.analyze_threats(iocs)
        assert isinstance(analysis, ThreatAnalysis)
        assert analysis.total_scanned == 3
        assert analysis.threats_detected >= 1

    def test_analyze_clean_iocs(self, modulo):
        """Test análisis de IOCs limpios"""
        iocs = ["google.com", "example.com"]
        analysis = modulo.analyze_threats(iocs)
        assert analysis.threats_detected == 0
        assert analysis.clean_count == 2


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_list(self, modulo):
        """Test analyze con lista de IOCs"""
        iocs = ["evil-snake-oil.com", "google.com"]
        result = modulo.analyze(iocs=iocs)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_single_ioc(self, modulo):
        """Test analyze con un IOC"""
        result = modulo.analyze(ioc="evil-snake-oil.com")
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("example.com") is True

    def test_validate_list(self, modulo):
        """Test validación con lista válida"""
        assert modulo.validate(["google.com", "yahoo.com"]) is True

    def test_validate_invalid_list(self, modulo):
        """Test validación con lista inválida"""
        assert modulo.validate(["google.com", 123]) is False


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Helix Filter"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

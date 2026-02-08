"""
Unit tests for VertexVuln (Production)
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

from vertex_vuln.core import VertexVuln
from vertex_vuln.models import AnalysisResult, ScanResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexVuln"""
    return VertexVuln()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Vertex Vuln"
        assert modulo.mission == "Paradise Mercifully Departed"
        assert modulo.role == "vuln-scanner"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"severity_threshold": "high", "scan_depth": 10}
        modulo = VertexVuln(config=config)
        assert modulo.severity_threshold == "high"
        assert modulo.scan_depth == 10


class TestScanning:
    """Tests para escaneo de vulnerabilidades"""

    def test_scan_target_with_vulns(self, modulo):
        """Test escaneo de objetivo con vulnerabilidades"""
        result = modulo.scan_target("openssl-1.0.2")
        assert isinstance(result, ScanResult)
        assert result.total_vulnerabilities > 0

    def test_scan_target_no_vulns(self, modulo):
        """Test escaneo de objetivo sin vulnerabilidades"""
        result = modulo.scan_target("unknown-component")
        assert result.total_vulnerabilities == 0


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_target(self, modulo):
        """Test analyze con un objetivo"""
        result = modulo.analyze(target="openssl-1.0.2")
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_multiple_targets(self, modulo):
        """Test analyze con múltiples objetivos"""
        result = modulo.analyze(targets=["openssl-1.0.2", "apache-2.4.41"])
        assert result.status == "success"
        assert result.data["total_targets"] == 2

    def test_analyze_no_input(self, modulo):
        """Test analyze sin input"""
        result = modulo.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("target") is True

    def test_validate_list(self, modulo):
        """Test validación con lista"""
        assert modulo.validate(["target1", "target2"]) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Vuln"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

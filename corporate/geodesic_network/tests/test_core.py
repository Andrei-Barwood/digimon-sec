"""
Unit tests for GeodesicNetwork (Production)
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

from geodesic_network.core import GeodesicNetwork
from geodesic_network.models import AnalysisResult, TrafficAnalysis


@pytest.fixture
def modulo():
    """Fixture para crear instancia de GeodesicNetwork"""
    return GeodesicNetwork()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Geodesic Network"
        assert modulo.mission == "A Kind and benevolent Despot"
        assert modulo.role == "network-monitor"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"max_connections": 500, "alert_threshold": 50}
        modulo = GeodesicNetwork(config=config)
        assert modulo.max_connections == 500
        assert modulo.alert_threshold == 50


class TestConnectionTracking:
    """Tests para rastreo de conexiones"""

    def test_add_connection(self, modulo):
        """Test añadir conexión"""
        modulo.add_connection("192.168.1.1", "10.0.0.1", source_port=12345, dest_port=80, protocol="TCP")
        assert len(modulo.connections) == 1
        assert modulo.connections[0].source_ip == "192.168.1.1"

    def test_analyze_traffic(self, modulo):
        """Test análisis de tráfico"""
        modulo.add_connection("192.168.1.1", "10.0.0.1", dest_port=80, protocol="TCP")
        modulo.add_connection("192.168.1.2", "10.0.0.2", dest_port=443, protocol="TCP")
        analysis = modulo.analyze_traffic()
        assert isinstance(analysis, TrafficAnalysis)
        assert analysis.total_connections == 2
        assert len(analysis.unique_ips) == 4


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_with_connections(self, modulo):
        """Test analyze con lista de conexiones"""
        connections = [
            {"source_ip": "192.168.1.1", "dest_ip": "10.0.0.1", "dest_port": 80, "protocol": "TCP"}
        ]
        result = modulo.analyze(connections=connections)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_without_connections(self, modulo):
        """Test analyze sin conexiones previas"""
        result = modulo.analyze()
        assert isinstance(result, AnalysisResult)
        assert result.status == "warning"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_list(self, modulo):
        """Test validación con lista"""
        assert modulo.validate([{"source_ip": "1.1.1.1", "dest_ip": "2.2.2.2"}]) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Geodesic Network"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
Unit tests for HelixIncident (Production)
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

from helix_incident.core import HelixIncident
from helix_incident.models import AnalysisResult, IncidentResponse


@pytest.fixture
def modulo():
    """Fixture para crear instancia de HelixIncident"""
    return HelixIncident()


@pytest.fixture
def modulo_auto_contain():
    """Fixture con auto_contain habilitado"""
    return HelixIncident(config={"auto_contain": True, "severity_threshold": "high"})


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Helix Incident"
        assert modulo.mission == "The Gunslinger"
        assert modulo.role == "incident-response"

    def test_init_with_config(self, modulo_auto_contain):
        """Test inicialización con configuración"""
        assert modulo_auto_contain.auto_contain is True
        assert modulo_auto_contain.severity_threshold == "high"


class TestIncidentResponse:
    """Tests para respuesta a incidentes"""

    def test_respond_to_incident(self, modulo):
        """Test respuesta a incidente"""
        response = modulo.respond_to_incident("malware", "medium", "server-01")
        assert isinstance(response, IncidentResponse)
        assert response.incident_id
        assert response.severity == "medium"

    def test_respond_to_critical_incident(self, modulo_auto_contain):
        """Test respuesta a incidente crítico con auto_contain"""
        response = modulo_auto_contain.respond_to_incident("breach", "critical", "server-01")
        assert response.contained is True
        assert len(response.actions_taken) > 0


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_incident(self, modulo):
        """Test analyze con un incidente"""
        result = modulo.analyze(incident_type="malware", severity="medium", target="server-01")
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_multiple_incidents(self, modulo):
        """Test analyze con múltiples incidentes"""
        incidents = [
            {"incident_type": "malware", "severity": "high", "target": "server-01"},
            {"incident_type": "intrusion", "severity": "medium", "target": "server-02"},
        ]
        result = modulo.analyze(incidents=incidents)
        assert result.status == "success"
        assert result.data["total_incidents"] == 2

    def test_analyze_no_input(self, modulo):
        """Test analyze sin input"""
        result = modulo.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"severity": "high", "target": "server-01"}
        assert modulo.validate(data) is True

    def test_validate_list(self, modulo):
        """Test validación con lista válida"""
        data = [{"severity": "high", "target": "server-01"}]
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Helix Incident"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

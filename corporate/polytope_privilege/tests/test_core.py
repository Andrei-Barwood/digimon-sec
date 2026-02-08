"""
Unit tests for PolytopePrivilege (Production)
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

from polytope_privilege.core import PolytopePrivilege
from polytope_privilege.models import AnalysisResult, PrivilegeAudit, PrivilegeEvent


@pytest.fixture
def modulo():
    """Fixture para crear instancia de PolytopePrivilege"""
    return PolytopePrivilege()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Polytope Privilege"
        assert modulo.mission == "Clemens Point"
        assert modulo.role == "privilege-auditor"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"require_justification": False, "max_elevation_duration": 1800}
        modulo = PolytopePrivilege(config=config)
        assert modulo.require_justification is False
        assert modulo.max_elevation_duration == 1800


class TestPrivilegeOperations:
    """Tests para operaciones de privilegios"""

    def test_request_elevation(self, modulo):
        """Test solicitar elevación"""
        event = modulo.request_elevation("user1", "admin", "Maintenance task")
        assert isinstance(event, PrivilegeEvent)
        assert event.user_id == "user1"

    def test_audit_privileges(self, modulo):
        """Test auditoría de privilegios"""
        modulo.request_elevation("user1", "admin", "Task")
        audit = modulo.audit_privileges()
        assert isinstance(audit, PrivilegeAudit)
        assert audit.total_events >= 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_audit(self, modulo):
        """Test analyze con audit action"""
        result = modulo.analyze(action="audit")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_request(self, modulo):
        """Test analyze con request action"""
        elevation_data = {"user_id": "user1", "privilege": "admin", "justification": "Task"}
        result = modulo.analyze(action="request", elevation_data=elevation_data)
        assert result.status in ["success", "warning"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"user_id": "user1", "privilege": "admin"}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Polytope Privilege"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


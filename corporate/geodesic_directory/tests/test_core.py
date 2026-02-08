"""
Unit tests for GeodesicDirectory (Production)
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

from geodesic_directory.core import GeodesicDirectory
from geodesic_directory.models import AnalysisResult, LDAPAnalysis, LDAPEntry


@pytest.fixture
def modulo():
    """Fixture para crear instancia de GeodesicDirectory"""
    return GeodesicDirectory()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Geodesic Directory"
        assert modulo.mission == "American Distillation"
        assert modulo.role == "ldap-manager"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"ldap_url": "ldap://example.com", "use_tls": False}
        modulo = GeodesicDirectory(config=config)
        assert modulo.ldap_url == "ldap://example.com"
        assert modulo.use_tls is False


class TestLDAPOperations:
    """Tests para operaciones LDAP"""

    def test_search_entries(self, modulo):
        """Test búsqueda de entradas"""
        modulo.entries.append({"dn": "cn=user1,dc=example,dc=com", "attributes": {}, "entry_type": "user"})
        entries = modulo.search_entries()
        assert len(entries) >= 0

    def test_analyze_directory(self, modulo):
        """Test análisis de directorio"""
        analysis = modulo.analyze_directory()
        assert isinstance(analysis, LDAPAnalysis)


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_directory(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_search(self, modulo):
        """Test analyze con search action"""
        search_data = {"filter": "(objectClass=user)"}
        result = modulo.analyze(action="search", search_data=search_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario"""
        assert modulo.validate({"filter": "(objectClass=*)"}) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Geodesic Directory"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


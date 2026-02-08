"""
Unit tests for LatticePermission (Production)
"""

import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

# Add src directory to Python path for local imports
# This ensures imports work both when running directly and with pytest
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import pytest

from lattice_permission.core import LatticePermission
from lattice_permission.models import AnalysisResult, PermissionCheck


@pytest.fixture
def modulo():
    """Fixture para crear instancia de LatticePermission"""
    return LatticePermission()


@pytest.fixture
def temp_file():
    """Crea un archivo temporal para testing"""
    with NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("test content")
        f.flush()
        yield f.name
    Path(f.name).unlink(missing_ok=True)


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Lattice Permission"
        assert modulo.mission == "American Distillation"
        assert modulo.role == "permission-checker"


class TestPermissionChecking:
    """Tests para verificación de permisos"""

    def test_check_permission_file(self, modulo, temp_file):
        """Test verificación de permisos de archivo"""
        result = modulo.check_permission(temp_file, "read")
        assert isinstance(result, PermissionCheck)
        assert result.resource_type == "file"

    def test_check_permission_nonexistent(self, modulo):
        """Test verificación de recurso inexistente"""
        result = modulo.check_permission("/nonexistent/file", "read")
        assert result.granted is False


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_resource(self, modulo, temp_file):
        """Test analyze con un recurso"""
        result = modulo.analyze(resource=temp_file)
        assert isinstance(result, AnalysisResult)

    def test_analyze_multiple_resources(self, modulo, temp_file):
        """Test analyze con múltiples recursos"""
        resources = [{"resource": temp_file, "permission": "read"}]
        result = modulo.analyze(resources=resources)
        assert result.status in ["success", "warning"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("/path/to/file") is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Lattice Permission"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


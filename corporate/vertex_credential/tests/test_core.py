"""
Unit tests for VertexCredential (Production)
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

from vertex_credential.core import VertexCredential
from vertex_credential.models import AnalysisResult, Credential, CredentialVault


@pytest.fixture
def modulo():
    """Fixture para crear instancia de VertexCredential"""
    return VertexCredential()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Vertex Credential"
        assert modulo.mission == "Good Intentions"
        assert modulo.role == "credential-vault"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"encryption_enabled": False, "key_rotation_days": 30}
        modulo = VertexCredential(config=config)
        assert modulo.encryption_enabled is False
        assert modulo.key_rotation_days == 30


class TestCredentialOperations:
    """Tests para operaciones con credenciales"""

    def test_store_credential(self, modulo):
        """Test almacenar credencial"""
        cred = modulo.store_credential("cred1", "user1", "service1", "password123")
        assert isinstance(cred, Credential)
        assert cred.credential_id == "cred1"

    def test_analyze_vault(self, modulo):
        """Test análisis de vault"""
        modulo.store_credential("cred1", "user1", "service1", "pass1")
        vault = modulo.analyze_vault()
        assert isinstance(vault, CredentialVault)
        assert vault.total_credentials == 1


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_vault(self, modulo):
        """Test analyze con analyze action"""
        result = modulo.analyze(action="analyze")
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_store(self, modulo):
        """Test analyze con store action"""
        cred_data = {
            "credential_id": "cred1",
            "username": "user1",
            "service": "service1",
            "password": "password123",
        }
        result = modulo.analyze(action="store", credential_data=cred_data)
        assert result.status == "success"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validación con diccionario válido"""
        data = {"credential_id": "cred1", "service": "service1", "password": "pass1"}
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Vertex Credential"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


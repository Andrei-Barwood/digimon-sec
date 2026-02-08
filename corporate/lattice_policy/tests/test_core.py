"""
Unit tests for LatticePolicy (Production)
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

from lattice_policy.core import LatticePolicy
from lattice_policy.models import AnalysisResult, PolicyCheck


@pytest.fixture
def modulo():
    """Fixture para crear instancia de LatticePolicy"""
    return LatticePolicy()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Lattice Policy"
        assert modulo.mission == "Charlotte Balfour"
        assert modulo.role == "policy-enforcer"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"strict_mode": False, "check_permissions": False}
        modulo = LatticePolicy(config=config)
        assert modulo.strict_mode is False
        assert modulo.check_permissions is False


class TestPolicyChecking:
    """Tests para verificación de políticas"""

    def test_check_password_policy_compliant(self, modulo):
        """Test verificación de política de contraseña cumplida"""
        data = {"password": "SecurePass123!"}
        result = modulo.check_policy("password_policy", data)
        assert isinstance(result, PolicyCheck)
        assert result.compliant is True

    def test_check_password_policy_violations(self, modulo):
        """Test verificación de política de contraseña con violaciones"""
        data = {"password": "weak"}
        result = modulo.check_policy("password_policy", data)
        assert result.compliant is False
        assert len(result.violations) > 0

    def test_check_encryption_policy(self, modulo):
        """Test verificación de política de encriptación"""
        data = {"key_bits": 256, "is_aead": True}
        result = modulo.check_policy("encryption_policy", data)
        assert isinstance(result, PolicyCheck)


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_single_policy(self, modulo):
        """Test analyze con una política"""
        policy_check = {"policy_name": "password_policy", "data": {"password": "SecurePass123!"}}
        result = modulo.analyze(policy_check=policy_check)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_multiple_policies(self, modulo):
        """Test analyze con múltiples políticas"""
        policy_checks = [
            {"policy_name": "password_policy", "data": {"password": "SecurePass123!"}},
            {"policy_name": "encryption_policy", "data": {"key_bits": 256, "is_aead": True}},
        ]
        result = modulo.analyze(policy_checks=policy_checks)
        assert result.status == "success"
        assert result.data["total_checks"] == 2

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
        data = {"policy_name": "test", "data": {}}
        assert modulo.validate(data) is True

    def test_validate_list(self, modulo):
        """Test validación con lista válida"""
        data = [{"policy_name": "test", "data": {}}]
        assert modulo.validate(data) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Lattice Policy"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

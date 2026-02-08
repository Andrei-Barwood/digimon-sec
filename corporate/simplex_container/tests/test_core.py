"""
Unit tests for SimplexContainer (Production)
"""

import pytest

from simplex_container.core import SimplexContainer
from simplex_container.models import AnalysisResult, AuditReport


@pytest.fixture
def modulo():
    """Fixture para crear instancia de SimplexContainer"""
    return SimplexContainer()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, modulo):
        """Test inicializacion con valores por defecto"""
        assert modulo.name == "Simplex Container"
        assert modulo.mission == "A Kind and benevolent Despot"
        assert modulo.role == "docker-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        modulo = SimplexContainer(config=config)
        assert modulo.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, modulo):
        """Test auditoria basica"""
        sample = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}
        report = modulo.audit_container(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, modulo):
        """Test analyze con datos"""
        sample = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}
        result = modulo.analyze(container_data=sample)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, modulo):
        """Test validacion con None"""
        assert modulo.validate(None) is False

    def test_validate_dict(self, modulo):
        """Test validacion con diccionario valido"""
        assert modulo.validate({"key": "value"}) is True


class TestInfo:
    """Tests para informacion del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Simplex Container"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

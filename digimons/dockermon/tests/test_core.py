"""
Unit tests for Dockermon (Mega)
"""

import pytest

from dockermon.core import Dockermon
from dockermon.models import AnalysisResult, AuditReport


@pytest.fixture
def digimon():
    """Fixture para crear instancia de Dockermon"""
    return Dockermon()


class TestInitialization:
    """Tests para inicializacion"""

    def test_init_default(self, digimon):
        """Test inicializacion con valores por defecto"""
        assert digimon.name == "Dockermon"
        assert digimon.mission == "A Kind and benevolent Despot"
        assert digimon.role == "docker-auditor"

    def test_init_with_config(self):
        """Test inicializacion con configuracion"""
        config = {"severity_threshold": "high"}
        digimon = Dockermon(config=config)
        assert digimon.severity_threshold == "high"


class TestAudit:
    """Tests para auditoria"""

    def test_audit(self, digimon):
        """Test auditoria basica"""
        sample = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}
        report = digimon.audit_container(sample)
        assert isinstance(report, AuditReport)
        assert report.total_checks > 0


class TestAnalyze:
    """Tests para funcionalidad de analisis"""

    def test_analyze(self, digimon):
        """Test analyze con datos"""
        sample = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}
        result = digimon.analyze(container_data=sample)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validacion"""

    def test_validate_none(self, digimon):
        """Test validacion con None"""
        assert digimon.validate(None) is False

    def test_validate_dict(self, digimon):
        """Test validacion con diccionario valido"""
        assert digimon.validate({"key": "value"}) is True


class TestInfo:
    """Tests para informacion del Digimon"""

    def test_get_info_returns_dict(self, digimon):
        """Test que get_info() retorna diccionario"""
        info = digimon.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Dockermon"
        assert info["status"] == "Mega"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

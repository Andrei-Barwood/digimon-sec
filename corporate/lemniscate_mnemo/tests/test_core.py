"""
Unit tests for LemniscateMnemo core module (Production)
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

from LemniscateMnemo.core import LemniscateMnemo
from LemniscateMnemo.models import AnalysisResult, BackupVerificationResult


@pytest.fixture
def modulo():
    """Fixture para crear instancia de lemniscate_mnemo"""
    
    
    return LemniscateMnemo()


def _create_temp_backup(tmp_path: Path, content: bytes = b"backup-data") -> Path:
    file_path = tmp_path / "sample.backup"
    file_path.write_bytes(content)
    return file_path


class TestInitialization:
    """Tests para inicialización"""
    
    def test_init_default(self):
        modulo = LemniscateMnemo()
        assert modulo.name == "Lemniscate Mnemo"
        assert modulo.mission == "Enter, Pursued by a Memory"
        assert modulo.role == "backup-auditor"
        assert modulo.hash_algorithm == "sha512"
    
    def test_init_with_config(self):
        config = {"hash_algorithm": "sha256", "min_retention_days": 15}
        modulo = LemniscateMnemo(config=config)
        assert modulo.hash_algorithm == "sha256"
        assert modulo.min_retention_days == 15


class TestIntegrity:
    """Tests de verificación de integridad"""

    def test_verify_integrity_success(self, modulo, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"hello-world")
        checksum = modulo.calculate_checksum(str(backup))
        result = modulo.verify_integrity(str(backup), expected_checksum=checksum)
        assert isinstance(result, BackupVerificationResult)
        assert result.integrity_verified is True
        assert result.errors == []

    def test_verify_integrity_missing_file(self, modulo):
        result = modulo.verify_integrity("/non/existent/file.bak", expected_checksum="deadbeef")
        assert result.exists is False
        assert "File does not exist" in result.errors


class TestAudit:
    """Tests de auditoría de carpeta"""

    def test_audit_directory(self, modulo, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"backup-content")
        _ = modulo.calculate_checksum(str(backup))
        audit = modulo.audit_backup_directory(str(tmp_path))
        assert audit.total_backups == 1
        assert audit.summary["total"] == 1
        assert len(audit.backup_details) == 1


class TestAnalyze:
    """Tests para analyze"""

    def test_analyze_directory(self, modulo, tmp_path: Path):
        audit = modulo.analyze(directory_path=str(tmp_path))
        assert isinstance(audit, AnalysisResult)
        assert audit.status == "success"

    def test_analyze_single_file(self, modulo, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"data")
        checksum = modulo.calculate_checksum(str(backup))
        result = modulo.analyze(backup_path=str(backup), expected_checksum=checksum)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_no_input(self, modulo):
        result = modulo.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""
    
    def test_validate_none(self, modulo):
        assert modulo.validate(None) is False
    
    def test_validate_string(self, modulo):
        assert modulo.validate("/tmp/backup") is True

    def test_validate_list(self, modulo):
        assert modulo.validate(["/tmp/a", "/tmp/b"]) is True

    def test_validate_bad_type(self, modulo):
        assert modulo.validate({"key": "value"}) is False


class TestInfo:
    """Tests para información del módulo"""
    
    def test_get_info(self, modulo):
        info = modulo.get_info()
        assert info["name"] == "Lemniscate Mnemo"
        assert info["status"] == "Production"
        assert "hash_algorithm" in info


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

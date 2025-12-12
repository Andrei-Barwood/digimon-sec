"""
Unit tests for Mnemomon core module (Mega)
"""

from pathlib import Path

import pytest

from Mnemomon.core import Mnemomon
from Mnemomon.models import AnalysisResult, BackupVerificationResult


@pytest.fixture
def digimon():
    """Fixture para crear instancia de mnemomon"""
    
    
    return Mnemomon()


def _create_temp_backup(tmp_path: Path, content: bytes = b"backup-data") -> Path:
    file_path = tmp_path / "sample.backup"
    file_path.write_bytes(content)
    return file_path


class TestInitialization:
    """Tests para inicialización"""
    
    def test_init_default(self):
        digimon = Mnemomon()
        assert digimon.name == "Mnemomon"
        assert digimon.mission == "Enter, Pursued by a Memory"
        assert digimon.role == "backup-auditor"
        assert digimon.hash_algorithm == "sha512"
    
    def test_init_with_config(self):
        config = {"hash_algorithm": "sha256", "min_retention_days": 15}
        digimon = Mnemomon(config=config)
        assert digimon.hash_algorithm == "sha256"
        assert digimon.min_retention_days == 15


class TestIntegrity:
    """Tests de verificación de integridad"""

    def test_verify_integrity_success(self, digimon, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"hello-world")
        checksum = digimon.calculate_checksum(str(backup))
        result = digimon.verify_integrity(str(backup), expected_checksum=checksum)
        assert isinstance(result, BackupVerificationResult)
        assert result.integrity_verified is True
        assert result.errors == []

    def test_verify_integrity_missing_file(self, digimon):
        result = digimon.verify_integrity("/non/existent/file.bak", expected_checksum="deadbeef")
        assert result.exists is False
        assert "File does not exist" in result.errors


class TestAudit:
    """Tests de auditoría de carpeta"""

    def test_audit_directory(self, digimon, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"backup-content")
        _ = digimon.calculate_checksum(str(backup))
        audit = digimon.audit_backup_directory(str(tmp_path))
        assert audit.total_backups == 1
        assert audit.summary["total"] == 1
        assert len(audit.backup_details) == 1


class TestAnalyze:
    """Tests para analyze"""

    def test_analyze_directory(self, digimon, tmp_path: Path):
        audit = digimon.analyze(directory_path=str(tmp_path))
        assert isinstance(audit, AnalysisResult)
        assert audit.status == "success"

    def test_analyze_single_file(self, digimon, tmp_path: Path):
        backup = _create_temp_backup(tmp_path, b"data")
        checksum = digimon.calculate_checksum(str(backup))
        result = digimon.analyze(backup_path=str(backup), expected_checksum=checksum)
        assert isinstance(result, AnalysisResult)
        assert result.status == "success"

    def test_analyze_no_input(self, digimon):
        result = digimon.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""
    
    def test_validate_none(self, digimon):
        assert digimon.validate(None) is False
    
    def test_validate_string(self, digimon):
        assert digimon.validate("/tmp/backup") is True

    def test_validate_list(self, digimon):
        assert digimon.validate(["/tmp/a", "/tmp/b"]) is True

    def test_validate_bad_type(self, digimon):
        assert digimon.validate({"key": "value"}) is False


class TestInfo:
    """Tests para información del Digimon"""
    
    def test_get_info(self, digimon):
        info = digimon.get_info()
        assert info["name"] == "Mnemomon"
        assert info["status"] == "Mega"
        assert "hash_algorithm" in info


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

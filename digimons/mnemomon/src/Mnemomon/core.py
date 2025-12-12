"""
Core functionality for Mnemomon (Mega)

This module implements backup integrity, encryption hygiene and
retention auditing aligned with 2025-2026 security best practices.
Misión: Enter, Pursued by a Memory
Rol: Backup Auditor
"""

import hashlib
import logging
import os
import stat
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .models import AnalysisResult, AuditResult, BackupVerificationResult

logger = logging.getLogger(__name__)


class Mnemomon:
    """
    Mnemomon - Cybersecurity Module (Mega)

    Descripción:
        Verifica integridad de backups, evalúa permisos y políticas de retención,
        y apoya verificaciones de cifrado con algoritmos modernos.

    Attributes:
        name: Nombre del Digimon
        mission: Misión RDR2 inspiradora
        role: Rol en ciberseguridad
        hash_algorithm: Algoritmo de hash usado para checksum (default: sha512)
        min_retention_days: Días mínimos de retención recomendados
        check_encryption: Habilita avisos si el archivo parece sin cifrar
        verify_permissions: Verifica permisos peligrosos (world-readable/writable)
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar Mnemomon con valores seguros por defecto.

        Args:
            config: Diccionario de configuración opcional:
                - hash_algorithm: sha512 (default), sha256, blake2b, blake2s
                - min_retention_days: 30 por defecto
                - check_encryption: True por defecto
                - verify_permissions: True por defecto
        """
        self.name = "Mnemomon"
        self.mission = "Enter, Pursued by a Memory"
        self.role = "backup-auditor"
        self.config = config or {}

        self.supported_algorithms = {
            "sha512": hashlib.sha512,
            "sha256": hashlib.sha256,
            "blake2b": hashlib.blake2b,
            "blake2s": hashlib.blake2s,
        }

        self.hash_algorithm = self.config.get("hash_algorithm", "sha512")
        if self.hash_algorithm not in self.supported_algorithms:
            logger.warning("Unsupported hash algorithm %s, fallback to sha512", self.hash_algorithm)
            self.hash_algorithm = "sha512"

        self.min_retention_days = int(self.config.get("min_retention_days", 30))
        self.check_encryption = bool(self.config.get("check_encryption", True))
        self.verify_permissions = bool(self.config.get("verify_permissions", True))

        logger.info(
            "Initialized %s - %s (hash=%s, retention=%sd)",
            self.name,
            self.role,
            self.hash_algorithm,
            self.min_retention_days,
        )

    # --------------------------------------------------------------------- #
    # Core capabilities
    # --------------------------------------------------------------------- #
    def _iter_files(self, directory_path: str, extensions: Iterable[str]) -> List[str]:
        files: List[str] = []
        base = Path(directory_path)
        for path in base.rglob("*"):
            if path.is_file() and (
                path.suffix.lower() in extensions or any(str(path).endswith(ext) for ext in extensions)
            ):
                files.append(str(path))
        return files

    def calculate_checksum(self, file_path: str, algorithm: Optional[str] = None) -> str:
        """
        Calcular checksum seguro leyendo en chunks para minimizar memoria.
        """
        algo = algorithm or self.hash_algorithm
        if algo not in self.supported_algorithms:
            raise ValueError(f"Unsupported hash algorithm: {algo}")

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Backup file not found: {file_path}")

        hash_obj = self.supported_algorithms[algo]()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def verify_integrity(self, file_path: str, expected_checksum: Optional[str] = None) -> BackupVerificationResult:
        """
        Verifica integridad y controles de superficie (permisos, cifrado indicativo).
        """
        result = {
            "file_path": file_path,
            "exists": False,
            "checksum": None,
            "checksum_algorithm": self.hash_algorithm,
            "integrity_verified": False,
            "file_size": 0,
            "last_modified": None,
            "errors": [],
            "warnings": [],
        }

        path = Path(file_path)
        if not path.exists():
            result["errors"].append("File does not exist")
            return BackupVerificationResult(**result)

        result["exists"] = True
        stat_info = path.stat()
        result["file_size"] = stat_info.st_size
        result["last_modified"] = datetime.fromtimestamp(stat_info.st_mtime).isoformat()

        try:
            result["checksum"] = self.calculate_checksum(file_path)
        except Exception as e:  # pragma: no cover - defensive
            logger.error("Checksum error for %s: %s", file_path, e)
            result["errors"].append(str(e))
            return BackupVerificationResult(**result)

        if expected_checksum:
            result["integrity_verified"] = (
                result["checksum"].lower() == expected_checksum.lower()
            )
            if not result["integrity_verified"]:
                result["errors"].append("Checksum mismatch: possible corruption or tampering")
        else:
            result["integrity_verified"] = True
            result["warnings"].append("No expected checksum provided; only computed value returned")

        if self.verify_permissions:
            mode = stat_info.st_mode
            if mode & stat.S_IWOTH:
                result["errors"].append("File is world-writable (security risk)")
            if mode & stat.S_IROTH:
                result["warnings"].append("File is world-readable; ensure encryption at rest")

        if self.check_encryption:
            # Heuristic: flag if file extension looks plaintext and not encrypted
            if path.suffix.lower() in {".sql", ".txt", ".log"}:
                result["warnings"].append("Backup appears plaintext; confirm encryption in storage")

        return BackupVerificationResult(**result)

    def audit_backup_directory(self, directory_path: str) -> AuditResult:
        """
        Audita un directorio de backups completo.
        """
        path = Path(directory_path)
        if not path.is_dir():
            return AuditResult(
                directory=directory_path,
                audit_timestamp=datetime.now().isoformat(),
                total_backups=0,
                verified_backups=0,
                corrupted_backups=0,
                old_backups=[],
                backup_details=[],
                summary={},
            )

        backup_extensions = {".bak", ".backup", ".tar", ".tar.gz", ".zip", ".sql", ".dump", ".db"}
        backups = self._iter_files(directory_path, backup_extensions)

        details: List[BackupVerificationResult] = []
        old_backups: List[Dict[str, Any]] = []
        verified_count = 0
        corrupted_count = 0

        for backup in backups:
            verification = self.verify_integrity(backup)
            details.append(verification)
            if verification.integrity_verified and not verification.errors:
                verified_count += 1
            else:
                corrupted_count += 1

            if verification.last_modified:
                age_days = (datetime.now() - datetime.fromisoformat(verification.last_modified)).days
                if age_days > self.min_retention_days:
                    old_backups.append(
                        {"file": backup, "age_days": age_days, "last_modified": verification.last_modified}
                    )

        total = len(backups)
        summary = {
            "total": total,
            "verified": verified_count,
            "corrupted": corrupted_count,
            "old_backups": len(old_backups),
            "verification_rate": (verified_count / total * 100) if total else 0,
        }

        return AuditResult(
            directory=directory_path,
            audit_timestamp=datetime.now().isoformat(),
            total_backups=total,
            verified_backups=verified_count,
            corrupted_backups=corrupted_count,
            old_backups=old_backups,
            backup_details=details,
            summary=summary,
        )

    def check_retention_policy(self, backup_paths: List[str]) -> Dict[str, Any]:
        """
        Verifica cumplimiento de retención mínima.
        """
        compliant: List[Dict[str, Any]] = []
        expired: List[Dict[str, Any]] = []
        non_compliant: List[Dict[str, Any]] = []
        now = datetime.now()

        for path_str in backup_paths:
            path = Path(path_str)
            if not path.exists():
                continue
            age_days = (now - datetime.fromtimestamp(path.stat().st_mtime)).days
            info = {"path": str(path), "age_days": age_days, "last_modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()}
            if age_days <= self.min_retention_days:
                compliant.append(info)
            elif age_days > self.min_retention_days * 2:
                expired.append(info)
            else:
                non_compliant.append(info)

        return {
            "policy_min_days": self.min_retention_days,
            "compliant_backups": compliant,
            "non_compliant_backups": non_compliant,
            "expired_backups": expired,
        }

    def analyze(
        self,
        backup_path: Optional[str] = None,
        directory_path: Optional[str] = None,
        expected_checksum: Optional[str] = None,
    ) -> AnalysisResult:
        """
        Ejecuta análisis principal: archivo individual o carpeta completa.
        """
        if directory_path:
            audit = self.audit_backup_directory(directory_path)
            return AnalysisResult(
                status="success",
                message=f"Audit completed for {directory_path}",
                data=audit.model_dump(),
                errors=None,
            )
        if backup_path:
            verification = self.verify_integrity(backup_path, expected_checksum)
            status = "success" if verification.integrity_verified and not verification.errors else "warning"
            return AnalysisResult(
                status=status,
                message="Backup integrity verification completed",
                data=verification.model_dump(),
                errors=verification.errors or None,
            )
        return AnalysisResult(
            status="error",
            message="No backup_path or directory_path provided",
            data={},
            errors=["missing_input"],
        )

    # --------------------------------------------------------------------- #
    # Utility
    # --------------------------------------------------------------------- #
    def validate(self, data: Any) -> bool:
        """
        Valida rutas individuales o listas de rutas.
        """
        if data is None:
            return False
        if isinstance(data, str):
            return bool(data)
        if isinstance(data, list):
            return all(isinstance(item, str) and item for item in data)
        return False

    def get_info(self) -> Dict[str, str]:
        """
        Obtener información del Digimon.
        """
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Mega",
            "hash_algorithm": self.hash_algorithm,
            "min_retention_days": str(self.min_retention_days),
        }


# Alias para retrocompatibilidad
Digimon = Mnemomon

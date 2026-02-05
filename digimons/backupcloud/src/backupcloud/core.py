"""
Core functionality for BackupCloud (Mega)

BackupCloud audita backups en cloud.
Misión: My Last Boy
Rol: Cloud Backup Auditor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class BackupCloud:
    """
    BackupCloud - Cloud Backup Auditor (Mega)

    Descripción:
        Audita backups cloud verificando retencion,
        frescura del ultimo backup y replicacion cross-region.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar BackupCloud.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - min_retention_days: Dias minimos de retencion
                - max_backup_age_hours: Maximo de horas desde el ultimo backup
                - require_cross_region: Requerir replicacion cross-region
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "BackupCloud"
        self.mission = "My Last Boy"
        self.role = "cloud-backup-auditor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.min_retention_days = int(self.config.get("min_retention_days", 7))
        self.max_backup_age_hours = int(self.config.get("max_backup_age_hours", 24))
        self.require_cross_region = bool(self.config.get("require_cross_region", True))
        self.severity_threshold = self.config.get("severity_threshold", "medium")

        logger.info("Initialized %s - %s", self.name, self.role)

    def _add_finding(
        self,
        findings: List[AuditFinding],
        finding_id: str,
        severity: str,
        title: str,
        description: str,
        resource: str,
        recommendation: str,
    ) -> None:
        findings.append(
            AuditFinding(
                finding_id=finding_id,
                severity=severity,
                title=title,
                description=description,
                resource=resource,
                recommendation=recommendation,
            )
        )

    def audit_backups(self, backup_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuracion de backups.

        Args:
            backup_data: Datos de backup a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        backup_enabled = backup_data.get("backup_enabled")
        if backup_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "backup-001",
                "high",
                "Missing backup setting",
                "No se especifica si los backups estan habilitados.",
                "backup_enabled",
                "Habilitar backups para recursos criticos.",
            )
        elif bool(backup_enabled):
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "backup-001",
                "high",
                "Backups disabled",
                "Los backups estan deshabilitados.",
                "backup_enabled",
                "Activar backups automaticos.",
            )

        retention_days = int(backup_data.get("backup_retention_days", 0))
        if retention_days < self.min_retention_days:
            failed += 1
            self._add_finding(
                findings,
                "backup-002",
                "medium",
                "Low backup retention",
                f"Retencion de backups: {retention_days} dias.",
                "backup_retention_days",
                f"Aumentar retencion a {self.min_retention_days} dias o mas.",
            )
        else:
            passed += 1

        last_backup_age = int(backup_data.get("last_backup_hours", 0))
        if last_backup_age > self.max_backup_age_hours:
            failed += 1
            self._add_finding(
                findings,
                "backup-003",
                "medium",
                "Stale backups detected",
                f"Ultimo backup hace {last_backup_age} horas.",
                "last_backup_hours",
                f"Ejecutar backups cada {self.max_backup_age_hours} horas o menos.",
            )
        else:
            passed += 1

        cross_region = backup_data.get("cross_region_replication")
        if cross_region is None:
            failed += 1
            self._add_finding(
                findings,
                "backup-004",
                "low",
                "Missing cross-region setting",
                "No se especifica replicacion cross-region.",
                "cross_region_replication",
                "Habilitar replicacion cross-region.",
            )
        elif bool(cross_region) == self.require_cross_region:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "backup-004",
                "low",
                "Cross-region replication disabled",
                "Replicacion cross-region deshabilitada.",
                "cross_region_replication",
                "Activar replicacion cross-region.",
            )

        total_checks = 4
        summary = "All checks passed" if failed == 0 else f"{failed} checks failed"
        return AuditReport(
            findings=findings,
            total_checks=total_checks,
            failed_checks=failed,
            passed_checks=passed,
            summary=summary,
            metadata={
                "severity_threshold": self.severity_threshold,
                "strict_mode": self.strict_mode,
            },
        )

    def analyze(self, backup_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de backups cloud."""
        if not backup_data:
            return AnalysisResult(
                status="error",
                message="No backup data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_backups(backup_data)
        status = "success" if report.failed_checks == 0 else "warning"
        return AnalysisResult(
            status=status,
            message=report.summary,
            data=report.model_dump(),
        )

    def validate(self, data: Any) -> bool:
        """Valida datos de entrada."""
        if data is None:
            return False
        return isinstance(data, dict) and len(data) > 0

    def get_info(self) -> Dict[str, str]:
        """Obtener informacion del Digimon."""
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Mega",
        }


# Alias para retrocompatibilidad
Digimon = BackupCloud


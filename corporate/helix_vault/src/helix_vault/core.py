"""
Core functionality for HelixVault (Production)

HelixVault audita configuraciones de bases de datos.
Misión: The Noblest of Men
Rol: Database Auditor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class HelixVault:
    """
    HelixVault - Database Auditor (Production)

    Descripción:
        Audita bases de datos cloud enfocandose en cifrado,
        backups, acceso publico y alta disponibilidad.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar HelixVault.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - min_backup_retention_days: Dias minimos de retencion
                - require_encryption: Requerir cifrado en storage
                - require_multi_az: Requerir despliegue Multi-AZ
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Helix Vault"
        self.mission = "The Noblest of Men"
        self.role = "database-auditor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.min_backup_retention_days = int(self.config.get("min_backup_retention_days", 7))
        self.require_encryption = bool(self.config.get("require_encryption", True))
        self.require_multi_az = bool(self.config.get("require_multi_az", True))
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

    def audit_database(self, db_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuracion de base de datos.

        Args:
            db_data: Datos de base de datos a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        public_access = bool(db_data.get("public_access", False))
        if public_access:
            failed += 1
            self._add_finding(
                findings,
                "rds-001",
                "high",
                "Public database detected",
                "Base de datos con acceso publico habilitado.",
                "public_access",
                "Deshabilitar acceso publico y usar redes privadas.",
            )
        else:
            passed += 1

        encryption_enabled = db_data.get("storage_encrypted")
        if encryption_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "rds-002",
                "medium",
                "Missing encryption setting",
                "No se especifica cifrado de storage.",
                "storage_encrypted",
                "Habilitar cifrado en almacenamiento.",
            )
        elif bool(encryption_enabled) == self.require_encryption:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "rds-002",
                "high",
                "Storage encryption disabled",
                "Cifrado de storage deshabilitado.",
                "storage_encrypted",
                "Activar cifrado en reposo.",
            )

        retention_days = int(db_data.get("backup_retention_days", 0))
        if retention_days < self.min_backup_retention_days:
            failed += 1
            self._add_finding(
                findings,
                "rds-003",
                "medium",
                "Low backup retention",
                f"Retencion de backups: {retention_days} dias.",
                "backup_retention_days",
                f"Aumentar retencion a {self.min_backup_retention_days} dias o mas.",
            )
        else:
            passed += 1

        multi_az = db_data.get("multi_az")
        if multi_az is None:
            failed += 1
            self._add_finding(
                findings,
                "rds-004",
                "low",
                "Missing Multi-AZ setting",
                "No se especifica configuracion Multi-AZ.",
                "multi_az",
                "Configurar Multi-AZ para alta disponibilidad.",
            )
        elif bool(multi_az) == self.require_multi_az:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "rds-004",
                "low",
                "Multi-AZ disabled",
                "Multi-AZ no esta habilitado.",
                "multi_az",
                "Habilitar Multi-AZ.",
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

    def analyze(self, db_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de bases de datos."""
        if not db_data:
            return AnalysisResult(
                status="error",
                message="No database data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_database(db_data)
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
        """Obtener informacion del módulo."""
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Production",
        }


# Alias para retrocompatibilidad
módulo = HelixVault


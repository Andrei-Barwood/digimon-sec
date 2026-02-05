"""
Core functionality for S3mon (Mega)

S3mon audita configuracion de buckets S3.
Misión: Paradise Mercifully Departed
Rol: S3 Auditor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class S3mon:
    """
    S3mon - S3 Auditor (Mega)

    Descripción:
        Audita buckets S3 enfocandose en acceso publico,
        cifrado, versionado y logging de acceso.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar S3mon.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - require_encryption: Requerir cifrado de buckets
                - require_versioning: Requerir versionado
                - require_logging: Requerir logging de acceso
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "S3mon"
        self.mission = "Paradise Mercifully Departed"
        self.role = "s3-auditor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.require_encryption = bool(self.config.get("require_encryption", True))
        self.require_versioning = bool(self.config.get("require_versioning", True))
        self.require_logging = bool(self.config.get("require_logging", True))
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

    def audit_bucket(self, bucket_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuracion de bucket S3.

        Args:
            bucket_data: Datos del bucket a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        public_access = bool(bucket_data.get("public_access", False))
        if public_access:
            failed += 1
            self._add_finding(
                findings,
                "s3-001",
                "high",
                "Public bucket detected",
                "Bucket con acceso publico habilitado.",
                "public_access",
                "Bloquear acceso publico y usar ACLs privadas.",
            )
        else:
            passed += 1

        encryption_enabled = bucket_data.get("encryption_enabled")
        if encryption_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "s3-002",
                "medium",
                "Missing encryption setting",
                "No se especifica cifrado en bucket.",
                "encryption_enabled",
                "Habilitar cifrado SSE/S3 o SSE/KMS.",
            )
        elif bool(encryption_enabled) == self.require_encryption:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "s3-002",
                "high",
                "Encryption disabled",
                "Bucket sin cifrado habilitado.",
                "encryption_enabled",
                "Activar cifrado en reposo.",
            )

        versioning_enabled = bucket_data.get("versioning_enabled")
        if versioning_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "s3-003",
                "low",
                "Missing versioning setting",
                "No se especifica versionado.",
                "versioning_enabled",
                "Habilitar versionado para recuperacion.",
            )
        elif bool(versioning_enabled) == self.require_versioning:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "s3-003",
                "low",
                "Versioning disabled",
                "Versionado deshabilitado en bucket.",
                "versioning_enabled",
                "Activar versionado.",
            )

        logging_enabled = bucket_data.get("logging_enabled")
        if logging_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "s3-004",
                "low",
                "Missing logging setting",
                "No se especifica logging de acceso.",
                "logging_enabled",
                "Habilitar logging para trazabilidad.",
            )
        elif bool(logging_enabled) == self.require_logging:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "s3-004",
                "low",
                "Access logging disabled",
                "Logging de acceso deshabilitado.",
                "logging_enabled",
                "Activar access logging.",
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

    def analyze(self, bucket_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de buckets S3."""
        if not bucket_data:
            return AnalysisResult(
                status="error",
                message="No bucket data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_bucket(bucket_data)
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
Digimon = S3mon


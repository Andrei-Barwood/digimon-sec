"""
Core functionality for GeodesicIdentity (Production)

GeodesicIdentity analiza configuraciones de IAM y politicas de acceso.
Misión: Charlotte Balfour
Rol: IAM Analyzer
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class GeodesicIdentity:
    """
    GeodesicIdentity - IAM Analyzer (Production)

    Descripción:
        Analiza configuraciones IAM buscando permisos excesivos,
        usuarios inactivos y falta de MFA en cuentas criticas.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar GeodesicIdentity.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - severity_threshold: Severidad minima a reportar
                - require_mfa: Requerir MFA en usuarios privilegiados
                - require_rotation: Requerir rotacion de llaves
                - max_inactive_users: Maximo de usuarios inactivos permitidos
        """
        self.name = "Geodesic Identity"
        self.mission = "Charlotte Balfour"
        self.role = "iam-analyzer"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.severity_threshold = self.config.get("severity_threshold", "medium")
        self.require_mfa = bool(self.config.get("require_mfa", True))
        self.require_rotation = bool(self.config.get("require_rotation", True))
        self.max_inactive_users = int(self.config.get("max_inactive_users", 0))

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

    def audit_iam(self, iam_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuracion IAM.

        Args:
            iam_data: Datos IAM a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        wildcard = bool(iam_data.get("wildcard_permissions", False))
        if wildcard:
            failed += 1
            self._add_finding(
                findings,
                "iam-001",
                "high",
                "Wildcard permissions detected",
                "Detected policies with wildcard permissions.",
                "policies",
                "Replace wildcards with least-privilege permissions.",
            )
        else:
            passed += 1

        mfa_enabled = iam_data.get("mfa_enforced")
        if mfa_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "iam-002",
                "medium",
                "Missing MFA configuration",
                "IAM data does not specify MFA enforcement.",
                "mfa_enforced",
                "Define and enforce MFA policies for privileged users.",
            )
        elif bool(mfa_enabled) == self.require_mfa:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "iam-002",
                "high",
                "MFA not enforced",
                "MFA is not enforced for privileged users.",
                "mfa_enforced",
                "Enable MFA for all privileged accounts.",
            )

        rotation_enabled = iam_data.get("rotation_enabled")
        if rotation_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "iam-003",
                "medium",
                "Missing rotation setting",
                "IAM data does not specify key rotation settings.",
                "rotation_enabled",
                "Enable access key rotation policies.",
            )
        elif bool(rotation_enabled) == self.require_rotation:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "iam-003",
                "medium",
                "Key rotation disabled",
                "Access key rotation is not enabled.",
                "rotation_enabled",
                "Enable rotation for access keys.",
            )

        inactive_users = int(iam_data.get("inactive_users", 0))
        if inactive_users > self.max_inactive_users:
            failed += 1
            self._add_finding(
                findings,
                "iam-004",
                "medium",
                "Inactive users detected",
                f"Found {inactive_users} inactive users.",
                "inactive_users",
                "Disable or remove inactive accounts.",
            )
        else:
            passed += 1

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

    def analyze(self, iam_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de IAM."""
        if not iam_data:
            return AnalysisResult(
                status="error",
                message="No IAM data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_iam(iam_data)
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
módulo = GeodesicIdentity


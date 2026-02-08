"""
Core functionality for FractalAxiom (Production)

FractalAxiom audita configuraciones cloud con controles basicos.
Misión: American Venom
Rol: Cloud Config Auditor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class FractalAxiom:
    """
    FractalAxiom - Cloud Config Auditor (Production)

    Descripción:
        Audita configuraciones cloud con foco en cifrado, logging,
        MFA y acceso publico en recursos criticos (2025-2026).
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar FractalAxiom.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - severity_threshold: Severidad minima a reportar
                - require_encryption: Requerir cifrado en reposo
                - require_logging: Requerir logging habilitado
                - require_mfa: Requerir MFA para administradores
        """
        self.name = "Fractal Axiom"
        self.mission = "American Venom"
        self.role = "cloud-config-auditor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.severity_threshold = self.config.get("severity_threshold", "medium")
        self.require_encryption = bool(self.config.get("require_encryption", True))
        self.require_logging = bool(self.config.get("require_logging", True))
        self.require_mfa = bool(self.config.get("require_mfa", True))

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

    def audit_config(self, config_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuraciones cloud clave.

        Args:
            config_data: Datos de configuracion cloud

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        checks = [
            ("encryption_enabled", self.require_encryption, "high", "Encryption disabled",
             "Enable encryption at rest for all resources."),
            ("logging_enabled", self.require_logging, "medium", "Logging disabled",
             "Enable audit logging and centralize logs."),
            ("mfa_enabled", self.require_mfa, "high", "MFA not enforced",
             "Require MFA for privileged accounts."),
            ("public_access", False, "high", "Public access detected",
             "Disable public exposure for sensitive resources."),
        ]

        for idx, (key, expected, severity, title, recommendation) in enumerate(checks, start=1):
            actual = config_data.get(key)
            if actual is None:
                failed += 1
                self._add_finding(
                    findings,
                    f"cloudsec-{idx:03d}",
                    "medium",
                    f"Missing setting: {key}",
                    f"Required setting '{key}' is missing.",
                    key,
                    "Define the setting explicitly in cloud configuration.",
                )
            elif bool(actual) == bool(expected):
                passed += 1
            else:
                failed += 1
                self._add_finding(
                    findings,
                    f"cloudsec-{idx:03d}",
                    severity,
                    title,
                    f"Expected {key}={expected} but got {actual}.",
                    key,
                    recommendation,
                )

        summary = "All checks passed" if failed == 0 else f"{failed} checks failed"
        return AuditReport(
            findings=findings,
            total_checks=len(checks),
            failed_checks=failed,
            passed_checks=passed,
            summary=summary,
            metadata={
                "severity_threshold": self.severity_threshold,
                "strict_mode": self.strict_mode,
            },
        )

    def analyze(self, config_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """
        Ejecuta el analisis principal de configuracion cloud.
        """
        if not config_data:
            return AnalysisResult(
                status="error",
                message="No config data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_config(config_data)
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
módulo = FractalAxiom


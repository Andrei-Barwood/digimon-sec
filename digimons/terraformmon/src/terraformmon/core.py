"""
Core functionality for Terraformmon (Mega)

Terraformmon valida configuraciones de Infrastructure as Code.
Misión: Red Dead Redemption
Rol: IaC Validator
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class Terraformmon:
    """
    Terraformmon - IaC Validator (Mega)

    Descripción:
        Valida codigo IaC detectando secretos hardcodeados,
        estado remoto sin cifrar y versiones sin pinning.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar Terraformmon.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - require_remote_state_encrypted: Requerir cifrado del state
                - require_plan_approval: Requerir aprobacion de plan
                - require_modules_pinned: Requerir versiones fijadas
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Terraformmon"
        self.mission = "Red Dead Redemption"
        self.role = "iac-validator"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.require_remote_state_encrypted = bool(
            self.config.get("require_remote_state_encrypted", True)
        )
        self.require_plan_approval = bool(self.config.get("require_plan_approval", True))
        self.require_modules_pinned = bool(self.config.get("require_modules_pinned", True))
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

    def validate_iac(self, iac_data: Dict[str, Any]) -> AuditReport:
        """
        Valida configuracion IaC.

        Args:
            iac_data: Datos IaC a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        hardcoded_secrets = bool(iac_data.get("contains_hardcoded_secrets", False))
        if hardcoded_secrets:
            failed += 1
            self._add_finding(
                findings,
                "iac-001",
                "high",
                "Hardcoded secrets detected",
                "Se detectaron secretos hardcodeados en IaC.",
                "contains_hardcoded_secrets",
                "Mover secretos a un vault o variables seguras.",
            )
        else:
            passed += 1

        remote_state_encrypted = iac_data.get("remote_state_encrypted")
        if remote_state_encrypted is None:
            failed += 1
            self._add_finding(
                findings,
                "iac-002",
                "medium",
                "Missing remote state encryption",
                "No se especifica cifrado del state remoto.",
                "remote_state_encrypted",
                "Habilitar cifrado en backend de state.",
            )
        elif bool(remote_state_encrypted) == self.require_remote_state_encrypted:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "iac-002",
                "medium",
                "Remote state not encrypted",
                "State remoto sin cifrado habilitado.",
                "remote_state_encrypted",
                "Activar cifrado en el backend.",
            )

        plan_approved = iac_data.get("plan_approved")
        if plan_approved is None:
            failed += 1
            self._add_finding(
                findings,
                "iac-003",
                "low",
                "Missing plan approval",
                "No se especifica aprobacion del plan.",
                "plan_approved",
                "Requerir aprobacion de plan antes del apply.",
            )
        elif bool(plan_approved) == self.require_plan_approval:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "iac-003",
                "low",
                "Plan not approved",
                "Plan de Terraform no aprobado.",
                "plan_approved",
                "Habilitar gates de aprobacion.",
            )

        modules_pinned = iac_data.get("modules_pinned")
        if modules_pinned is None:
            failed += 1
            self._add_finding(
                findings,
                "iac-004",
                "low",
                "Missing module pinning",
                "No se especifica pinning de modulos.",
                "modules_pinned",
                "Fijar versiones de modulos.",
            )
        elif bool(modules_pinned) == self.require_modules_pinned:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "iac-004",
                "low",
                "Modules not pinned",
                "Modulos sin version fija.",
                "modules_pinned",
                "Usar versiones exactas para modulos.",
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

    def analyze(self, iac_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de IaC."""
        if not iac_data:
            return AnalysisResult(
                status="error",
                message="No IaC data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.validate_iac(iac_data)
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
Digimon = Terraformmon


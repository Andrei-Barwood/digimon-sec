"""
Core functionality for ComplianceCloud (Mega)

ComplianceCloud audita cumplimiento en entornos cloud.
Misión: Good Intentions
Rol: Cloud Compliance
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class ComplianceCloud:
    """
    ComplianceCloud - Cloud Compliance (Mega)

    Descripción:
        Audita cumplimiento en cloud evaluando controles,
        evidencia y monitoreo continuo.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar ComplianceCloud.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - min_passed_controls: Controles minimos aprobados
                - require_evidence: Requerir evidencia de cumplimiento
                - require_continuous_monitoring: Requerir monitoreo continuo
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "ComplianceCloud"
        self.mission = "Good Intentions"
        self.role = "cloud-compliance"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.min_passed_controls = int(self.config.get("min_passed_controls", 1))
        self.require_evidence = bool(self.config.get("require_evidence", True))
        self.require_continuous_monitoring = bool(
            self.config.get("require_continuous_monitoring", True)
        )
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

    def audit_compliance(self, compliance_data: Dict[str, Any]) -> AuditReport:
        """
        Audita controles de cumplimiento en cloud.

        Args:
            compliance_data: Datos de cumplimiento

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        passed_controls = int(compliance_data.get("passed_controls", 0))
        if passed_controls < self.min_passed_controls:
            failed += 1
            self._add_finding(
                findings,
                "comp-001",
                "medium",
                "Insufficient passed controls",
                f"Controles aprobados: {passed_controls}.",
                "passed_controls",
                f"Incrementar controles aprobados a {self.min_passed_controls} o mas.",
            )
        else:
            passed += 1

        evidence_collected = compliance_data.get("evidence_collected")
        if evidence_collected is None:
            failed += 1
            self._add_finding(
                findings,
                "comp-002",
                "medium",
                "Missing evidence setting",
                "No se especifica recoleccion de evidencia.",
                "evidence_collected",
                "Recolectar evidencia de cumplimiento.",
            )
        elif bool(evidence_collected) == self.require_evidence:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "comp-002",
                "medium",
                "Evidence not collected",
                "No se recolecta evidencia de cumplimiento.",
                "evidence_collected",
                "Habilitar recoleccion de evidencia.",
            )

        continuous_monitoring = compliance_data.get("continuous_monitoring")
        if continuous_monitoring is None:
            failed += 1
            self._add_finding(
                findings,
                "comp-003",
                "low",
                "Missing continuous monitoring setting",
                "No se especifica monitoreo continuo.",
                "continuous_monitoring",
                "Activar monitoreo continuo de controles.",
            )
        elif bool(continuous_monitoring) == self.require_continuous_monitoring:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "comp-003",
                "low",
                "Continuous monitoring disabled",
                "Monitoreo continuo deshabilitado.",
                "continuous_monitoring",
                "Habilitar monitoreo continuo.",
            )

        frameworks = compliance_data.get("frameworks_checked", [])
        if not frameworks:
            failed += 1
            self._add_finding(
                findings,
                "comp-004",
                "low",
                "No frameworks evaluated",
                "No se reportan frameworks evaluados.",
                "frameworks_checked",
                "Definir frameworks de cumplimiento (ISO, SOC2, etc).",
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

    def analyze(self, compliance_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de cumplimiento cloud."""
        if not compliance_data:
            return AnalysisResult(
                status="error",
                message="No compliance data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_compliance(compliance_data)
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
Digimon = ComplianceCloud


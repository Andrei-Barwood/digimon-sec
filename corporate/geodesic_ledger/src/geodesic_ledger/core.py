"""
Core functionality for GeodesicLedger (Production)

GeodesicLedger optimiza costos de seguridad en cloud.
Misión: The Gilded Cage
Rol: Cost Optimizer
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class GeodesicLedger:
    """
    GeodesicLedger - Cost Optimizer (Production)

    Descripción:
        Analiza costos cloud para detectar anomalías,
        recursos ociosos y ausencia de guardrails.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar GeodesicLedger.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - max_idle_resources: Maximo de recursos ociosos
                - max_cost_anomalies: Maximo de anomalías permitidas
                - require_budget_guardrails: Requerir guardrails de presupuesto
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Geodesic Ledger"
        self.mission = "The Gilded Cage"
        self.role = "cost-optimizer"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.max_idle_resources = int(self.config.get("max_idle_resources", 0))
        self.max_cost_anomalies = int(self.config.get("max_cost_anomalies", 0))
        self.require_budget_guardrails = bool(
            self.config.get("require_budget_guardrails", True)
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

    def audit_costs(self, cost_data: Dict[str, Any]) -> AuditReport:
        """
        Audita costos de seguridad en cloud.

        Args:
            cost_data: Datos de costos a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        anomalies = int(cost_data.get("cost_anomalies", 0))
        if anomalies > self.max_cost_anomalies:
            failed += 1
            self._add_finding(
                findings,
                "cost-001",
                "medium",
                "Cost anomalies detected",
                f"Anomalias de costos: {anomalies}.",
                "cost_anomalies",
                "Investigar picos y aplicar alertas.",
            )
        else:
            passed += 1

        idle_resources = int(cost_data.get("idle_resources", 0))
        if idle_resources > self.max_idle_resources:
            failed += 1
            self._add_finding(
                findings,
                "cost-002",
                "medium",
                "Idle resources detected",
                f"Recursos ociosos: {idle_resources}.",
                "idle_resources",
                "Eliminar o reducir recursos ociosos.",
            )
        else:
            passed += 1

        guardrails = cost_data.get("budget_guardrails")
        if guardrails is None:
            failed += 1
            self._add_finding(
                findings,
                "cost-003",
                "low",
                "Missing budget guardrails",
                "No se especifican guardrails de presupuesto.",
                "budget_guardrails",
                "Definir limites de presupuesto y alertas.",
            )
        elif bool(guardrails) == self.require_budget_guardrails:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "cost-003",
                "low",
                "Budget guardrails disabled",
                "Guardrails de presupuesto deshabilitados.",
                "budget_guardrails",
                "Habilitar guardrails y alertas de costo.",
            )

        total_checks = 3
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

    def analyze(self, cost_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de costos."""
        if not cost_data:
            return AnalysisResult(
                status="error",
                message="No cost data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_costs(cost_data)
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
módulo = GeodesicLedger


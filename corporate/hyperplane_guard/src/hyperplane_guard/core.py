"""
Core functionality for HyperplaneGuard (Production)

HyperplaneGuard gestiona y audita reglas de firewall.
Misión: Good, Honest Snake Oil
Rol: Firewall Manager
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class HyperplaneGuard:
    """
    HyperplaneGuard - Firewall Manager (Production)

    Descripción:
        Gestiona reglas de firewall y detecta aperturas riesgosas,
        verificando politicas de deny-by-default y logging.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar HyperplaneGuard.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - allowed_ports: Lista de puertos permitidos
                - require_logging: Requerir logging de firewall
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Hyperplane Guard"
        self.mission = "Good, Honest Snake Oil"
        self.role = "firewall-manager"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.allowed_ports = list(self.config.get("allowed_ports", [80, 443]))
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

    def audit_rules(self, rules_data: Dict[str, Any]) -> AuditReport:
        """
        Audita reglas de firewall.

        Args:
            rules_data: Datos de reglas de firewall

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        default_deny = rules_data.get("default_deny")
        if default_deny is None:
            failed += 1
            self._add_finding(
                findings,
                "fw-001",
                "medium",
                "Missing default deny",
                "No se especifica la politica deny-by-default.",
                "default_deny",
                "Habilitar deny-by-default para trafico entrante.",
            )
        elif bool(default_deny):
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "fw-001",
                "high",
                "Default deny disabled",
                "La politica deny-by-default esta deshabilitada.",
                "default_deny",
                "Activar deny-by-default para reforzar seguridad.",
            )

        open_ports = rules_data.get("open_ports", [])
        risky_ports = [port for port in open_ports if port not in self.allowed_ports]
        if risky_ports:
            failed += 1
            self._add_finding(
                findings,
                "fw-002",
                "high",
                "Unexpected open ports",
                f"Puertos abiertos no permitidos: {sorted(risky_ports)}.",
                "open_ports",
                "Cerrar puertos no autorizados o actualizar allowlist.",
            )
        else:
            passed += 1

        logging_enabled = rules_data.get("logging_enabled")
        if logging_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "fw-003",
                "medium",
                "Missing logging setting",
                "No se especifica logging de firewall.",
                "logging_enabled",
                "Habilitar logging para auditoria de reglas.",
            )
        elif bool(logging_enabled) == self.require_logging:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "fw-003",
                "medium",
                "Firewall logging disabled",
                "Logging de firewall esta deshabilitado.",
                "logging_enabled",
                "Activar logging de firewall.",
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
                "allowed_ports": self.allowed_ports,
                "severity_threshold": self.severity_threshold,
                "strict_mode": self.strict_mode,
            },
        )

    def analyze(self, rules_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de firewall."""
        if not rules_data:
            return AnalysisResult(
                status="error",
                message="No firewall rules provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_rules(rules_data)
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
módulo = HyperplaneGuard


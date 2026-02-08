"""
Core functionality for VertexStillness (Production)

VertexStillness monitorea configuraciones de redes privadas.
Misión: Outlaws from the West
Rol: VPC Monitor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class VertexStillness:
    """
    VertexStillness - VPC Monitor (Production)

    Descripción:
        Monitorea configuraciones VPC con foco en flow logs,
        segmentacion y exposicion publica de subredes.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar VertexStillness.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - require_flow_logs: Requerir flow logs habilitados
                - require_nat_gateway: Requerir NAT gateway para subredes privadas
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Vertex Stillness"
        self.mission = "Outlaws from the West"
        self.role = "vpc-monitor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.require_flow_logs = bool(self.config.get("require_flow_logs", True))
        self.require_nat_gateway = bool(self.config.get("require_nat_gateway", True))
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

    def audit_vpc(self, vpc_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuraciones de red privada.

        Args:
            vpc_data: Datos de VPC a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        flow_logs_enabled = vpc_data.get("flow_logs_enabled")
        if flow_logs_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "vpc-001",
                "medium",
                "Missing flow logs setting",
                "No se especifica si los flow logs estan habilitados.",
                "flow_logs_enabled",
                "Habilitar flow logs para auditoria.",
            )
        elif bool(flow_logs_enabled) == self.require_flow_logs:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "vpc-001",
                "medium",
                "Flow logs disabled",
                "Flow logs no estan habilitados.",
                "flow_logs_enabled",
                "Habilitar flow logs en la VPC.",
            )

        public_subnets = bool(vpc_data.get("public_subnets", False))
        if public_subnets:
            failed += 1
            self._add_finding(
                findings,
                "vpc-002",
                "high",
                "Public subnets detected",
                "Se detectaron subredes publicas expuestas.",
                "public_subnets",
                "Minimizar subredes publicas y aislar servicios.",
            )
        else:
            passed += 1

        nacl_restrictive = vpc_data.get("network_acl_restrictive")
        if nacl_restrictive is None:
            failed += 1
            self._add_finding(
                findings,
                "vpc-003",
                "medium",
                "Missing ACL posture",
                "No se reporta la postura de NACL.",
                "network_acl_restrictive",
                "Definir NACL restrictivas para trafico externo.",
            )
        elif bool(nacl_restrictive):
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "vpc-003",
                "medium",
                "Open NACLs detected",
                "Las NACL permiten trafico amplio.",
                "network_acl_restrictive",
                "Restringir reglas NACL a lo necesario.",
            )

        nat_configured = vpc_data.get("nat_gateway_configured")
        if nat_configured is None:
            failed += 1
            self._add_finding(
                findings,
                "vpc-004",
                "low",
                "Missing NAT gateway setting",
                "No se especifica configuracion de NAT gateway.",
                "nat_gateway_configured",
                "Configurar NAT gateway para subredes privadas.",
            )
        elif bool(nat_configured) == self.require_nat_gateway:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "vpc-004",
                "low",
                "NAT gateway missing",
                "No se detecta NAT gateway para subredes privadas.",
                "nat_gateway_configured",
                "Agregar NAT gateway o ruta segura.",
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

    def analyze(self, vpc_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de red privada."""
        if not vpc_data:
            return AnalysisResult(
                status="error",
                message="No VPC data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_vpc(vpc_data)
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
módulo = VertexStillness


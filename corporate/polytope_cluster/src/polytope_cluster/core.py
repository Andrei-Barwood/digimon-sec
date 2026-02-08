"""
Core functionality for PolytopeCluster (Production)

PolytopeCluster escanea configuraciones de clusters Kubernetes.
Misión: Fleeting Joy
Rol: K8s Scanner
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class PolytopeCluster:
    """
    PolytopeCluster - K8s Scanner (Production)

    Descripción:
        Escanea clusters Kubernetes buscando configuraciones inseguras
        en RBAC, politica de pods, cifrado de etcd y API publica.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar PolytopeCluster.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - require_rbac: Requerir RBAC habilitado
                - require_psp: Requerir pod security policies
                - require_etcd_encryption: Requerir cifrado en etcd
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Polytope Cluster"
        self.mission = "Fleeting Joy"
        self.role = "k8s-scanner"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.require_rbac = bool(self.config.get("require_rbac", True))
        self.require_psp = bool(self.config.get("require_psp", True))
        self.require_etcd_encryption = bool(self.config.get("require_etcd_encryption", True))
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

    def scan_cluster(self, cluster_data: Dict[str, Any]) -> AuditReport:
        """
        Escanea configuracion de cluster Kubernetes.

        Args:
            cluster_data: Datos del cluster a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        rbac_enabled = cluster_data.get("rbac_enabled")
        if rbac_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "k8s-001",
                "medium",
                "Missing RBAC setting",
                "No se especifica si RBAC esta habilitado.",
                "rbac_enabled",
                "Habilitar RBAC para control de acceso.",
            )
        elif bool(rbac_enabled) == self.require_rbac:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "k8s-001",
                "high",
                "RBAC disabled",
                "RBAC no esta habilitado.",
                "rbac_enabled",
                "Activar RBAC para restringir privilegios.",
            )

        psp_enabled = cluster_data.get("pod_security_policies")
        if psp_enabled is None:
            failed += 1
            self._add_finding(
                findings,
                "k8s-002",
                "medium",
                "Missing pod security policies",
                "No se especifican pod security policies.",
                "pod_security_policies",
                "Definir y aplicar pod security policies.",
            )
        elif bool(psp_enabled) == self.require_psp:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "k8s-002",
                "medium",
                "Pod security policies disabled",
                "Las politicas de pods estan deshabilitadas.",
                "pod_security_policies",
                "Habilitar y reforzar pod security policies.",
            )

        etcd_encryption = cluster_data.get("etcd_encryption")
        if etcd_encryption is None:
            failed += 1
            self._add_finding(
                findings,
                "k8s-003",
                "medium",
                "Missing etcd encryption setting",
                "No se especifica cifrado de etcd.",
                "etcd_encryption",
                "Habilitar cifrado de secretos en etcd.",
            )
        elif bool(etcd_encryption) == self.require_etcd_encryption:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "k8s-003",
                "high",
                "etcd encryption disabled",
                "Cifrado de etcd deshabilitado.",
                "etcd_encryption",
                "Activar cifrado para datos sensibles.",
            )

        public_api = bool(cluster_data.get("public_api", False))
        if public_api:
            failed += 1
            self._add_finding(
                findings,
                "k8s-004",
                "high",
                "Public API exposed",
                "El API server esta expuesto publicamente.",
                "public_api",
                "Restringir acceso al API server.",
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

    def analyze(self, cluster_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de cluster Kubernetes."""
        if not cluster_data:
            return AnalysisResult(
                status="error",
                message="No cluster data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.scan_cluster(cluster_data)
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
módulo = PolytopeCluster


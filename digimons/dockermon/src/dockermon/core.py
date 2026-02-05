"""
Core functionality for Dockermon (Mega)

Dockermon audita configuraciones de contenedores Docker.
Misión: A Kind and benevolent Despot
Rol: Docker Auditor
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class Dockermon:
    """
    Dockermon - Docker Auditor (Mega)

    Descripción:
        Audita contenedores Docker detectando ejecucion como root,
        modo privilegiado y configuracion insegura del filesystem.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar Dockermon.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - require_signed_images: Requerir imagenes firmadas
                - require_read_only_fs: Requerir filesystem read-only
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Dockermon"
        self.mission = "A Kind and benevolent Despot"
        self.role = "docker-auditor"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.require_signed_images = bool(self.config.get("require_signed_images", True))
        self.require_read_only_fs = bool(self.config.get("require_read_only_fs", True))
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

    def audit_container(self, container_data: Dict[str, Any]) -> AuditReport:
        """
        Audita configuracion de contenedor Docker.

        Args:
            container_data: Datos del contenedor a evaluar

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        run_as_root = bool(container_data.get("run_as_root", False))
        if run_as_root:
            failed += 1
            self._add_finding(
                findings,
                "docker-001",
                "high",
                "Container running as root",
                "El contenedor se ejecuta como root.",
                "run_as_root",
                "Usar un usuario no root en el contenedor.",
            )
        else:
            passed += 1

        privileged = bool(container_data.get("privileged", False))
        if privileged:
            failed += 1
            self._add_finding(
                findings,
                "docker-002",
                "high",
                "Privileged container",
                "El contenedor esta en modo privilegiado.",
                "privileged",
                "Deshabilitar modo privilegiado salvo necesidad.",
            )
        else:
            passed += 1

        read_only_fs = container_data.get("read_only_fs")
        if read_only_fs is None:
            failed += 1
            self._add_finding(
                findings,
                "docker-003",
                "medium",
                "Missing filesystem setting",
                "No se especifica read-only filesystem.",
                "read_only_fs",
                "Configurar filesystem como read-only.",
            )
        elif bool(read_only_fs) == self.require_read_only_fs:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "docker-003",
                "medium",
                "Filesystem not read-only",
                "El filesystem no esta en modo read-only.",
                "read_only_fs",
                "Activar read-only filesystem.",
            )

        signed_images = container_data.get("signed_images")
        if signed_images is None:
            failed += 1
            self._add_finding(
                findings,
                "docker-004",
                "low",
                "Missing image signing setting",
                "No se especifica si las imagenes estan firmadas.",
                "signed_images",
                "Habilitar verificacion de firmas en imagenes.",
            )
        elif bool(signed_images) == self.require_signed_images:
            passed += 1
        else:
            failed += 1
            self._add_finding(
                findings,
                "docker-004",
                "low",
                "Unsigned images",
                "Se detectan imagenes no firmadas.",
                "signed_images",
                "Usar firmas de imagen y validacion en el registry.",
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

    def analyze(self, container_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de contenedores."""
        if not container_data:
            return AnalysisResult(
                status="error",
                message="No container data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_container(container_data)
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
Digimon = Dockermon


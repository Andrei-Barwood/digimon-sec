"""
Core functionality for Resourcemon (Mega)

Resourcemon limita y audita uso de recursos.
Misión: American Distillation
Rol: Resource Limiter
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, AuditFinding, AuditReport

logger = logging.getLogger(__name__)


class Resourcemon:
    """
    Resourcemon - Resource Limiter (Mega)

    Descripción:
        Analiza uso de CPU, memoria y storage para detectar
        excesos y aplicar limites de recursos.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar Resourcemon.

        Args:
            config: Diccionario de configuracion opcional:
                - strict_mode: Si True, falla cuando faltan settings criticos
                - max_cpu_percent: Maximo de CPU permitido
                - max_memory_percent: Maximo de memoria permitida
                - max_storage_percent: Maximo de storage permitido
                - severity_threshold: Severidad minima a reportar
        """
        self.name = "Resourcemon"
        self.mission = "American Distillation"
        self.role = "resource-limiter"
        self.config = config or {}

        self.strict_mode = bool(self.config.get("strict_mode", True))
        self.max_cpu_percent = int(self.config.get("max_cpu_percent", 80))
        self.max_memory_percent = int(self.config.get("max_memory_percent", 80))
        self.max_storage_percent = int(self.config.get("max_storage_percent", 85))
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

    def audit_usage(self, usage_data: Dict[str, Any]) -> AuditReport:
        """
        Audita uso de recursos.

        Args:
            usage_data: Datos de uso de recursos

        Returns:
            AuditReport con hallazgos
        """
        findings: List[AuditFinding] = []
        passed = 0
        failed = 0

        cpu_usage = int(usage_data.get("cpu_usage", 0))
        if cpu_usage > self.max_cpu_percent:
            failed += 1
            self._add_finding(
                findings,
                "res-001",
                "medium",
                "High CPU usage",
                f"CPU usage {cpu_usage}% exceeds limit.",
                "cpu_usage",
                f"Reducir consumo o aumentar limite ({self.max_cpu_percent}%).",
            )
        else:
            passed += 1

        memory_usage = int(usage_data.get("memory_usage", 0))
        if memory_usage > self.max_memory_percent:
            failed += 1
            self._add_finding(
                findings,
                "res-002",
                "medium",
                "High memory usage",
                f"Memory usage {memory_usage}% exceeds limit.",
                "memory_usage",
                f"Reducir consumo o aumentar limite ({self.max_memory_percent}%).",
            )
        else:
            passed += 1

        storage_usage = int(usage_data.get("storage_usage", 0))
        if storage_usage > self.max_storage_percent:
            failed += 1
            self._add_finding(
                findings,
                "res-003",
                "low",
                "High storage usage",
                f"Storage usage {storage_usage}% exceeds limit.",
                "storage_usage",
                f"Reducir uso o ampliar storage ({self.max_storage_percent}%).",
            )
        else:
            passed += 1

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

    def analyze(self, usage_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        """Ejecuta el analisis principal de recursos."""
        if not usage_data:
            return AnalysisResult(
                status="error",
                message="No usage data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.audit_usage(usage_data)
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
Digimon = Resourcemon


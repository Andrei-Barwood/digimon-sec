"""
Core functionality for PolytopeMetrics (Production)

PolytopeMetrics - KPI Tracker
Misión: Charlotte Balfour
Rol: kpi-tracker
"""

import logging
from typing import Any, Dict, List, Optional

from .models import AnalysisResult, DetectionFinding, DetectionReport

logger = logging.getLogger(__name__)


class PolytopeMetrics:
    """
    PolytopeMetrics - KPI Tracker (Production)

    Descripción:
        Rastrea KPIs de seguridad para medir madurez, riesgo y rendimiento del SOC.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.name = "Polytope Metrics"
        self.mission = "Charlotte Balfour"
        self.role = "kpi-tracker"
        self.config = config or {}

        self.severity_threshold = self.config.get("severity_threshold", "medium")
        self.confidence_threshold = float(self.config.get("confidence_threshold", 0.7))
        self.enable_enrichment = bool(self.config.get("enable_enrichment", True))

        self._severity_rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        self._severity_threshold_rank = self._severity_rank.get(self.severity_threshold.lower(), 2)
        self._risk_signals = {
            "critical": ["critical", "violation", "breach", "tamper", "missing"],
            "high": ["suspicious", "drift", "failed", "delay", "risk"],
            "medium": ["overlap", "coverage", "backlog", "queue", "duplicate"],
        }

        logger.info(
            "Initialized %s - %s (threshold=%s, confidence=%.2f)",
            self.name,
            self.role,
            self.severity_threshold,
            self.confidence_threshold,
        )

    def _normalize_signal(self, value: Any) -> float:
        if isinstance(value, bool):
            return 1.0 if value else 0.0
        if isinstance(value, (int, float)):
            if value <= 1.0:
                return float(value)
            return min(float(value) / 100.0, 1.0)
        if isinstance(value, str):
            return 1.0 if value.lower() in ("true", "yes", "high", "critical") else 0.3
        return 0.0

    def track_security_kpis(self, metrics_data: Dict[str, Any]) -> DetectionReport:
        findings: List[DetectionFinding] = []

        for key, value in metrics_data.items():
            score = self._normalize_signal(value)
            key_l = key.lower()
            if score < self.confidence_threshold:
                continue

            severity = "low"
            if any(token in key_l for token in self._risk_signals["critical"]):
                severity = "critical"
            elif any(token in key_l for token in self._risk_signals["high"]):
                severity = "high"
            elif any(token in key_l for token in self._risk_signals["medium"]):
                severity = "medium"

            if self._severity_rank[severity] > self._severity_threshold_rank:
                continue

            findings.append(
                DetectionFinding(
                    indicator=key,
                    category=self.role,
                    severity=severity,
                    confidence=round(score, 2),
                    recommendation="Escalar al responsable de seguridad y aplicar playbook definido"
                    if severity in ("critical", "high")
                    else "Monitorear y revisar tendencia en siguiente ciclo operativo",
                )
            )

        return DetectionReport(
            total_checks=len(metrics_data),
            alerts_count=len(findings),
            findings=findings,
            summary={
                "engine": self.name,
                "role": self.role,
                "severity_threshold": self.severity_threshold,
                "confidence_threshold": self.confidence_threshold,
                "enrichment_enabled": self.enable_enrichment,
            },
        )

    def analyze(self, metrics_data: Optional[Dict[str, Any]] = None) -> AnalysisResult:
        if not metrics_data:
            return AnalysisResult(
                status="error",
                message="No input data provided",
                data={},
                errors=["missing_input"],
            )

        report = self.track_security_kpis(metrics_data)
        status = "warning" if report.alerts_count > 0 else "success"
        return AnalysisResult(
            status=status,
            message=f"Analysis completed: {report.alerts_count} alerts generated",
            data=report.model_dump(),
        )

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and len(data) > 0

    def get_info(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Production",
            "severity_threshold": self.severity_threshold,
            "confidence_threshold": str(self.confidence_threshold),
        }


módulo = PolytopeMetrics

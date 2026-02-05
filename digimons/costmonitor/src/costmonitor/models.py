"""
Data models for costmonitor (Mega).

Define Pydantic models for type validation and documentation.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class DigimonConfig(BaseModel):
    """Configuration model for costmonitor"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(default="costmonitor", description="Digimon name")
    strict_mode: bool = Field(default=True, description="Fail on missing critical settings")
    max_idle_resources: int = Field(default=0, description="Max idle resources allowed")
    max_cost_anomalies: int = Field(default=0, description="Max cost anomalies allowed")
    require_budget_guardrails: bool = Field(default=True, description="Require budget guardrails")
    severity_threshold: str = Field(default="medium", description="Minimum severity to report")
    debug: bool = Field(default=False, description="Enable debug mode")


class AuditFinding(BaseModel):
    """Finding detected during audit"""

    finding_id: str = Field(description="Unique finding identifier")
    severity: str = Field(description="Severity level")
    title: str = Field(description="Short title")
    description: str = Field(description="Detailed description")
    resource: str = Field(description="Resource or setting name")
    recommendation: str = Field(description="Recommended fix")


class AuditReport(BaseModel):
    """Audit report with findings and summary"""

    findings: List[AuditFinding] = Field(default_factory=list, description="List of findings")
    total_checks: int = Field(description="Total checks executed")
    failed_checks: int = Field(description="Checks that failed")
    passed_checks: int = Field(description="Checks that passed")
    summary: str = Field(description="Short summary of audit")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class AnalysisResult(BaseModel):
    """Result model for analysis operations"""

    status: str = Field(description="Status of the analysis")
    message: str = Field(description="Descriptive message")
    data: Dict[str, Any] = Field(default_factory=dict, description="Result data")
    errors: Optional[List[str]] = Field(default=None, description="List of errors if any")


class DigimonInfo(BaseModel):
    """Information model for Digimon metadata"""

    name: str
    mission: str
    role: str
    status: str
    version: str = "3.0.0"


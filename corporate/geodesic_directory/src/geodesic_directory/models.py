"""
Data models for geodesic_directory (Production).

Define Pydantic models for type validation and documentation.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ModuleConfig(BaseModel):
    """Configuration model for geodesic_directory"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(default="Geodesic Directory", description="Module name")
    ldap_url: Optional[str] = Field(default=None, description="LDAP server URL")
    base_dn: Optional[str] = Field(default=None, description="Base DN for searches")
    use_tls: bool = Field(default=True, description="Use TLS for connections")
    timeout: int = Field(default=30, ge=1, description="Connection timeout in seconds")
    debug: bool = Field(default=False, description="Enable debug mode")


class LDAPEntry(BaseModel):
    """LDAP directory entry"""

    dn: str = Field(description="Distinguished Name")
    attributes: Dict[str, List[str]] = Field(default_factory=dict, description="Entry attributes")
    entry_type: str = Field(description="Entry type (user/group/organizationalUnit)")


class LDAPAnalysis(BaseModel):
    """Result of LDAP analysis"""

    total_entries: int = Field(description="Total LDAP entries")
    entries_by_type: Dict[str, int] = Field(default_factory=dict, description="Entries by type")
    connection_status: str = Field(description="LDAP connection status")
    violations: List[str] = Field(default_factory=list, description="Security violations")
    analysis_summary: Dict[str, Any] = Field(default_factory=dict, description="Analysis summary")


class AnalysisResult(BaseModel):
    """Result model for analysis operations"""

    status: str = Field(description="Status of the analysis")
    message: str = Field(description="Descriptive message")
    data: Dict[str, Any] = Field(default_factory=dict, description="Result data")
    errors: Optional[List[str]] = Field(default=None, description="List of errors if any")


class ModuleInfo(BaseModel):
    """Information model for módulo metadata"""

    name: str
    mission: str
    role: str
    status: str
    use_tls: str
    timeout: str
    version: str = "3.0.0"


"""
Data models for lattice_permission (Production).

Define Pydantic models for type validation and documentation.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ModuleConfig(BaseModel):
    """Configuration model for lattice_permission"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(default="Lattice Permission", description="Module name")
    check_file_permissions: bool = Field(default=True, description="Check file permissions")
    check_directory_permissions: bool = Field(default=True, description="Check directory permissions")
    enforce_least_privilege: bool = Field(default=True, description="Enforce least privilege principle")
    debug: bool = Field(default=False, description="Enable debug mode")


class PermissionCheck(BaseModel):
    """Result of permission check"""

    resource: str = Field(description="Resource being checked")
    resource_type: str = Field(description="Type of resource (file/directory/endpoint)")
    required_permission: str = Field(description="Required permission (read/write/execute)")
    granted: bool = Field(description="Whether permission is granted")
    current_permissions: Optional[str] = Field(default=None, description="Current permissions (octal)")
    violations: List[str] = Field(default_factory=list, description="Permission violations")


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
    enforce_least_privilege: str
    version: str = "3.0.0"


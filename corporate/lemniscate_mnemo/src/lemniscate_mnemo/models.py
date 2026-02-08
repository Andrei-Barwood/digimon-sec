"""
Data models for LemniscateMnemo

Define Pydantic models for type validation and documentation.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class ModuleConfig(BaseModel):
    """Configuration model for LemniscateMnemo"""
    
    model_config = ConfigDict(frozen=True)

    name: str = Field(default="Lemniscate Mnemo", description="Module name")
    hash_algorithm: str = Field(default="sha512", description="Hash algorithm for integrity checks")
    min_retention_days: int = Field(default=30, ge=1, description="Minimum retention period in days")
    check_encryption: bool = Field(default=True, description="Check if backups look encrypted")
    verify_permissions: bool = Field(default=True, description="Verify file permissions for hygiene")
    debug: bool = Field(default=False, description="Enable debug mode")
    timeout: int = Field(default=30, ge=1, description="Request timeout in seconds")


class BackupVerificationResult(BaseModel):
    """Result model for backup verification operations"""

    file_path: str = Field(description="Path to the backup file")
    exists: bool = Field(description="Whether the file exists")
    checksum: Optional[str] = Field(default=None, description="Calculated checksum")
    checksum_algorithm: str = Field(description="Algorithm used for checksum")
    integrity_verified: bool = Field(description="Whether integrity check passed")
    file_size: int = Field(default=0, description="File size in bytes")
    last_modified: Optional[str] = Field(default=None, description="Last modification timestamp")
    errors: List[str] = Field(default_factory=list, description="List of errors if any")
    warnings: Optional[List[str]] = Field(default=None, description="List of warnings if any")


class AuditResult(BaseModel):
    """Result model for directory audit operations"""

    directory: str = Field(description="Directory path audited")
    audit_timestamp: str = Field(description="Timestamp of the audit")
    total_backups: int = Field(description="Total number of backups found")
    verified_backups: int = Field(description="Number of verified backups")
    corrupted_backups: int = Field(description="Number of corrupted backups")
    old_backups: List[Dict[str, Any]] = Field(default_factory=list, description="Backups exceeding retention")
    backup_details: List[BackupVerificationResult] = Field(default_factory=list, description="Detailed results")
    summary: Dict[str, Any] = Field(default_factory=dict, description="Summary statistics")


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
    hash_algorithm: str
    min_retention_days: str
    supported_algorithms: str
    version: str = "3.0.0"

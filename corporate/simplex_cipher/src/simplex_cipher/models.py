"""
Data models for simplex_cipher.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ModuleConfig(BaseModel):
    """Configuration model for simplex_cipher."""

    model_config = ConfigDict(frozen=True)

    name: str = Field(default="Simplex Cipher", description="Module name")
    default_cipher: str = Field(default="AES-256-GCM", description="Default cipher policy")
    min_key_bits: int = Field(default=256, ge=128, description="Minimum key size in bits")
    allow_legacy: bool = Field(default=False, description="Allow legacy/weak ciphers")
    require_aead: bool = Field(default=True, description="Require AEAD modes")
    debug: bool = Field(default=False, description="Enable debug mode")


class PolicyCheck(BaseModel):
    """Result of a crypto policy evaluation."""

    cipher: str = Field(description="Cipher name under evaluation")
    key_bits: int = Field(description="Key length in bits")
    aead: bool = Field(description="Whether cipher/mode is AEAD")
    compliant: bool = Field(description="Whether policy passes")
    warnings: List[str] = Field(default_factory=list)
    errors: List[str] = Field(default_factory=list)


class EncryptionResult(BaseModel):
    """Result of encrypt/decrypt helper."""

    status: str = Field(description="Status of operation")
    message: str = Field(description="Human friendly message")
    data: Dict[str, Any] = Field(default_factory=dict)
    errors: Optional[List[str]] = Field(default=None)


class AnalysisResult(BaseModel):
    """High-level analysis output."""

    status: str
    message: str
    data: Dict[str, Any] = Field(default_factory=dict)
    errors: Optional[List[str]] = Field(default=None)


class ModuleInfo(BaseModel):
    """Information model for módulo metadata."""

    name: str
    mission: str
    role: str
    status: str
    default_cipher: str
    min_key_bits: str
    version: str = "3.0.0"

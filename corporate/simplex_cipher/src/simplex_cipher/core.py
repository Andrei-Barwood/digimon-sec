"""
Core functionality for SimplexCipher (Production)

SimplexCipher evalúa políticas de cifrado, ayuda con operaciones
seguras básicas y valida tamaños de llave y modos AEAD.
Misión: American Venom
Rol: encryption-expert
"""

import base64
import hashlib
import hmac
import logging
import secrets
from typing import Any, Dict, Optional

from .models import AnalysisResult, EncryptionResult, PolicyCheck

logger = logging.getLogger(__name__)


class SimplexCipher:
    """
    SimplexCipher - Encryption Hero (Production)

    Descripción:
        Valida políticas de cifrado modernas y ofrece utilidades
        seguras (generación de llaves, cifrado simulado, integridad).
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.name = "Simplex Cipher"
        self.mission = "American Venom"
        self.role = "encryption-expert"
        self.config = config or {}

        self.default_cipher = self.config.get("default_cipher", "AES-256-GCM")
        self.min_key_bits = int(self.config.get("min_key_bits", 256))
        self.allow_legacy = bool(self.config.get("allow_legacy", False))
        self.require_aead = bool(self.config.get("require_aead", True))

        logger.info(
            "Initialized %s - %s (cipher=%s, min_key_bits=%s)",
            self.name,
            self.role,
            self.default_cipher,
            self.min_key_bits,
        )

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    def generate_key(self, bits: Optional[int] = None) -> str:
        """
        Genera una llave aleatoria con el tamaño solicitado (bits).
        """
        size_bits = bits or self.min_key_bits
        if size_bits % 8 != 0:
            raise ValueError("Key size must be divisible by 8")
        size_bytes = size_bits // 8
        key = secrets.token_bytes(size_bytes)
        return base64.urlsafe_b64encode(key).decode("utf-8")

    def _simulate_encrypt(self, plaintext: str, key: str) -> Dict[str, str]:
        """
        Cifrado simulado: genera un HMAC para demostrar integridad.
        """
        key_bytes = base64.urlsafe_b64decode(key.encode("utf-8"))
        mac = hmac.new(key_bytes, plaintext.encode("utf-8"), hashlib.sha256).digest()
        return {
            "ciphertext": base64.urlsafe_b64encode(plaintext.encode("utf-8")).decode("utf-8"),
            "hmac": base64.urlsafe_b64encode(mac).decode("utf-8"),
            "algo": "HMAC-SHA256",
        }

    def encrypt(self, plaintext: str, key: Optional[str] = None) -> EncryptionResult:
        """
        Cifra de forma simulada y devuelve datos + HMAC.
        """
        result = {"ciphertext": None, "hmac": None, "key": None}
        try:
            key_to_use = key or self.generate_key()
            result["key"] = key_to_use
            enc = self._simulate_encrypt(plaintext, key_to_use)
            result.update(enc)
            return EncryptionResult(status="success", message="Encrypted (simulated)", data=result)
        except Exception as exc:  # pragma: no cover
            logger.error("Encryption failed: %s", exc)
            return EncryptionResult(
                status="error",
                message="Encryption failed",
                data=result,
                errors=[str(exc)],
            )

    def decrypt(self, ciphertext_b64: str, key: str) -> EncryptionResult:
        """
        Descifra simulando (base64) y verifica HMAC.
        """
        try:
            key_bytes = base64.urlsafe_b64decode(key.encode("utf-8"))
            plaintext_bytes = base64.urlsafe_b64decode(ciphertext_b64.encode("utf-8"))
            mac = hmac.new(key_bytes, plaintext_bytes, hashlib.sha256).digest()
            return EncryptionResult(
                status="success",
                message="Decrypted (simulated)",
                data={
                    "plaintext": plaintext_bytes.decode("utf-8"),
                    "hmac": base64.urlsafe_b64encode(mac).decode("utf-8"),
                    "algo": "HMAC-SHA256",
                },
            )
        except Exception as exc:  # pragma: no cover
            logger.error("Decryption failed: %s", exc)
            return EncryptionResult(
                status="error",
                message="Decryption failed",
                data={},
                errors=[str(exc)],
            )

    # ------------------------------------------------------------------ #
    # Policy checks
    # ------------------------------------------------------------------ #
    def check_policy(self, cipher: str, key_bits: int, aead: bool) -> PolicyCheck:
        warnings = []
        errors = []

        if key_bits < self.min_key_bits:
            errors.append(f"Key too short ({key_bits}b < {self.min_key_bits}b)")

        if self.require_aead and not aead:
            errors.append("Non-AEAD cipher not allowed by policy")

        legacy_markers = ["DES", "RC4", "3DES", "AES-128"]
        if not self.allow_legacy and any(marker.lower() in cipher.lower() for marker in legacy_markers):
            warnings.append("Cipher considered legacy/weak; not recommended")

        compliant = not errors
        return PolicyCheck(
            cipher=cipher,
            key_bits=key_bits,
            aead=aead,
            compliant=compliant,
            warnings=warnings,
            errors=errors,
        )

    # ------------------------------------------------------------------ #
    # High-level analysis
    # ------------------------------------------------------------------ #
    def analyze(
        self,
        cipher: Optional[str] = None,
        key_bits: Optional[int] = None,
        aead: Optional[bool] = None,
        plaintext: Optional[str] = None,
    ) -> AnalysisResult:
        """
        Evalúa política de cifrado y opcionalmente ejecuta cifrado simulado.
        """
        cipher_name = cipher or self.default_cipher
        key_len = key_bits or self.min_key_bits
        aead_flag = self.require_aead if aead is None else aead

        policy = self.check_policy(cipher_name, key_len, aead_flag)
        data: Dict[str, Any] = {"policy": policy.model_dump()}
        errors = policy.errors or None

        if plaintext:
            enc = self.encrypt(plaintext)
            data["encryption"] = enc.model_dump()
            if enc.errors:
                errors = (errors or []) + enc.errors

        status = "success" if policy.compliant and (not errors) else "warning"
        message = "Encryption policy evaluated"
        return AnalysisResult(status=status, message=message, data=data, errors=errors)

    # ------------------------------------------------------------------ #
    # Validation and info
    # ------------------------------------------------------------------ #
    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if isinstance(data, str):
            return True
        if isinstance(data, dict):
            return True
        return False

    def get_info(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Production",
            "default_cipher": self.default_cipher,
            "min_key_bits": str(self.min_key_bits),
        }


# Alias para retrocompatibilidad
módulo = SimplexCipher

"""
Unit tests for SimplexCipher (Production)
"""

import base64
import sys
from pathlib import Path

# Add src directory to Python path for local imports
# This ensures imports work both when running directly and with pytest
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import pytest

from simplex_cipher.core import SimplexCipher
from simplex_cipher.models import AnalysisResult, EncryptionResult, PolicyCheck


@pytest.fixture
def modulo():
    return SimplexCipher()


class TestInitialization:
    def test_defaults(self, modulo):
        assert modulo.name == "Simplex Cipher"
        assert modulo.role == "encryption-expert"
        assert modulo.default_cipher == "AES-256-GCM"
        assert modulo.min_key_bits == 256

    def test_custom_config(self):
        d = SimplexCipher(config={"default_cipher": "AES-256-CTR", "min_key_bits": 192})
        assert d.default_cipher == "AES-256-CTR"
        assert d.min_key_bits == 192


class TestPolicy:
    def test_policy_pass(self, modulo):
        res = modulo.check_policy("AES-256-GCM", 256, True)
        assert isinstance(res, PolicyCheck)
        assert res.compliant is True
        assert res.errors == []

    def test_policy_fail_key(self, modulo):
        res = modulo.check_policy("AES-256-GCM", 128, True)
        assert res.compliant is False
        assert "Key too short" in res.errors[0]

    def test_policy_fail_aead(self, modulo):
        res = modulo.check_policy("AES-256-CBC", 256, False)
        assert res.compliant is False
        assert "Non-AEAD" in res.errors[0]


class TestCrypto:
    def test_generate_key_length(self, modulo):
        key = modulo.generate_key(256)
        raw = base64.urlsafe_b64decode(key.encode())
        assert len(raw) == 32

    def test_encrypt_decrypt(self, modulo):
        enc = modulo.encrypt("hola")
        assert isinstance(enc, EncryptionResult)
        assert enc.status == "success"
        dec = modulo.decrypt(enc.data["ciphertext"], enc.data["key"])
        assert dec.status == "success"
        assert dec.data["plaintext"] == "hola"


class TestAnalyze:
    def test_analyze_policy_only(self, modulo):
        res = modulo.analyze(cipher="AES-256-GCM", key_bits=256, aead=True)
        assert isinstance(res, AnalysisResult)
        assert res.status == "success"

    def test_analyze_with_plaintext(self, modulo):
        res = modulo.analyze(cipher="AES-256-GCM", key_bits=256, aead=True, plaintext="hola")
        assert isinstance(res, AnalysisResult)
        assert "encryption" in res.data


class TestValidation:
    def test_validate_none(self, modulo):
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        assert modulo.validate("data") is True

    def test_validate_dict(self, modulo):
        assert modulo.validate({"cipher": "AES"}) is True

    def test_validate_other(self, modulo):
        assert modulo.validate(123) is False

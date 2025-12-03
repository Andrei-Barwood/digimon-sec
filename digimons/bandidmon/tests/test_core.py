"""
Unit tests for Bandidmon core module
"""

import pytest
from bandidmon.core import Bandidmon

@pytest.fixture
def digimon():
    return Bandidmon()

class TestAnalysis:
    """Tests para la protección de datos"""
    
    def test_redact_email(self, digimon):
        """Prueba que los emails sean censurados"""
        unsafe_text = "Contactame en kirtantegsingh@whatsapp.com para mas info."
        result = digimon.analyze(unsafe_text)
        
        safe_text = result["data"]["safe_text"]
        
        assert "kirtan@example.com" not in safe_text
        assert "[REDACTED:EMAIL]" in safe_text
        assert result["data"]["details"]["email"] == 1

    def test_redact_credit_card(self, digimon):
        """Prueba que las tarjetas de crédito sean censuradas"""
        unsafe_text = "Mi tarjeta es 1234-5678-9012-3456, no la robes."
        result = digimon.analyze(unsafe_text)
        
        safe_text = result["data"]["safe_text"]
        
        assert "1234-5678-9012-3456" not in safe_text
        assert "[REDACTED:CREDIT_CARD]" in safe_text

    def test_no_secrets(self, digimon):
        """Texto sin secretos no debe cambiar"""
        clean_text = "Hola mundo, todo seguro aqui."
        result = digimon.analyze(clean_text)
        
        assert result["data"]["safe_text"] == clean_text
        assert result["data"]["redacted_count"] == 0

class TestValidation:
    def test_validate_string(self, digimon):
        assert digimon.validate("Texto valido") is True
        assert digimon.validate(123) is False

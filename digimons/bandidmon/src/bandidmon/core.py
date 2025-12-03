"""
Core functionality for Bandidmon

This module contains the main logic and class definitions for Bandidmon.
Misión: Outlaws from the West
Rol: data-protector
"""

import logging
import re
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class Bandidmon:
    """
    Bandidmon - Cybersecurity Module
    
    Descripción:
        Protege datos sensibles redactando información personal (PII)
    
    Attributes:
        name: Nombre del Digimon
        mission: Misión RDR2 inspiradora
        role: Rol en ciberseguridad
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializar Bandidmon
        """
        self.name = "Bandidmon"
        self.mission = "Outlaws from the West"
        self.role = "data-protector"
        self.config = config or {}
        
        # Patrones Regex para detectar datos sensibles
        self.patterns = {
            # Detecta emails simples
            "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            # Detecta posibles tarjetas de crédito (simplificado: grupos de 4 dígitos)
            "credit_card": r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        }
        
        logger.info(f"Initialized {self.name} - {self.role}")
    
    def analyze(self, text_data: str) -> Dict[str, Any]:
        """
        Analiza un texto y redacta (oculta) la información sensible encontrada.
        
        Args:
            text_data: El texto a proteger (string)
            
        Returns:
            Diccionario con el texto seguro y estadísticas de lo redactado.
        """
        logger.debug(f"Running analysis in {self.name}")
        
        if not text_data:
            return {"status": "success", "data": {"safe_text": "", "redacted_count": 0}}

        safe_text = text_data
        redacted_count = 0
        findings = {}

        # Aplicar cada filtro
        for key, pattern in self.patterns.items():
            # Contar coincidencias
            matches = re.findall(pattern, safe_text)
            count = len(matches)
            
            if count > 0:
                findings[key] = count
                redacted_count += count
                # Reemplazar por [REDACTED:TIPO]
                safe_text = re.sub(pattern, f"[REDACTED:{key.upper()}]", safe_text)
        
        result = {
            "status": "success",
            "message": f"Data protection complete. Redacted {redacted_count} items.",
            "data": {
                "original_length": len(text_data),
                "safe_text": safe_text,
                "redacted_count": redacted_count,
                "details": findings
            }
        }
        
        return result
    
    def validate(self, data: Any) -> bool:
        """
        Validar datos de entrada. Bandidmon espera un string de texto.
        """
        if not isinstance(data, str):
            logger.error("Input data must be a string")
            return False
        return True
    
    def get_info(self) -> Dict[str, str]:
        """Obtener información del Digimon"""
        return {
            "name": self.name,
            "mission": self.mission,
            "role": self.role,
            "status": "Rookie",
            "filters": ", ".join(self.patterns.keys())
        }

# Alias para retrocompatibilidad
Digimon = Bandidmon

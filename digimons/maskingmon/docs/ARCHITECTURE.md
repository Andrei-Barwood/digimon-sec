# Arquitectura - maskingmon

## Visión General

maskingmon es un módulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Misión**: Good, Honest Snake Oil
- **Rol de Seguridad**: data-masker
- **Nivel**: Mega (v3.0.0)
- **Versión**: 3.0.0

## Propósito

Enmascara datos sensibles en logs preservando formato y contexto,
con soporte para múltiples tipos de PII (2025-2026).

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `Maskingmon` es el punto de entrada principal. Implementa la lógica de negocio y orquesta las operaciones de seguridad.

**Responsabilidades:**
- `mask_text()`: Enmascara PII de un texto
- `analyze()`: Ejecuta análisis: enmascarar texto(s)
- `validate()`: Valida datos de entrada
- `get_info()`: Obtener información del Digimon


### 2. Models (`models.py`)

Define la estructura de datos utilizando **Pydantic v2**, asegurando validación estricta y serialización segura.

**Modelos Principales:**
- `DigimonConfig`: Configuration model for maskingmon
- `MaskingRecord`: Record of a masking operation
- `MaskingResult`: Result of masking operation
- `AnalysisResult`: Result model for analysis operations
- `DigimonInfo`: Information model for Digimon metadata


### 3. Utils (`utils.py`)

Proporciona utilidades auxiliares como configuración de logging y helpers comunes.

## Configuración y Personalización

El digimon se configura mediante un diccionario inmutable (`frozen=True` en Pydantic) pasado al inicializador.

```python
config = {
    "mask_character": "*",  # Configura mask_character
    "pii_types": ["email", "phone", "credit_card", "ssn", "ip"],  # Configura pii_types
}
```

## Flujo de Trabajo Típico

1. **Inicialización**: Se carga la configuración y se validan las dependencias.
2. **Validación**: `validate()` verifica que los inputs cumplan los requisitos mínimos.
3. **Ejecución**: `analyze()` (u otros métodos específicos) procesa los datos aplicando la lógica de seguridad.
4. **Resultado**: Se retorna un objeto `AnalysisResult` estandarizado con estado, mensaje y datos.

## Estándares de Seguridad (2025-2026)

- **Validación de Tipos**: Uso extensivo de Type Hints y Pydantic.
- **Manejo de Errores Seguro**: Los errores se capturan y retornan estructurados, evitando crash no controlados.
- **Configuración Inmutable**: Previene modificaciones accidentales en tiempo de ejecución.

## Extensibilidad

Para agregar nuevas funcionalidades:
1. Definir nuevos modelos en `models.py`.
2. Implementar la lógica en `core.py`.
3. Agregar pruebas unitarias en `tests/test_core.py`.

---

Ver también: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

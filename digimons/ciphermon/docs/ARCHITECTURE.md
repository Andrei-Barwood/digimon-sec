# Arquitectura - ciphermon

## Visión General

ciphermon es un módulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Misión**: American Venom
- **Rol de Seguridad**: encryption-expert
- **Nivel**: Mega (v3.0.0)
- **Versión**: 3.0.0

## Propósito

Valida políticas de cifrado modernas y ofrece utilidades
seguras (generación de llaves, cifrado simulado, integridad).

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `Ciphermon` es el punto de entrada principal. Implementa la lógica de negocio y orquesta las operaciones de seguridad.

**Responsabilidades:**
- `generate_key()`: Genera una llave aleatoria con el tamaño solicitado (bits)
- `encrypt()`: Cifra de forma simulada y devuelve datos + HMAC
- `decrypt()`: Descifra simulando (base64) y verifica HMAC
- `check_policy()`: Sin documentación
- `analyze()`: Evalúa política de cifrado y opcionalmente ejecuta cifrado simulado
- `validate()`: Sin documentación
- `get_info()`: Sin documentación


### 2. Models (`models.py`)

Define la estructura de datos utilizando **Pydantic v2**, asegurando validación estricta y serialización segura.

**Modelos Principales:**
- `DigimonConfig`: Configuration model for ciphermon
- `PolicyCheck`: Result of a crypto policy evaluation
- `EncryptionResult`: Result of encrypt/decrypt helper
- `AnalysisResult`: High-level analysis output
- `DigimonInfo`: Information model for Digimon metadata


### 3. Utils (`utils.py`)

Proporciona utilidades auxiliares como configuración de logging y helpers comunes.

## Configuración y Personalización

El digimon se configura mediante un diccionario inmutable (`frozen=True` en Pydantic) pasado al inicializador.

```python
config = {
    "default_cipher": "AES-256-GCM",  # Configura default_cipher
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

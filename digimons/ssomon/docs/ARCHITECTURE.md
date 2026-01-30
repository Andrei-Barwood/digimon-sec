# Arquitectura - ssomon

## Visión General

ssomon es un módulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Misión**: Goodbye, Dear Friend
- **Rol de Seguridad**: sso-manager
- **Nivel**: Mega (v3.0.0)
- **Versión**: 3.0.0

## Propósito

Implementa Single Sign-On con soporte SAML y OpenID Connect,
gestión de sesiones y análisis de seguridad (2025-2026).

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `SSOmon` es el punto de entrada principal. Implementa la lógica de negocio y orquesta las operaciones de seguridad.

**Responsabilidades:**
- `create_sso_session()`: Crea una sesión SSO
- `analyze_sso()`: Analiza las sesiones SSO activas
- `analyze()`: Ejecuta análisis: analizar SSO o crear sesión
- `validate()`: Valida datos de entrada
- `get_info()`: Obtener información del Digimon


### 2. Models (`models.py`)

Define la estructura de datos utilizando **Pydantic v2**, asegurando validación estricta y serialización segura.

**Modelos Principales:**
- `DigimonConfig`: Configuration model for ssomon
- `SSOSession`: SSO session information
- `SSOAnalysis`: Result of SSO analysis
- `AnalysisResult`: Result model for analysis operations
- `DigimonInfo`: Information model for Digimon metadata


### 3. Utils (`utils.py`)

Proporciona utilidades auxiliares como configuración de logging y helpers comunes.

## Configuración y Personalización

El digimon se configura mediante un diccionario inmutable (`frozen=True` en Pydantic) pasado al inicializador.

```python
config = {
    # "opcion": "valor",  # Configuración específica
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

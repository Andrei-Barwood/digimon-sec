# Arquitectura - hyperplane_guard

## Vision General

hyperplane_guard es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Good, Honest Snake Oil
- **Rol de Seguridad**: Firewall Manager
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Gestiona y audita reglas de firewall para detectar aperturas riesgosas
y asegurar logging de seguridad.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `HyperplaneGuard` es el punto de entrada principal.

**Responsabilidades:**
- `audit_rules()`: Ejecuta checks de reglas
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)


# Arquitectura - lemniscate_horizon

## Vision General

lemniscate_horizon es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Good Intentions
- **Rol de Seguridad**: Cloud Compliance
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Audita cumplimiento en cloud con controles basicos.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `LemniscateHorizon` es el punto de entrada principal.

**Responsabilidades:**
- `audit_compliance()`: Ejecuta checks principales
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

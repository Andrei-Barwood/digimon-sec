# Arquitectura - torus_vault

## Vision General

torus_vault es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Paradise Mercifully Departed
- **Rol de Seguridad**: S3 Auditor
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Audita buckets S3 para detectar acceso publico, falta de cifrado,
versionado y logging de acceso.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `TorusVault` es el punto de entrada principal.

**Responsabilidades:**
- `audit_bucket()`: Ejecuta checks de buckets
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)


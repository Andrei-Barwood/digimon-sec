# Arquitectura - geodesic_identity

## Vision General

geodesic_identity es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Charlotte Balfour
- **Rol de Seguridad**: IAM Analyzer
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Analiza configuraciones IAM para detectar permisos excesivos,
usuarios inactivos y falta de MFA.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `GeodesicIdentity` es el punto de entrada principal.

**Responsabilidades:**
- `audit_iam()`: Ejecuta checks principales de IAM
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)


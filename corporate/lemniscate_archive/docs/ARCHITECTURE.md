# Arquitectura - lemniscate_archive

## Vision General

lemniscate_archive es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: My Last Boy
- **Rol de Seguridad**: Cloud Backup Auditor
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Audita backups en cloud con controles basicos.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `LemniscateArchive` es el punto de entrada principal.

**Responsabilidades:**
- `audit_backups()`: Ejecuta checks principales
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

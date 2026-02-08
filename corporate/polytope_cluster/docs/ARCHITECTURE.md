# Arquitectura - polytope_cluster

## Vision General

polytope_cluster es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Fleeting Joy
- **Rol de Seguridad**: K8s Scanner
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Escanea clusters Kubernetes con controles de seguridad.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `PolytopeCluster` es el punto de entrada principal.

**Responsabilidades:**
- `scan_cluster()`: Ejecuta checks principales
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

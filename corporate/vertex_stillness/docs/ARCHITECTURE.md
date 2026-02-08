# Arquitectura - vertex_stillness

## Vision General

vertex_stillness es un modulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Mision**: Outlaws from the West
- **Rol de Seguridad**: VPC Monitor
- **Nivel**: Production (v3.0.0)
- **Version**: 3.0.0

## Proposito

Monitorea configuraciones de redes privadas para detectar
exposicion publica y ausencia de logs.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `VertexStillness` es el punto de entrada principal.

**Responsabilidades:**
- `audit_vpc()`: Ejecuta checks de red privada
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del módulo

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)


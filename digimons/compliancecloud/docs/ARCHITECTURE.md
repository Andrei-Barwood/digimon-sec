# Arquitectura - compliancecloud

## Vision General

compliancecloud es un modulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Mision**: Good Intentions
- **Rol de Seguridad**: Cloud Compliance
- **Nivel**: Mega (v3.0.0)
- **Version**: 3.0.0

## Proposito

Audita cumplimiento en cloud con controles basicos.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `ComplianceCloud` es el punto de entrada principal.

**Responsabilidades:**
- `audit_compliance()`: Ejecuta checks principales
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del Digimon

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

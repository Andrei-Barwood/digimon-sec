# Arquitectura - terraformmon

## Vision General

terraformmon es un modulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Mision**: Red Dead Redemption
- **Rol de Seguridad**: IaC Validator
- **Nivel**: Mega (v3.0.0)
- **Version**: 3.0.0

## Proposito

Valida Infrastructure as Code con controles basicos.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `Terraformmon` es el punto de entrada principal.

**Responsabilidades:**
- `validate_iac()`: Ejecuta checks principales
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del Digimon

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)

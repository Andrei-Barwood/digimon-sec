# Arquitectura - iammon

## Vision General

iammon es un modulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

- **Mision**: Charlotte Balfour
- **Rol de Seguridad**: IAM Analyzer
- **Nivel**: Mega (v3.0.0)
- **Version**: 3.0.0

## Proposito

Analiza configuraciones IAM para detectar permisos excesivos,
usuarios inactivos y falta de MFA.

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `IAMmon` es el punto de entrada principal.

**Responsabilidades:**
- `audit_iam()`: Ejecuta checks principales de IAM
- `analyze()`: Orquesta la auditoria y retorna `AnalysisResult`
- `validate()`: Valida inputs
- `get_info()`: Retorna metadata del Digimon

### 2. Models (`models.py`)

Define estructuras Pydantic para resultados y hallazgos.

---

Ver tambien: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)


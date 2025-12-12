# Arquitectura - Mnemomon (Mega)

## Visión General

Mnemomon es un módulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

**Misión**: Enter, Pursued by a Memory  
**Rol de Seguridad**: backup-auditor

## Componentes Principales

### 1. Core Module (`core.py`)

Contiene la clase principal `UMnemomon` con lógica Mega:

- `calculate_checksum()` - Hash seguro por chunks (SHA-512 por defecto)
- `verify_integrity()` - Checksum + permisos + alertas de cifrado
- `audit_backup_directory()` - Auditoría recursiva y estadísticas
- `check_retention_policy()` - Cumplimiento de retención mínima
- `analyze()` - Orquestación (archivo único o carpeta)

### 2. Models (`models.py`)

Define tipos y esquemas usando Pydantic:
- `DigimonConfig` - Configuración (hash, retención, cifrado, permisos)
- `BackupVerificationResult` - Resultado de verificación puntual
- `AuditResult` - Resultado de auditoría de carpeta
- `AnalysisResult` - Resumen de ejecución
- `DigimonInfo` - Metadata del Digimon

### 3. Utils (`utils.py`)

- `setup_logging()` - Configurar logging
- `format_result()` - Formatear resultados
- `validate_input()` - Validar tipos
- `format_file_size()` - Mostrar tamaños legibles

---

Ver también: [README.md](../README.md), [USAGE.md](USAGE.md)

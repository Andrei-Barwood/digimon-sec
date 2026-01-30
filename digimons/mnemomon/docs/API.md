# API Reference - mnemomon

## Class: Mnemomon

### Constructor

```python
Mnemomon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `hash_algorithm`: Configura hash_algorithm (Default: `"sha512"`)

### Métodos Principales

#### `calculate_checksum(file_path, algorithm)`

Calcular checksum seguro leyendo en chunks para minimizar memoria.

#### `verify_integrity(file_path, expected_checksum)`

Verifica integridad y controles de superficie (permisos, cifrado indicativo).

#### `audit_backup_directory(directory_path)`

Audita un directorio de backups completo.

#### `check_retention_policy(backup_paths)`

Verifica cumplimiento de retención mínima.

#### `analyze(backup_path, directory_path, expected_checksum)`

Ejecuta análisis principal: archivo individual o carpeta completa.

#### `validate(data)`

Valida rutas individuales o listas de rutas.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for Mnemomon

**Campos:**
- `name`
- `hash_algorithm`
- `min_retention_days`
- `check_encryption`
- `verify_permissions`
- `debug`
- `timeout`

### BackupVerificationResult

Result model for backup verification operations

**Campos:**
- `file_path`
- `exists`
- `checksum`
- `checksum_algorithm`
- `integrity_verified`
- `file_size`
- `last_modified`
- `errors`
- `warnings`

### AuditResult

Result model for directory audit operations

**Campos:**
- `directory`
- `audit_timestamp`
- `total_backups`
- `verified_backups`
- `corrupted_backups`
- `old_backups`
- `backup_details`
- `summary`

### AnalysisResult

Result model for analysis operations

**Campos:**
- `status`
- `message`
- `data`
- `errors`

### DigimonInfo

Information model for Digimon metadata

**Campos:**
- `name`
- `mission`
- `role`
- `status`
- `hash_algorithm`
- `min_retention_days`
- `supported_algorithms`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

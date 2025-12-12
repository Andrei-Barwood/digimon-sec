# API Reference - Mnemomon (Mega)

## Class: UMnemomon

### Constructor

```python
UMnemomon(config: Optional[Dict[str, Any]] = None)
```

Config keys:
- `hash_algorithm`: "sha512" (default), "sha256", "blake2b", "blake2s"
- `min_retention_days`: int, default 30
- `check_encryption`: bool, default True
- `verify_permissions`: bool, default True

### Methods

- `calculate_checksum(file_path, algorithm=None)` → str  
  Calcula checksum seguro leyendo en chunks.

- `verify_integrity(file_path, expected_checksum=None)` → `BackupVerificationResult`  
  Verifica checksum, permisos y alerta sobre posible falta de cifrado.

- `audit_backup_directory(directory_path)` → `AuditResult`  
  Audita una carpeta completa de backups, suma resultados y alerta por retención.

- `check_retention_policy(backup_paths)` → dict  
  Clasifica backups según política de retención mínima.

- `analyze(backup_path=None, directory_path=None, expected_checksum=None)` → `AnalysisResult`  
  Orquesta verificaciones (archivo puntual o carpeta completa).

- `validate(data)` → bool  
  Valida rutas únicas o listas de rutas.

- `get_info()` → dict  
  Metadata del Digimon (hash, retención, estado).

---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

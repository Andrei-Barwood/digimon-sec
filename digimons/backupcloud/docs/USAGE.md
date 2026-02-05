# Guia de Uso - backupcloud

## Tutorial Paso a Paso

Este tutorial muestra como usar **BackupCloud** para backups.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from backupcloud.core import BackupCloud

digimon = BackupCloud()
```

### 3) Preparar los datos de entrada

```python
backup_data = {
    "backup_enabled": True,
    "backup_retention_days": 7,
    "last_backup_hours": 6,
    "cross_region_replication": True,
}
```

### 4) Validar los datos (opcional)

```python
if not digimon.validate(backup_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(backup_data=backup_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

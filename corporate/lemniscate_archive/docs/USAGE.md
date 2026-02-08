# Guia de Uso - lemniscate_archive

## Tutorial Paso a Paso

Este tutorial muestra como usar **LemniscateArchive** para backups.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from lemniscate_archive.core import LemniscateArchive

modulo = LemniscateArchive()
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
if not modulo.validate(backup_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(backup_data=backup_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

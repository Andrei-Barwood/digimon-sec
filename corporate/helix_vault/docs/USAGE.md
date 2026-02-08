# Guia de Uso - helix_vault

## Tutorial Paso a Paso

Este tutorial muestra como usar **HelixVault** para base de datos.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from helix_vault.core import HelixVault

modulo = HelixVault()
```

### 3) Preparar los datos de entrada

```python
db_data = {
    "public_access": False,
    "storage_encrypted": True,
    "backup_retention_days": 7,
    "multi_az": True,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(db_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(db_data=db_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

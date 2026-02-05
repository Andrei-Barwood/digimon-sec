# Guia de Uso - rdsmon

## Tutorial Paso a Paso

Este tutorial muestra como usar **RDSmon** para base de datos.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from rdsmon.core import RDSmon

digimon = RDSmon()
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
if not digimon.validate(db_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(db_data=db_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

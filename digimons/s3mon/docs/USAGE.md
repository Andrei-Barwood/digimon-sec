# Guia de Uso - s3mon

## Tutorial Paso a Paso

Este tutorial muestra como auditar buckets S3 con **S3mon**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from s3mon.core import S3mon

digimon = S3mon()
```

### 3) Preparar los datos de entrada

```python
bucket_data = {
    "public_access": False,
    "encryption_enabled": True,
    "versioning_enabled": True,
    "logging_enabled": True,
}
```

### 4) Validar los datos (opcional)

```python
if not digimon.validate(bucket_data):
    raise ValueError("Bucket data invalida")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(bucket_data=bucket_data)
print(result.status)
print(result.message)
```

### 6) Ajustar configuracion avanzada

```python
digimon = S3mon(config={
    "require_encryption": True,
    "require_versioning": True,
    "require_logging": True,
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)


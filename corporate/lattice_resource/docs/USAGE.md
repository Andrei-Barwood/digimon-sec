# Guia de Uso - lattice_resource

## Tutorial Paso a Paso

Este tutorial muestra como usar **LatticeResource** para uso de recursos.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from lattice_resource.core import LatticeResource

modulo = LatticeResource()
```

### 3) Preparar los datos de entrada

```python
usage_data = {
    "cpu_usage": 40,
    "memory_usage": 35,
    "storage_usage": 50,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(usage_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(usage_data=usage_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

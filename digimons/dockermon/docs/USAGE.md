# Guia de Uso - dockermon

## Tutorial Paso a Paso

Este tutorial muestra como usar **Dockermon** para contenedor.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from dockermon.core import Dockermon

digimon = Dockermon()
```

### 3) Preparar los datos de entrada

```python
container_data = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}
```

### 4) Validar los datos (opcional)

```python
if not digimon.validate(container_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(container_data=container_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

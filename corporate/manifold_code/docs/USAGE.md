# Guia de Uso - manifold_code

## Tutorial Paso a Paso

Este tutorial muestra como usar **ManifoldCode** para IaC.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from manifold_code.core import ManifoldCode

modulo = ManifoldCode()
```

### 3) Preparar los datos de entrada

```python
iac_data = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(iac_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(iac_data=iac_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

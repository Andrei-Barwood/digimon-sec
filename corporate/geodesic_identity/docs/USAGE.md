# Guia de Uso - geodesic_identity

## Tutorial Paso a Paso

Este tutorial muestra como analizar configuraciones IAM con **GeodesicIdentity**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from geodesic_identity.core import GeodesicIdentity

modulo = GeodesicIdentity()
```

### 3) Preparar los datos de entrada

```python
iam_data = {
    "wildcard_permissions": False,
    "mfa_enforced": True,
    "rotation_enabled": True,
    "inactive_users": 0,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(iam_data):
    raise ValueError("IAM data invalida")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(iam_data=iam_data)
print(result.status)
print(result.message)
```

### 6) Interpretar resultados

```python
if result.status == "success":
    print("Configuracion IAM segura")
elif result.status == "warning":
    print("Se detectaron hallazgos")
else:
    print("Error en el analisis")
```

### 7) Ajustar configuracion avanzada

```python
modulo = GeodesicIdentity(config={
    "require_mfa": True,
    "require_rotation": True,
    "max_inactive_users": 0,
    "severity_threshold": "medium",
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)


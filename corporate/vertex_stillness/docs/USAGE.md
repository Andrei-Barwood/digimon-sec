# Guia de Uso - vertex_stillness

## Tutorial Paso a Paso

Este tutorial muestra como monitorear redes privadas con **VertexStillness**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from vertex_stillness.core import VertexStillness

modulo = VertexStillness()
```

### 3) Preparar los datos de entrada

```python
vpc_data = {
    "flow_logs_enabled": True,
    "public_subnets": False,
    "network_acl_restrictive": True,
    "nat_gateway_configured": True,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(vpc_data):
    raise ValueError("VPC data invalida")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(vpc_data=vpc_data)
print(result.status)
print(result.message)
```

### 6) Ajustar configuracion avanzada

```python
modulo = VertexStillness(config={
    "require_flow_logs": True,
    "require_nat_gateway": True,
    "severity_threshold": "medium",
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)


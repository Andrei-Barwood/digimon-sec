# Guia de Uso - vpcmon

## Tutorial Paso a Paso

Este tutorial muestra como monitorear redes privadas con **VPCmon**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from vpcmon.core import VPCmon

digimon = VPCmon()
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
if not digimon.validate(vpc_data):
    raise ValueError("VPC data invalida")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(vpc_data=vpc_data)
print(result.status)
print(result.message)
```

### 6) Ajustar configuracion avanzada

```python
digimon = VPCmon(config={
    "require_flow_logs": True,
    "require_nat_gateway": True,
    "severity_threshold": "medium",
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

